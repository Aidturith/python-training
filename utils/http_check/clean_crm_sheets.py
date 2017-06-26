# -*- coding: utf-8 -*-
# tools, 8 juin 2017

import threading
import time

import xlrd
import xlwt
from xlutils.copy import copy

from utils.http_check import regex
from utils.http_check import my_request


PASS_COLOR = u'pass_color'
WARN_COLOR = u'warn_color'
ERROR_COLOR = u'error_color'
MOD_COLOR = u'mod_color'


def set_colors(workbook):
    wb_colors = {}
    
    # add new colour to palette and set RGB colour value
    xlwt.add_palette_colour(PASS_COLOR, 0x8)
    workbook.set_colour_RGB(0x8, 155, 240, 150)
    wb_colors[PASS_COLOR] = xlwt.easyxf(u'pattern: pattern solid, fore_colour ' + PASS_COLOR)
    
    xlwt.add_palette_colour(WARN_COLOR, 0x9)
    workbook.set_colour_RGB(0x9, 240, 230, 150)
    wb_colors[WARN_COLOR] = xlwt.easyxf(u'pattern: pattern solid, fore_colour ' + WARN_COLOR)
    
    xlwt.add_palette_colour(ERROR_COLOR, 0xA)
    workbook.set_colour_RGB(0xA, 240, 160, 150)
    wb_colors[ERROR_COLOR] = xlwt.easyxf(u'pattern: pattern solid, fore_colour ' + ERROR_COLOR)
    
    xlwt.add_palette_colour(MOD_COLOR, 0xB)
    workbook.set_colour_RGB(0xB, 120, 160, 225)
    wb_colors[MOD_COLOR] = xlwt.easyxf(u'pattern: pattern solid, fore_colour ' + MOD_COLOR)
    
    return wb_colors


def check_emails(xlpath_in, xlpath_out, sheet_num, col_num, start_row=0):
    readbook = xlrd.open_workbook(xlpath_in)
    workbook = copy(readbook)
    
    wb_colors = set_colors(workbook)
    
    sheet = workbook.get_sheet(sheet_num)
    
    col = readbook.sheet_by_index(sheet_num).col_values(col_num)
    
    for row_index, cell in enumerate(col, start=start_row):
        if len(cell) > 0:
            mail_count, mail_adress = regex.count_regex(regex.PAT_EMAIL, cell)
            print(u"%s\t%s - %s" % (row_index, mail_count, mail_adress))
            
            row_index -= start_row
            
            if mail_count == 0:
                sheet.write(row_index, col_num, mail_adress, wb_colors[ERROR_COLOR])
            elif mail_count == 1:
                sheet.write(row_index, col_num, mail_adress, wb_colors[PASS_COLOR])
            else:
                sheet.write(row_index, col_num, mail_adress, wb_colors[WARN_COLOR])
    
    workbook.save(xlpath_out)


def _check_websites_t(results, row_index, url):
    url, status_code = my_request.check_http(url, False)
    results.append((row_index, url, status_code))
    
    string_disp = (u"%s\t%s - %s\n" % (row_index, status_code, url)).encode(u'utf-8')
    print(string_disp)
    
    return

def check_websites(xlpath_in, xlpath_out, sheet_num, col_num, start_row=0):
    readbook = xlrd.open_workbook(xlpath_in)
    workbook = copy(readbook)
    
    wb_colors = set_colors(workbook)
    
    sheet = workbook.get_sheet(sheet_num)
    
    col = readbook.sheet_by_index(sheet_num).col_values(col_num)
    
    # check websites, threaded
    results = []
    for row_index, cell in enumerate(col, start=start_row):
        if len(cell) > 0:
            if len(threading.enumerate()) < 16:
                t = threading.Thread(target=_check_websites_t, args=(results, row_index, cell))
            else:
                while len(threading.enumerate()) >= 16:
                    time.sleep(0.1)
                t = threading.Thread(target=_check_websites_t, args=(results, row_index, cell))
            
            t.start()
            
            #url, status_code = my_request.check_http(cell, False)
            
            #string_disp = (u"%s\t%s - %s\n" % (row_index, status_code, url)).encode(u'utf-8')
            #print(string_disp)
            
            #with open(u'result.txt', u'a') as myfile:
            #    myfile.write(string_disp)
            
    
    # cleaning threads
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    
    # write in sheet
    for row_index, url, status_code, in results:
            row_index -= start_row
            
            if 200 <= status_code <= 299:
                sheet.write(row_index, col_num, url, wb_colors[PASS_COLOR])
            elif 300 <= status_code <= 399:
                sheet.write(row_index, col_num, url, wb_colors[MOD_COLOR])
            elif 400 <= status_code <= 499:
                sheet.write(row_index, col_num, url, wb_colors[ERROR_COLOR])
            else:
                sheet.write(row_index, col_num, url, wb_colors[WARN_COLOR])
    
    workbook.save(xlpath_out)


if __name__ == '__main__':
    pass

#check_emails(xlin, xlout_mail_pro, 0, 16, 2)
#check_emails(xlin, xlout_mail_perso, 0, 17, 2)
check_websites(xlin, xlout_website, 0, 15, 2)

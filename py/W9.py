# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:24:19 2018

@author: pritespa
"""

import re
import xlsxwriter
import csv
import xlrd

filename = "txt/W9_2.txt"
infile = open(filename,'r')
lines=infile.readlines()

        
        
        
def BusinessName(string):   
    for count,line in enumerate(lines):
        if re.match(string, line):
            NameofBusiness = lines[count+1]
            print('The name of the orgranization is:',NameofBusiness)
            return NameofBusiness
        
        

        
def CityAddress(string):   
    for count,line in enumerate(lines):
        if re.match(string, line):
            FullAddress = lines[count+1]
            print('The city address is:',FullAddress)
            return FullAddress

def csv_from_excel():
    wb = xlrd.open_workbook('W-9.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    dl_csv_file = open('txt/output.csv', 'w')
    wr = csv.writer(dl_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    dl_csv_file.close()       

        
if __name__=='__main__':
    
    string_for_fullname=lines[9]
    string_for_businessname='2 Business name/disregarded entity name, if different from above '
    string_for_streetaddress=lines[37]
    string_for_cityaddress='6 City, state, and ZIP code '
    string_for_code=lines[32]
    
    
    # print('The full name of the individual is: ',string_for_fullname)
    bname=BusinessName(string_for_businessname)
    # print('The street address is: ',string_for_streetaddress)
    caddress=CityAddress(string_for_cityaddress)
    # print('Exemption code as given: ',string_for_code)
    
    
    workbook = xlsxwriter.Workbook('W-9.xlsx')

    worksheet = workbook.add_worksheet('Sheet1')
    
    
    worksheet.write(0,0,'Full name')
    worksheet.write(0,1,'Business Name')
    worksheet.write(0,2,'Full address')
    worksheet.write(0,3,'Exemption Code')
    
    worksheet.write(1,0,string_for_fullname)
    worksheet.write(1,1,bname)
    worksheet.write(1,2,string_for_streetaddress+caddress)
    worksheet.write(1,3,string_for_code)

    
    workbook.close()

    csv_from_excel()
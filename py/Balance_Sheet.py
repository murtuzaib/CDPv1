# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:27:53 2018

@author: Gambit
"""

import xlsxwriter
import csv
import xlrd

#Read the Balance Sheet text file
filename = "txt/BalanceSheet1.txt"
infile = open(filename,'r')
lines=infile.readlines()

#Initialize a workbook
workbook = xlsxwriter.Workbook('BalanceSheet.xlsx')
worksheet = workbook.add_worksheet('Sheet1') 

#Global variables for line number and row number for excel sheet.
i=0
row=1

#Adding Global Value variables to easily reuse for workbook creation and extraction.
value1='Current Assets'
value01='Total'
value2='Cash & Equivalents'
value3='Total Current Assets'
value4='Total Assets'
value5='Total Current Liabilities'
value6='Total Liabilities'
value7='Total Stockholder Equity'


worksheet.write(0,1,'December 31, 2001')
worksheet.write(0,2,'December 31, 1999')
worksheet.write(1,0,value2)
worksheet.write(2,0,value3)
worksheet.write(3,0,value4)
worksheet.write(4,0,value5)
worksheet.write(5,0,value6)
worksheet.write(6,0,value7)


while i<len(lines):
    if value1 in lines[i] and value01 not in lines[i]:
        a=lines[i].split()
        StartDate=a[2]+a[3]+a[4]
        EndDate=a[5]+a[6]+a[7]
        # print('Balance Sheet Start Date:',StartDate)
        # print('Balance Sheet End Date:',EndDate)
        i+=1
        
    if value2 in lines[i]:
        a=lines[i].split()
        # print(value2,'in 1999=',a[4])
        # print(value2,'in 2001=',a[3])
        worksheet.write(row,1,a[3])
        worksheet.write(row,2,a[4])
        row+=1
        i+=1
        
    if value3 in lines[i]:
        a=lines[i].split()
        # print(value3,'in 1999=',a[4])
        # print(value3,'in 2001=',a[3])
        worksheet.write(row,1,a[3])
        worksheet.write(row,2,a[4])
        row+=1
        i+=1
        
    if value4 in lines[i]:
        a=lines[i].split()
        # print(value4,'in 1999=',a[3])
        # print(value4,'in 2001=',a[2])
        worksheet.write(row,1,a[2])
        worksheet.write(row,2,a[3])
        row+=1
        i+=1
        
    if value5 in lines[i]:
        a=lines[i].split()
        # print(value5,'in 1999=',a[4])
        # print(value5,'in 2001=',a[3])
        worksheet.write(row,1,a[3])
        worksheet.write(row,2,a[4])
        row+=1
        i+=1
        
    if value6 in lines[i]:
        a=lines[i].split()
        # print(value6,'in 1999=',a[3])
        # print(value6,'in 2001=',a[2])
        worksheet.write(row,1,a[2])
        worksheet.write(row,2,a[3])
        row+=1
        i+=1
        
    if value7 in lines[i]:
        a=lines[i].split()
        # print(value7,'in 1999=',a[4])
        # print(value7,'in 2001=',a[3])
        worksheet.write(row,1,a[3])
        worksheet.write(row,2,a[4])
        row+=1
        i+=1
        
    else: 
        i+=1
workbook.close()

wb = xlrd.open_workbook('BalanceSheet.xlsx')
sh = wb.sheet_by_name('Sheet1')
dl_csv_file = open('txt/output.csv', 'w')
wr = csv.writer(dl_csv_file, quoting=csv.QUOTE_ALL)

for rownum in range(sh.nrows):
    wr.writerow(sh.row_values(rownum))
dl_csv_file.close()
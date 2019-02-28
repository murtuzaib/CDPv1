# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:33:19 2018

@author: pritespa
"""

import linecache
import xlwt
import csv
import xlrd

#Importing the Dataset
filename="txt/DL.txt"
myfile=open(filename, 'r') 
lines=myfile.readlines()

#Global Varibles
start1='SEX:'
end1='EYES:'
start2='ISSUED:'
end2='EXPIRES:'
start3='EXPIRES:'
end3='BAJt'

#Entities Extraction
#Name of the issued State of DL
print("Name of the State DL issued:",lines[0])

#Name of the Card Holder
Name = (lines[4])

#splitting the Card Holder
for i, value in enumerate(Name.split()):
    #print (" word #%d: %s" % (i,value))
    splitsent2 = Name.split(' ')
    word1=splitsent2[0]
    word2=splitsent2[1]


print("The candidates name is: ",lines[4])



#Address of the Card Holder
megaline=(lines[5]).replace('\n', '')
print("The candidates address is: ",megaline)

megaline2=(lines[6].replace('\n',''))
#print("The candidates address is: ",megaline2)

#splitting the Megaline2
for i, word in enumerate(megaline2.split()):
    #print (" word #%d: %s" % (i,word))
           
#splitting words from sentence
    splitsent1 = megaline2.split(' ')
    word3=splitsent1[0]
    word4=splitsent1[1]
    word5=splitsent1[2]


print("City:",word3)
print("State:",word4)
print("Pincode:",word5)


#Date of Birth of the DL Card Holder
print("Date of Birth of Card Holder",lines[7])

#Gender of the Card Holder
s1=lines[8]
split=(s1.split(start1))[1].split(end1)[0]
sex=split[1]
print('Sex:',sex)

#Card Issue Date
s2=lines[15]
DOI=(s2.split(start2))[1].split(end2)[0]
print('Date of Issue:',DOI)

#Card Expiry Date
s2=lines[15]
DOE=(s2.split(start3))[1].split(end3)[0]
print('Date of expiry',DOE)

#Main Function¶
def main():
    book= xlwt.Workbook()
    sheet1 = book.add_sheet('Sheet1')
    # sheet.write(r, c, <text>)
    sheet1.write(0,1,'State Name')
    sheet1.write(0,2, 'DOB')
    sheet1.write(0,3, 'FirstName')
    sheet1.write(0,4, 'LastName')
    sheet1.write(0,5, 'Address')
    sheet1.write(0,6,'City Name')
    sheet1.write(0,7,'State Name')
    sheet1.write(0,8,'Pincode')
    sheet1.write(0,9, 'Sex')
    sheet1.write(0,10, 'Date of Issue')
    sheet1.write(0,11, 'Date of expiry')
    sheet1.write(1,1, lines[0])
    sheet1.write(1,2, lines[7])
    sheet1.write(1,3, word1)
    sheet1.write(1,4, word2)
    sheet1.write(1,5,megaline)
    sheet1.write(1,6,word3)
    sheet1.write(1,7,word4)
    sheet1.write(1,8,word5)
    sheet1.write(1,9, sex)
    sheet1.write(1,10, DOI)
    sheet1.write(1,11, DOE)

    
    book.save('Sample.xls')

# xls to csv file for php to work with
def csv_from_excel():
    wb = xlrd.open_workbook('Sample.xls')
    sh = wb.sheet_by_name('Sheet1')
    dl_csv_file = open('txt/output.csv', 'w')
    wr = csv.writer(dl_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    dl_csv_file.close()

if __name__ == '__main__':
    main()
    csv_from_excel()
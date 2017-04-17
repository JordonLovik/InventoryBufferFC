import csv
from shutil import copyfile
import ftplib
"""
This program reads the 01_inventory.txt file converts inventory to integer, removes buffer from integer,
and converts integer back to string. all the while writing updated data to new inventory file called InventoryBuffered.txt

This program should be run at 1 hour intervals
file location on server: root@10.1.1.5/s/01_Inventory.txt
"""
#### DOWNLOAD 01_INVENTORY.TXT FROM 10.1.1.5/s/ #####
downloadfile = '01_Inventory.txt'
uploadfile = 'InventoryBuffered.txt'
ftp = ftplib.FTP('10.1.1.5')
ftp.login('hubsoft', 'Mgfj9RZRaz')
ftp.cwd('s/')
ftp.retrbinary('RETR ' + downloadfile,open(downloadfile, 'wb').write) #RETR = retreve file

#Create Back of local INVENTORY file
copyfile('C:/Users/jordon.AFTCO/PycharmProjects/InventoryManagerFC/01_inventory.txt', 'C:/Users/jordon.AFTCO/PycharmProjects/InventoryManagerFC/01_inventory_Bkup.txt')

inventory = []
buffer = 7
bufferfile = open('C:/Users/jordon.AFTCO/PycharmProjects/InventoryManagerFC/InventoryBuffered.txt', 'w')

with open('C:/Users/jordon.AFTCO/PycharmProjects/InventoryManagerFC/01_inventory.txt','r') as f:
    reader = csv.reader(f,delimiter='\t')
    for lines in reader:
        lines.pop(-1) #remove last tab in list
        if lines[3]:
            temp = int(lines[3]) - buffer #remove buffer
            if temp < 0: #if inventory dips below 0 set to 0
                temp = 0
                lines[3] = str(temp)
            else:
                lines[3] = str(temp)
        for string in lines:
            bufferfile.write(string + '\t') #write data with new inventory
            if string == lines[-1]: #if last element in string print new line in doc
                bufferfile.write('\n')

#### FTP local INVENTORY file to 10.1.1.5/s/InventoryBuffered.txt
ftp.storbinary('STOR ' + uploadfile, open(uploadfile, "rb"))
ftp.quit()
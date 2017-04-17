import ftplib

downloadfile = '01_Inventory.txt'
uploadfile = 'InventoryBuffered.txt'

ftp = ftplib.FTP('*.*.*.*')
ftp.login('*******', '******')
ftp.cwd('s/')
ftp.retrbinary('RETR ' + downloadfile,open(downloadfile, 'wb').write) #RETR = retreve file


ftp.storbinary('STOR ' + uploadfile, open(uploadfile, "rb"))
ftp.quit()

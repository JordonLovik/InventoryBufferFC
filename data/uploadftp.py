import ftplib

ftp = ftplib.FTP('*.*.*.*')
ftp.login('********', '*********')
ftp.cwd('s/')
ftp.storbinary("STOR X01_Inventory.txt", open("X01_Inventory.txt", "rb"))
#ftp.storbinary('STOR ' + 'X01_Inventory.txt',open('X01_Inventory.txt', 'wb'))
ftp.quit()

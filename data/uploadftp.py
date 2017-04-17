import ftplib

ftp = ftplib.FTP('10.1.1.5')
ftp.login('hubsoft', 'Mgfj9RZRaz')
ftp.cwd('s/')
ftp.storbinary("STOR X01_Inventory.txt", open("X01_Inventory.txt", "rb"))
#ftp.storbinary('STOR ' + 'X01_Inventory.txt',open('X01_Inventory.txt', 'wb'))
ftp.quit()

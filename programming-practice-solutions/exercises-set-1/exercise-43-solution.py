from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username',passwd='password')

ftp.cwd('working_dir')

def grabFile():
    fileName = 'filename.txt'
    localfile = open(filename,'wb')
    ftp.retrbinary('RETR '+ filename, localfile.write,1024)

    ftp.quit()
    localfile.close()

def placeFile():
    fileName = 'filename.txt'
    ftp.storbinary('STOR '+filename, open(filename,'rb'))
    ftp.quit()
    

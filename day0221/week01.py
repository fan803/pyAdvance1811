import ftplib
def ftpconnect(host, username, passwd):
    ftp = ftplib.FTP(host=host, user=username, passwd=passwd)
    return ftp
def upload(ftp, localfile, remotefile):
    buffersize = 1024
    file = open(localfile, "rb")
    ftp.storbinary("STOR " + remotefile, file, buffersize)
    file.close()
def download(ftp, localfile, remotefile):
    buffersize = 1024
    file = open(localfile, "wb")
    ftp.retrbinary("RETR " + remotefile, file.write, buffersize)
    file.close()
if __name__ == "__main__":
    ftp = ftpconnect("192.168.15.33", "ftpzzy", "123456")
    upload(ftp, "d:/flashfxp.png", "newxp.png")
    # download(ftp, "d:/newxpp.png", "newxp.png")
    ftp.quit()
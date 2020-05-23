import os
from ftplib import FTP
import subprocess as sp
from configparser import ConfigParser;

config = ConfigParser()
config.read('config.ini')
host = config['FTP']['host']
user = config['FTP']['username']
password = config['FTP']['password']

fileLocation = 'vspub/Desktop_Main'
filename = input('Enter file name => ')

with FTP(host=host, user=user, passwd=password) as ftp:
    ftp.cwd(fileLocation)
    # download the file
    local_filename = os.path.join(r"c:\myfolder", filename)
    lf = open(local_filename, "wb")
    ftp.retrbinary("RETR " + filename, lf.write, 8*1024)
    lf.close()

    # Install software
    process = sp.Popen(local_filename, shell=True)
    process.wait()



import time
import os
import random
import sys
import datetime
import importlib

configparser_spec = importlib.util.find_spec("configparser")
found = configparser_spec is not None
if(found == False):
    n = input ("Configparser module is missing, if you want to install it enter 1, else, enter anything")
    if n == 1 :
        os.system("pip3 install configparser")
        sys.exit(-1)
    else:
        sys.exit(-1)

import configparser

nmap_spec = importlib.util.find_spec("nmap")
found = nmap_spec is not None
if(found == False):
    n = input ("Nmap module is missing, if you want to install it enter 1, else, enter anything")
    if n == 1 :
        os.system("pip3 install python-nmap")
        sys.exit(-1)
    else:
        sys.exit(-1)
import nmap


#recover conf
cfg = configparser.ConfigParser(allow_no_value=True)
cfg.read('./conf.cfg')
hour_start = int(cfg.get('nmapscan','hour_start'))
hour_stop = int(cfg.get('nmapscan','hour_stop'))
port_fin = cfg.get('nmapscan','portfin')
port_debut = cfg.get('nmapscan','portdebut')

#Return True if current hour is the hour_start for sleeping
def getCurrentHour():
    now = datetime.datetime.now()
    if(now == hour_start):
        return True
    else:
        return False
    

def nmapOnIp(allRanges,number):
    i=0
    for ip in allRanges:
            nm = nmap.PortScanner()
            for i in range(int(port_debut),int(port_fin)):
                print("Scanning port : "+str(i))
                nm.scan(str(ip),str(i))

            ##On écrit les résultats du nmap
            f = open("results"+str(number)+".csv","a")
            for line in nm.csv():
                f.write(line)
            f.close()

            f = open("scanned_ip_"+str(number)+".txt","a")
            f.write(str(ip))
            f.close()


#This method will be used to recover ips from a file and write 
def main():
    toVerify = []
    alreadyScannedIps = []
    allIps = []

    try:
        for i in range(1,7):
            with open("scanned_ip_"+str(i)+".txt","r") as lines:
                for line in lines:
                    alreadyScannedIps.append(line)
    except:
        #On créé les fichiers
        for i in range(1,7):
            open("scanned_ip_"+str(i)+".txt","w")
    try:
        with open('ips.txt','r') as lines:
            for line in lines:
                toVerify.append(line)
    except:
        f"File ips.txt is missing, exiting."
        sys.exit(-1)
    if(len(alreadyScannedIps) > 0):
        toScan = []
        for item in toVerify:
            if item not in alreadyScannedIps:
                allIps.append(item)
    else: allIps = toVerify
    if(len(allIps) == 0):
        f"No ip to scan, exiting."
        sys.exit(-1)
    
if __name__ == "__main__":
    main()  
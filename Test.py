import nmap
import os

sc = nmap.PortScanner()
def main():
    n = input ("Choisissez une fonctionnalité :\n1 - NetworkScan \n")

    if n == '1':
        nmap()
    if n =='2':
        vuln() 
    if n =='3':
        os.system('msfconsole')
    else :
        print("Veuillez entrer un nombre entre 1 et 3")


    def nmap():
        ip = input("\nEnter an IP address : ")
        sc.scan(pip, "1-1024")
        print(sc.scaninfo())
        print(sc[ip]['tcp'].keys())

    def vuln():
        ip = input("\nEnter an IP address : ")
        print(os.system('nmap -sV --script=vulscan.nse' + ip))
        

##Pour G. Molveau :
##J'ai changé légèrement de projet par rapport à ce que j'avais dit au début.
##J'ai arrêté la boîte à outils de scan IP pour faire un scan IP simple je trouvais ça plus intéressant, pour comprendre comment tout fonctionnait,
##maintenant le programme permet de faire un scan IP, on peut choisir le port de début et de fin ainsi que l'heure de début et de fin. 
##Le tout est répertorié dans un fichier extérieur qui s'écrit au fur et à mesure."""

import configparser
import nmap
import os
import sys
import datetime
import importlib

# Cherche s'il y a configparser sur le PC et sinon, l'installe.
configparser_spec = importlib.util.find_spec("configparser")
found = configparser_spec is not None
if(found == False):
    n = input("Configparser module is missing, if you want to install it enter 1, else, enter anything")
    if n == 1:
        os.system("pip3 install configparser")
        sys.exit(-1)
    else:
        sys.exit(-1)


# Cherche s'il y a python-nmap et sinon, l'installe
nmap_spec = importlib.util.find_spec("nmap")
found = nmap_spec is not None
if(found == False):
    n = input(
        "Nmap module is missing, if you want to install it enter 1, else, enter anything")
    if n == 1:
        os.system("pip3 install python-nmap")
        sys.exit(-1)
    else:
        sys.exit(-1)


# Récupérer la conf via le fichier conf.cfg
cfg = configparser.ConfigParser(allow_no_value=True)
cfg.read('./conf.cfg')
hour_start = int(cfg.get('nmapscan', 'hour_start'))
hour_stop = int(cfg.get('nmapscan', 'hour_stop'))
port_fin = cfg.get('nmapscan', 'port_fin')
port_debut = cfg.get('nmapscan', 'port_debut')

# Récupérer l'heure actuelle


def getCurrentHour():
    now = datetime.datetime.now()
    if(now == hour_start):
        return True
    else:
        return False

# On appelle nmap dans une range d'IP entre celle du début que l'on a choisi et celle de fin.


def nmap_ip(all_ranges, number):
    i = 0
    for ip in all_ranges:
        nm = nmap.PortScanner()
        for i in range(int(port_debut), int(port_fin)):
            print("Scanning port : "+str(i))
            nm.scan(str(ip), str(i))

            # On écrit les résultats du nmap
            f = open("results"+str(number)+".csv", "a")
            for line in nm.csv():
                f.write(line)
            f.close()

            # On écrit sur le fichier les IPs scannés dans un txt
            f = open("scanned_ip_"+str(number)+".txt", "a")
            f.write(str(ip))
            f.close()


def main():
    to_verify = []
    already_scanned_ips = []
    all_ips = []

    try:
        for i in range(1, 7):
            with open("scanned_ip_"+str(i)+".txt", "r") as lines:
                for line in lines:
                    already_scanned_ips.append(line)
    except:
        # On créé le fichier
            open("scanned_ip.txt", "w")
    try:
        with open('ip.txt', 'r') as lines:
            for line in lines:
                to_verify.append(line)
    except:
        print("Le fichier ip.txt manque, ou, veuillez rentrer au moins une IP dans le fichier")
        sys.exit(-1)
    if(len(already_scanned_ips) > 0):
        for item in to_verify:
            if item not in already_scanned_ips:
                all_ips.append(item)
    else:
        all_ips = to_verify
    if(len(all_ips) == 0):
        print("Il n'y a pas d'IP à scanner.")
        sys.exit(-1)


if __name__ == "__main__":
    main()

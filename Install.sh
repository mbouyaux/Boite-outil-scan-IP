#!/bin/bash
#if [[ $EUID -e 0 ]]; then
#    echo "[-] This script should not be run as a root !" 1>&2
#	exit 1
#fi
pip3 install configparser
pip3 install python-nmap
echo "[+] All dependencies have been installed, you can use the tool."
rm *.sh
rm *.bat
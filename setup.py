#!/usr/bin/env python3

import sys
import subprocess
import os

dire = "/etc/certs"
cert = "ca.cer"
conf = "/etc/wpa_supplicant/wpa_supplicant.conf"


def main():
	#check for python3 and superuser
	if (not (sys.version).startswith("3.")) or (str(subprocess.check_output("whoami")) != "b'root\\n'"):
			subprocess.call("sudo python3 setup.py", shell=True)

	else:
		
		un = input("UN (NUR DIE NR): ")
		pw = input("PW: ")
		
		newText ='\n\tidentity="el' + un + '@lehre.dhbw-stuttgart.de"\n\tpassword="' + pw + '"\n\tproto=RSN\n\tkey_mgmt=WPA-EAP\n\tpairwise=CCMP\n\tauth_alg=OPEN\n\teap=PEAP\n\tca_cert="/etc/certs/ca.cer"\n\tphase2="auth=MSCHAPV2"\n'
		
		#create folder
		if not os.path.exists(dire):
			subprocess.call("mkdir " + dire, shell=True)
		
		#copy certificat
		subprocess.call("cp -b " + cert + " "+ dire + "/" + cert, shell=True)
		
		confText = getText(conf)
		networkX = findBetween(confText, 'network={\n\tssid="DHBW-802.1x"', '}')
		if networkX != "":
			confText = confText.replace(networkX, newText)
		else:
			confText = confText + '\nnetwork={\n\tssid="DHBW-802.1x"' + newText + "}"
		writeText(conf, confText)
		
		print("please reboot!!!")
	
	
	
	
def getText(textFile):
	if os.path.isfile(textFile):
		f = open(textFile)
		text = f.read()
		f.close()
		return text
	return ""


def writeText(textFile, text):
	open(textFile, 'a').close()
	f = open(textFile, 'w')
	f.truncate()
	f.write(text)
	f.close()
	
def findBetween(s, first, last ):
	try:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
	except ValueError:
			return ""

main()

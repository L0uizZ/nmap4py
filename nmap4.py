"""
-------------------------------------------------
# Nmap4py - Network Scanner
-------------------------------------------------
"""
__author__ = "L0uizZ"
__version__ = "0.0.1"

import nmap

openports = []

def portScan(host, scantype):
	scanner = nmap.PortScanner()

	if scantype == "1":
		#CLEAR ANSI ESCAPE SEQUENCE
		print('\033c')
		print("NMAP", scanner.nmap_version())
		print("[*] RUN SYN ACK")

		scanner.scan(host, '1-1024', '-v -sS')
		scaninfo = scanner.scaninfo()  
		hoststate = scanner[host].state()
		protocols = scanner[host].all_protocols()
		ports = scanner[host]['tcp'].keys()

		for port in scanner[host]['tcp'].keys():
			openports.append(port)

		#print(scaninfo)
		print("[*]", host, hoststate)
		print("[*] Ports:", protocols, openports)

	elif scantype == "2":
		#CLEAR ANSI ESCAPE SEQUENCE
		print('\033c')
		print("NMAP", scanner.nmap_version())
		print("[*] RUN UDP")

		scanner.scan(host, '1-1024', '-v -sU')
		scaninfo = scanner.scaninfo()  
		hoststate = scanner[host].state()
		protocols = scanner[host].all_protocols()
		ports = scanner[host]['udp'].keys()

		for port in scanner[host]['udp'].keys():
			openports.append(port)

		#print(scaninfo)
		print("[*]", host, hoststate)
		print("[*] Ports:", protocols, openports)

	elif scantype == "3":
		#CLEAR ANSI ESCAPE SEQUENCE
		print('\033c')
		print("NMAP", scanner.nmap_version())
		print("[*] RUN COMPREHENSIVE")

		scanner.scan(host, '1-1024', '-v -sS -sV -sC -A -O')
		scaninfo = scanner.scaninfo()  
		hoststate = scanner[host].state()
		protocols = scanner[host].all_protocols()
		ports = scanner[host]['tcp'].keys()

		for port in scanner[host]['tcp'].keys():
			openports.append(port)

		#print(scaninfo)
		print("[*]", host, hoststate)
		print("[*] Ports:", protocols, openports)

def __main__():
	host = input("[*] Enter host address: ")
	type(host)

	scantype = input("1) SYN ACK 2) UDP 3) COMPREHENSIVE\n[*] Select scan-type: ")

	portScan(host, scantype)

__main__()

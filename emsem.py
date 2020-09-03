#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

#https://github.com/liris/websocket-client
## sudo pip install --user websocket-client
from websocket import create_connection
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)
class inbox(object):
	def __init__(self):
		super(inbox, self).__init__()
		self.ws = create_connection("wss://dropmail.me/websocket")
		self.next = self.ws.recv
		self.close = self.ws.close
		self.email = self.next()[1:].split(":")[0]
		self.next()

def banner():
	print('   ◕▬▬▬▬▬('+Fore.GREEN+Style.BRIGHT+Back.RED+'EMAIL SEMENTARA/EMAIL RECEIVER'+Style.RESET_ALL+Back.RESET+')▬▬▬▬▬◕')
	print('''
	 	      █████████ 
		      █▄█████▄█ 
		      █ ▼▼▼▼▼ █ 
		      ██▌    ██▌ 
		      █ ▲▲▲▲▲ █ 
		      █████████ 
		       ██   ██
''')
	print(Fore.GREEN+Style.BRIGHT+Back.RED+"LEARNCODE")
def main(box):
	#stdlib
	import sys
	from json import loads
	from subprocess import call
	from datetime import datetime
	print ('Email : '+box.email+" \nsilahkan copy email tersebut")
	while True:
		result =  box.next()
		try:
			print(Fore.GREEN+"\nDiterima pada {0}".format( datetime.now()))
			for k in loads(result[1:]).items():
				print(Fore.GREEN+"\t%s: %s" % k)
		except:
			print(Fore.GREEN+"Diterima:{1} {0}\n".format(result, datetime.now()))

if __name__ == '__main__':
	import os, sys
	os.system('clear')
	banner()
	print("UNTUK KELUAR TEKAN : CTRL + C")
	try:
		box = inbox()
		main(box)
	except KeyboardInterrupt:
		box.close()
		sys.exit(0)
	countdownTimer(25, 00)

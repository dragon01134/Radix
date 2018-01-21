#!/usr/bin/python

import os
import time
#this one for quick fix
import _thread

try:
	from webSocketServer import WebServer
	from radix import Radix
except Exception as e:
	print("Import err of WebServer")

#Global lists
downloading_list = list()


class RadixServerConfig():
	"""This class stores server config, Like Webserver listening port"""
	def __init__(self):
		self.web_server_port_number = 9999

	def setWebServerPortNumber(self,port=0):
		if port == 0:
			print("Port Number is 0")
			return -1
		if port < 0:
			print("Port Number is less than 0")
			return
		self.web_server_port_number = port
	def getWebServerPortNumber(self):
		return self.web_server_port_number




def init_server():
	pass

def read_config():
	pass

def listener_function(url_obj):
	global downloading_list
	print("Creating radix object"+ url_obj['url'])
	radix = Radix(url_obj['url'])
	print("Adding to global list")
	downloading_list.append(radix)
	print("Starting")
	radix.start()
	print("exiting")

def run_web_server(webServer):
	webServer.run()

def print_downloading():
	os.system('clear')
	print("{0}-{1}-{2}-{3}".format("".center(40,"-"),"".center(10,"-"),"".center(20,"-"),"".center(20,"-")))
	print("|{0}|{1}|{2}|{3}|".format("Name".center(40),"ETA".center(10),"Percentage".center(20),"Status".center(20)))
	print("{0}-{1}-{2}-{3}".format("".center(40,"-"),"".center(10,"-"),"".center(20,"-"),"".center(20,"-")))
	for radix in downloading_list:
		stats = radix.status()
		print("|{0}|{1}|{2}|{3}|".format(stats['name'][:39].center(40),str(stats['eta']).center(10),stats['percent'].center(20),stats['status'].center(20)))
	print("{0}-{1}-{2}-{3}".format("".center(40,"-"),"".center(10,"-"),"".center(20,"-"),"".center(20,"-")))
	time.sleep(1)			
	




def main():
	"""Main function of radix server"""
	config = RadixServerConfig()
	web_server = WebServer(config.getWebServerPortNumber())
	web_server.addListener(listener_function)
	_thread.start_new_thread(run_web_server,(web_server,))
	while True:
		if len(downloading_list) > 0:
			print_downloading()
		else:
			time.sleep(2)




if __name__ == '__main__':
	main()




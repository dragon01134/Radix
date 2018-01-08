#!/usr/bin/python3
from __future__ import unicode_literals
import threading 
import youtube_dl
import os
import time

class Radix(threading.Thread):
	"""This class is for Every Download elements.
	This class contains all the info needed to work on. """
	_status = ''
	_eta = 0
	_percent = ''
	_DEFAULT_DOWNLOAD_DIR = os.environ['HOME']

	def __init__(self,url,downloadDir=None):
		"""Init function for radix"""
		threading.Thread.__init__(self)
		if url is None:
			return None
		if downloadDir is None:
			downloadDir = self._DEFAULT_DOWNLOAD_DIR
		self._url=url
		ydl_opts = {
    		'quiet':True,
    		'verbose':False,
    		'no_warnings':True
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			#print(self._url)
			self._info = ydl.extract_info(url, download=False)
			if 'title' in self._info.keys():
				self.name = self._info['title']
			else:
				self.name = url

	def run(self):
		"""Calling of this function starts downloading."""
		ydl_opts = {
    		'progress_hooks': [self.__hook],
    		'quiet':True,
    		'verbose':False,
    		'no_warnings':True
		}
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			#print(self._url)
			ydl.download([self._url])

	def stop(self):
		"""TODO:Calling of this function stops downloading."""
		
	def status(self):
		"""Calling of this function return dict of status
			status['name':name,
					'status': downloading|stoped|paused|error,
					'ETA':eta,
					'percent':percent,
				   ]
		"""
		stats = dict()
		stats['name'] = self.name
		stats['url'] = self._url
		stats['status'] = self._status 
		stats['eta'] = self._eta
		stats['percent'] = self._percent

		return stats

	def __hook(self,statusDict):
		#os.system('clear')
		for key,value in statusDict.items():
			#print(str(key)+":"+str(value))
			if key is 'status' :
				self._status = value
			elif key is 'eta':
				self._eta = value
			elif key is '_percent_str':
				self._percent = value
	
	

	



 

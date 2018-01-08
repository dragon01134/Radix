#!/usr/bin/python3
from __future__ import unicode_literals
import _thread
import youtube_dl
import os
import time

__DEFAULT_DOWNLOAD_DIR="/home/jeet"

class Radix():
	"""This class is for Every Download elements.
	This class contains all the info needed to work on. """
	_status=''
	_eta=0
	_percent=''

	def __init__(self,url,downloadDir=None):
		global __DEFAULT_DOWNLOAD_DIR
		if url is None:
			return None
		if downloadDir is None:
			downloadDir="/home/jeet"
		self._url=url

	def start(self):
		"""Calling of this function starts downloading."""

		ydl_opts = {
    		'progress_hooks': [self.__hook],
    		'quiet':True,
    		'verbose':False,
    		'no_warnings':True
		}
		_thread.start_new_thread(self.__thread_func,(ydl_opts,))

	def stop():
		"""Calling of this function stops downloading."""

	def status(self):
		"""Calling of this function return dict of status
			status['name':name,
					'status': downloading|stoped|paused|error,
					'ETA':eta,
					'percent':percent,
				   ]
		"""
		stats = dict()
		stats['url'] = self._url
		stats['status'] = self._status 
		stats['eta'] = self._eta
		stats['percent'] = self._percent

		return stats

	def __hook(self,statusDict):
		#os.system('clear')
		for key,value in statusDict.items():
		#	print(str(key)+":"+str(value))
			if key is 'status' :
				self._status = value
			elif key is 'eta':
				self._eta = value
			elif key is '_percent_str':
				self._percent = value

		
	def __thread_func(self,ydl_opts):
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			print(self._url)
			ydl.download([self._url])


def main():
	url='https://www.youtube.com/watch?v=7lmCu8wz8ro&t=2512s'
	radix = Radix(url)
	radix.start()
	radix1 = Radix('https://www.youtube.com/watch?v=N4mEzFDjqtA&t=960s')
	radix1.start()
	while True:
		stats = radix.status()
		stats1 = radix1.status()
		print("URL:" + stats['url']+"   ETA: "+ str(stats['eta'])+" Percentage: "+stats['percent'])
		print("URL:" + stats1['url']+"   ETA: "+ str(stats1['eta'])+" Percentage: "+stats1['percent'])
		time.sleep(1)
		os.system('clear')
if __name__ == '__main__':
	main()

			
	



 

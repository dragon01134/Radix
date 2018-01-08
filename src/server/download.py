#!/usr/bin/python


class DownloadTask():
	"""This class represent each download entry, it may be video or simple file
		Properties are comming under like:--

	"""
	def __init__(self,url=None):
		if url is None:
			print "url shouldn't be None"
			return None

		self.url=url
		self.is_meta_data_extracted=False
		self.get_meta_data()

	def get_meta_data(self):
		"""This metthod get all required meta data for this download task.
			First send GET Request and observe the response,
				According to response extract meta data.
				Valid Type:
					1.Video
					2.Files
		"""
		#TODO- i am going to add for other file so for now i am going to explicitly add for video.
		self.type='video'
		

		


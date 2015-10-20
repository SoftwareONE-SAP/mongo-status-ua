from pymongo import MongoClient
from datetime import datetime

'''
Licence: Copyright Centiq Ltd
Author: W.Overton <woverton@centiq.co.uk>
Note:  Connect to the MongoDB server using the config file parameters.
'''

class mongoConnectionEngine:

	def getCurrentTime(self):
		return float(datetime.now().microsecond)

	def connect(self, address, port):
		startTime = self.getCurrentTime()
		try:
			self.client = MongoClient(address, int(port))
			self.client.server_info()
			return (str(0), "Connected OK", str(float(self.getCurrentTime() - startTime)/1000))
		except Exception as e:
			#connection unsuccesful
			return (str(1), str(e), str(float(self.getCurrentTime() - startTime)/1000))
		

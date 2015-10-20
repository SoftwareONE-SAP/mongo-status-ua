#!/usr/bin/python

'''
Licence: Copyright Centiq Ltd
Author: W.Overton <woverton@centiq.co.uk>
Note:   Check local instance of MongoDB. Config file takes 2 parameters, host and port under block 'Mongo_Server'.
'''

import ConfigParser
from datetime import datetime
from mongo_function_class import *

class main:
	def __init__(self):
		self.outputHeader()
		self.config = ConfigParser.RawConfigParser()
		self.config.read("config.conf")
		self.outputRowData()
	
	def outputRowData(self):
		mongo_Host = self.config.get("Mongo_Server","Hostname")
		mongo_Port = self.config.get("Mongo_Server","Port")
		self.mongoConnectionEngine = mongoConnectionEngine()
		serverInfo = self.mongoConnectionEngine.connect(mongo_Host,mongo_Port)
		print(self.config.get("Mongo_Server", "Hostname") + "@@@" + self.config.get("Mongo_Server", "Port") + "@@@" + serverInfo[0] + "@@@" + serverInfo[1] + "@@@" + serverInfo[2])

	def outputHeader(self):
		print("ma_name: mongo_status")
		print("ma_group_name: Information")
		print("ma_short_name: mgst")
		print("ma_mon_order: 30")
		print("ma_keys: Remote Address @@@ Port")
		print("ma_data:")
		print("Remote Address @@@ Port @@@ Status @@@ Info @@@ Connection Time")

main()



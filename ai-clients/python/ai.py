#!/usr/bin/env python

import socket
import sys

class AI:

	def __init__(self, s=None):
		if s is None:
			self.s = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.s = s

	def connect(self, host, port):
		print "Connecting to", host, port
		try:
			self.s.connect((host, port))
		except Exception, e:
			print >>sys.stderr, e
			sys.exit(1)

	def name(self, nick):
		print "Sending name:", nick
		self.s.send("NAME %s" % (nick,))

	def start(self):
		print "Waiting on server start..."
		while 1:
			ready = self.s.recv(4096)
			if 'START' in ready:
				print "Received START"
				break

	def wind(self, x, y):
		print "Sending WIND", x, y
		self.s.send('WIND %s %s' % (x,y))

	def getState(self):
		print "Sending GET_STATE"
		self.s.send('GET_STATE')

		currentState = self.s.recv(1024)
		return currentState

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
		raw = currentState.split('\n')

		# remove the last \n from END_STATE
		# if not we get: IndexError: list index out of range
		raw = raw[:-1]

		if not "END_STATE" in raw:
			print "Missing END_STATE"

		state = {}
		state["rainclouds"] = []
		state["thunderstorms"] = []

		for i in raw:
			l = i.split()

			if l[0] == "BEGIN_STATE":
				state["interation"] = int(l[1])

			if l[0] == "YOU":
				state["you"] = int(l[1])

			if l[0] == "THUNDERSTORM":
				state["thunderstorms"].append({
					"px": float(l[1]),
					"py": float(l[2]),
					"vx": float(l[3]),
					"vy": float(l[4]),
					"vapor": float(l[5]),
					})

			if l[0] == "RAINCLOUD":
				state["rainclouds"].append({
					"px": float(l[1]),
					"py": float(l[2]),
					"vx": float(l[3]),
					"vy": float(l[4]),
					"vapor": float(l[5]),
					})

		return state

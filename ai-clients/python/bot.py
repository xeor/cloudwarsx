#!/usr/bin/env python

import random
from ai import AI

ai = AI()
ai.connect("127.0.0.1", 1986)
ai.name('oklien')
ai.start()
print "Game started!"

while 1:
	state = ai.getState()
	print state

	ai.wind(random.randint(-200,200), random.randint(-200,200))
	ai.sleep(5)

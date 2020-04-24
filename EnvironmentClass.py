# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:36:28 2020
"""

class Environment:

	def __init__(self, name, position, size, people_counter, infected_people, duration, capacity):
		'''Size  - tuple (x,y)'''
		self.position = position
		self.name = name
		self.size = size
		self.people_counter = 0
		self.infected_people = 0
		self.duration = duration
		self.capacity = capacity

class Transport(Environment):
	
	def __init__(self, name, position, size, people_counter, infected_people, duration, capacity, velocity):
		self.velocity = velocity

		super().__init__(name, position, size, people_counter, infected_people, duration, capacity)

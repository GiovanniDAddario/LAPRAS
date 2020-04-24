# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:16:53 2020

@author: Diganta
"""


class Person:

	def __init__(self,id,position, age, vulnerability, infection_status, compliance, commuter, possible_locations):
		self.id = id
		self.position = position
		self.age = age
		self.vulnerability = vulnerability
		self.infection_status = infection_status 
        # Infection status: 0=Not infected, 1=Infected, asymptomatic, 2=Infected, symptomatic, 3=immune/recovered
		self.compliance = compliance
		self.commuter = commuter
		self.possible_locations = possible_locations

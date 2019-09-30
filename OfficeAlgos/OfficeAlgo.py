import csv
import time
import datetime
import math 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import re

name = [] #array of names that sign in to hours 

outcsv = csv.writer(open("Updated_Office_hours_3.csv","w")) # Updated_Office_hours_(WEEK) enter the week to avoid overwriting
outcsv.writerow(['Name','time'])

for row in csv.DictReader(open("/Users/valazeinali/Desktop/Office hours/datafromoffice/Week 3.csv")): #put path of file here!
	date = row["date"] # gets date col values
	banner_id = row["banner"]

	if banner_id == "%810942089?":
		name = "Vala Zeinali"
	elif banner_id == "%810887137?":
		name = "Hannah Robinson"
	elif banner_id == "%810785323?":
		name = "Arian Sajjady"
	elif banner_id == "%810958290?":
		name = "Donny Wolford"
	elif banner_id == "%811015942?":
		name = "Brandon Taylor"
	elif banner_id == "%810886143?":
		name = "Spencer McCrea"
	elif banner_id == "%810866367?":
		name = "Thomas Beeler"
	elif banner_id == "%810940960?":
		name = "Claire Weihe"
	elif banner_id == "%810877372?":
		name = "Caroline Henneman"
	elif banner_id == "%810848210?":
		name = "Drake Wartmen"
	elif banner_id == "%810880467?":
		name = "Lauren Novick"
	elif banner_id == "%810943251?":
		name = "Laith Tabbaa"
	elif banner_id == "%810314681?":
		name = "Peter Kierstead"
	elif banner_id == "%810954700?":
		name = "Tiera Moore"
	elif banner_id == "%810878109?":
		name = "Keegan Lax"
	elif banner_id == "%811002660?":
		name = "Kaelee Dingey"
	elif banner_id == "%810888310?":
		name = "Aditi Vilas Tidke"
	elif banner_id == "%810972830?":
		name = "Janki Desai"
	elif banner_id == "%810951276?":
		name = "Connor Meehan"
	elif banner_id == "%810870996?":
		name = "Michael Klein"
	elif banner_id == "%810600348?":
		name = "Lance Stumpf"
	elif banner_id == "%810883717?":
		name = "Diamond Daniel"
	elif banner_id == "%810874825?":
		name = "Steven Farhart"
	elif banner_id == "%810910792?":
		name = "Thomas Niepsuj"
	elif banner_id == "%810908788?":
		name = "Alexis Springer"
	elif banner_id == "%810870890?":
		name = "Grace Braunlich"
	elif banner_id == "%810851807?":
		name = "Chanelle Waligura"
	else:
		name = banner_id

	outcsv.writerow([name,date])
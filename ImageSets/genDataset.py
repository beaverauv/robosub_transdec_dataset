#!/usr/bin/python
import os
import re
import random


def genTest():
	with open("traintest.txt") as f:
		dataset = f.readlines()
	with open("train.txt") as f:
		train = f.readlines()

	output = []

	for i in range(len(dataset)):
		found = False
		for j in range(len(train)):
			if dataset[i] == train[j]:
				found = True
			if found == False:
				output.append(dataset[i])

	outfile = open("test.txt", "w")
	for f in output:
		outfile.write(f) 

	outfile.close()


def genBuoySet():
	with open("traintest.txt") as f:
		dataset = f.readlines()

	trainList = []
	testList = []

	for i in range(len(dataset)):
		matches = re.search(r'GOPR0(\d{3})', dataset[i])
		if matches: 
			if 424 <= int(matches.group(1)) <=954:
				if random.random() < 0.8:#80% train
					trainList.append(dataset[i])
				else:
					testList.append(dataset[i])
	
	writeSetFile(trainList, "train.txt")
	writeSetFile(testList, "test.txt")
	

def genFullDataSet():
	directory = "../Images"
	files = [f for f in os.listdir("../Images") if os.path.isfile(os.path.join(directory, f))]

	trainList = []
	testList = []

	for f in files:
		if random.random() < 0.8:#80% train
			trainList.append(os.path.splitext(f)[0])
		else:
			testList.append(os.path.splitext(f)[0])

	writeSetFile(trainList, "train.txt")
	writeSetFile(testList, "test.txt")
	writeSetFile(testList + trainList, "traintest.txt")



def writeSetFile(images, filename):
	f = open(filename, "w")
	for i in images:
		f.write(i+"\n") 


genFullDataSet()

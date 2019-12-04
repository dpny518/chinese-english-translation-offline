#!/usr/bin/env python3

import re
import os.path
import sys
import csv


cedict_file =  './cedict_1_0_ts_utf-8_mdbg.txt'



def parse_cedict_file(filename):
	chinese_re = re.compile(r"""(?P<traditional>[\w・，○]+)\s+
								(?P<simplified>[\w・，○]+)\s+
								\[(?P<pinyin>.*)\]\s+
								/(?P<english>.*)/""", re.VERBOSE)
	cedict={}
	for line in open(filename):
		if line.startswith('#'): continue
		match = chinese_re.match(line)
		if match is None: continue

		traditional = match.group('traditional')
		simplified  = match.group('simplified')
		pinyin      = match.group('pinyin')
		english     = match.group('english')
		definitions = english.split('/')
		cedict[simplified]=definitions
	return cedict

#Get a list of keys from dictionary which has the given value

def getKeysByValue(dictOfElements, valueToFind):
	listOfKeys = list()
	listOfItems = dictOfElements.items()
	for listofitems  in listOfItems:
		for item in listofitems[1]:
			if item == valueToFind:
				listOfKeys.append(listofitems[0])
	return  listOfKeys

if __name__ == "__main__":
	cedict=parse_cedict_file(cedict_file)
	word=sys.argv[1]
	language=sys.argv[2]
	if language=='zh':
		print(cedict[word])
	if language=='en':
		print(getKeysByValue(cedict,word))

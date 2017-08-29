#!/usr/bin/env python
import sys
import re
import os

from_station=[]
to_station=[]
via_station=[]
value=[]
between_station=[]
flag=0
fp=open("output.txt","rU")
data=fp.readlines()
for line in data:
	lis=[]
	lis= re.findall(r'\w+', line)
	if(len(lis)>0):
		if((lis[0]=="amod" or lis[0]=="advmod")and lis[1]=="train"):
			value.append(lis[3])
		if(lis[0]=="prep_from" or lis[0]=="prepc_from" or( lis[0]=="pobj" and lis[1]=="from")):
			from_station.append(lis[3])
		if(lis[0]=="prep_to" or lis[0]=="prep_for" or lis[0]=="infmod" or(lis[0]=="pobj" and lis[1]=="to")):
			to_station.append(lis[3])
		if(lis[0]=="aux" and lis[3]=="to"):
			to_station.append(lis[1])
		if(lis[0]=="prep_via" or lis[0]=="prep_through" or(lis[0]=="pobj" and (lis[1]=="via" or lis[1]=="through"))):
			via_station.append(lis[3])
		if(lis[0]=="prep_between" or (lis[0]=="pobj" and lis[1]=="between")):
			flag=1
			between_station.append(lis[3])
if flag==0:
	if(len(from_station)==0):
		print "can i take falaknuma as the from station?\nyes or no"
		inp=raw_input()
		if(inp=="yes"):
			from_station.append("falaknuma")
		if(inp=="no"):
			print "please give the station from where you want the train\n"
			stat=raw_input()
			from_station.append(stat)
	if(len(to_station)==0):
		print "looks like you forgot to mention your destination :P\ncan you please give the destination"
		tostat=raw_input()
		to_station.append(tostat)
	if(len(value)!=0):
		print "so you want the"+value[0]+"train from"+from_station[0]+"to"+to_station[0]
	else:
		print "so you want trains from"+from_station[0]+"to"+to_station[0]
else:
	if(len(between_station)==0):
		print "between which two stations do you want to travel?"
		inp=raw_input()
		for word in inp:
			if(word!="and" and word!=","):
				between_station.append(word)
	if(len(between_station)==1):
		print "can you please mention the other station"
		inp=raw_input()
		between_station.append(inp)

print "from"
print from_station
print "to"
print to_station
print "via"
print via_station
print "between"
print between_station
print "flag==",flag
print "value"
print value

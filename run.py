#!/usr/bin/env python
import sys
import re
import os
from time import gmtime, strftime,localtime
import MySQLdb;
import cpspellcheck
import intro
import cluster
'''
1 - from to between variations
2 - after time so and so
3 - train #train number at
'''
def time_compare(a,b):
	hr1=a[0]+a[1]
	mn1=a[3]+a[4]
	hr2=b[0]+b[1]
	mn2=b[3]+b[4]
	if(hr1 < hr2):
		return 1
	elif (hr1 > hr2):
	 	return 2
	elif(hr1==hr2):
		if(mn1 < mn2):
			return 1
		elif(mn1 > mn2):
			return 2
		else:	
			return 0

time_list=[]
time_list2=[]
path=[]
path2=[]
ex_stat="hello"
before=0
after=0

def extract_station():
	words=ex_stat.split()
	for i in words:
		if word in all_station:
			return word

#HOW TO HANDLE STATION NAME WITH SPACES
RAJDHANI=["Ernakulam", "Ranchi", "Kanpur_Central", "Vadodara", "Raipur", "Patna", "Bhopal", "Chennai", "Ludhiana", "Dibrugarh", "Muzaffarpur", "Howrah", "Jaipur", "Nizamuddin", "Allahabad", "Katihar", "Bangalore", "Ahmedabad", "Jammu_Tawi", "Kota", "New_Jalpaiguri", "Ajmer", "Rajendranagar", "Lucknow", "Gaya", "Nagpur", "Dalton_Ganj", "Secunderabad", "Bilaspur", "Surat", "Vijayawada", "Dibrugarh_Town", "Mughalsarai", "New_Delhi", "Kanpur", "Barauni", "Durg", "Mumbai_Central", "Bokaro_Steel_City", "Sealdah", "Thiruvananthapuram", "Madgaon", "Guwahati", "Bhubaneswar", "Dhanbad"]

SHATABDHI=["Ranchi", "Jaipur", "Mysore", "Pune", "Vadodara", "Amritsar", "Jalandhar", "Moga", "Puri", "Malda_Town", "Bhopal", "Chandigarh", "Ludhiana", "Ambala_Cant.", "Howrah", "Kanpur_Central", "Kathgodam", "Bangalore", "Ahmedabad", "Bhubaneswar", "New_Jalpaiguri", "Ajmer", "Agra_Fort", "Lucknow", "Gwalior", "Katpadi", "Secunderabad", "Surat", "Chennai_Central", "New_Delhi", "Kanpur", "Bokaro_Steel_City", "Kalka", "Haridwar", "Dehradun", "Dhanbad", "Bharatpur", "Anand_Vihar_(T)", "Mumbai_Central", "Jhansi", "Agra"]

JANSHATABDHI=["Ernakulam", "Asansol", "Ranchi", "Barbil", "Raipur", "Sawai_Madhopur", "Raigarh", "Amritsar", "Patna", "Dimapur", "Manmad", "Chandigarh", "Ludhiana", "Mayiladuturai", "Howrah", "Jabalpur", "Dadar", "Nizamuddin", "Vijayawada", "Bangalore", "Jorhat_Town", "Ernakulam_Town", "Ambala_Cantt.", "Tenali", "Kottayam", "Kota", "Ratnagiri", "Madgaon", "Coimbatore", "Davangere", "Gaya", "Kharagpur", "Tiruchchirappalli", "Una", "Bilaspur", "Kannur", "Itarsi", "Chennai_Central", "New_Delhi", "Hubli", "Alappuzha", "Durg", "Shoranur", "Bokaro_Steel_City", "Haridwar", "Dehradun", "Thiruvananthapuram", "Kozhikode", "Gondia", "Kumbakonam", "Aurangabad", "Guwahati", "Habibganj", "Tatanagar", "Bhubaneswar"]	






query_type=0
bet_flag=0
from_station=[]
to_station=[]
via_station=[]
after_time=[]
before_time=[]
value=[]
between_station=[]
flag=0
via_flag=0
between_flag=0
tno=0
fp=open("output.txt","rU")
data=fp.readlines()
for line in data:
	lis=[]
	lis= re.findall(r'\w+', line)
#	lis=line.split()
	if(len(lis)>0):
#		print "i am in------------------"
#		print lis[0]
		if((len(lis)>=4) and lis[3]=="mmts"):
			intro.info()
			sys.exit();
		if(lis[0]=="prep_after" or (lis[0]=="pobj" and str(lis[1])=="after")):
			query_type=2
			after=1
			if(len(lis)>5):
				timer=lis[3]+':'+lis[4]
				after_time.append(timer)
			else:
				timer=lis[3]+':00'
				after_time.append(timer)
		if(lis[0]=="prep_before" or (lis[0]=="pobj" and str(lis[1])=="before")):
			query_type=2
			before=1
			if(len(lis)>5):
				timer=lis[3]+':'+lis[4]
				before_time.append(timer)
			else:
				timer=lis[3]+':00'
				before_time.append(timer)
		if(lis[0]=="nn" or lis[0]=="num" or lis[0]=="nsubj"):
			if(lis[0]=="num" or lis[0]=="nsubj"):
				tno=lis[-2]
			else:
				tno=lis[1]
		if(lis[0]=="prep_at" or lis[0]=="prepc_at"):
			query_type=3
			to_station.append(lis[3])
			from_station.append(lis[3])
			#print str(to_station[0])+" "+str(tno)
		if((lis[0]=="amod" or lis[0]=="advmod")and lis[1]=="train"):
			if(len(lis)>5):
				value.append(lis[4])
			else:
				value.append(lis[3])
		if(lis[0]=="prep_from" or lis[0]=="prepc_from" or (lis[0]=="pobj" and lis[1]=="from")):
			if(len(lis)>5):
#				if((lis[4] not in LF) and (lis[4] not in HF) and (lis[4] not in HF)):
#					clusstat=cluster.clus(lis[4])
#					print "there is no station at "+str(lis[4])+" taking the nearest station "+str(clusstat)
#					from_station.append(clusstat)
#				else:
					from_station.append(lis[4])

			else:
#				if((lis[3] not in LF) and (lis[3] not in HF) and (lis[3] not in HF)):
#					clusstat=cluster.clus(lis[3])
#					print "there is no station at "+str(lis[3])+" taking the nearest station "+str(clusstat)
#					from_station.append(clusstat)
#				else:
					from_station.append(lis[3])
#					print "yoyoyoyo"
#					print lis[3]
		if(lis[0]=="prep_to" or lis[0]=="prep_for" or lis[0]=="infmod" or(lis[0]=="pobj" and lis[1]=="to")):
			query_type=1
			if(len(lis)>5):
#				if((lis[4] not in LF) and (lis[4] not in HF) and (lis[4] not in HF)):
#					clusstat1=cluster.clus(lis[4])
#					print "there is no station at "+str(lis[4])+" taking the nearest station "+str(clusstat1)
#					to_station.append(clusstat1)
#				else:
					to_station.append(lis[4])
			else:
#				if((lis[3] not in LF) and (lis[3] not in HF) and (lis[3] not in HF)):
#					clusstat1=cluster.clus(lis[3])
#					print "there is no station at "+str(lis[3])+" taking the nearest station "+str(clusstat1)
#					to_station.append(clusstat1)
#				else:
					to_station.append(lis[3])
#					print lis[3]
		if(lis[0]=="aux" and lis[3]=="to"):
			to_station.append(lis[1])
		if(lis[0]=="prep_via" or lis[0]=="prep_through" or (lis[0]=="pobj" and lis[1]=="via") or (lis[0]=="pobj" and lis[1]=="through")):
			via_station.append(lis[3])
		if(lis[0]=="prep_between" or (lis[0]=="pobj" and lis[1]=="between")):
			query_type=1
			bet_flag=1
		#	flag=1
		#	print lis
		#	if((lis[3] not in LF) and (lis[3] not in HF) and (lis[3] not in HF)):
		#		clusstat=cluster.clus(lis[3])
				#print clusstat
	#			print "there is no station at "+str(lis[3])+" taking the nearest station "+str(clusstat)
	#			between_station.append(clusstat)
	#		else:
			if between_flag==0:
				from_station.append(lis[3])
				between_flag=1
			else:
				to_station.append(lis[3])
				between_flag=0
	#		between_station.append(lis[3])
		if(lis[0]=="conj_and"):
			to_station.append(lis[3])
#print from_station
#print to_station
#print via_station
#print value
#print before_time
#print after_time
def none():
	print "Please submit a valid query"
	return
if(len(from_station)==0 and len(to_station)==0 and len(via_station)==0 and len(value)==0 and before ==0 and after == 0):
	none()
	exit(0)

if(flag==0):
	'''
	if(len(from_station)==0):
		print "can i take Delhi as the from station?\nyes or no"
		inp=raw_input()
		if(inp=="yes"):
			from_station.append("Delhi")
		if(inp=="no"):
			print "please give the station from where you want the train\n"
			stat=raw_input()
			newstat=cpspellcheck.spelli(stat)
			if((newstat not in LF) and (newstat not in HF) and (newstat not in HF)):
				clusstat=cluster.clus(newstat)
#				print "there is no station at "+str(newstat)+" taking the nearest station "+str(clusstat)
				from_station.append(clusstat)
			else:
				from_station.append(newstat)
	if(len(to_station)==0):
		print "looks like you forgot to mention the destination :P\ncan you please give the destination"
		tostat=raw_input()
		newtostat=cpspellcheck.spelli(tostat)
		if((newtostat not in LF) and (newtostat not in HF) and (newtostat not in HF)):
			clusstat1=cluster.clus(newtostat)
#			print "there is no station at "+str(newtostat)+" taking the nearest station "+str(clusstat1)
			to_station.append(clusstat1)
		else:
			to_station.append(newtostat)
	if(len(value)!=0):
		print "so you want the "+str(value[0])+" train from "+str(from_station[0])+" to "+str(to_station[0])
		print "yes or no"
		response=raw_input()
		if(response=="no"):
			print "then plese give the required query"
			sys.exit();
	if(len(value)==0):
		print "so you want trains from "+str(from_station[0])+" to "+str(to_station[0])
		print "yes or no"
		response=raw_input()
		if(response=="no"):
			print "then plese give the required query"
			sys.exit();
	'''
	if(len(from_station)==0):
		from_station.append(to_station[0]);
	if(len(to_station)==0):
		to_station.append(from_station[0]);
	if((from_station[0] in RAJDHANI) and (to_station[0] in RAJDHANI)):
		if(len(via_station)>0):
			for x in via_station:
				if(x not in RAJDHANI):
					via_flag=1
	#	if(RAJDHANI.index(from_station[0]) < RAJDHANI.index(to_station[0])):
		if via_flag!=1:
			path.append("RAJDHANI")
	via_flag=0
	if((from_station[0] in SHATABDHI) and (to_station[0] in SHATABDHI)):
		if(len(via_station)>0):
			for x in via_station:
				if(x not in SHATABDHI):
					via_flag=1
	#	if(SHATABDHI.index(from_station[0]) < SHATABDHI.index(to_station[0])):
#			print "POKEMONNNNNNNNNNNNN"
		if via_flag!=1:
			path.append("SHATABDHI")
	via_flag=0
	if((from_station[0] in JANSHATABDHI) and (to_station[0] in JANSHATABDHI)):
		if(len(via_station)>0):
			for x in via_station:
				if(x not in HL):
					via_flag=1
	#	if(JANSHATABDHI.index(from_station[0]) < JANSHATABDHI.index(to_station[0])):
		if via_flag!=1:
			path.append("JANSHATABDHI")
#	if((from_station[0] in LH) and (to_station[0] in LH)):
#		if(len(via_station)>0):
#			for x in via_station:
#				if(x not in LH):
#					via_flag=1
#		if(LH.index(from_station[0]) < LH.index(to_station[0])):
#			path.append("LH")
#	if((from_station[0] in FH) and (to_station[0] in FH)):
#		if(len(via_station)>0):
#			for x in via_station:
#				if(x not in FH):
#					via_flag=1
#		if(FH.index(from_station[0]) < FH.index(to_station[0])):
#			path.append("FH")
#	if((from_station[0] in HF) and (to_station[0] in HF)):
#		if(len(via_station)>0):
#			for x in via_station:
#				if(x not in HF):
#					via_flag=1
#		if(HF.index(from_station[0]) < HF.index(to_station[0])):
#			path.append("HF")

else:
#	if(len(between_station)==2):
#		print "mention the other station"
#		inp=raw_input()
#		newinp=cpspellcheck.spelli(inp)
#		if((newinp not in LF) and (newinp not in HF) and (newinp not in HF)):
#			clusstat1=cluster.clus(newinp)
#			between_station.append(clusstat1)
#		else:
#			between_station.append(newinp)
	if((between_station[0] in RAJDHANI) and( between_station[1] in RAJDHANI)):
		if(len(via_station)>0):
			for x in via_station:
				if(x not in RAJDHANI):
					via_flag=1
		if(RAJDHANI.index(between_station[0])<RAJDHANI.index(between_station[1])):
			path.append("RAJDHANI")
			path2.append("RAJDHANI")
		#else:
		#	path.append("FH")
		#	path2.append("HF")
	if((between_station[0] in SHATABDHI) and( between_station[1] in SHATABDHI)):
		if(len(via_station)>0):
			for x in via_station:
				if(x not in SHATABDHI):
					via_flag=1
		if(SHATABDHI.index(between_station[0])<SHATABDHI.index(between_station[1])):
			path.append("SHATABDHI")
			path2.append("SHATABDHI")
#		else:
#			path.append("HL")
#			path2.append("LH")
	if((between_station[0] in JANSHATABDHI) and( between_station[1] in JANSHATABDHI)):
		if(len(via_station)>0):
			for x in via_station:
				if(x not in JANSHATABDHI):
					via_flag=1
		if(JANSHATABDHI.index(between_station[0])<JANSHATABDHI.index(between_station[1])):
			path.append("JANSHATABDHI")
			path2.append("JANSHATABDHI")
#		else:
#			path.append("LF")
#			path2.append("FL")

	from_station.append(between_station[0])
	from_station.append(between_station[1])

	

#print "path"
#print path
#print "from"
#print from_station
#print "to"
#print to_station
#print "via"
#print via_station
#print "between"
#print between_station
#print "value"
#print value
#print "before"
#print before_time
#print "after"
#print after_time
#print "flag==",flag
if(len(between_station)==0 and (from_station[0]==to_station[0])and len(from_station)!=0 and tno==""):

	print "check your question please"
	sys.exit();
if(len(between_station)!=0 and (between_station[0]==between_station[1])):
	print between_station
	print "check your question please"
	sys.exit();

Current_time=strftime("%H:%M", localtime())
db=MySQLdb.connect(host="localhost", 
		     user="root",
		     passwd="201101053", 
		     db="rail")


cur=db.cursor();
"""if(len(between_station)!=0):
	from_station.append(between_station[0])
	from_station.append(between_station[1])"""





#if(len(from_station)==0):
#	from_station.append("Faluknuma")
#print 'SELECT MIN'+(from_station[0]) +'FROM FL WHERE'+ from_station[0] + ">" + Current_time
def comp2(time1,time2,time3):
	if time1[-1]<time2[-1]:
		if time3[-1]>time1[-1] and time3[-1] < time2[-1]:
			return 1
		else:
			return -1
	else:
		return -1
def comp1(time1,time2):
	if time1[-1]<=time2[-1]:
		return 1
	else:
		return 2
	
c=0
if (len(value)==0):
	if(before==0 and after==0):
		value.append("next");
	else:
		value.append("all");
for i in range(len(path)):
	if query_type==3:
		if len(via_station)==0:
			cur.execute("SELECT Tno"+","+from_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL")
#			print "SELECT Tno"+","+from_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL"
			for row in cur.fetchall():
	#			print str(row[0])+str(tno)
				if(str(tno)==str(row[0])):
					print "Train "+str(row[0])+" arrives "+"at "+str(from_station[0])+" at " +str(row[1][:-2]);

		else:
			cur.execute("SELECT Tno"+","+from_station[0]+","+via_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL AND "+via_station[0]+" IS NOT NULL")
			for row in cur.fetchall():
				if(comp2(str(row[1]),str(row[2]),str(row[3]))==1 and str(tno)==str(row[0])):
					print "Train "+str(row[0])+" leaves "+str(from_station[0])+" at " +str(row[1][:-2])+" passes "+str(via_station[0])+" at "+str(row[2][:-2])
	if query_type==1:
		if len(via_station)==0:
			cur.execute("SELECT Tno"+","+from_station[0]+","+to_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL AND "+to_station[0]+" IS NOT NULL")
			for row in cur.fetchall():
				if(comp1(str(row[1]),str(row[2]))==1):
					if(from_station[0]==to_station[0]):	
						print "Train "+str(row[0])+" arrives at "+str(to_station[0])+" at "+str(row[2][:-2])
					else:
						print "Train "+str(row[0])+" leaves "+str(from_station[0])+" at " +str(row[1][:-2])+" and arrives at "+to_station[0]+" at "+str(row[2][:-2])

		else:
			cur.execute("SELECT Tno"+","+from_station[0]+","+to_station[0]+","+via_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL AND "+to_station[0]+" IS NOT NULL AND "+via_station[0]+" IS NOT NULL")
			for row in cur.fetchall():
				if(comp2(str(row[1]),str(row[2]),str(row[3]))==1):
					print "Train "+str(row[0])+" leaves "+str(from_station[0])+" at " +str(row[1][:-2])+" passes "+str(via_station[0])+" at "+str(row[3][:-2])+" and arrives at "+to_station[0]+" at "+str(row[2][:-2])
#	print after_time
	if query_type==2:
		if after==1:
			if len(via_station)==0:
				cur.execute("SELECT Tno"+","+from_station[0]+","+to_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL AND "+to_station[0]+" IS NOT NULL")

				for row in cur.fetchall():
					if(time_compare(row[1],after_time[0])==2):
						if(comp1(str(row[1]),str(row[2]))==1):
							if(from_station[0]==to_station[0]):	
								print "Train "+str(row[0])+" arrives at "+str(from_station[0])+" at " +str(row[1][:-2])
							else:
								print "Train "+str(row[0])+" leaves "+str(from_station[0])+" at " +str(row[1][:-2])+" and arrives at "+str(to_station[0])+" at "+str(row[2][:-2])
			else:
				#print "SELECT Tno"+","+from_station[0]+","+to_station[0]+","+via_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL AND "+to_station[0]+" IS NOT NULL AND "+via_station[0]+" IS NOT NULL"
				cur.execute("SELECT Tno"+","+from_station[0]+","+to_station[0]+","+via_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL AND "+to_station[0]+" IS NOT NULL AND "+via_station[0]+" IS NOT NULL")
				for row in cur.fetchall():
					if(time_compare(row[1],after_time[0])==2):
						if(comp2(str(row[1]),str(row[2]),str(row[3]))==1):
							print "Train "+str(row[0])+" leaves "+str(from_station[0])+" at " +str(row[1][:-2])+" passes "+str(via_station[0])+" at "+str(row[3][:-2])+" and arrives at "+to_station[0]+" at "+str(row[2][:-2])
		if before==1:
			if len(via_station)==0:
				cur.execute("SELECT Tno"+","+from_station[0]+","+to_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL AND "+to_station[0]+" IS NOT NULL")
				for row in cur.fetchall():
					if(time_compare(row[1],before_time[0])==1):
						if(comp1(str(row[1]),str(row[2]))==1):
							if(from_station[0]==to_station[0]):	
								print "Train "+str(row[0])+" arrives at "+str(from_station[0])+" at " +str(row[1][:-2])
							else:
								print "Train "+str(row[0])+" leaves "+str(from_station[0])+" at " +str(row[1][:-2])+" and arrives at "+str(to_station[0])+" at "+str(row[2][:-2])
			else:
				cur.execute("SELECT Tno"+","+from_station[0]+","+to_station[0]+","+via_station[0]+" FROM "+ path[i] +" WHERE "+from_station[0]+" IS NOT NULL AND "+to_station[0]+" IS NOT NULL AND "+via_station[0]+" IS NOT NULL")
				for row in cur.fetchall():
					if(time_compare(row[1],before_time[0])==1):
						if(comp2(str(row[1]),str(row[2]),str(row[3]))==1):
							print "Train "+str(row[0])+" leaves "+str(from_station[0])+" at " +str(row[1][:-2])+" passes "+str(to_station[0])+" at "+str(row[3][:-2])+" and arrives at "+via_station[0]+" at "+str(row[2][:-2])
#print time_list
		
'''
#	print Current_time
#	print from_station[0]
#	print "SELECT MIN("+from_station[0]+ ") FROM "+ path[i] +" WHERE "+ from_station[0] + ">" +"'"+Current_time+"'";
	if(value[0]=="next"):
		print "YOYOYOYOYO1"
		if(after==1):
			#from station 1 where time > some time
			cur.execute("SELECT MIN("+from_station[0]+ ") FROM "+path[i] +" WHERE "+ from_station[0] + ">" +"'"+after_time[0]+"'")
			for row in cur.fetchall():
				time_list.append(row[0])
			if(len(between_station)!=0):
				cur.execute("SELECT MIN("+from_station[1]+ ") FROM "+path2[i] +" WHERE "+ from_station[1] + ">" +"'"+after_time[0]+"'")
				for row in cur.fetchall():
					time_list2.append(row[0])
		else :
#			print "TESTING"
			
			print "SELECT Tno FROM "+ path[i] +" WHERE "+from_station[0]+"!=NULL AND "+to_station[0]+"!=NULL"
			cur.execute("SELECT Tno FROM "+ path[i] +" WHERE "+from_station[0]+"!=NULL AND "+to_station[0]+"!=NULL")
#			cur.execute("SELECT MIN("+from_station[0]+ ") FROM "+ path[i] +" WHERE "+ from_station[0] + ">" +"'"+Current_time+"'")
			for row in cur.fetchall():
				time_list.append(row[0])
			if(len(to_station)!=0):
				cur.execute("SELECT MIN("+to_station[0]+ ") FROM " +path[i]+ " WHERE "+ to_station[0] + ">" +"'"+Current_time+"'")
				for row in cur.fetchall():
					time_list2.append(row[0])
			if(c==0):
				c=c+1
				print '----------------'
				print 'The next train is at '
	elif(value[0]=="last"):
		print "YOYOYOYOYO2"
		if(before==0):
			cur.execute("SELECT MAX("+from_station[0]+ ") FROM "+path[i])
			for row in cur.fetchall():
				time_list.append(row[0])
			if(len(between_station)!=0):
				cur.execute("SELECT MAX("+from_station[1]+ ") FROM "+path2[i])
				for row in cur.fetchall():
					time_list2.append(row[0])
		if(before==1):
			cur.execute("SELECT MAX("+from_station[0]+ ") FROM " +path[i]+ " WHERE "+ from_station[0] + "<" +"'"+before_time[0]+"'")
			for row in cur.fetchall():
				time_list.append(row[0])
			if(len(between_station)!=0):
				cur.execute("SELECT MAX("+from_station[1]+ ") FROM " +path2[i]+ " WHERE "+ from_station[1] + "<" +"'"+before_time[0]+"'")
				for row in cur.fetchall():
					time_list2.append(row[0])
		if(c==0):
			c=c+1
			print '----------------'
			print 'The last train is at '
	elif (value[0]=="first"):
		print "YOYOYOYOYO3"
		if(after==0):
			cur.execute("SELECT MIN("+from_station[0]+ ") FROM "+path[i])
			for row in cur.fetchall():
				time_list.append(row[0])
			if(len(between_station)!=0):
				cur.execute("SELECT MIN("+from_station[1]+ ") FROM "+path2[i])
				for row in cur.fetchall():
					time_list2.append(row[0])
		if(after==1):
			print "SELECT MIN("+from_station[0]+ ") FROM "+path[i] +" WHERE "+ from_station[0] + ">" +"'"+after_time[0]+"'"
			cur.execute("SELECT MIN("+from_station[0]+ ") FROM "+path[i] +" WHERE "+ from_station[0] + ">" +"'"+after_time[0]+"'")
			for row in cur.fetchall():
				time_list.append(row[0])
			if(len(between_station)!=0):
				cur.execute("SELECT MIN("+from_station[1]+ ") FROM "+path2[i] +" WHERE "+ from_station[1] + ">" +"'"+after_time[0]+"'")
				for row in cur.fetchall():
					time_list2.append(row[0])

		if(c==0):
			c=c+1
			print '--------------'
			print 'the first train is at '

	#elif (len(between_station)!=0):
	#	cur.execute("SELECT 
	else:

		if(before==0 and after==0):
			cur.execute("SELECT "+from_station[0]+ " FROM "+path[i])
			for row in cur.fetchall():
				time_list.append(row[0])
			if(len(between_station)!=0):
				cur.execute("SELECT MAX("+from_station[1]+ ") FROM " +path2[i])
				for row in cur.fetchall():
					time_list2.append(row[0])
		if(before==1):
			cur.execute("SELECT "+from_station[0]+ " FROM " +path[i]+ " WHERE "+ from_station[0] + "<" +"'"+before_time[0]+"'")
			for row in cur.fetchall():
				time_list.append(row[0])
			if(len(between_station)!=0):
				cur.execute("SELECT "+from_station[1]+ " FROM " +path2[i]+ " WHERE "+ from_station[1] + "<" +"'"+before_time[0]+"'")
				for row in cur.fetchall():
					time_list2.append(row[0])
		if(after==1):
			cur.execute("SELECT "+from_station[0]+ " FROM "+path[i] +" WHERE "+ from_station[0] + ">" +"'"+after_time[0]+"'")
			for row in cur.fetchall():
				time_list.append(row[0])
			if(len(between_station)!=0):
				cur.execute("SELECT "+from_station[1]+ " FROM "+path2[i] +" WHERE "+ from_station[1] + ">" +"'"+after_time[0]+"'")
				for row in cur.fetchall():
					time_list2.append(row[0])


if(len(time_list)>0):
	print min(time_list)
else:
	print "there are no trains"
if(len(time_list2)>0):
	print "from "+from_station[0]+" to "+to_station[0]
	print min(time_list2)
	print "from "+to_station[0]+" to "+from_station[0]
'''

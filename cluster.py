#!/usr/bin/python

def clus(word1):

	lgpally = ['Gachibowli','HCU','Patancheruvu','BHEL']
	lakdi = ['Mehdipatnam','MasabTank','Nampally']
	hitech = ['Madhapur','Kukatpally','JNTU','KPHB']
	secunder = ['Tarnaka','Mushirabad']
	imp= ['Gachibowli','HCU','Patancheruvu','BHEL','Mehdipatnam','MasabTank','Madhapur','Kukatpally','JNTU','Tarnaka','Mushirabad']

	if word1 in imp:
#		print 'The from station mentioned does not have MMTS service'
#		print 'The nearest staion is--'
		if word1 in lgpally:
			return 'Lingampally'
		if word1 in lakdi:
			return 'Lakdikapul'
		if word1 in hitech:
			return 'HitechCity'
		if word1 in secunder:
			return 'Secunderabad'
#		print 'If you want to know details retype with the nearest station mentioned above'
"""def clus2(word2):

	lgpally= ['Gachibowli','HCU','Patancheruvu','BHEL']
	lakdi= ['Mehdipatnam','MasabTank']
	hitech= ['Madhapur','Kukatpally','JNTU']
	secunder= ['Tarnaka','Mushirabad']
	imp= ['Gachibowli','HCU','Patancheruvu','BHEL','Mehdipatnam','MasabTank','Madhapur','Kukatpally','JNTU','Tarnaka','Mushirabad']

	if word2 in imp:
        	print 'The to station mentioned does not have MMTS service'
       		print 'The nearest staion is--'
        	if word2 in lgpally:
                	print 'LINGAMPALLY'
        	if word2 in lakdi:
                	print 'LAKDIKAPOOL'
        	if word2 in hitech:
                	print 'HITECH CITY'
        	if word2 in secunder:
                	print 'SECUNDERABAD'
		print 'If you want to know details retype with the nearest station mentioned above'
 """                                                           

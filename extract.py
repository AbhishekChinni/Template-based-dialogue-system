#!/usr/env/python
import os
import sys
import subprocess
fp=open("output.txt","wa")
sentence = str(sys.argv[1][0:])
#sentence=raw_input()
#print sentence
os.popen("echo '"+sentence+"' > stanfordtemp.txt")
parser_out = os.popen("/home/abhishek/stanford-parser-2012-11-12/lexparser.sh stanfordtemp.txt").readlines()

'''
comm="/home/abhishek/stanford-parser-2012-11-12/lexparser.sh ~/stanfordtemp.txt"
p=subprocess.Popen(comm.split(" "),stdout=subprocess.PIPE);
op,err=p.communicate()
if(op):
	print op
if(err):
	print err
'''
for i, tag in enumerate(parser_out):
    if len(tag.strip()) > 0 and tag.strip()[0] == '(':
        parse = " ".join(tag.strip())
    elif len(tag.strip()) > 0:
#        fp.write(tag)
	print tag
#fp.close()
#bracketed_parse = " ".join( [tag.strip() for tag in parser_out if len(tag.strip()) > 0 and tag.strip()[0] == "("] )
#print bracketed_parse

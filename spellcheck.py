#!/usr/bin/python
import sys
flag=0
def edit(a,b):
	if(""==a):
		return len(b)
	if("" ==b):
		return len(a)
	return min(edit(a[:-1],b[:-1])+(a[-1]!=b[-1]),edit(a[:-1],b)+1,edit(a,b[:-1])+1)

def substring(a,b):
	a=a.lower()
	b=b.lower()
	maxi=0
	flag=0
	for i in range(0,len(a)):
		for j in range(i,len(a)):
			if a[i:j+1] in b:
				if j-i+1 > maxi:
					maxi=j-i+1
	return maxi

def spelli():
	f=open("corpus.c")
	lines=f.read()
	mini=10000
	answer=[]
	corp_words=lines.split()
	corp_words=list(set(corp_words))
#	print corp_words
	var=list(sys.argv)
	vari=var[1:]
	mapi={}
	for word in vari:
		for corp_word in corp_words:
#			print "YOYOYOYO" + corp_word
			if(word==corp_word):
				mapi[word]=1
				break
			else:
				mapi[word]=0


	for word in vari:
		output=word
		mini=10000
		flag=0
		maximum=0;
		max_corp_word=""
		for corp_word in corp_words:
			if(word.lower()[0]==corp_word.lower()[0]):
				if(len(word)<8):
					if(mapi[word]!=1):
						temp=edit(word,corp_word)
						if(temp<=mini):
							mini=temp
							output=corp_word
				else:
					check1=substring(word,corp_word)
					if(check1>maximum):
						max_corp_word=corp_word
						maximum=check1
					output=max_corp_word;
		if(flag!=1):
			answer.append(output)
	spell_checked=" ".join(answer)
	print spell_checked


def main():
	spelli()

if __name__== "__main__":
	main()


import sys 
import re


def extract_names(filename,fl):
	names=[]
	fine=open(filename,'r')	
	fine1=open(filename,'r')			#<h3 align="center">Popularity in 2006</h3>
	for line in fine1:
		match=re.search(r'([\w\.-]+)\sin\s(\d\d\d\d)',line)
		if(match):
			pop=str(match.group())
			break
	ymatch=re.search(r'\d\d\d\d',pop)
	if(ymatch):
		year=str(ymatch.group())	
	#print year

	x=fine.read()
	name=re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>',x)

	namesrank={}
	for row in name:
        	(rank, boy, girl) = row  # unpack the tuple into 3 vars
    		if boy not in namesrank:
      			namesrank[boy] = rank
    		if girl not in namesrank:
  			namesrank[girl] = rank
	
	sorted_names = sorted(namesrank.keys())

  	for name in sorted_names:
    		names.append(name + " " + namesrank[name])

	text = '\n'.join(names) + '\n'

	if(fl==0):
		fout=open(filename+".summary","w")
		fout.write(year+'\n')
		fout.write(text)
		fout.close()
	elif(fl==1):
		print year
		print text

        fine.close()
	fine1.close()
	
	



def main():
	if(len(sys.argv)<2):
		print "File has to be specified"
	else:
		if(sys.argv[1]=="-summaryfile"):
			f=sys.argv[2]
			fl=0
		else:
			f=sys.argv[1]
			fl=1
		extract_names(f,fl)


if __name__=='__main__':
	fl=0
	main()




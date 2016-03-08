''' 
Read the access_log and count the number of connection
''' 
count = dict()
#Inser the file name and choose the way of sort
tar = raw_input('Enter Filename:')                                      
cho = raw_input('Sort:(Max/Min)')


#Check the input variables
try:
	handle = open(tar)
except:
	print 'File cannot opened:',tar
	exit()


if cho == 'Max':
	op = True
elif cho == 'Min':
	op = False
else:
	print 'Wrong Command:',cho
	exit()
	
#Handle the access_log and count the number of connection each hour
for line in handle:
	if line.split()[3][1:].split(':')[0].split('/')[2]+'/'+line.split()[3][1:].split(':')[0].split('/')[1]+'/'+line.split()[3][1:].split(':')[0].split('/')[0]+'+'+line.split()[3][1:].split(':')[1]+':59:59~'+line.split()[3][1:].split(':')[1]+':00:00' not in count:
		count[line.split()[3][1:].split(':')[0].split('/')[2]+'/'+line.split()[3][1:].split(':')[0].split('/')[1]+'/'+line.split()[3][1:].split(':')[0].split('/')[0]+'+'+line.split()[3][1:].split(':')[1]+':59:59~'+line.split()[3][1:].split(':')[1]+':00:00']=1
	else:
		count[line.split()[3][1:].split(':')[0].split('/')[2]+'/'+line.split()[3][1:].split(':')[0].split('/')[1]+'/'+line.split()[3][1:].split(':')[0].split('/')[0]+'+'+line.split()[3][1:].split(':')[1]+':59:59~'+line.split()[3][1:].split(':')[1]+':00:00']=count[line.split()[3][1:].split(':')[0].split('/')[2]+'/'+line.split()[3][1:].split(':')[0].split('/')[1]+'/'+line.split()[3][1:].split(':')[0].split('/')[0]+'+'+line.split()[3][1:].split(':')[1]+':59:59~'+line.split()[3][1:].split(':')[1]+':00:00']+1

#Sort the dictionary by value

lst = list()
for key,val in count.items():
	lst.append((val,key))
	
lst.sort(reverse=op)

for key,val in lst:
	print val, key




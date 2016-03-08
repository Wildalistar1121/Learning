import re
s = 0
count = 0
tar = raw_input('Enter Filename:')
hand = open(tar)
count=0
for line in hand:
	line = line.rstrip()
	x = re.findall('([0-9]+)',line)

	for a in x: 
		
		count=count+1
		s=s+int(a)
print 'Sum',s
print 'Count',count
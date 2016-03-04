import urllib
import xml.etree.ElementTree as ET
sum = 0


address = raw_input('Enter location: ')

print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
tree = ET.fromstring(data)
tree2 = tree.findall('comments/comment')
print 'Count', len(tree2)
for item in tree2:
	sum = sum + int(item.find('count').text)
print 'Sum', sum
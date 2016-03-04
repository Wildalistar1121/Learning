import json
import urllib

counts = 0
Sum = 0
input = raw_input("Enter location:")

#info = json.loads(input)
print 'Retrieving', input
uh = urllib.urlopen(input)
data = uh.read()
print 'Retrieved', len(data), 'characters'
info = json.loads(data)


for item in info['comments']:
    counts = counts + 1
    Sum = Sum + int(item["count"])
print 'Counts', counts
print 'Sum', Sum
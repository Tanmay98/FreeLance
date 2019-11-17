import math
import sqlite3
import numpy as np 
import operator
import collections
import matplotlib.pyplot as plt 

how_many = input('How many earthquakes locations to show  ')

conn = sqlite3.connect('index2.sqlite')
conn.text_factory = str
cur = conn.cursor()
cur.execute("SELECT * from Earthquakes")
quakes_data = cur.fetchall()
data = []
data.append(quakes_data)

tsunami = []
depth = []
place = []
region = []
mag = []
felt = []
time = []
for i in data[0]:
	place.append(i[3])
	mag.append(i[2])
	time.append(i[1])
	felt.append(i[5])
	region.append(i[4])
	tsunami.append(i[6])
	depth.append(i[10])

placecounts = {}
regioncounts = {}
magcounts = {}
depthcounts = {}

for i in range(len(felt)):
	if felt[i] != None:			
		temp_dict = {region[i]:int(felt[i])}
		regioncounts.update(temp_dict)
		temp_dict2 = {region[i]:int(felt[i])}
		regioncounts.update(temp_dict2)

#sorted the regioncounts dict in ascending order
sorted_r = sorted(regioncounts.items(), key=operator.itemgetter(1))
sorted_regioncounts = collections.OrderedDict(sorted_r)
regions = list(sorted_regioncounts.keys())
counts = list(sorted_regioncounts.values())

X = []
y1 = []

for i in range(1, int(how_many)+1):
	X.append(regions[-i])
	y1.append(counts[-i])


plt.bar(X, y1)
plt.xlabel('Regions')
plt.ylabel('No. of earthquakes')
plt.title('First plot')
plt.show()

for i in range(len(mag)):
	if mag[i] != None:
		temp_dict3 = {region[i]:float(mag[i])}
		magcounts.update(temp_dict3) 

sorted_rr = sorted(magcounts.items(), key=operator.itemgetter(1))
sorted_magcounts = collections.OrderedDict(sorted_rr)
regionss = list(sorted_magcounts.keys())
mags = list(sorted_magcounts.values())

X2 = []
y2 = []
for i in range(1, int(how_many)+1):
	X2.append(regionss[-i])
	y2.append(mags[-i])

plt.scatter(X2,y2, label='skitscat', color='k', s=25, marker="o")
plt.xlabel('Regions')
plt.ylabel('Felt Magnitudes')
plt.title('Second plot')
plt.legend()
plt.show()

for i in range(len(depth)):
	if depth[i] != None:
		temp_dict4 = {region[i]:float(depth[i])}
		depthcounts.update(temp_dict4)

sorted_rrr = sorted(depthcounts.items(), key=operator.itemgetter(1))
sorted_depthcounts = collections.OrderedDict(sorted_rrr)
regionsss = list(sorted_depthcounts.keys())
depths = list(sorted_depthcounts.values())

X3 = []
y3 = []

for i in range(1, int(how_many)+1):
	X3.append(regionsss[-i])
	y3.append(depths[-i])

plt.scatter(X3,y3, label='skitscat', color='k', s=25, marker="o")
plt.xlabel('Regions')
plt.ylabel('Felt Earthquake depths')
plt.title('Third plot')
plt.legend()
plt.show()


# plt.xticks(rotation=90). you can rotate if you want










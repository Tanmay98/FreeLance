import math
import sqlite3
import numpy as np 
import operator
import collections
import statistics

while True:

	how_many = input('How many earthquakes locations to show or type EXIT to exit ')

	if how_many == 'EXIT':
		break

	elif int(how_many) >= 1 and int(how_many) <= 20:

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

		# print(place.count(data[0][687][1]))
		placecounts = {}
		regioncounts = {}

		for i in range(len(felt)):
			if felt[i] != None:			
				temp_dict = {place[i]:int(felt[i])}
				placecounts.update(temp_dict)
				temp_dict2 = {region[i]:int(felt[i])}
				regioncounts.update(temp_dict2)

		#sorted the placecounts dict in ascending order
		sorted_p = sorted(placecounts.items(), key=operator.itemgetter(1))
		sorted_placecounts = collections.OrderedDict(sorted_p)
		places = list(sorted_placecounts.keys())
		counts = list(sorted_placecounts.values())

		print('\nTop', how_many, 'earthquake regions are: \n')
		for i in range(1, int(how_many)+1):
			print(places[-i], ': ', counts[-i])

		print('\nBasic statistics')

		print('Number of earthquakes: ', len(mag))

		sum_mag = 0
		for i in range(len(mag)):
			sum_mag += mag[i]

		mean_mag = float(sum_mag)/float(len(mag))

		print('\n Mean magnitude: ', mean_mag)
		print('\n Median: ', statistics.median(sorted(mag)))
		print('\n StdDev: ', statistics.stdev(mag))

		npfilter_felt = np.array(felt)
		npfilter_tsunami = np.array(tsunami)
		npfilter_depth = np.array(depth)

		zero = [0]*len(felt)

		for i in range(len(felt)):
			if felt[i] == None or tsunami[i] == None or depth[i] == None:
				zero[i] = None
			elif int(felt[i]) > 0 or int(tsunami[i] > 0 or float(depth[i]) < 50):
				zero[i] = True
			else:
				zero[i] = False

		filterB = np.array(zero)

		print('\n Number of felt earthquakes: ', len(felt))
		sum_felt = 0
		for i in range(len(felt)):
			sum_felt += felt[i]

		mean_felt = float(sum_felt)/float(len(felt))
		print('\nMean Felt: ', mean_felt)
		print('\n Median: ', statistics.median(sorted(felt)))
		print('\n StdDev: ', statistics.stdev(felt))

	else:
		print('Enter number between 1 and 20')


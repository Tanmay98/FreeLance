import math
import numpy as np 

#1
def remainingvolume(l,w,h,r):
    volume_box = l*w*h
    volume_drill = math.pi * r**2 * h
    ans = volume_box - volume_drill

    return ans

#2
def fac(list1,list2,list3):
    profitability_list = list(np.array(list3) - np.array(list2))
    name = profitability_list.index(min(profitability_list))
    min_profitability = min(profitability_list)

    return list1[name], min_profitability

#3
def personalinfo(name,city,state,zipcode,address):
    print('Name: ' + name)
    print('City: ' + city)
    print('State: ' + state)
    print('ZipCode: ' + str(zipcode))
    print('Address: ' + address)

#4
def csvtotsv(name):
    import csv
    csv_file = name + '.csv'
    tsv_file = name + '.tsv'
    with open(tsv_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\t') for row in csv.reader(my_input_file)]
        my_output_file.close()

csvtotsv('person')
#5
def listname(name):
    minimum = min(name)
    maximum = max(name)
    summ = 0
    for i in name:
        summ+=i
    mean = summ/len(name)

    return minimum, maximum, mean

#6
def avgvel(list1, list2):
    time_intervals = []
    dist_intervals = []
    for i in range(len(list1)-1):
        time_intervals.append(list1[i+1]-list1[i])

    for j in range(len(list2)-1):
        dist_intervals.append(list2[j+1]-list2[j])

    avgvelocities = list(np.array(dist_intervals)/np.array(time_intervals))

    return avgvelocities



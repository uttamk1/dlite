# there are n gas station along a circular route where the amount of gas
# at the ith station is gas[i]
# you have a car with an unlimited gas tank and it costs cost[i]
# of gas to travel from the ith station to its next (i+1)th station, you begin the journey with an exmpty gas tank 
# at one of the gas stations.
# given two integer arrays gas and cost, return the staring gas station's index if you can travel around the 
# circuit once in the clockwise direction, otherwise return -1. if threr exists a solution, it is 
# gauranteed to be unique
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
totalgas = 0
currgas = 0
start = 0
for i in range(5):
    totalgas += gas[i] - cost[i]
    if currgas<0:
       start = i+1
       currgas = 0

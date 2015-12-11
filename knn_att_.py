# ATT dataset -----KNN program

import csv
import math
import operator

	            
#counts distance between test and trainig data
def countDistance(testPart, trainingPart, length):
	distance = 0
	for x in range(length):
		distance += pow((testPart[x] - trainingPart[x]), 2)
	return math.sqrt(distance)

# clloects near by data.  
def collectsNearby(trainingData, testInstance, k):
	distanceset = []
	length = len(testInstance)-1
	for x in range(len(trainingData)):
		distance = countDistance(testInstance, trainingData[x], length)
		distanceset.append((trainingData[x], distance))
	distanceset.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distanceset[x][0])
	return neighbors

#counts majority class of the neighbor
def finalResult(neighbors):
	majority = {}
	for x in range(len(neighbors)):
		predictedClass = neighbors[x][-1]# gets predicted class value
		if predictedClass in majority:
			majority[predictedClass] += 1
		else:
			majority[predictedClass] = 1
	majorityClass = sorted(majority.iteritems(), key=operator.itemgetter(1), reverse=True)
	return majorityClass[0][0]


# Open data file and divide it into test and training data. 
def openFile(filename, i, trainingData=[] , testData=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    data = list(lines)
	    for x in range(len(data)):
	        for y in range(644):
	            data[x][y] = float(data[x][y])
	        if x==(1+(i*2)) or x==(0+(i*2)):#Create testingdata
	            testData.append(data[x])
	        elif x%10==(0+(i*2)) or x%10==(1+(i*2)):#Create testingdata
	            testData.append(data[x])
	        else:# Create trainindata
	            trainingData.append(data[x])	
	
#counts accuracy of the predicted classes
def countAccuracy(testData, predict):
	correct = 0
	for x in range(len(testData)):
		if testData[x][-1] == predict[x]:
			correct += 1
	return (correct/float(len(testData))) * 100.0
	
# main function
def main():
	accuracy=0
	# loop for five folds 
	for i in range(5):
	   trainingData=[]
	   testData=[]
	   print('Round = '+str(i+1))
 	   openFile('D:\\UTA\\5334\\Proj 1\\att.csv', i, trainingData, testData)
           print 'Train set: ' + repr(len(trainingData))
           print 'Test set: ' + repr(len(testData))
           # generate predictions
           predict=[]
           k = 3 # kNN where k=3
           for x in range(len(testData)):
            	neighbors = collectsNearby(trainingData, testData[x], k)
           	result = finalResult(neighbors)
           	predict.append(result)
           accuracy += countAccuracy(testData, predict)
           print("Round accuracy: "+str(countAccuracy(testData,predict))+"%")
           print('--------------------------------------------------------------------------------------------')
        print(' Average Accuracy: ' + repr(accuracy/5) + '%')
	
main()
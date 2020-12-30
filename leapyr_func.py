def isYearLeap(year):
 #   if year % 400 == 0:
 #       return testResults[i]
 #   elif year % 100 == 0:
 #       return testResults[i]
    if year % 4 == 0:
        return testResults[i]

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
    
#testData = [1900, 2000, 2016, 1987]
#testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
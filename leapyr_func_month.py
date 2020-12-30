
def daysInMonth(year, month):
    if year % 4 == 0 and month == "Feb":
        
        testResults[i] = 29
        print("Leap year and has", +testResults[i],"days")
        return testResults[i]
        
    elif year % 4 != 0 and month == "Feb":
        
        print("Not a Leap year and has", +testResults[i], "days")
        testResults[i] = 28
        return testResults[i]
        
    elif year % 4 == 0 and month in ("Jan","Mar","May","July","Aug","Oct","Dec"):
        print("Leap year and has", +testResults[i], "days")
        testResults[i] = 31
        return testResults[i]
        
    elif year % 4 == 0 and month in ("Sep","Apr","Jun","Nov"):
        print("Leap year and has",+testResults[i], "days")
        testResults[i] = 30
        return testResults[i]
        
    elif year % 4 != 0 and month in ("Jan","Mar","May","July","Aug","Oct","Dec","Sep","Apr","Jun","Nov"):
        print("Not a Leap year")
         
        return testResults[i]
     
testYears = [1900, 2000, 2016, 1987]
testMonths = ["Jan", "Feb", "Mar","Apr"]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
import pandas as pd
import sys

#merge Sort algorithm
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the arr 
        L = arr[:mid] # getting the first half of the arr (the one smaller than the mid) 
        R = arr[mid:] # getting the second half of the arr (the one bigger than the mid) 
  
        mergeSort(L) # Sorting the first half in a recursive manner
        mergeSort(R) # Sorting the second half in a recursive manner
  
        i = j = k = 0 #initiliazing iterators
          
        # making temp arrays L[] & R[] and copying the data into them
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if all the elements were copied
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

#-----------------------------------------------
#binary Search algorithm
def binarySearch (arr, start, end, searchToken ): 
	while start <= end: 
  		
	        mid = start + (end- start) // 2 # calculating the mid value
	          
	        # Check if the wanted item is the mid value we return the mid item
	        if arr[mid] == searchToken or arr[mid].split()[0] == searchToken: 
	            return mid 

	 
	        # If If the wanted item is greater than the mid value, ignore left half (the values less than the mid value)
	        elif arr[mid] < searchToken: 
	            start = mid + 1
	  
	        # If If the wanted item is less than the mid value, ignore right half (the values greater than the mid value)
	        else: 
	            end = mid - 1
      
    # If the wanted item is does not exist we return -1  
	return -1

#-----------------------------------------------
#special binary Search algorithm for Function 5 in main menu
def specialBinarySearch(df, start_index):
  
    # Initialize 'first' and 'last' for Binary Search 
	first = 0
	last = start_index - 1
  
    # Perform binary Search iteratively 
	while first <= last:
		mid = (first + last) // 2
		if df[mid][1] <= df[start_index][0]:
			if df[mid + 1][1] <= df[start_index][0]:
				first = mid + 1
			else:
				return mid
		else: 
			last = mid - 1
	return -1
#-----------------------------------------------
#Function 1 in main menu
def employeSearch(df,employeName):
	employeeNames = df['Name'].tolist() # take the Name column from the dataframe and convert it to list 

	# sort the names list using mergeSort algorithm
	mergeSort(employeeNames)

	# search for the employeeName using binarySearch algorithm to find the first index that contain the desired name
	index = binarySearch(arr = employeeNames,start = 0,end = len(employeeNames)-1,searchToken = employeName)
	start = index
	end = index

	# check if there is more of the desired name 
	if len(employeName.split()) == 1:
		while employeeNames[start].split()[0] == employeeNames[start -1].split()[0]:
			start = start-1 # here we expand the search area by going towards index 0 to see if there is more of the same name

			# if we reached the very bigenning of the list then break
			if start <= 0:
				break
			
		while employeeNames[end].split()[0] == employeeNames[end +1].split()[0] :
			end = end +1 # here we expand the search area by going towards index n to see if there is more of the same name

			#if we reached the end of the list then break
			if end >= len(employeeNames)-1:
				break

		# print all the names that meet the name desired to be searched for
	print(df[df['Name'].isin(employeeNames[start:end+1])]) 

#-----------------------------------------------
#Function 2 in main menu
def viewDataSet(df,sortingProcedure):

	newDataFrame = pd.DataFrame(columns = ['Name','YearsExperience','Salary']) # create new data frame with column names (Name, YearExperience, Salary)

	# check on the wanted sorting procedure 
	if sortingProcedure == 'Name' or sortingProcedure == 'Salary':
		wantedProcedure = df[sortingProcedure].tolist() # convert the wanted sorting procedure column to a list 

		# sorting the list we just created using mergeSort algorithm
		mergeSort(wantedProcedure)

		# here we move the rows according to the sorted list to make the newDataFrame sorted the way the client wants
		for i in range(len(wantedProcedure)):
			newDataFrame.loc[i] = (df[df[sortingProcedure] == wantedProcedure[i]].values)[0]

		# we print the dataSet in Alpabetical order
		if sortingProcedure == 'Name':
			print(newDataFrame)
        
        #we print the top 5 most paid employess
		elif sortingProcedure == 'Salary':
			print(newDataFrame.iloc[-5: ,[0, 2]])

	# if the chosen sorting procedure is YearExperience we take the data frame as it is passed in the parameter because it is already sorted with YearsExperience
	# and then print the top 5 newest employees
	elif sortingProcedure == 'YearsExperience':
		newDataFrame = df
		print(newDataFrame.loc[:4, ['Name', 'YearsExperience']])

#-----------------------------------------------
#Function 3 in main menu
def maxNoOfEmployees(df,totalBudget):
	noOfEmployees = 0
	currentSalary = 0
	salaries = df['Salary'].tolist() # convert the Salary column to list 
	newDataFrame = pd.DataFrame(columns = ['Name','YearsExperience','Salary']) # create new data frame with column names (Name, YearExperience, Salary)

	# sorting the list we just created using mergeSort algorithm
	mergeSort(salaries)

	#adding the salaries to the currentSalary starting at the lowest salary in our list 
	for i in range(len(salaries)):
		currentSalary+=salaries[i]

		# we break if the totalBudget is passed by the currrent Salary 
		if currentSalary > totalBudget:
			break
		noOfEmployees+=1
		newDataFrame.loc[i] =df[df['Salary']==salaries[i]].values[0] # here we re-arrange the DataFrame according to the sorted Salary list

	# return the number of employees and the new data frame	
	return noOfEmployees,newDataFrame

#-----------------------------------------------
#Function 4 in main menu
def SalaryinGivenYOE(YOE):

	#Initialization of variables
	yoe=YOE
	juniorRank= 3.00
	seniorRank = 6.00
	expertRank= 9.00
	rank = ''
	leftToPromote = 0.00
	YOE = round(YOE)
	baseSalary = 40000
	currentSalary = [0 for i in range(0,YOE+1)] # we create a list of zeros with the same length as the variable YOE
	currentSalary[1] = baseSalary
	increseaRate = 0.15

	# we calculate the salary by multiplying it with the increase rate 
	for i in range (2,YOE+1):
		currentSalary[i] = currentSalary[i-1] + (currentSalary[i-1]*increseaRate)

	# we determine the position of the employee based on the variable yoe
	# the variable yoe is of type float so we have to make the numbers to combare float to get the accurate answer
	if yoe >= 0.00 and yoe < 3.00:
		rank = 'Entry Level'
		leftToPromote = juniorRank - yoe
	elif yoe >= 3.00 and yoe < 6.00:
		rank = 'Junior'
		leftToPromote = seniorRank - yoe
	elif yoe >= 6.00 and yoe < 9.00:
		rank = 'Senior'
		leftToPromote = expertRank - yoe
	else:
		rank = 'expert'
		leftToPromote = 0

	#we return the salary after the increase rate , the position of the employee, and the years left to promote
	return currentSalary[YOE],rank,leftToPromote

#-----------------------------------------------
#Function 5 in main menu
def TaskAcceptance(df):
	arr = df.values.tolist() # converting the dataframe to list of lists

	job = sorted(arr, key = lambda arr: arr[1]) # sorting the list based on the endDay column
		
	length = len(job)
	schedule = [0 for i in range(length)] #creating list of zeros with the length of the job list
	
	#initializing more variables
	schedule[0] = job[0][2]
	jobSchedule = []
	jobSchedule.append([1])

	for i in range(1, length): 
  
        # Find profit including the current job by adding the non overlapping jobs to each other 
		jobProfit = job[i][2]
		l = specialBinarySearch(job, i)
		if (l != -1):
			jobProfit += schedule[l]			

        # Store maximum of the job profit we just calculated and the one calculated in the last iteration
		schedule[i] = max(jobProfit, schedule[i - 1])
		
		if (schedule[i] == schedule [i-1]):
			jobSchedule.append(jobSchedule[l-1]) 
		else:
			jobSchedule.append([l+1,i+1])
		newList = [0 for i in range(len(jobSchedule))]   
        
	for i in range(0,len(jobSchedule)):
		if(jobSchedule[i][0] != 1):
			index = jobSchedule[i][0] -1 
			temp = jobSchedule[i][-1]
			newList[i] = newList[index].copy()
			newList[i].append(temp)
		else:
			newList[i] = jobSchedule[i].copy()
	return schedule[length-1], newList[length-1]
#-----------------------------------------------
#The Main Function containing the main menu, the function calls and the dataframes needed.
def main():
	arr = pd.read_csv('D:\\Study\\Analysis of Algorithms\\project\\New\\Employee_dataset.csv')
	arr2 = pd.read_csv('D:\\Study\\Analysis of Algorithms\\project\\New\\Tasks_dataset.csv')
	print('Hello to our employee assigment service')
	print('---------------------------------------')
	print('Choose one of the following services:')
	print('(N.B. 1 for first service | 2 for second .. etc)')
	print('------------------------------------------------')
	print('1- Employees searching service')
	print('2- Employees browse service')
	print('3- Maxmium employees for specific budget service')	
	print('4- Employee current rank with the current salary based on years of experince service')
	print('5- Task Acceptance Service')
	print('6- exit from system')
	print('------------------------------------------------')
	userInput = int(input('Enter your choosen service: '))
	if userInput == 1 :
		employeSearch(arr,""+input('Enter employee name'))
	elif userInput == 2:
		viewDataSet(arr,""+input("Enter your sorting procedure:\nName (result: will print the employee in alphabetical order \nSalary (result: will print the top 5 most paid employees\nYearsExperience (result: will print the newest 5 employess): "))
	elif userInput == 3:
		noOfEmp,empDataSet= maxNoOfEmployees(arr,int(input("Enter your specific budget: ")))
		print("The maxmium number of employees according to your budget: "+str(noOfEmp))
		print("-------------------------------------------------------------------")
		print(empDataSet)	
	elif userInput == 4:
		currentSalary,Rank,leftToPromote = SalaryinGivenYOE(int(input("enter the employee's years of experince: ")))
		print("The Employee position: "+Rank)
		print("The current salary based on the position: "+str(currentSalary))
		if leftToPromote == 0:
			print("There is no higher position")

		else:
			print("Years left to get promoted: "+str(leftToPromote))
	elif userInput == 5:
		maximumProfit,tasksAccepted = TaskAcceptance(arr2)
		print("The maximum Profit that can be achieved is: "+str(maximumProfit))
		print("And the tasks accepted to achieve the maximum profit are: "+str(tasksAccepted))
	else:
		sys.exit(0) 	
if __name__ == '__main__':
		main()


"""
Chapter 4 practice project.
Program: payroll2.py
Author: Joseph Reccardo 6/28/2023
Description: Payroll application that reads employee data from a txt file and outputs payroll info in tabular format.
"""

#Input Phase
fileName = input("Please provide the name of the employee file that you wish to use: ")

#Processing Phase
data = open(fileName, "r")

#Output Phase
print()
print("%-18s%9s%9s%10s" % ("Emplyee Name", "Wage", "Worked", "Earnings"))
print("-" * 47)

#Loop through the file data line by line. Split up the data from each line. Place each component into tabular format.
for line in data:
	
	#Break the line into individual string values.
	dataArray = line.split()
	
	# extract the last name from that array and store it(in the memory of our application).
	name = dataArray[0]

	#extract the Hourly wage from the array, convert it to a float, and store it.
	wage = float(dataArray[1])

	#extract hours worked from array, convert it to a float, and store it.
	hours = float(dataArray[2])

	#Calculate the earnings and store it (creating a new variable).
	earnings = wage * hours

	#output the employee's info in tabular format.
	print("%-18s%9.2f%9.2f%10.2f" % (name, wage, hours, earnings))

#Final sign off, and dummy prompt
input("\nAll data is shown on screen, press ENTER to exit.")
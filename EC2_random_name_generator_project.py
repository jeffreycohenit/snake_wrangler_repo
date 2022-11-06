#!/usr/bin/env python3.7

# Adding python libraries
import random
import string

# Define function to generate random names
def server_name(size=5, string=string.ascii_letters + string.digits):    
    return ''.join(random.choice(string) for _ in range(size))

# Only the below three departments can use this program
print("EC2 Name Generator Program")
print("------------------------------------------")
department = input("Please enter your department name (Marketing, Accounting, FinOps): ")

for _ in department:
    if department == "Marketing" or department.lower() == "marketing" :
        print("Checking your permissions....")
        break
    elif department == "Accounting" or department.lower() == "accounting" :
        print("Checking your permissions....")
        break
    elif department == "FinOps" or department.lower() == "finops" :
        print("Checking your permissions....")
        break
    else:
        print("Error: Your department does not have permission.  Please appropriate department. If you have any questions, please reach out to the IT department. ")
        department = input("Enter department: Marketing, Accounting, FinOps: ")  

# How many EC2 instances do you need a unique name for
number = int(input("Enter number of EC2 instances with a unique name: "))

# Print results from function
print("Creating your unique EC2 instance names.... ")

for _ in range(1, number + 1):
    request_EC2_name = department
    new_EC2_name = request_EC2_name + "_" + server_name()
    print("Your unique EC2 Instance name: ", new_EC2_name)
#!/usr/bin/env python3.7

# Make an empty list 

my_list_of_aws_services = []

# insert data into list 

my_list_of_aws_services.append('EC2')
my_list_of_aws_services.append('S3')
my_list_of_aws_services.append('IAM')
my_list_of_aws_services.append('VPC')
my_list_of_aws_services.append('DynamoDB')
my_list_of_aws_services.append('Lambda')
my_list_of_aws_services.append('RDS')
my_list_of_aws_services.append('CloudFormation')
my_list_of_aws_services.append('CloudWatch')
my_list_of_aws_services.append('CloudTrail')

# print the list and the length of the list

print(my_list_of_aws_services)
print(len(my_list_of_aws_services))

# remove two specific services from the list by name or by index

del my_list_of_aws_services[3]
del my_list_of_aws_services[5]

# print the new list and the new length of the list

print(my_list_of_aws_services)
print(len(my_list_of_aws_services))
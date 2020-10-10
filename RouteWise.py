#loading the Data Set, this compound Commands are still not completely understood
import csv
with open('EmployeeBusRequirement.csv') as f:
    a=[{k.rstrip():v.rstrip() for k,v in row.items()} for row in csv.DictReader(f,skipinitialspace=True)]
#print(a)
#print(a[0].keys())
#print(a[0].values())
employee_on_route ={}
for employee in a:
    if employee['BUS ROUTE'] in employee_on_route.keys():
        employee_on_route[employee['BUS ROUTE']]=employee_on_route[employee['BUS ROUTE']]+1
    else :
        employee_on_route[employee['BUS ROUTE']]=1
print(employee_on_route)



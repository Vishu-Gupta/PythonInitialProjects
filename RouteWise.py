#loading the Data Set, this compound Commands are still not completely understood
import csv
import math
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
#print(employee_on_route)
bus_capacity = int(input('Please enter the max no of people allowed per bus\n'))
print("Bus plan can be as follows\n")
for route in employee_on_route.keys():
    pax_no= employee_on_route[route]
    bus_req=math.ceil(pax_no/bus_capacity)
    utilization = pax_no*100/(bus_capacity*bus_req)
    employee_on_route[route]={"Pax":pax_no,"req_buses":bus_req,"filling":utilization}
    print(f'For {route},{bus_req} bus(es) will be required to cater to {pax_no} employee(s), in which filling will be {utilization:0.1f} %')
    #print(pax_no)

    




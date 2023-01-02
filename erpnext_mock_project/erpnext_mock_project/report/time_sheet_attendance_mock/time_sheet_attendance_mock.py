# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime


def execute(filters=None):
	return get_columns(), get_data(filters)

def get_columns():
    return [
		"Employee ID:Data/Employee:150",
		"Employee Name:Data/Employee:150",
		"No of Days in a month:Int/Employee:150",
		"Total working Days:Int/Employee:150",
		"Present Days:Int/Employee:150",
		"Absent:Int/Employee:150",
		"no. Half Day:Int/Employee:150",
		"Shift:Day/Employee:150",
	]
    
def get_data(filters):

    dateFrom = filters.get("from")
    dateto = filters.get("to")
    employeeName = filters.get('employee')
    noPresent = 0
    noAbsent = 0
    noHalfDay = 0
    condStr =f"AND  employee = '{employeeName}'"

    # if filters.get('shift') != None :
    #     condStr += f" AND {filters.get('shift')}"

    # print(f"{condStr}\n {filters.get('status')}")
    
    data = frappe.db.sql(f"Select count(status) as count, status, employee_name, employee, shift  from tabAttendance where (attendance_date between '{dateFrom}' and '{dateto}' )  {condStr} group by status ", as_dict=True)

    noHolidays =  frappe.db.sql(f"Select count(*) as hoildays from tabHoliday where (holiday_date between '{dateFrom}' and '{dateto}')") ;
    
    
    dateFrom = datetime.strptime(dateFrom, "%Y-%m-%d")
    dateto = datetime.strptime(dateto, "%Y-%m-%d")
    noDays = dateto - dateFrom    # Total days
    noActualWorkDays = noDays.days - noHolidays[0][0] #nAD = tD - nH
    
    for val in data:
      if val.status == "Absent":
        noAbsent = val.count
      elif val.status == "Half Day":
        noHalfDay = val.count
      else:
        noPresent = val.count
    try :
      
          dataToReturn = [
            (data[0].get('employee'),data[0].get('employee_name'),noDays.days,
            noActualWorkDays,noPresent,noAbsent,noHalfDay,data[2].get('shift'))
            ]
    except :
        dataToReturn = []
        

        
    return dataToReturn
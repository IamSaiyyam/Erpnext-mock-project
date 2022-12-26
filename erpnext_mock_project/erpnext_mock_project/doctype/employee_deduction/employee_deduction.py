# Copyright (c) 2022, Saiyyam Chhetri and contributors
# For license information, please see license.txt

import frappe, calendar
from frappe.model.document import Document

class EmployeeDeduction(Document):
	def validate(self): pass
		
		# for val in self.deduction_detail:
		# 	monthNo = val.end_date.split("-")
		# 	month = calendar.month_abbr[int(monthNo[1])]
		# 	MonthName = f"{month}-{monthNo[0]}"

		# 	dCalculation = frappe.get_doc({'doctype': 'Deduction Calculation', 
        #                         'month':MonthName,
        #                         'onetime': val.amount,
        #                         'parent' : self.name,
        #                         'parentfield' : 'deduction_calculation',
        #                         'parenttype' : 'Employee Deduction',
        #                         })

		# dCalculation.insert()
		# frappe.db.commit()
		# print(f'data :\n{}')
		
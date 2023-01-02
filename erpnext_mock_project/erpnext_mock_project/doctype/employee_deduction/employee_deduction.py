# Copyright (c) 2022, Saiyyam Chhetri and contributors
# For license information, please see license.txt

import frappe, calendar, datetime
from frappe.model.document import Document

class EmployeeDeduction(Document):pass

@frappe.whitelist()
def get_account_details(dataDetails):
    doc = frappe.parse_json(dataDetails)
    item = frappe.parse_json(doc.item)
    dCalculation = frappe.parse_json(doc.dCalculation)

    recurring = False if item.deduction_type == "Onetime" else True
    response = frappe.db.get_value("Deduction Detail", item.name,"*")

    if(response == None and dCalculation == None):
        return addRow(doc)
    else:

        if(len(dCalculation)):
            print("In ChildTable If")
            return addRow(doc,dCalculation)
        else:
            print("In ChildTable else..")
            
            addRow(doc,response)

def checkMonthExist(doc2, monthName, doc, amount=0):

    obj = False
    doc = frappe.parse_json(doc.item)
    for itemDict in doc2:
        item = frappe.parse_json(itemDict)

        if item.month == monthName : 
            if amount !=0 :
                return addCalculation(doc, item, amount)

            return addCalculation(doc, item, doc.amount)

        else : False

    return obj

def addCalculation(doc, doc2, amount):

    doc = frappe.parse_json(doc)
    doc2 = frappe.parse_json(doc2)
    if doc.deduction_type == "Onetime":
        doc2.onetime =  doc2.onetime + amount

    else:
        doc2.recurring =  doc2.recurring + amount

    doc2.total = doc2.recurring + doc2.onetime
    doc2.balance = doc2.total - doc2.actual_paid_amount
    
    obj = {
        "idx":doc2.idx,
        "data" : doc2
    }
    return obj

def monthNameMaker(dateOf):
    try:
        datetime_str = datetime.datetime.strptime(dateOf, '%Y-%m-%d')
    except:
        datetime_str = dateOf

    datetime_str = f"{calendar.month_abbr[datetime_str.month]}-{datetime_str.year}"
    return datetime_str

def addRow(doc, doc2 = None):
    item = frappe.parse_json(doc.item)
    monthName = monthNameMaker(item.start_date)
    obj = []
    val = frappe.db.get_value("Deduction Calculation",{'month':monthName, 'parent':doc.empID},"*")
    if(val):
        pass
    else:
        if item.deduction_type == "Onetime":
            if doc2 != None:
                val = checkMonthExist(doc2, monthName, doc)
                if(val):
                    obj.append(val)
                else:
                    obj.append(creatDCObj(monthName, item.amount, False))
            else:
                obj.append(creatDCObj(monthName, item.amount, False))
        else:
            end = datetime.datetime.strptime(item.end_date, '%Y-%m-%d')
            start = datetime.datetime.strptime(item.start_date, '%Y-%m-%d')
            res = ((end.year - start.year) * 12 + (end.month - start.month))+1
            amount = item.amount/res
            index = start.month
            yearIndex = start.year
            
            for i in range(res):
                if doc2 != None:
                    val = checkMonthExist(doc2, monthName, doc, amount)
                    if(val):
                        obj.append(val)
                    else:
                        obj.append(creatDCObj(monthName, amount, False))
                else:

                    obj.append(creatDCObj(monthName, amount, True))

                index = 1 if index == 12 else start.month + 1
                yearIndex = yearIndex+1 if index == 1 else yearIndex
                start = start.replace(year = yearIndex, month=index,day=1)
                monthName = monthNameMaker(start)
    return obj        

def creatDCObj(monthName,amount, recurring):
    
    obj = {
        "month" : monthName,
        "total" : amount,
        "onetime" : 0,
        "recurring" : 0,
        "balance" : amount,
        "actual_paid_amount" : 0
    }

    returnObj = {
        "idx":None,
        "data" : obj
    }
    totalAmount = 0

    if(recurring):
        obj["recurring"] = amount
    else:
        obj["onetime"] = amount

    totalAmount = int(obj["recurring"]) + int(obj["onetime"])
    obj["balance"] = totalAmount
    obj["total"] = totalAmount

    return returnObj
import frappe, json
# methods="POST"
@frappe.whitelist()
def checkNameExist(val = None):
    return frappe.db.get_value("Deduction Detail", val, ["name","deduction_type","start_date", "end_date" ,"amount"])

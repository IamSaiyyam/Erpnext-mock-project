// Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Time_sheet Attendance Mock"] = {
	"filters": [

		{
			"fieldname":"from",
			"label": __("From"),
			"fieldtype": "Date",
			"default": frappe.datetime.month_start(),
			"reqd": 1
		},
		{
			"fieldname":"to",
			"label": __("To"),
			"fieldtype": "Date",
			"default": frappe.datetime.month_end(),
			"reqd": 1
		},
		{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options":"Employee",
			"reqd": 1
		},
		{
			"fieldname":"shift",
			"label": __("Shift"),
			"fieldtype": "Select",
			"options":["Day","Night"],
			"reqd": 0
		}
	]
};

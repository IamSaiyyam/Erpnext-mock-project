// Copyright (c) 2022, Saiyyam Chhetri and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Deduction', {
	refresh:(frm)=>{
		callCulateAmount(frm)
	},
	employee:(frm)=>{
		frappe.db.get_value("Employee", frm.doc.employee, "employee_name", (data)=>{
			frm.set_value("employee_name",data.employee_name)
		})
	}

});

frappe.ui.form.on('Deduction Detail', {
	start_date:(frm)=>{
		let item = frm.selected_doc

		if(item.deduction_type == "Onetime"){

			let dateFrom = new Date(item.start_date);
			let lastDayOfMonth = new Date(dateFrom.getFullYear(), dateFrom.getMonth()+1, 0);
			lastDayOfMonth = `${lastDayOfMonth.getFullYear()}-${parseInt(lastDayOfMonth.getMonth())+1}-${lastDayOfMonth.getDate()}`

			frappe.model.set_value("Deduction Detail", item.name, "end_date", lastDayOfMonth)				
		}
	},

	amount:(frm)=>{
		let dCalculation = (frm.doc.deduction_calculation == undefined)? null : frm.doc.deduction_calculation
		let data = {
			"item":frm.selected_doc,
			"empID" :  frm.doc.employee,
			"dCalculation" : dCalculation
		}

		// console.log(data)

		frappe.call({
			method:"erpnext_mock_project.erpnext_mock_project.doctype.employee_deduction.employee_deduction.get_account_details",
            type:"POST",
            args:{dataDetails : data},
            callback:(response)=>{

				console.log(response.message)

				for(let item of response.message){
					if (item.idx != null){
						let row = frm.doc.deduction_calculation[item.idx-1] 
						row.onetime  =  item.data.onetime
						row.recurring = item.data.recurring
						row.actual_paid_amount = item.data.actual_paid_amount
						row.total = item.data.total
						row.balance =  item.data.balance
					} else {
						frm.add_child('deduction_calculation', item.data)
					}
				}

				frm.refresh_field('deduction_calculation');
				callCulateAmount(frm)
			}
		})
	}
	
});

frappe.ui.form.on("Deduction Calculation",{
	actual_paid_amount:(frm)=>{
		let row = frm.selected_doc
		row.balance = row.total - row.actual_paid_amount
		frm.refresh_field('deduction_calculation')
		callCulateAmount(frm)
		frm.refresh_field('deduction_calculation')
	}
})

function callCulateAmount(frm){
	
	let currMonth = new Date(), currMonthAmt = 0, totalAmount = 0
	
	if(frm.doc.deduction_calculation == undefined){
		return
	}
	for(let row of frm.doc.deduction_calculation){
		let monthName = new Date(row.month)
		
		if(currMonth >= monthName){
			totalAmount += row.balance
		}
		if((currMonth.getFullYear() == monthName.getFullYear()) && (currMonth.getMonth() == monthName.getMonth())){

			currMonthAmt += row.balance
		}
	}

	frm.set_value("total_balance",totalAmount)
	frm.set_value("current_month_balance",currMonthAmt)

	frm.refresh_field('employee_deduction');
}
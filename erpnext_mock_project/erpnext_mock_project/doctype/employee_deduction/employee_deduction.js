// Copyright (c) 2022, Saiyyam Chhetri and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Deduction', {
	
	refresh:(frm)=>{

		callCulateAmount(frm)	},

	employee:(frm)=>{
		frappe.db.get_value("Employee", frm.doc.employee, "employee_name", (data)=>{
			frm.set_value("employee_name",data.employee_name)
		})
	}

});

frappe.ui.form.on('Deduction Detail', {
	
	start_date:(frm)=>{
		$.each(frm.doc.deduction_detail, (idx, item)=>{
			let today = new Date(item.start_date);
			let lastDayOfMonth = new Date(today.getFullYear(), today.getMonth()+1, 0);
			
			let lastDayOfMonthObj = `${lastDayOfMonth.getFullYear()}-${parseInt(lastDayOfMonth.getMonth())+1}-${lastDayOfMonth.getDate()}`
			
			if(item.deduction_type == "Onetime"){
				frappe.model.set_value("Deduction Detail", item.name, "end_date", lastDayOfMonthObj)				
			}
		})	
	},
	end_date: (frm)=>{
		let dateTo = new Date(frm.selected_doc.end_date), dateFrom = new Date(frm.selected_doc.start_date)
		if(dateFrom > dateTo){
			frappe.throw("Please enter the valid end date!")
		}
	
	},
	amount:(frm)=>{

		if(frm.selected_doc.amount <= 0){
			frappe.throw("Please enter the valid amount!")
		}
		frappe.call(
			{
				method:"erpnext_mock_project.erpnext_mock_project.doctype.api.checkNameExist",
				type:"POST",
				args:{val : frm.selected_doc.name},
				callback:(r)=>{

					// When  Row is edited in DDetails
					if(r.message !== undefined){
						let temp =  frm.selected_doc.amount
						frm.selected_doc.amount =  frm.selected_doc.amount - r.message[4] 
						addRow(frm, true)
						frm.selected_doc.amount = temp
						frm.refresh_field('deduction_calculation');
					} else{
						//When there is new row add in DDetails
						
						if(checkRowExist(frm)){
							//Compare and Update DCalculation Table
							addRow(frm, true)
						} else{
							// Directly add Data in  DCalculation Table
							addRow(frm)
						}
					}
				}
			})
	}	
});

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

function checkRowExist(frm){
	if(frm.doc.deduction_calculation == undefined){
		return
	}
	return frm.doc.deduction_calculation.length;
	
}

function editRow(frm,idx, amount, recurring = false){
	idx -= 1
	let item = frm.doc.deduction_calculation[idx], temp
	
	if(!recurring){
		temp = item.onetime
		temp += amount
		item.onetime = (item.onetime == 0)? Math.abs(amount):temp

	}	else{
		temp = item.recurring
		temp += amount
		item.recurring = (item.recurring == 0)? Math.abs(amount):temp
	}

	item.total = item.recurring + item.onetime
	item.balance = item.recurring + item.onetime

	frm.refresh_field('deduction_calculation')
}

function addObj(monthName, frm, amount, recurring = false){
	amount = Math.abs(amount)
	let obj = {
		"month" : monthName,
		"total" : amount,
		"balance" : amount,
		"actual_paid_amount" : 0
	} 
	if(!recurring){
		obj['onetime'] = amount
		obj['recurring'] = 0
	
	}	else{
		obj['onetime'] = 0
		obj['recurring'] = amount
	}
	
	frm.add_child('deduction_calculation', obj)
	frm.refresh_field('deduction_calculation');

}

function addRow(frm, edit=false){

	let  dateTo = new Date(frm.selected_doc.end_date),dateFrom = new Date(frm.selected_doc.start_date)
	,monthName,month, monthDiffIndex, monthNo, index = 0, monthDiffNo, amount;

	if(frm.selected_doc.deduction_type == "Onetime"){
		month = dateFrom.toLocaleString('default', { month: 'short' })
		monthName = `${month}-${dateFrom.getFullYear()}`;
		if(!edit){
			addObj(monthName, frm, frm.selected_doc.amount)
		} else{
			let idx = monthExist(monthName, frm)
			if(idx){
				editRow(frm, idx, frm.selected_doc.amount ,false)
			} else {
				addObj(monthName, frm, frm.selected_doc.amount)
			}
		}
		
	}else{

		monthDiffIndex = monthDiff(dateFrom, dateTo)+1
		amount = frm.selected_doc.amount/monthDiffIndex;
		
		
		while(index < monthDiffIndex){
			month = dateFrom.toLocaleString('default', { month: 'short' }), monthNo;
			monthName = `${month}-${dateFrom.getFullYear()}`;

			if(edit){
				let idx = monthExist(monthName, frm)
				if(idx){	editRow(frm, idx, amount, true)	}
				else {	addObj(monthName, frm, amount, true)}
				
			} else{
				addObj(monthName, frm, amount, true)

			}

			monthNo = dateFrom.getMonth()+1
			dateFrom.setMonth(monthNo)
			index++
		}
	}

	callCulateAmount(frm)

}

function monthExist(monthName, frm){
	for(let val of frm.doc.deduction_calculation){
		if(val.month == monthName){
			return val.idx
		}
	}
}

function monthDiff(dateFrom, dateTo) {
	return dateTo.getMonth() - dateFrom.getMonth() + 
	  (12 * (dateTo.getFullYear() - dateFrom.getFullYear()))
}





// Copyright (c) 2021, RAHUL.S and contributors
// For license information, please see license.txt

frappe.ui.form.on('SUPPLIER INVOICE', {
	// refresh: function(frm) {

	// }
quantity: function(frm){
		frappe.call({
			method: 'sales_purchase.sales_purchase.doctype.supplier_invoice.supplier_invoice.get_total',
			args: {
				'costprice':frm.doc.cp,
				'quantity':frm.doc.quantity
				},
			callback: function(r) {
				if(r.message) {
						// code 
						frm.set_value('total',r.message)
						frm.refresh_fields();
			
			    }
			}
		});
			
	}
});

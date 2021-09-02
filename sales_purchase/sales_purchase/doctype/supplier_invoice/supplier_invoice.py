# Copyright (c) 2021, RAHUL.S and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
class SUPPLIERINVOICE(Document):
    def before_save(self):
        if frappe.db.exists("COMPANY STOCK DETAILS",{'item_name':self.item}):
           # pq=frappe.db.get_value("COMPANY STOCK DETAILS",{'item_name':self.item},current_stock)
            pq=frappe.db.get_value("COMPANY STOCK DETAILS",{'item_name':self.item},'current_stock')   
            frappe.db.set_value("COMPANY STOCK DETAILS",{'item_name':self.item},'current_stock',self.quantity+pq)
        else:
            new_stock=frappe.new_doc("COMPANY STOCK DETAILS")
            new_stock.item_name=self.item
            new_stock.current_stock=self.quantity
            new_stock.save()
    
@frappe.whitelist()
def get_total( costprice,quantity):
    x=int(costprice)*int(quantity)
    return x

   
# Copyright (c) 2021, RAHUL.S and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class PROFITANDLOSSSTATISTICS(Document):
	def before_save(self):
		self.cpot=q=frappe.db.get_value("SUPPLIER INVOICE",{'item':self.item_},"cp")
		self.selling_price_of_the_product=r=frappe.db.get_value("CUSTOMER INVOICE",{'item':self.item_},"selling_price")
		Quantity=frappe.get_value("SUPPLIER INVOICE",{'item':self.item_},"quantity")
		Current_quantity=frappe.get_value("COMPANY STOCK DETAILS",{'item_name':self.item_},"current_stock")
		self.quantity_sold=int(Quantity)-int(Current_quantity)
		self.profit=(int(r)-int(q))*int(self.quantity_sold)
		#int(q-r)*int((self.quantity_sold))

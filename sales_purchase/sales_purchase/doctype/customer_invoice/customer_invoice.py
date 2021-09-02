import frappe
from frappe.model.document import Document
class CUSTOMERINVOICE(Document):
	def before_save(self):
		if frappe.db.exists("COMPANY STOCK DETAILS",{'item_name':self.item}):
			pq=frappe.db.get_value("COMPANY STOCK DETAILS",{'item_name':self.item},'current_stock')
			if (self.qop>pq):
				frappe.throw("The product is not avilable with the quantity specified!")
			else:
			frappe.db.set_value("COMPANY STOCK DETAILS",{'item_name':self.item},'current_stock',pq-self.qop)
		    #self.total_price=self.selling_price*self.qop

			
		
		else:
			frappe.throw("No stock is available!!!!!!!!!")
	
	def validate(self):
		self.total_price=self.selling_price*self.qop
			
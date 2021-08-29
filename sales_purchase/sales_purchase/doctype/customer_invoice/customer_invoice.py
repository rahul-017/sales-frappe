import frappe
from frappe.model.document import Document
class CUSTOMERINVOICE(Document):
	def before_save(self):
		if frappe.db.exists("COMPANY STOCK DETAILS",{'item_name':self.item}):
			pq=frappe.db.get_value("COMPANY STOCK DETAILS",{'item_name':self.item},'current_stock')
			frappe.db.set_value("COMPANY STOCK DETAILS",{'item_name':self.item},'current_stock',pq-self.qop)
		else:
			frappe.throw("No stock is available!!!!!!!!!")
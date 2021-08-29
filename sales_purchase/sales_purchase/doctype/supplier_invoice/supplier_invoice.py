import frappe
from frappe.model.document import Document
class SUPPLIERINVOICE(Document):
    def before_save(self):
        if frappe.db.exists("COMPANY STOCK DETAILS",{'item_name':self.iname}):
           # pq=frappe.db.get_value("COMPANY STOCK DETAILS",{'item_name':self.iname},current_stock)
            pq=frappe.db.get_value("COMPANY STOCK DETAILS",{'item_name':self.iname},'current_stock')   
            frappe.db.set_value("COMPANY STOCK DETAILS",{'item_name':self.iname},'current_stock',self.qty+pq)
        else:
            new_stock=frappe.new_doc("COMPANY STOCK DETAILS")
            new_stock.item_name=self.iname
            new_stock.current_stock=self.qty
            new_stock.save()  

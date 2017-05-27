from __future__ import unicode_literals
import frappe

x=""
def get_context(context):
    context.products = x



@frappe.whitelist(allow_guest=True)
def ping(name):
	global x
	x= frappe.db.sql("select product_name,image,description from tabProducts where choose_trade_mark='"+name+"'")
	return x
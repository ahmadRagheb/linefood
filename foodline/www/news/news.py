from __future__ import unicode_literals
import frappe


def get_context(context):
    context.news = frappe.db.sql("select name from `tabNews` where name= ")



@frappe.whitelist(allow_guest=True)
def get_news(name):
    return frappe.db.sql("select title,image,subject from `tabNews` where name ='"+name+"'")

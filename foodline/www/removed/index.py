from __future__ import unicode_literals
import frappe


def get_context(context):
    context.newslist = frappe.db.sql("select name,title,image,subject from `tabNews`")
    context.productslist = frappe.db.sql("select product_name,description,image from `tabProducts`")
    context.sliders = frappe.db.sql("select image from `tabSlider`")

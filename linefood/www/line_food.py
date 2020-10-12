from __future__ import unicode_literals
import frappe


def get_context(context):
  # context.sliders = frappe.db.sql("select image from `tabSlider`")
  # context.marks = frappe.db.sql("select trade_mark_name,image,name from `tabTrade Mark`")
  # context.news = frappe.db.sql("select title,image,subject,name from `tabNews`")
  # context.products = frappe.db.sql("select product_name,image,description,choose_trade_mark from `tabProducts`")
  # context.name = "Mai"

  return {'name': 'Test Name from line_food.py'} 
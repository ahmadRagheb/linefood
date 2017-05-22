from __future__ import unicode_literals
import frappe


def get_context(context):
    context.sliders = frappe.db.sql("select image from `tabSlider`")
    context.marks = frappe.db.sql("select name,image from `tabTrade Mark`")
   
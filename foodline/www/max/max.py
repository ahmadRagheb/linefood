from __future__ import unicode_literals
import frappe


def get_context(context):
    context.products = frappe.db.sql("select product_name,image,description,choose_trade_mark from `tabProducts`")

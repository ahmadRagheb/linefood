from __future__ import unicode_literals
import frappe


def get_context(context):
  # context.sliders = frappe.db.sql("select image from `tabSlider`")
  # context.marks = frappe.db.sql("select trade_mark_name,image,name from `tabTrade Mark`")
  # context.news = frappe.db.sql("select title,image,subject,name from `tabNews`")
  # context.products = frappe.db.sql("select product_name,image,description,choose_trade_mark from `tabProducts`")
  context.name = "Mai"
  homepage = frappe.get_doc('Homepage')
  context.hero = homepage.hero_section_based_on
  context.hero_img = homepage.hero_image
  context.title = homepage.tag_line
  context.description = homepage.description

  return context
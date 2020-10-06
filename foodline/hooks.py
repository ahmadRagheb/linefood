# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "foodline"
app_title = "Foodline"
app_publisher = "ahmad ragheb"
app_description = "Foodline application "
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "ahmedragheb75@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/foodline/css/foodline.css"
# app_include_js = "/assets/foodline/js/foodline.js"

# include js, css files in header of web template
# web_include_css = "/assets/foodline/css/main-style.css"
# web_include_js = "/assets/foodline/js/main-scripts.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}
# page_js = {"main" : "public/js/main-scripts.js"}


# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }
role_home_page = {
    "Guest": "index"
}


# Website user home page (by function)
# get_website_user_home_page = "foodline.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "foodline.install.before_install"
# after_install = "foodline.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "foodline.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"foodline.tasks.all"
# 	],
# 	"daily": [
# 		"foodline.tasks.daily"
# 	],
# 	"hourly": [
# 		"foodline.tasks.hourly"
# 	],
# 	"weekly": [
# 		"foodline.tasks.weekly"
# 	]
# 	"monthly": [
# 		"foodline.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "foodline.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "foodline.event.get_events"
# }
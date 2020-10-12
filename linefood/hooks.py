# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "linefood"
app_title = "linefood"
app_publisher = "ahmad ragheb"
app_description = "linefood application "
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "ahmedragheb75@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/linefood/css/linefood.css"
# app_include_js = "/assets/linefood/js/linefood.js"

# include js, css files in header of web template
# "/assets/linefood/css/main-style.css",
web_include_css = [
    "/assets/linefood/css/bootstrap.css",
    "/assets/linefood/css/style.css",
    "/assets/linefood/css/responsive.css",
    "/assets/linefood/css/animate.css",
    "/assets/linefood/css/colors/color1.css",
]
# "/assets/linefood/js/main-scripts.js",
web_include_js = [
    "/assets/linefood/js/jquery.min.js",
    "/assets/linefood/js/tether.min.js",
    "/assets/linefood/js/bootstrap.min.js",
    "/assets/linefood/js/jquery.easing.js",
    "/assets/linefood/js/parallax.js",
    "/assets/linefood/js/jquery-waypoints.js",
    "/assets/linefood/js/jquery-countTo.js",
    "/assets/linefood/js/jquery.countdown.js",
    "/assets/linefood/js/jquery.flexslider-min.js",
    "/assets/linefood/js/images-loaded.js",
    "/assets/linefood/js/jquery.isotope.min.js",
    "/assets/linefood/js/magnific.popup.min.js",
    "/assets/linefood/js/jquery.hoverdir.js",
    "/assets/linefood/js/owl.carousel.min.js",
    "/assets/linefood/js/equalize.min.js",
    "/assets/linefood/js/gmap3.min.js",
    "/assets/linefood/js/jquery-ui.js",
    "/assets/linefood/js/jquery.cookie.js",
    "/assets/linefood/js/main.js",
    "/assets/linefood/rev-slider/js/jquery.themepunch.tools.min.js",
    "/assets/linefood/rev-slider/js/jquery.themepunch.revolution.min.js",
    "/assets/linefood/js/rev-slider.js",
    "/assets/linefood/js/switcher.js",
    "/assets/linefood/rev-slider/js/extensions/revolution.extension.actions.min.js",
    "/assets/linefood/rev-slider/js/extensions/revolution.extension.carousel.min.js",
    "/assets/linefood/rev-slider/js/extensions/revolution.extension.kenburn.min.js",
    "/assets/linefood/rev-slider/js/extensions/revolution.extension.layeranimation.min.js",
    "/assets/linefood/rev-slider/js/extensions/revolution.extension.migration.min.js",
    "/assets/linefood/rev-slider/js/extensions/revolution.extension.navigation.min.js",
    "/assets/linefood/rev-slider/js/extensions/revolution.extension.parallax.min.js",
    "/assets/linefood/rev-slider/js/extensions/revolution.extension.slideanims.min.js",
    "/assets/linefood/rev-slider/js/extensions/revolution.extension.video.min.js"
]

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
home_page = "line_food"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# role_home_page = {
#     "Guest": "home"
# }


# Website user home page (by function)
# get_website_user_home_page = "linefood.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "linefood.install.before_install"
# after_install = "linefood.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "linefood.notifications.get_notification_config"

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
# 		"linefood.tasks.all"
# 	],
# 	"daily": [
# 		"linefood.tasks.daily"
# 	],
# 	"hourly": [
# 		"linefood.tasks.hourly"
# 	],
# 	"weekly": [
# 		"linefood.tasks.weekly"
# 	]
# 	"monthly": [
# 		"linefood.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "linefood.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "linefood.event.get_events"
# }
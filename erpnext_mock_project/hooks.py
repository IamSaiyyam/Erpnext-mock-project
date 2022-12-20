from . import __version__ as app_version

app_name = "erpnext_mock_project"
app_title = "Erpnext Mock Project"
app_publisher = "Saiyyam Chhetri"
app_description = "Here I\'ll practice the mock project"
app_email = "saiyyam.d@promantia.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_mock_project/css/erpnext_mock_project.css"
# app_include_js = "/assets/erpnext_mock_project/js/erpnext_mock_project.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_mock_project/css/erpnext_mock_project.css"
# web_include_js = "/assets/erpnext_mock_project/js/erpnext_mock_project.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erpnext_mock_project/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "erpnext_mock_project.utils.jinja_methods",
#	"filters": "erpnext_mock_project.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erpnext_mock_project.install.before_install"
# after_install = "erpnext_mock_project.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erpnext_mock_project.uninstall.before_uninstall"
# after_uninstall = "erpnext_mock_project.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_mock_project.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"erpnext_mock_project.tasks.all"
#	],
#	"daily": [
#		"erpnext_mock_project.tasks.daily"
#	],
#	"hourly": [
#		"erpnext_mock_project.tasks.hourly"
#	],
#	"weekly": [
#		"erpnext_mock_project.tasks.weekly"
#	],
#	"monthly": [
#		"erpnext_mock_project.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "erpnext_mock_project.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "erpnext_mock_project.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "erpnext_mock_project.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"erpnext_mock_project.auth.validate"
# ]

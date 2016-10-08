from report_generator import *


class PeriodReport:
	"""
	Parent class for time periods reports
	"""
	def __init__(self, since, till, report_format='count', report_type='txt'):
		# Define time limits
		self.since = since
		self.till = till
		self.report_type = report_type
		self.report_format = report_format
		# Generate a title for a report
		self.report_name = self.get_report_name(self.report_format + '_report_all')
		# According to the db_path and redefinition of child classes
		self.report_class = self.choose_report_class()
		# Generating the data for the report
		self.report_data = self.report_class.generate_report_data()
		# For further generating a report the self.generate_report() should be called

	def get_report_name(self, slug):
		time_format = '%H.%M_%d%m%y'
		since = self.since.strftime(time_format)
		till = self.till.strftime(time_format)
		time_alias = since + '-' + till
		report_name = slug + '(' + time_alias + ')'
		return report_name

	def choose_report_class(self):
		if self.report_format == 'count':
			report_class = CountPeriodReport(self.since, self.till)
		elif self.report_format == 'event':
			report_class = EventPeriodReport(self.since, self.till)
		else:
			report_class = CountPeriodReport(self.since, self.till)
		return report_class

	def generate_report(self):
		"""
		Main reporting function
		:return: None
		"""
		if self.report_type == 'txt':
			self.report_class.create_txt_report(self.report_data, self.report_name)
		elif self.report_type == 'html':
			self.report_class.create_html_report(self.report_data, self.report_name)
		else:
			self.report_class.create_txt_report(self.report_data, self.report_name)


class ProjectPeriodReport(PeriodReport):
	def __init__(self, since, till, project, report_format='count', report_type='txt'):
		self.project = project
		super().__init__(since, till, report_format=report_format, report_type=report_type)
		# Redefines report name according to the sibling class alias
		self.report_name = self.get_report_name(self.report_format + '_' + self.project + '_project_report')

	def choose_report_class(self):
		if self.report_format == 'count':
			report_class = ProjectCountPeriodReport(self.since, self.till, self.project)
		elif self.report_format == 'event':
			report_class = ProjectEventPeriodReport(self.since, self.till, self.project)
		else:
			report_class = ProjectCountPeriodReport(self.since, self.till, self.project)
		return report_class


class ItemPeriodReport(PeriodReport):
	def __init__(self, since, till, item, report_format='count', report_type='txt'):
		self.item = item
		super().__init__(since, till, report_format=report_format, report_type=report_type)
		# Redefines report name according to the sibling class alias
		self.report_name = self.get_report_name(self.report_format + '_' + self.item + '_item_report')

	def choose_report_class(self):
		if self.report_format == 'count':
			report_class = ItemCountPeriodReport(self.since, self.till, self.item)
		elif self.report_format == 'event':
			report_class = ItemEventPeriodReport(self.since, self.till, self.item)
			self.report_name = 'event_' + self.report_name
		else:
			report_class = ItemCountPeriodReport(self.since, self.till, self.item)
		return report_class

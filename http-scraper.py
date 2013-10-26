import httplib
from StringIO import StringIO
from lxml import etree
from lxml.cssselect import CSSSelector

class HttpScraper:
	def __init__(self):
		self.html_parser = etree.HTMLParser()

	# Ex. get_response("google.se", "/more/about")
	def get_response(self, base_url, page):
		response = ""
		try:
			connection = httplib.HTTPConnection(base_url)
			connection.request("GET", page)
			http_response = connection.getresponse()
			response = http_response.read()
			connection.close()
		except Exception, err:
			print err

		return response

	# cssselector looks like this: 'div.some-class'
	def extract_values(self, raw_html, cssselector):
		parsed_data = []
		try:
			# Create the css-selector
			selector = CSSSelector(cssselector)
		
			# Parse the raw html data
			tree = etree.parse(StringIO(raw_html), self.html_parser)
		
			# Grap the interesting content with the css-selector
			parsed_data = selector(tree)
		except Exception, err:
			print err

		return parsed_data

	def scrape(self, base_url, page, cssselector):
		# Make the HTTP request
		html_data = self.get_response(base_url, page)
		
		# Extract the values we are looking for
		extracted_data = self.extract_values(html_data, cssselector)
		
		return extracted_data

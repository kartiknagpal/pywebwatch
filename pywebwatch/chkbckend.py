def check_backend(html_content):
	''' (BeautifulSoup) -> bool

	    This is a custom function to check for themeefy.com/browse url only.

	'''
	return not (len(html_content.find_all(id='featuredthemes')[0].contents) == 0)
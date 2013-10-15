from tkinter import Tk, messagebox
from time import sleep
from bs4 import BeautifulSoup
from httplib2 import Http
from datetime import datetime

from logger import lgr
from chkbckend import check_backend


def is_ok_backend(html_content):
	''' (BeautifulSoup) -> bool

	    This is the function, that needs rewritting depending upon on the targetted site markup.
	    plus, this function can be ignored for websites that didn't decoupled backend as an seperate entity/server.

	'''
	is_ok_backend = True
	try:
		is_ok_backend =  check_backend(html_content)
		return is_ok_backend
	except:
		alert(1)
		return False


def alert(alert_type):
	''' (int) -> None

	    According to the alert type message is displayed in tk messagebox, which gets destroyed when clicked ok.
	    It is important to note that it is an program blocking event waiting to happen.

	'''
	root = Tk()
	if alert_type == 1:
		msg = messagebox.showwarning("WARNING: ", "FRONTEND IS DOWN. Close this warning?", icon='warning', parent=root)
		if msg == 'ok':
			root.destroy()
	elif alert_type == 2:
		msg = messagebox.showwarning("WARNING: ", "BACKEND IS DOWN. Close this warning?", icon='warning', parent=root)
		if msg == 'ok':
			root.destroy()
	elif alert_type == 3:
		msg = messagebox.showwarning("WARNING: ", "HTTP 404 response recieved, verify url_to_check again. Close this warning?", icon='warning', parent=root)
		if msg == 'ok':
			root.destroy()
	elif alert_type == 4:
		msg = messagebox.showwarning("WARNING: ", "Cannot connect to internet. Close this warning?", icon='warning', parent=root)
		if msg == 'ok':
			root.destroy()

def grab_from_web(url):
	''' (str) -> BeautifulSoup, bool

	    It grabs html content from given url, if possible, handles exceptions otherwise.
	    It is also here that frontend failures are detected and returned as a bool.

	'''
	h = Http('.cache')
	is_ok_frontend = True
	try:
		response, content = h.request(url)
		if response.status == 404:	#reached server, but given resource not available on server
			alert(3)
		return BeautifulSoup(str(content)), is_ok_frontend
	except:	#cannot reach server
		try:
			response, content = h.request('http://www.google.com/')
			is_ok_frontend = False
			return None, is_ok_frontend
		except:	#cannot reach google server, perhaps your internet is not connected
			lgr.warn('CANNOT CONNECT TO INTERNET')
			alert(4)
			is_ok_frontend = True 	#cannot be sure, internet not available, better to assume is OK
			return None, is_ok_frontend

	

def main(url_to_check, time_interval, time_interval_on_failure):
	''' (str, int, int) -> None

	    Runs an infinte loop that keep running the program, it accepts:
	      url_to_check -> url for which server status is to be checked
	      time_interval -> this many seconds between each check
	      time_interval_on_failure -> this many seconds between next check when failure is detected

	'''
	while True:
		is_all_good = True
		html_content, is_ok_frontend = grab_from_web(url_to_check)
		if not is_ok_frontend:
			is_all_good = False
			lgr.critical('FRONTEND DOWN')
			alert(1)
			sleep(time_interval_on_failure)
		else:
			if not is_ok_backend(html_content):
				is_all_good = False
				lgr.critical('BACKEND DOWN')
				alert(2)
				sleep(time_interval_on_failure)
		if is_all_good:
			lgr.info('All is Well ')
		sleep(time_interval)


if __name__ == '__main__':
	from config import url_to_check, time_interval, time_interval_on_failure
	main(url_to_check, time_interval, time_interval_on_failure)
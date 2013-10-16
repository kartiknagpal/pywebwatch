# file src/__main__.py

if __name__ == '__main__':
	from pww import main
	from config import url_to_check, time_interval, time_interval_on_failure
	main(url_to_check, time_interval, time_interval_on_failure)
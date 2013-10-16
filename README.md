#Monitor a website from client machine

Inspired by the need to look over running status of a website indefinetly, instead relying on cumbersome and hopeless manual techniques.<br/>

This command-line utility runs indefinetly in the background polling server url at regular intervals* to check whether frontend* or backend* are down, when fault found:<br> 
+ Alerts by showing warning dialog using tcl/tk gui interface.
+ Logs the fault in Webwatch.log file
<br/>

###Dependencies:<br/>
    * BeautifulSoup4
    * httplib2
    * tcl/tk
####Update: No need to install dependencies manually, included within the package itself.

##How to set up for use:
1). First edit config.py as follows:<br/>
```python
#main configs
url_to_check = 'http://localhost:3001/browse/' #url to specific page that can when scrapped helps identifying whether backend is down or not
time_interval = 45 	        # after these many seconds recheck
time_interval_on_failure = 180  # after these many seconds do subsequent rechecks, when a fault is found
```
<br/>
2). execute program: $ python pywebsearch.zip<br/>

Note: i wrote this program to monitor a website that has frontend and backend decoupled, running on seperate servers. So if you want to monitor site
backed by single server only, it will work just fine treating the only server as frontend server.<br/>
Note: * are configurable


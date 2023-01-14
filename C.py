from stackapi import StackAPI
from datetime import datetime


site = StackAPI('stackoverflow')


time_delta = datetime.now() - datetime.strptime('1970-Jan-01 00:00:00', '%Y-%b-%d %H:%M:%S')
todate = int(time_delta.total_seconds())

time_delta = datetime.now() - datetime.strptime('1970-Jan-03 00:00:00', '%Y-%b-%d %H:%M:%S')
fromdate = int(time_delta.total_seconds())


questions = site.fetch('questions', fromdate = fromdate, todate = todate, tagged = 'python')

for i in range( len(questions) ):
	print(questions['items'][i]['title'])









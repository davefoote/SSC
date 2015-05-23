from flask import Flask, render_template, request
from datetime import datetime
from flaskext.markdown import Markdown
import os

app = Flask(__name__)
app.config['DEBUG'] = True

Markdown(app)

path = 'static/events'

#creates list of upcoming and past events
def get_events_lists():
	upcoming = []
	past = []
	present = datetime.now()

	for f in os.listdir(path):
		year, mon, day = int(f[0:4]), int(f[5:7]), int(f[8:10])
		if datetime(year,mon,day)<present:
			event_dict = file_to_dict(f)
			past.append(event_dict)
		else:
			event_dict = file_to_dict(f)
			upcoming.append(event_dict)
	return upcoming, past


#makes event.txt into dictionary
def file_to_dict(filename):
	file_dict = {}
	with open(os.path.join(path, filename)) as f:
		content = f.read().split('|')
		if len(content) < 4: 
			file_dict['title']=content[0]
			file_dict['date']=content[1]
			file_dict['description']=content[2]
		else:
			file_dict['title']=content[0]
			file_dict['date']=content[1]
			file_dict['description']=content[2]
			file_dict['website']=content[3]
	return file_dict


@app.route('/')
def root():
	upcoming, past = get_events_lists()
	return render_template('index.html', upcoming=upcoming)


@app.route('/past_events')
def past_events():
	upcoming, past = get_events_lists()
	past.reverse()
	return render_template('past_events.html', past=past)

if __name__ == '__main__':
	app.run()

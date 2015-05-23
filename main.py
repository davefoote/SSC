from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def root():
   return render_template('index.html')

@app.route('/events')
def events():
   return render_template('events.html', events = events)

if __name__ == '__main__':
   app.run()

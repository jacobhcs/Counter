from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
	if 'count' not in session:
		session['count']=0
	session['count']+=1
	return render_template('index.html', count=session['count'])

@app.route('/count2', methods=['POST'])
def count2():
	if 'count' not in session:
		session['count']=0
	session['count']+=1
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	if 'count' not in session:
		session['count']=0
	session['count']=0
	return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

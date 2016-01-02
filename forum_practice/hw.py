from flask import Flask,render_template


app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/welcome')
def profile():
    return render_template('welcome.html')	
if __name__ == "__main__":
    app.run(debug=True)	
	
	
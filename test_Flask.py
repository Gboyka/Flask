from flask import Flask

app = Flask(__name__) #main


@app.route('/')
@app.route('/home')
def home():
    return '<h2>Hello, World!</h2>' 

@app.route('/about')
def about():
	return'<h1>About Page !</h1>'  

if __name__ == '__main__':
	app.run(debug=True)
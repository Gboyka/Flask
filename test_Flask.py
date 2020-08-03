from flask import Flask,render_template

app = Flask(__name__) 


posts=[
	{
		'author':'Pranav',
		'title':'Blog Dummy',
		'content':'First Post',
		'date':'Aug-02',


	}
	,
	{
		'author':'Duke',
		'title':'Blog Dummy 2',
		'content':'Second Post',
		'date':'Aug-04'


	}
	
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts,title='HOME')  

@app.route('/about')
def about():
	return  render_template('about.html',title='ABOUT')

if __name__ == '__main__':
	app.run(debug=True)
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Amanda Sinamane',
        'title' : 'My first blog',
        'content': 'First blog post',
        'date_posted': 'May 31, 2023'
    },
    {
        'author': 'Naruto Uzumaki',
        'title' : 'Resenngan',
        'content': 'Learning from my sensei Jiraiya',
        'date_posted': 'May 31, 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

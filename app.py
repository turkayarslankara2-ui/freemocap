from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    users = ['User1', 'User2', 'User3']  # Sample users
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
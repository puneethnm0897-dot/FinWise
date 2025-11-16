from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # this will load your index.html file from the 'templates' folder
    return render_template('index.html')

if __name__ == '__main__':
    # run on port 80 so your localhost:80 works
    app.run(host='0.0.0.0', port=80)

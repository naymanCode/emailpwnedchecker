import requests


from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '7b09add526e0f9d38f575bca8c20a1fac116122d136b3d5d'
messages = [
            ]

@app.route("/mail")
def hello():
    return "Hello World!"

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

#
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        content = request.form['content']
        emaill = request.form['content']
        response = requests.get(f'https://2ip.ru/?area=ajaxHaveIBeenPwned&query={content}')
        parsed = response.json()
        content = parsed
        if not content:
            flash('Content is required!')
        else:
            messages.append({'title': emaill, 'content': content})

            return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == "__main__":
    app.run()







'''import json
dict1={}

json_object = json.dumps(response, indent=4)


out_file = open("myfile.json", "w")
json.dumps(response, out_file, indent=2)'''
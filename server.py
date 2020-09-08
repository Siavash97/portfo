from flask import Flask, render_template, redirect, request
import csv
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('uploads.csv', 'a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['text']
        csvwriter = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email,subject,message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thanks.html')
        except:
            return 'did not save to database.'
    else:
        return 'Form not submitted.'





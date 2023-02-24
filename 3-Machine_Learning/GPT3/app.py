from flask import Flask, request, render_template
import openai
import os

os.chdir(os.path.dirname(__file__))

try:
    openai.api_key = open("api_key.txt", "r").read()
except:
    print("No api_key.txt in the directory with your credentials")

application = Flask(__name__)


@application.route('/')
def my_form():
    return render_template('index.html')

@application.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=variable,
    max_tokens=300,
    temperature=0.9
    )
    text_output = response.choices[0].text
    text_output = text_output.replace('\n', '<br>')
    text_output = text_output.replace('\t', '    ')
    return text_output + '<p><a href="/">Back</a></p>\n'


if __name__ == "__main__":
    application.run()
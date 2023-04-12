from flask import Flask, request
from gpt import ask_gpt
from save_file import save_file

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
	# retrieve prompt and apiKey parameters from JSON payload
	api_key = request.form.get('api_key')
	prompt = request.form.get('prompt')

    # retrieve file from request
	file = request.files.get('file')
	print('request', request.files.get('file'))

    # save file to data folder
	save_file(file)

    # call ask_gpt function with prompt and apiKey parameters
	response = ask_gpt(api_key, prompt)

	return response

if __name__ == '__main__':
    app.run(debug=True)
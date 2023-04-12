import os

def save_file(file):
	if file:
		filename = file.filename
		file.save(os.path.join('./data', filename))
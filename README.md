# Flask GPT3 API (with fine tuning)

This is a simple Flask app that uses OpenAI's GPT-3 API to generate text based on a user's prompt. The app includes a simple HTML form where users can input their prompt and API key, as well as upload a text file to be used as part of the GPT-3 training data.

## Requirements

To run this app, you'll need:

- Python 3
- Flask
- OpenAI API key

You can install Flask using pip:

```
pip install Flask
```

You'll also need an OpenAI API key, which you can get by [signing up for OpenAI](https://beta.openai.com/signup/) and following their instructions.

## Running the app

To run the app, first make sure you've installed Flask and have your OpenAI API key handy. Then, clone this repository and navigate to the project directory. Run the following command to start the Flask server:

```
export FLASK_APP=app.py
flask run
```

This should start the Flask app on port 5000. You can access the app by navigating to `http://localhost:5000` in your web browser.

## Usage

Once the app is running, you can use the HTML form to submit a prompt and API key, as well as upload a text file to be used as training data. After submitting the form, the app will generate text based on your prompt using GPT-3, and display the results on the page.

## Contributing

If you'd like to contribute to this project, feel free to open a pull request with any changes or improvements you'd like to make.

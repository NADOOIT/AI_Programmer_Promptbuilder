from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__, template_folder="./templates")

app.template_engine = "mako"

openai.api_key = os.getenv("OPENAI_API_KEY")


def create_prompt_form_config(config):
    prompt = ""
    for word in config:
        prompt += word + ""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user inputs from form
        text = request.form["text"]
        config = request.form.getlist("config")

        # Build prompt string
        prompt = create_prompt_form_config(config)

        # Call OpenAI GPT API
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Display response to user
        return render_template(
            "result.html",
            text=text,
            config=config,
            response=response.choices[0].text,
        )
    else:
        config = [
            "flask",
            "openai",
            "requirements.txt",
            "app.py",
            "templates",
            "index.html",
            "result.html",
            "Procfile",
            "runtime.txt",
            "README.md",
            "LICENSE",
            "setup.sh",
            "requirements.txt",
            "ru",
        ]
        # Display form for user input
        return render_template("index.html", config=config)


if __name__ == "__main__":
    app.run(debug=True)

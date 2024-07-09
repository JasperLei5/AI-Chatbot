from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "key"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(chat_with_gpt(user_text))

if __name__ == "__main__":
    app.run(debug=True)


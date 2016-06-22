from flask import Flask
from translator import Translator

app = Flask(__name__)
t = Translator()

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/<lang>")
def translate(lang):
  if len(lang) > 2:
    return ""
  return t.translate("Hello World", lang)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

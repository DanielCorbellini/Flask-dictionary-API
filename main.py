from flask import Flask, render_template, redirect, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("dictionary.csv")


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/redirect', methods=['POST'])
def redirect_url():
    """ When the person type a word in the input box, this function is called, and it will redirect the user
     to the definition page
    """
    word = request.form['word']
    url = f"http://127.0.0.1:5001/api/v1/{word}"
    return redirect(url)


@app.route("/api/v1/<word>/")
def search(word):
    """ This function collects the definition of the word that was typed in the input box
    """
    definition = df.loc[df["word"] == word.lower()]["definition"].squeeze()
    dictionary = {"definition": definition,
                  "word": word
                  }
    return dictionary


if __name__ == "__main__":
    app.run(debug=True, port=5001)

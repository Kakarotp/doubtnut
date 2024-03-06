from flask import Flask, render_template, request

app = Flask(__name__)

def process_text(text):
    # Replace this with your actual processing logic
    return f"You entered: {text.upper()}"

@app.route("/result", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        output = process_text(user_input)
        return render_template("index.html", output=output)
    else:
        return render_template("index.html", output="")

if __name__ == "__main__":
    app.run(debug=True)

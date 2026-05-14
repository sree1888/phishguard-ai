from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        text = request.form["message"].lower()

        phishing_words = [
            "urgent",
            "click here",
            "verify account",
            "bank",
            "password",
            "login",
            "suspended",
            "winner",
            "free money"
        ]

        score = 0
        reasons = []

        for word in phishing_words:
            if word in text:
                score += 10
                reasons.append(word)

        if score >= 30:
            status = "⚠ Possible Phishing Detected"
        else:
            status = "✅ Looks Safe"

        result = f"""
        {status}

        Risk Score: {score}%

        Suspicious Words Found:
        {', '.join(reasons)}
        """

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
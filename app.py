from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

FLAG = "FLAG{WEIRD_HEADERS_ARE_FUN}"

# HTML template with CSS + form
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Beta Portal</title>
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: #1e1e1e;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px #00ff99;
            text-align: center;
            width: 400px;
        }
        h1 {
            color: #00ff99;
        }
        input[type="text"] {
            width: 80%;
            padding: 10px;
            border-radius: 5px;
            border: none;
            margin-bottom: 10px;
        }
        input[type="submit"] {
            background: #00ff99;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        input[type="submit"]:hover {
            background: #00cc7a;
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Beta Portal</h1>
        <form method="post">
            <input type="text" name="header" placeholder="Enter header value">
            <br>
            <input type="submit" value="Submit">
        </form>
        {% if result %}
            <div class="result">{{ result|safe }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        header_value = request.form.get("header", "").strip()

        if header_value.lower() == "client-ip: 127.0.0.1":
            result = f"<span style='color:#00ff99'>{FLAG}</span>"
        else:
            result = f"<span style='color:#ff5555'>Access Denied: {header_value}</span>"

        # Render result immediately, but do not persist it
        return render_template_string(template, result=result)

    # On GET (refresh/new visit) → always reset to clean state
    return render_template_string(template, result=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


from flask import Flask, render_template_string, request

app = Flask(__name__)
 
# ---------- HTML TEMPLATE ----------
base_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Propose Day 💖</title>

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Playfair Display', serif;
        }

        body {
            height: 100vh;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            overflow: hidden;
        }

        .card {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 50px;
            width: 420px;
            text-align: center;
            box-shadow: 0 0 40px rgba(255, 182, 193, 0.2);
            animation: fadeIn 2s ease;
        }

        h1 {
            font-size: 32px;
            margin-bottom: 15px;
        }

        p {
            font-size: 17px;
            line-height: 1.6;
            margin-bottom: 30px;
            color: #f2f2f2;
        }

        button {
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
            border: none;
            border-radius: 30px;
            padding: 12px 25px;
            font-size: 16px;
            cursor: pointer;
            color: white;
            margin: 8px;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(255, 118, 136, 0.4);
        }

        .heart {
            position: absolute;
            color: pink;
            font-size: 20px;
            animation: float 6s infinite ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes float {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-800px); opacity: 0; }
        }
    </style>
</head>
<body>

    <!-- Floating hearts -->
    {% for i in range(20) %}
        <div class="heart" style="left: {{ i * 5 }}%; animation-delay: {{ i * 0.4 }}s;">💗</div>
    {% endfor %}

    <div class="card">
        {{ content|safe }}
    </div>

</body>
</html>
"""

# ---------- ROUTES ----------
@app.route("/")
def home():
    content = """
    <h1>Hey You 🌸</h1>
    <p>
        Valentine's Week feels incomplete<br>
        without saying what my heart already knows.
    </p>
    <form action="/propose" method="post">
        <button type="submit">Open My Heart 💌</button>
    </form>
    """
    return render_template_string(base_template, content=content)


@app.route("/propose", methods=["POST"])
def propose():
    content = """
    <h1>Will You Be Mine? 💖</h1>
    <p>
        Like an anime moment frozen in time,<br>
        I want every tomorrow to start with you.
    </p>
    <form action="/yes" method="post">
        <button>Yes 💕</button>
        <button formaction="/think">Let Me Think 🤭</button>
    </form>
    """
    return render_template_string(base_template, content=content)


@app.route("/yes", methods=["POST"])
def yes():
    content = """
    <h1>You Said Yes 😭💖</h1>
    <p>
        This is officially my favorite scene.<br>
        Happy Propose Day, my Valentine 🌹
    </p>
    """
    return render_template_string(base_template, content=content)


@app.route("/think", methods=["POST"])
def think():
    content = """
    <h1>I'll Wait 🌙</h1>
    <p>

        Some love stories take time,<br>
        and I don't mind waiting for you 💫
    </p>
    """
    return render_template_string(base_template, content=content)

# ---------- RUN ----------

if __name__ == "__main__":
    app.run(debug=True)
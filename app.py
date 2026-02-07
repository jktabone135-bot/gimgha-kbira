from flask import Flask, request

app = Flask(__name__)

# Dictionary for Vara outputs
responses = {
    "1": "Cena etc...",
    "2": "Ort etc...",
    "3": "Guda etc...",
    "4": "Sinedriju etc...",
    "5": "Marbut etc...",
    "6": "Pilatu etc...",
    "7": "Redentur etc...",
    "8": "Raba Stazzjon etc...",
    "9": "Veronica etc...",
    "10": "Vara L-Kbira etc...",
    "11": "Pieta etc...",
    "12": "Monument etc...",
    "13": "Duluri etc..."
}

@app.route("/")
def home():
    # HTML form with dropdown
    return """
    <h1>Merhba Ghal Gimgha L-Kbira Ta Hal Qormi San Gorg</h1>

    <style>
        img {
            width: 180px;
            margin: 10px;
            cursor: pointer;
            border: 2px solid #ccc;
        }
        img:hover {
            border-color: black;
        }
    </style>

    <form action="/result">
        <input type="image" src="/static/CENA.jpg" name="vara" value="1">
        <input type="image" src="/static/ORT.jpg" name="vara" value="2">
        <input type="image" src="/static/GUDA.jpg" name="vara" value="3">
        <input type="image" src="/static/SINEDRIJU.jpg" name="vara" value="4">
        <input type="image" src="/static/MARBUT.jpg" name="vara" value="5">
        <input type="image" src="/static/PILATU.jpg" name="vara" value="6">
        <input type="image" src="/static/REDENTUR.jpg" name="vara" value="7">
        <input type="image" src="/static/RABA' STAZZJON.jpg" name="vara" value="8">
        <input type="image" src="/static/VERONICA.jpg" name="vara" value="9">
        <input type="image" src="/static/VARA L-KBIRA.jpg" name="vara" value="10">
        <input type="image" src="/static/PIETA'.jpg" name="vara" value="11">
        <input type="image" src="/static/MONUMENT.jpg" name="vara" value="12">
        <input type="image" src="/static/DULURI.jpg" name="vara" value="13">
    </form>
    """



@app.route("/result")
def result():
    @app.route("/result")
    def result():
    # Image buttons send vara.x / vara.y, so we detect which one was clicked
        vara = None
    for key in request.args:
        if key.startswith("vara"):
            vara = request.args.get(key)
            break

    text = responses.get(vara, "Kellek Taghzel Minn 1-13")

    return f"""
    <h2>{text}</h2>
    <a href="/">Mur lura</a>
    """


    # Show result and link back
    return f"""
    <h2>{text}</h2>
    <a href="/">Mur lura</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

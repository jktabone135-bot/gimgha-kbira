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

    <form action="/result">
        <label>Ghazel Il Vara Li Qed Tara:</label><br><br>

        <select name="vara">
            <option value="1">Cena</option>
            <option value="2">Ort</option>
            <option value="3">Guda</option>
            <option value="4">Sinedriju</option>
            <option value="5">Marbut</option>
            <option value="6">Pilatu</option>
            <option value="7">Redentur</option>
            <option value="8">Raba Stazzjon</option>
            <option value="9">Veronica</option>
            <option value="10">Vara L-Kbira</option>
            <option value="11">Pieta</option>
            <option value="12">Monument</option>
            <option value="13">Duluri</option>
        </select>

        <br><br>
        <button type="submit">Ara</button>
    </form>
    """

@app.route("/result")
def result():
    vara = request.args.get("vara")
    text = responses.get(vara, "Kellek Taghzel Minn 1-13")

    # Show result and link back
    return f"""
    <h2>{text}</h2>
    <a href="/">Mur lura</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

from flask import Flask, request, jsonify, send_from_directory
import wolframalpha
import os

app = Flask(__name__)
APP_ID = "HKRW24-Y39AGGJQP8"  # Inserisci la tua vera AppID Wolfram qui

@app.route("/", methods=["GET"])
def home():
    return "Wolfram API attiva ✅"

@app.route("/ask", methods=["POST"])
def ask_wolfram():
    data = request.json
    query = data.get("query")
    try:
        client = wolframalpha.Client(APP_ID)
        res = client.query(query)
        answer = next(res.results).text
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/.well-known/ai-plugin.json")
def serve_plugin():
    return send_from_directory(os.path.join(app.root_path, '.well-known'), 'ai-plugin.json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

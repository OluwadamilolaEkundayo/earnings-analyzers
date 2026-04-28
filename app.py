from flask import Flask, request, jsonify, render_template
import anthropic
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    transcript = request.json.get("transcript", "")

    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400

    prompt = f"""
You are a senior equity analyst. Analyze the following earnings call transcript and extract the key investment signals.

Return your analysis in exactly this format:

TONE: (one word — Confident, Cautious, or Neutral)

FORWARD GUIDANCE: (2-3 sentences on what management said about future revenue, margins, or growth)

KEY RISKS: (bullet point list of 3-5 risks mentioned or notably avoided)

INVESTMENT THESIS: (3-4 sentences — is the overall signal Bullish, Bearish, or Mixed, and why)

Here is the transcript:
{transcript}
"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify({"result": message.content[0].text})

if __name__ == "__main__":
    app.run(debug=True)
import anthropic
from dotenv import load_dotenv

load_dotenv()

# Load the transcript
with open("transcript.txt", "r") as f:
    transcript = f.read()

# Build the prompt
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

# Send to Claude
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(message.content[0].text)
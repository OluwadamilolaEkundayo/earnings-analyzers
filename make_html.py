html = open("templates/index.html", "w")
html.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Earnings Call Analyzer</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, sans-serif; background: #f5f5f5; color: #1a1a1a; }
    .container { max-width: 800px; margin: 48px auto; padding: 0 24px; }
    h1 { font-size: 28px; font-weight: 600; margin-bottom: 8px; }
    p.subtitle { color: #666; margin-bottom: 32px; }
    textarea { width: 100%; height: 240px; padding: 16px; border: 1px solid #ddd; border-radius: 10px; font-size: 14px; resize: vertical; background: white; outline: none; }
    button { margin-top: 16px; padding: 12px 28px; background: #1a1a1a; color: white; border: none; border-radius: 8px; font-size: 15px; cursor: pointer; width: 100%; }
    button:disabled { background: #999; cursor: not-allowed; }
    #results { margin-top: 40px; display: none; }
    .card { background: white; border-radius: 12px; padding: 24px; margin-bottom: 16px; border: 1px solid #e5e5e5; }
    .card h2 { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #888; margin-bottom: 10px; }
    .card p { font-size: 15px; line-height: 1.7; }
    .tone { font-size: 24px; font-weight: 600; }
    .tone.Confident { color: #16a34a; }
    .tone.Cautious { color: #dc2626; }
    .tone.Neutral { color: #d97706; }
    .loading { text-align: center; color: #888; padding: 40px 0; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Earnings Call Analyzer</h1>
    <p class="subtitle">Paste an earnings call transcript to extract key investment signals.</p>
    <textarea id="transcript" placeholder="Paste your earnings call transcript here..."></textarea>
    <button id="btn" onclick="analyze()">Analyze Transcript</button>
    <div id="results"></div>
  </div>
  <script>
    async function analyze() {
      const transcript = document.getElementById("transcript").value.trim();
      const btn = document.getElementById("btn");
      const results = document.getElementById("results");
      if (!transcript) { alert("Please paste a transcript first."); return; }
      btn.disabled = true;
      btn.textContent = "Analyzing...";
      results.style.display = "block";
      results.innerHTML = "<div class=loading>Analyzing transcript, about 10 seconds...</div>";
      try {
        const res = await fetch("/analyze", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ transcript }) });
        const data = await res.json();
        const text = data.result;
        const tone = text.match(/TONE:\\s*(\\w+)/)?.[1] || "N/A";
        const guidance = text.match(/FORWARD GUIDANCE:\\s*([\\s\\S]*?)(?=KEY RISKS:)/)?.[1]?.trim() || "N/A";
        const risks = text.match(/KEY RISKS:\\s*([\\s\\S]*?)(?=INVESTMENT THESIS:)/)?.[1]?.trim() || "N/A";
        const thesis = text.match(/INVESTMENT THESIS:\\s*([\\s\\S]*)/)?.[1]?.trim() || "N/A";
        results.innerHTML = "<div class=card><h2>Tone</h2><p class=tone>" + tone + "</p></div><div class=card><h2>Forward Guidance</h2><p>" + guidance + "</p></div><div class=card><h2>Key Risks</h2><p>" + risks.replace(/\\n/g,"<br>") + "</p></div><div class=card><h2>Investment Thesis</h2><p>" + thesis + "</p></div>";
      } catch(e) {
        results.innerHTML = "<div class=card><p>Something went wrong. Try again.</p></div>";
      }
      btn.disabled = false;
      btn.textContent = "Analyze Transcript";
    }
  </script>
</body>
</html>""")
html.close()
print("Done!")

# Earnings Call Analyzer

An AI-powered web tool that analyzes earnings call transcripts and extracts key investment signals, built to demonstrate how LLMs can augment financial analysis workflows.

## What it does

Paste any earnings call transcript into the tool and it returns:
- **Tone** - management's overall sentiment (Confident, Cautious, or Neutral)
- **Forward Guidance** - what management said about future revenue, margins, and growth
- **Key Risks** - risks mentioned or notably avoided
- **Investment Thesis** - a plain-English Bullish, Bearish, or Mixed signal with reasoning

## Why I built this
As a Yale economics graduate exploring the interestion of AI and finance, I want to build something that addresses a real workflow problem: analysts spend hours manually reading earnings call transcripts to extract the same categories of information every quarter. This tool does that in seconds using Claude's API, freeing up analyst time for higher-judgement

## Tech stack
- **Backend** - Python, Flask, Anthropic Claude API
- **Frontend** - HTML, CSS, Javascript
- **Key libraries** - anthropic, flask, python-dotenv

## How to run it locally

  1. Clone the repo
  2. Create a virtual environment and install dependecies:
     python3 -m venv venv
     
     source venv/bin/activate
     
     pip install anthropic flask python-dotenv
  4. Create a '.env' file with your Anthropic API key:
     ANTHROPIC_API_KEY=your_key_here
  5. Run the app:
     python3 app.py
  6. Open 'localhost:5000' in your browser

MarketMind AI: Intelligent Stock Research Agent
📖 Overview
MarketMind AI is a sophisticated, conversational AI agent designed to perform comprehensive research on multiple publicly traded stocks. It leverages a powerful stack of modern tools to fetch real-time financial data, search for the latest news, and provide intelligent, summarized insights to inform your investment strategy.

The agent integrates yfinance for quantitative data, duckduckgo-search for qualitative news and web articles, and the Groq LPU Inference Engine for high-speed language processing and analysis.

🎯 Core Functionality
This agent is designed to answer complex financial questions by breaking them down into a series of steps:

Fetch Financial Data: Retrieves real-time stock prices, historical data, and corporate financials.

Search the Web: Scans the internet for relevant news, press releases, and market analysis.

Synthesize & Analyze: Uses a Large Language Model (LLM) powered by Groq to understand the collected data and generate a coherent, human-like summary.

✨ Features
Multi-Stock Analysis: Research and compare several stocks in a single query.

Real-Time Data: Pulls the latest market data using yfinance.

Web Search Integration: Uses duckduckgo-search to gather up-to-the-minute news and sentiment.

High-Speed AI Processing: Employs the Groq LPU for extremely fast language understanding and generation.

Secure API Key Management: Uses python-dotenv to keep your API keys safe and out of the source code.

Conversational Interface: Interact with the agent in plain English.

💻 Technologies Used
Python

yfinance: To fetch financial market data from Yahoo! Finance.

duckduckgo-search: For a clean, privacy-respecting, and ad-free web search API.

groq: To interact with the GroqCloud API for ultra-low-latency LLM inference.

agnoc: To provide a structured framework for building the AI agent.

python-dotenv: To manage environment variables and API keys securely.

🚀 Getting Started
Prerequisites
Ensure you have Python installed. You will also need API keys for Groq.

Groq API Key: Sign up on the GroqCloud website to get your free API key.

Create a .env file in your project's root directory.

Add your API key to the .env file:

GROQ_API_KEY="your_groq_api_key_here"

Installation
Clone the repository:

git clone https://github.com/your-username/MarketMind-AI.git

Navigate to the project directory:

cd MarketMind-AI

Install the required Python libraries:

pip install yfinance duckduckgo-search groq agnoc python-dotenv

🛠️ How It Works
The agent operates through a structured framework provided by agnoc.

User Input: You provide a prompt, such as "Compare the recent performance and news for Tesla and Ford."

Tool Selection: The agent, powered by the Groq LLM, determines which tools to use. It recognizes that it needs both financial data (yfinance) and news (duckduckgo-search).

Data Fetching:

It calls yfinance to get stock tickers, prices, and other quantitative metrics for TSLA and F.

It uses duckduckgo-search to find recent news articles and analysis for both companies.

Synthesis: All the collected information (both numerical data and text from articles) is compiled into a comprehensive context.

Final Response: This context is sent back to the Groq LLM, which generates a final, detailed summary that directly answers your initial question. The speed of the Groq LPU makes this final step feel nearly instantaneous.

⚖️ Ethical Considerations & Disclaimer
Not Financial Advice: This AI agent is a powerful information-gathering tool, but it is not a licensed financial advisor. The insights it provides are for informational and educational purposes only.

Do Your Own Research (DYOR): Never make investment decisions based solely on the output of this agent. Always consult with a qualified professional.

Data Accuracy: The agent relies on third-party APIs (yfinance, duckduckgo-search). The accuracy of its output is dependent on the accuracy of these sources.

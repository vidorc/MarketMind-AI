from agno.agent import Agent
from agno.models.groq import Groq

from agno.tools.duckduckgo import DuckDuckGoTools

from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv



load_dotenv()



llm = Groq(id="llama-3.3-70b-versatile",temperature=0)

web_agent = Agent(
    name="Web Agent",
    role="Search the Web for information",
    model=llm,
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(

name="Wen Agent",

role="Search the Web for information",

model=llm,

tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,company_info=True)],

instructions="Use tables to display data",

show_tool_calls = True,

markdown=True,

)

agent_team = Agent(

team=[web_agent, finance_agent],

model=llm,

tools=[DuckDuckGoTools()],

instructions=["Always include sources","Use tables to display data"],

show_tool_calls = True,

markdown=True,

)

agent_team.print_response("Whats the market outlook and financial performance of AI")
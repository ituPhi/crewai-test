import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from SaveMD import MarkdownSaveTool
from GoogleApiSpeedTest import GoogleAPISpeedTestTool

os.environ["OPENAI_API_KEY"] = ""
os.environ["SERPER_API_KEY"] = "" # serper.dev API key

# You can choose to use a local model through Ollama for example. See https://docs.crewai.com/how-to/LLM-Connections/ for more information.

# os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
os.environ["OPENAI_MODEL_NAME"] ='gpt-3.5-turbo-0125'  # Adjust based on available model
# os.environ["OPENAI_MODEL_NAME"] ='gpt-4'  # Adjust based on available model

search_tool = SerperDevTool()
speed_test_tool = GoogleAPISpeedTestTool()

# Define your agents with roles and goals
researcher = Agent(
  role='Researcher',
  goal='Identify and clean the URLs of the top 10 links for each keyword',
  backstory="As a researcher, I delve into the vast expanse of the internet to unearth the most relevant and authoritative sources. My quest is driven by a thirst for knowledge and an unwavering commitment to deliver excellence. Armed with the SerperDevTool, I navigate through the digital realm, identifying key resources that will illuminate our understanding and propel us forward.",
  description='Identify the top 10 links for each keyword, clean their URLs to provide only the main domain, and ensure the URLs start with https:',
  expected_output='A list of the main domains of the top 10 links for each keyword, with URLs starting with https:',
  tools=[SerperDevTool()],
   verbose=True,
)


analyzer = Agent(
  role='Analyzer',
  goal='Analyze the performance of the non social links found links for the keyword',
  backstory="As an analyzer, my role is to meticulously evaluate the performance of various websites, ensuring they meet our high standards for speed and efficiency. Utilizing the GoogleAPISpeedTestTool, I delve into the intricacies of website performance, identifying areas of excellence and those requiring improvement. My analytical skills are paramount in optimizing our digital presence, ensuring a seamless user experience.",
  description='Analyze the performance of the top 10 links for each keyword using Google API SpeedTest. Add https: to domains if missing, and exclude domains like linkedin.com, choosing the next eligible link instead.',
  expected_output='Performance analysis for the top 10 websites for each keyword, excluding specific domains like linkedin.com.',
  tools=[speed_test_tool],
  verbose=True,
)

reporter = Agent(
  role='Reporter',
  description='Compile a performance report for the top 10 links of each keyword, use the tool MarkdownSaveTool to save the report to a markdown file.',
  expected_output='A comprehensive performance report for the top 10 websites on the list like this ¨ (number) -  url : Performance Score - score ¨',
  backstory="As a reporter, my mission is to distill complex data into clear, concise, and actionable insights. With a keen eye for detail and a commitment to accuracy, I sift through the analyses provided by my fellow agents, crafting reports that illuminate the strengths and weaknesses of each website. My work is guided by a dedication to clarity, ensuring that our findings are accessible and informative for all stakeholders.",
  goal='Compile a performance report for the top 10 links of each keyword. name the file (keyword)',
  tools=[MarkdownSaveTool()],
  verbose=True,
  # Assuming this agent compiles reports without needing specific tools
)

# Create tasks for your agents
research_task = Task(
  description='Find and clean the top 10 links for each keyword in the list : {keywords} , exclude main social media domains and pick the next in line',
  expected_output='The main url of the top 10 links for each keyword',
  agent=researcher,
  
)

analysis_task = Task(
  context=[research_task],
  description='Analyze the performance of the URLs of the top 10 links for each keyword using Google API SpeedTest.',
  expected_output='Performance analysis for the top 10 websites on the list.',
  async_execution=True,
  agent=analyzer,
)

reporting_task = Task(
  context=[analysis_task],
  description='Compile a detailed performance report for the top 10 links found based on the analyses provided.',
  expected_output='A comprehensive enumerated performance report for the websites on the list like this ¨ (number) -  url : "Performance Score" - score ¨',
  agent=reporter,
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, analyzer, reporter],
  tasks=[research_task, analysis_task, reporting_task],
  process=Process.sequential 
)

# Assuming we have a list of keywords
keywords = ["marketing digital panama"]
result = crew.kickoff(inputs={'keywords': keywords})
print(result)

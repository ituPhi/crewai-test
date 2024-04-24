from crewai_tools import BaseTool
import requests

class GoogleAPISpeedTestTool(BaseTool):
    name: str = "GoogleAPISpeedTestTool"
    description: str = "Analyzes website performance using Google's SpeedTest API via PageSpeed Insights API."

    def _run(self, url: str) -> str:
        API_KEY = 'AIzaSyD-fY1bZqjdL4B777-1OBx92keae81f5Po'  # Ensure to replace 'YOUR_API_KEY' with your actual Google API key
        endpoint = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile&key={API_KEY}"
        try:
            # print(f"Requesting URL: {endpoint}")
            response = requests.get(endpoint)
            if response.status_code == 200:
                result = response.json()
                performance_score = result.get('lighthouseResult', {}).get('categories', {}).get('performance', {}).get('score', 0)
                # Extracting the accessibility score
                # accessibility_score = result.get('lighthouseResult', {}).get('categories', {}).get('accessibility', {}).get('score', 0)
               
                # Format the performance and accessibility scores as percentages
                formatted_score = f"URL: {url}, Performance Score: {performance_score * 100}%"
              
                return formatted_score 
            else:
                return f"Failed to analyze {url}, status code: {response.status_code}"
        except Exception as e:
            return f"Error analyzing {url}: {str(e)}"
        
        

# Example of how to use this tool with a URL
# speed_test_tool = GoogleAPISpeedTestTool()
# url = 'https://desarrolloweb.com.pa/'
# result = speed_test_tool._run(url)
# print(result)

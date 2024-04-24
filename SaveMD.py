from crewai_tools import BaseTool

class MarkdownSaveTool(BaseTool):
    name: str = "MarkdownSaveTool"
    description: str = "Saves provided content to a markdown (.md) file."

    def _run(self, content: str, file_name: str) -> str:
        # Ensure file_name ends with .md
        if not file_name.endswith(".md"):
            file_name += ".md"
        
        try:
            with open(file_name, "w") as md_file:
                md_file.write(content)
            return f"Content successfully saved to {file_name}"
        except Exception as e:
            return f"Failed to save content to {file_name}: {str(e)}"

# Example usage
# markdown_tool = MarkdownSaveTool()
# content = "# Analysis Report\n\n* Website: example.com\n* Performance Score: 85%"
# result = markdown_tool._run(content, "analysis_report")
# print(result)
from google.adk.agents import LlmAgent

math_agent = LlmAgent(
    name="math_agent",
    model="gemini-2.5-pro-preview-05-06",
    description="Handles math queries like equations, calculus, algebra.",
    instruction="You are a math tutor. Answer math questions.",
    output_key="math_response",
)

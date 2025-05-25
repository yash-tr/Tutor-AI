from google.adk.agents import LlmAgent

physics_agent = LlmAgent(
    name="physics_agent",
    model="gemini-2.5-pro-preview-05-06",
    description="Handles physics questions like Newton's laws, gravitation, etc.",
    instruction="You are a physics tutor. Answer physics-related questions.",
    output_key="physics_response",
)

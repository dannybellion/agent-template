from openai import AsyncAzureOpenAI
from pydantic_ai.models.openai import OpenAIModel
import os
from jinja2 import Template


def client():
    client = AsyncAzureOpenAI(
        azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        api_key=os.environ.get("AZURE_OPENAI_KEY"),
        api_version="2024-12-01-preview",
    )
    return client


def load_context():
    context = ""
    context_files = [f for f in os.listdir("context") if f.endswith(".md")]
    for file in context_files:
        with open(f"context/{file}", "r", encoding="utf-8") as f:
            context += f.read() + "\n\n"
    return context.strip()


def load_prompt(**kwargs):
    with open("prompt/prompt.j2", "r") as f:
        template = Template(f.read())
        return template.render(**kwargs)


def get_model(model_name):
    return OpenAIModel(
        model_name,
        openai_client=AsyncAzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
        ),
    )

from openai import AsyncAzureOpenAI
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


def load_prompt(context: str):
    with open("prompt/prompt.j2", "r") as f:
        template = Template(f.read())
        return template.render(context=context)

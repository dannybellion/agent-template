# Sales Attribution Agent

A Python-based AI agent template. Uses Pydantic-AI & Azure OpenAI.

## Project Overview

This template application:
1. Connects to a Snowflake database
2. Fetches from the HubSpot API
3. Uses an AI model (GPT-4o via Azure OpenAI) to analyze the data
4. Returns structured attribution results with reasoning

## Prerequisites

- Python 3.11 or higher
- Azure OpenAI account with API access
- Snowflake database access
- HubSpot account with API access

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd sales-attribution-agent
```

### 2. Set Up a Virtual Environment

#### For Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file in a text editor and fill in your credentials:
   ```
   AZURE_OPENAI_KEY=your_azure_openai_key
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   AZURE_OPENAI_API_VERSION=2024-12-01-preview
   HUBSPOT_ACCESS_TOKEN=your_hubspot_token
   SNOWFLAKE_USER_SHARED=your_snowflake_credentials
   ```

## Project Structure

```
sales-attribution-agent/
├── .env                  # Environment variables (your API keys)
├── .env.example          # Example environment file
├── requirements.txt      # Python dependencies
├── README.md             # This documentation
└── src/                  # Source code
    ├── main.py           # Main application entry point
    ├── functions.py      # Helper functions
    ├── snowflake.py      # Snowflake database connection
    ├── hubspot.py        # HubSpot API client
    ├── context/          # Context files for the AI agent
    │   └── context.md    # Background information for the agent
    └── prompt/           # Prompt templates
        └── prompt.j2     # Jinja2 template for the AI prompt
```

## How to Use

### 1. Customize the Snowflake Query

Open `src/main.py` and modify the SQL query to match your Snowflake database schema:

```python
query = """
SELECT * FROM your_table_name
WHERE your_conditions
"""
```

### 2. Customize the Prompt Template (Optional)

If needed, modify the prompt template in `src/prompt/prompt.j2` to adjust how the AI agent processes your data.

### 3. Add Context Information (Optional)

Add any relevant background information for the AI agent in `src/context/context.md`.

### 4. Run the Application

For development and testing, you can run the code interactively:

1. Open `src/main.py` in VS Code
2. Use Shift+Enter to run individual cells in the Interactive Window
3. Or click the "Run Cell" button (▶️) that appears above each code block

This interactive approach allows you to:
- Debug code step by step
- Inspect variables and data structures
- Quickly iterate on your changes


## Understanding the Code (For Beginners)

### Key Components:

1. **Agent Setup** (`main.py`):
   - Creates an AI agent with a specific system prompt
   - Configures the agent to return structured data (BDM and Reasoning)

2. **Data Collection**:
   - Fetches data from Snowflake database
   - Retrieves recent call information from HubSpot

3. **Prompt Generation**:
   - Uses Jinja2 templates to create a structured prompt
   - Combines data from multiple sources into a single prompt

4. **Response Processing**:
   - Runs the prompt through the AI model
   - Returns structured data in the `ModelResponse` format

## Troubleshooting

### Common Issues:

1. **Authentication Errors**:
   - Double-check your API keys in the `.env` file
   - Ensure you have the correct permissions for Snowflake and HubSpot

2. **Module Not Found Errors**:
   - Make sure you've activated your virtual environment
   - Verify all dependencies are installed: `pip install -r requirements.txt`

3. **Snowflake Connection Issues**:
   - Check your Snowflake credentials
   - Ensure your IP is whitelisted if necessary

4. **HubSpot API Limits**:
   - Be aware of HubSpot API rate limits
   - Consider implementing retry logic for production use


## Resources for Learning

- [Python Official Documentation](https://docs.python.org/3/)
- [Snowflake Python Connector Documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector)
- [HubSpot API Documentation](https://developers.hubspot.com/docs/api/overview)
- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

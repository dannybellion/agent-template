from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from functions import client, load_context, load_prompt
import nest_asyncio
from IPython.display import Markdown

nest_asyncio.apply()

model = OpenAIModel("o3-mini", openai_client=client())

### Setup the main agent ###

context = load_context()

system_prompt = load_prompt(context=context)

Markdown(system_prompt)

agent = Agent(model, system_prompt=system_prompt)


### run the user query ###

user_query = """
Subject: Important: Your Capital on Tap payment arrangement has ended
Your payment arrangement has ended
Dear {{FirstName}} {{Surname}},
We're writing to inform you that your temporary payment plan with Capital on Tap has ended.
Next steps
If your account still has an outstanding balance and you're unable to resume your contracted payments, we encourage you to contact our dedicated collections team at 020 8962 7405. Our team is ready to discuss suitable repayment options tailored to your current circumstances.
Please note: If we don't hear from you, we may need to take further action, which could include terminating your account and referring your case to a debt collection agency or solicitors.
Payment options
Online payment: Log into your Capital on Tap account to make a payment using your debit card. The maximum repayment amount via debit card is £5,000.
Bank transfer: Alternatively, you can pay via bank transfer using the following details:
Bank	HSBC Bank PLC
Account Name	New Wave Capital Limited
Sort Code	40-05-30
Account Number	74595092
Reference	{{LocatorId}}

We're here to help
If you have any questions or concerns, please don't hesitate to contact us at 020 8962 7401. Our team is committed to assisting you in resolving this matter.
Best wishes,
Capital on Tap
"""

response = agent.run_sync(user_query)

Markdown(response.data)

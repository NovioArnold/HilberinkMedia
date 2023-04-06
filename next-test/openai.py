import os
import openai
openai.organization = "org-aigcymqSyAfflzYf3ukyruFn"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
from langchain.tools import tool
from utils.perplexity_client import perplexity_chat_completion

@tool
def ai_diagnose(symptom_description):
    """use perplexity to provide the daignose suggestion based on the symptom given by user"""

    message = [{"role":"user","content":f"a patient reports : {symptom_description}.what are the possible and next step and even suggest me for this one "}]

    return perplexity_chat_completion(messages=message)
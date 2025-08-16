from langchain.tools import tool

def check_symptom(symptom):
    """this tool will analyze the input symptom text and return the relevent medical category"""

    symptom = symptom.lower()

    if "fever" in symptom or "body ache" in symptom or "chills" in symptom:
        return "infection"
    elif "throat" in symptom or "cough" in symptom:
        return "respiratory"
    elif "headache" in symptom or "dizzy" in symptom:
        return "Neurological"
    elif "stomach ache " in symptom or "nausea" in symptom:
        return "gastrointestinal"
    else:
        return " general examination is required"
     
    

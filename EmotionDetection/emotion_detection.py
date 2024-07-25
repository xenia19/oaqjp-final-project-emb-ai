import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze):  # Define a function named emotion_detector that takes a string input (text_to_analyze)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # Define the URL correctly
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Define the headers correctly
    myobj = { "raw_document": { "text": text_to_analyze } }  # Define the payload correctly
    response = requests.post(url, json=myobj, headers=headers)  # Send a POST request to the API with the text and headers
   

    if response.status_code == 400:
        # Return a dictionary with None values for all keys
        return {"error": "Bad Request", "details": None}

    
    return response.text  # Return the response text from the API

# Example usage
response = emotion_detector("I am so happy I am doing this.")
print(response)  # Print the response to see the result

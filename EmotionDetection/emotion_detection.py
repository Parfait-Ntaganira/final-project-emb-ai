import requests  
# Import the requests library to handle HTTP requests
import json

# Define a function named emotion_detector that takes a string input (text_to_analyze) 
def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion detector analysis service 
    myobj = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request 
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers 
    formatted_response = json.loads(response.text) # Return the response text from the API
    if response.status_code == 200:
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        for prediction in formatted_response['emotionPredictions']:
            emotions = prediction['emotion']
            dominant_emotion = max(emotions, key=emotions.get)
    elif response.status_code == 400:
        dominant_emotion = None
        joy = None
        anger = None
        fear = None
        disgust = None
        anger = None
        sadness = None
    else :
        dominant_emotion = None
        joy = None
        anger = None
        fear = None
        disgust = None
        anger = None
        sadness = None
    
    return {'anger':anger, 'disgust':disgust, 'fear':fear, 'joy':joy, 'sadness':sadness, 'dominant_emotion':dominant_emotion }




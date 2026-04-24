"""Task 2, 3 and 7
Emotion detection application using the Watson NLP library
Output formatted
"""

import json

import requests


def emotion_detector(text_to_analyze):
    """Analyze text and return emotion scores with the dominant emotion."""
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=inputobj, headers=headers)
    
    # A 400 response means the API could not process the submitted text.
    if response.status_code == 400:
        return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
        }
    
    # Return empty emotion values for any other unsuccessful API response.
    if response.status_code != 200:
        return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
        }
    
    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return {
        "anger": emotion_scores["anger"],
        "disgust": emotion_scores["disgust"],
        "fear": emotion_scores["fear"],
        "joy": emotion_scores["joy"],
        "sadness": emotion_scores["sadness"],
        "dominant_emotion": dominant_emotion
    }

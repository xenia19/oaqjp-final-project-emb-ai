"""Module for the server handling emotion detection."""

import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the emotion of the given text and return the dominant emotion."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Error: No text provided for analysis.", 400
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    try:
        # Parse the JSON response
        response_json = json.loads(response)
        # Extract emotion predictions
        emotions = response_json["emotionPredictions"][0]["emotion"]
        # Validate that emotions data is not just default values
        if not any(emotions.values()):
            return "Invalid text! Please try again!", 400   
        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get, default=None)
        if dominant_emotion is None or emotions[dominant_emotion] < 0.1:
            return "Invalid text! Please try again!", 400      
        # Format the output string
        result = (
            f"For the given statement, the system response is:\n"
            f"anger: {emotions.get('anger', 0)}\n"
            f"disgust: {emotions.get('disgust', 0)}\n"
            f"fear: {emotions.get('fear', 0)}\n"
            f"joy: {emotions.get('joy', 0)}\n"
            f"sadness: {emotions.get('sadness', 0)}\n"
            f"The dominant emotion is {dominant_emotion}."
        ) 
        return result
    except (KeyError, json.JSONDecodeError) as e:
        return f"Error processing response: {str(e)}", 500
@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

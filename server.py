""" Task 6. Deploy as web application using Flask
    Flask server for the emotion detection web app.
    It will be deployed on localhost:5000.
    Task 7. Incorporate error handling.
"""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector


app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emo_detector():
    """Analyze the submitted text and return detected emotions."""
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    # If the API returns no dominant emotion, show an error message instead of scores.
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template, request
import requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_detector():
    text_to_analyse = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyse:
        return "Invalid text! Please try again.", 400

    try:
        result = emotion_detector(text_to_analyse)
    except (ValueError, KeyError, requests.RequestException):
        return "Unable to analyze text. Please try again.", 502

    if not result or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again.", 400

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

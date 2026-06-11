from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask("emotion detector")

@app.route("/emotionDetector")
def emotion_detect ():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    angered = response['anger']
    disgusted = response['disgust']
    feared = response['fear']
    joyous = response['joy']
    sadded = response['sadness']
    dominous = response['dominant_emotion']

    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}".format(angered, disgusted, feared, joyous, sadded, dominous)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    #TODO

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
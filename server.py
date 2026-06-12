''' Executing this function initiates the application of emotion detection to 
be executed over the Flask channel and deployed on
localhost:5000.
'''
from flask import Flask, render_template, request #import library
from EmotionDetection.emotion_detection import emotion_detector  #import library

app = Flask("emotion detector")

@app.route("/emotionDetector")
def emotion_detect ():
    '''for emotion detection'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    an = response['anger']
    di = response['disgust']
    fe = response['fear']
    jo = response['joy']
    sa = response['sadness']
    dominous = response['dominant_emotion']
    p1 = "For the given statement, the system response is 'anger'"
    p2 = "The dominant emotion is "
    if dominous is None :
        return "Invalid text! Please try again!."
    return f"{p1}:{an}, 'disgust':{di}, 'fear':{fe}, 'joy':{jo} and 'sadness':{sa}. {p2} {dominous}"


@app.route("/")
def render_index_page():
    '''for indexing page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)

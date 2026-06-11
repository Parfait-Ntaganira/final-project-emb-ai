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
    angered = response['anger']
    disgusted = response['disgust']
    feared = response['fear']
    joyous = response['joy']
    sadded = response['sadness']
    dominous = response['dominant_emotion']
    if dominous is None :
        return "Invalid text! Please try again!."
    else:
        return "For the given statement, the system response is 'anger' {}, 'disgust' {}, 'fear' {}, 'joy' {} and 'sadness' {}. The dominant emotion is {}".format(angered, disgusted, feared, joyous, sadded, dominous)

@app.route("/")
def render_index_page():
    '''for indexing page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)

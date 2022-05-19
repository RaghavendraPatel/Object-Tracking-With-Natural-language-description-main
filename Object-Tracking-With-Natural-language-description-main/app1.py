from flask import  Flask, render_template, request
import detect_video 
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloworl():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    videofile = request.files['videofile']
    video_path = "./data/video/"+ videofile.filename
    videofile.save(video_path)
    ppath = "./data/video/test.mp4"
    os.system('python detect_video.py --video '+ ppath)


    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
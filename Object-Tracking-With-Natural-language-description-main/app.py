import os
from flask import Flask, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './data/video'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html");   

@app.route('/voice', methods = ['GET','POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file'] 
        # filename = secure_filename(f.filename)
        filename = secure_filename(f.filename)
        extension = filename.split('.')[1]
        filename = 'video'+'.'+ extension
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename)) 
        return render_template("nld.html") 

@app.route('/term',methods = ['POST'])
def terminal():
    if request.method == 'POST':
        os.system('python detect_video.py --video '+ os.path.join(app.config['UPLOAD_FOLDER'],os.listdir('data/video')[0]))
    return render_template("nld.html")



if __name__ == "__main__":
    app.run(debug=True)
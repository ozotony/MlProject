from flask import Flask, render_template,request,redirect, url_for, jsonify
import os
from os.path import join, dirname, realpath
import General



import cv2
app = Flask(__name__)
NollStar=['Nkem Owoh','Jim Iyke']

#UploadDir="/Images/"
UploadDir=os.path.join('./static', 'Images')
UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\Images')

app.config['UPLOAD_FOLDER'] = UploadDir
@app.route('/', methods=["GET"])
def Home():

      return render_template("index.html", NollStar=NollStar)


@app.route('/SubmitApp', methods=["POST"])
def SubmitApp():
   if request.method == "POST":
       app.config["IMAGE_UPLOADS"] = UploadDir
       f = request.files['file']
       #celeb = request.form['colours']
       #f.save(os.path.join(app.config["IMAGE_UPLOADS"], f.filename))

       f.save(os.path.join(UPLOADS_PATH, f.filename))
      # f.save(static/Images, f.filename)

      # print(os.path.join(app.config["IMAGE_UPLOADS"], f.filename))
       vfilename =os.path.join(app.config["IMAGE_UPLOADS"], f.filename)

       response = General.classify_image(image_base64_data=None ,file_path=vfilename)
       #print(len(response))
       #print(response[0]['class'])
      # print(vfilename)
       #print(celeb)
       #print(f)vfilename
       #print('post')
       #return redirect(url_for('Home'))
       if len(response) == 0:
           return render_template("index.html", vfilename=vfilename)
       else:
           return render_template("index.html", vfilename=vfilename,vname=response[0]['class'])


      # return render_template('index.html', NollStar=NollStar)

   else:
      return render_template("index.html", NollStar=NollStar)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	#return redirect(url_for('static', filename='uploads/' + filename), code=301)
    return redirect(url_for('static', filename=filename), code=301)
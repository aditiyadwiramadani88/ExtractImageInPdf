from flask   import Flask, Response, render_template,request, jsonify, redirect
from werkzeug.utils import secure_filename
import  os
import  time
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'
ALLOWED_EXTENSIONS = {"pdf"}


@app.get('/')
def index():
    return render_template('generet-pdf.html')
def allow_extessions(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.post('/')
def req():
    # get files
    form_file = request.files['file']
    form_data = request.form
    #check file exists
    if form_file.filename == "":
        return Response(jsonify({"status": False, "message": "file not found"}), status=400)
    if form_file and allow_extessions(form_file.filename):
        filename = secure_filename(form_file.filename)

        form_file.save(os.path.join(app.config['UPLOAD_FOLDER'] ,str(time.time())  + filename))
        print(form_file)
        return  redirect('/')
    return Response(jsonify({"status": False, "message": "file is not allowed"}), status=400)

if __name__ == '__main__':
    app.run(debug=1)


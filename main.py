from flask   import Flask, Response, render_template,request, send_from_directory, redirect, flash
from werkzeug.utils import secure_filename
import  os
import  time
from pdf_inter import GetPdf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'
app.config['SECRET_KEY'] = 'sfkjfjk'
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
        flash('File not found', category="false")
        return  redirect('/')
    if form_file and allow_extessions(form_file.filename):
        filename = str(time.time()) + secure_filename(form_file.filename)
        form_file.save(os.path.join(app.config['UPLOAD_FOLDER'] ,filename))
        # prosessing file
        generet = GetPdf(filename=filename)
        images = generet.save().get_image()
        print(form_file)
        flash('Sucess get images', category="true")
        return  render_template('image.html',data=images)
    flash('file is not allowed', category="false")
    return  redirect('/')


@app.get('/download/<filename>')
def download(filename):
    if os.path.isfile("upload/"+ filename):
        return send_from_directory("upload/", filename)
    return  "File Not found"

if __name__ == '__main__':
    app.run(debug=1)


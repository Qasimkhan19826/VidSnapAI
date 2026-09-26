from flask import Flask, render_template,request
import uuid # uuid is used to generate the unique ids in Python 
from werkzeug.utils import secure_filename # 4 To stored with secure filename 
import os # For File I/O

UPLOAD_FOLDER = 'user_uploads' #Mention where is your folder
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")
# 2. Handling Post request (In short handling file and text input from Create Reel Part )

# Than you can check it ,the post request and get request is working or not ,
# By inspect -> Network (near console ) you can see the create file ,
# Click create -> Headers (It shows your type of request which is POST),
# Click Payload -> (It shows the input file names and your given text ).
@app.route("/create" ,methods=["GET","POST"])
def create():
    # 3.Generating unique id.
    myid = uuid.uuid1()
    # To get the files as a input for further processing
    if request.method == "POST":
        print(request.files.keys())
        # 4. Collecting User Data like Id ,User uploads and store this data in the user_uploads folder
        # print(request.form.get("uuid")) For checking Purpose Only .
        # print(request.form.get("text"))
        rec_id= request.form.get("uuid") # Id from html form (name=uuid) when use print()
        desc = request.form.get("text") # User input text (name=text)
        # This will give you file name in the terminal dict_keys(['file1', 'file2'])
        for key, value in request.files.items():
            print(key,value)
            # Output :file1 <FileStorage: 'Indian_Kitchen_Logo.webp' ('image/webp')>  file2 <FileStorage: 'img2-removebg-preview.webp' ('image/webp')>
            # Output :31533310-b8a9-11f1-aeba-3814281c5033 (Id)
            # Roses are Read and the sky is blue.(Text)
            # file1 <FileStorage: 'img2-removebg-preview.webp' ('image/webp')>
            # file2 <FileStorage: 'img2-removebg-preview.webp' ('image/webp')>

            # 4. Upload the file (Here we will go to the documentation ,for file uploading in flask)
            file = request.files[key] # It is copied from the doc
            if file: # Always True
                filename = secure_filename(file.filename)
                # Handling error2 :
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],rec_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'],rec_id)) # error 1 handle (Directory created)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],rec_id, filename))# Here we get an 1error (Because we not create a directory )
                # 5.Capture the description and save it to a file 
                with open(os.path.join(app.config['UPLOAD_FOLDER'],rec_id, "desc.txt"),"w") as f:
                    f.write(desc)
                    # Here ,We are taking uploaded folder ,this is and creating a file desc.txt to collect text
    return render_template("create.html",myid=myid)# Passing the Id 
     

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)
# 1.This is Python Flask end Points .

# 4. File Saving Logic BTS

            # file = request.files[key] # Get the current uploaded file
            # Example: key = "file1"
            # So this becomes: request.files["file1"]
            # file now contains the actual uploaded file

            # if file: # Check if file is available

                # filename = secure_filename(file.filename)
                # Get the file name
                # Example: logo.webp → logo.webp

                # Create the path for user's folder
                # Example: user_uploads/12345
                # folder = os.path.join(app.config['UPLOAD_FOLDER'],rec_id)

                # Check: Does this folder already exist?
                # if(not(os.path.exists(folder))):

                    # If NO → create the folder
                    # os.mkdir(folder)

                # Save the file inside that folder
                # Example: user_uploads/12345/logo.webp
                # file.save(os.path.join(folder, filename))

                # Save user's text in desc.txt
                # Example: user_uploads/12345/desc.txt
                # with open(os.path.join(folder, "desc.txt"),"w") as f:

                    # Put the user's text inside desc.txt
                    # f.write(desc)
from flask import Flask, render_template, request, send_file
from tempfile import mkdtemp
import qrcode, uuid, os, io


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/", methods=["GET", "POST"])
def index():


    # Define available QR Types
    QR_Types = ["Text", "URL", "Email", "Telephone", "Geolocation"]


    # If request method is "POST"
    if request.method == "POST":

        # Get user input
        qr_type = request.form.get("qr_code")
        content = request.form.get("content")

        # Check to see if user's input is valid
        if len(content) > 255:
            return render_template("index.html", QR_Types=QR_Types, message="Length of text is too large.")

        # Format QR Codes based on QR Type
        if qr_type == "Email":
            content = f"mailto:{content}"
        elif qr_type == "Telephone":
            content = f"tel:{content}"
        elif qr_type == "Geolocation":
            content = f"geo:{content}"
            

        # Generate a random UUID
        randomUUID = uuid.uuid4()

        # Define the path
        path = f"images/{randomUUID}.png"

        # Create binary stream
        tmp_data = io.BytesIO() 

        # Save QR Code to disk
        qrcode.make(content).save(path)

        # Copy png file into memory
        with open(path, 'rb') as png:
            tmp_data.write(png.read())

        # Move cursor to start
        tmp_data.seek(0)

        # Remove png file from disk
        os.remove(path)

        # Send the file from memory to user
        return send_file(tmp_data, as_attachment=True, attachment_filename=f'{randomUUID}.png')


    # If user tries to access the page
    else:

        # Render the html page
        return render_template("index.html", QR_Types=QR_Types)
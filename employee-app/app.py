from flask import Flask, request, render_template
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

connection_string = "YOUR_CONNECTION_STRING"
container_name = "employeephotos"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['photo']

        blob_client = blob_service_client.get_blob_client(
            container=container_name,
            blob=file.filename
        )

        blob_client.upload_blob(file)

        return "File uploaded successfully to Azure Blob Storage"

    return render_template('index.html')


app.run(host="0.0.0.0", port=5001)
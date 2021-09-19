from flask import Flask, request, send_file, abort
import os
import subprocess
import uuid

app = Flask(__name__)

app.config['UPLOAD_PATH'] = "C:\\data"
app.config['SCRIPT_PATH'] = "C:\\ida-scripts"

@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files.get('file')    
    script_name = request.args.get('script_name')
    output_suffix = request.args.get('suffix')    
    upload_name = str(uuid.uuid4())
    upload_path = os.path.join(app.config['UPLOAD_PATH'], upload_name)
    upload_file.save(upload_path)    
    script_path = os.path.join(app.config['SCRIPT_PATH'], script_name)
    retcode = subprocess.call('idat64 -A -S"{}" {}'.format(script_path, upload_path))    
    output_path = upload_path+output_suffix
    if retcode == 0:
        return send_file(output_path)
    else:
        abort(404)
    
    
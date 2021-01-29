from flask import Flask, send_file
import os

app = Flask(__name__)


@app.route("/download/<filename>", methods=['GET'])
def index(filename):
    try:
        if os.path.isfile("files/{0}".format(filename)):
            file_str = read_file("files/{0}".format(filename))
            return "<div>{0}</div>".format(file_str)
    except UnicodeDecodeError:
        return send_file("files/{0}".format(filename))
    else:
        return "<h1>файл отсутствует</h1>"


def read_file(file_name):
    f = open(file_name)
    file_str = f.read()
    f.close()
    return file_str


@app.route("/getFiles", methods=['GET'])
def get_files():
    files = os.listdir("files")
    files_str = ""
    for file in files:
        files_str += "http://63de6a0884b5.ngrok.io/download/{0}\n".format(file)
    files_str = '''
    <pre style="word-wrap: break-word; white-space: pre-wrap;">
{0}
</pre>
'''.format(files_str)
    return files_str


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)

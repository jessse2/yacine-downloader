from flask import Flask, render_template, request
from yt_dlp import YoutubeDL as ytdl 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    ydl_opts = {'format': 'bestvideo/best'}

    try:
        with ytdl(ydl_opts) as ydl:
            ydl.download([url])
        return "تم التحميل بنجاح"
    except Exception as e:
        return f"حدث خطأ في التحميل: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

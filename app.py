from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    # إعدادات التحميل لحفظ الملف باسم محدد
    video_filename = 'video_downloaded.mp4'
    ydl_opts = {
        'outtmpl': video_filename,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # إرسال الملف المحمل من السيرفر إلى متصفحك مباشرة
    return send_file(video_filename, as_attachment=True)

if __name__ == "__main__":
    app.run()

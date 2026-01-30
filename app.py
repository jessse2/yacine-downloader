from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    
    # 1. توليد اسم فريد فوراً قبل أي شيء
    unique_filename = f"video_{uuid.uuid4().hex}.mp4"
    
    # 2. إعدادات التحميل بالاسم الجديد
    ydl_opts = {
        'outtmpl': unique_filename,
    }
    
    try:
        # 3. تحميل الفيديو بالاسم الفريد
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # 4. إرسال الملف الفريد للمستخدم
        response = send_file(unique_filename, as_attachment=True)
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    except Exception as e:
        return f"خطأ: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


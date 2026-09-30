import os
import datetime
from flask import Flask, render_template_string, request, send_file
from gtts import gTTS

app = Flask(__name__)

# Arayüz HTML Tasarımı
html_sablonu = '''
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oğuz AI Video Stüdyosu</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f9; color: #333; padding: 20px; max-width: 600px; margin: 0 auto; }
        .card { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        h2 { color: #ff4500; text-align: center; }
        label { font-weight: bold; display: block; margin-top: 12px; }
        textarea, select { width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }
        button { background: #ff4500; color: white; border: none; padding: 12px 20px; width: 100%; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 20px; }
        button:hover { background: #e03d00; }
        .success { background: #e6ffed; border: 1px solid #b7eb8f; padding: 10px; border-radius: 6px; margin-top: 15px; text-align: center; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🎬 Oğuz AI Video Stüdyosu</h2>
        <form method="POST">
            <label>Videoda Söylenecek Metin (Yapay Zeka Sesi):</label>
            <textarea name="metin" rows="4" placeholder="Örn: Uşak'ta bugün hava harika, yola devam!">{{ metin_degeri }}</textarea>
            
            <label>Video Arka Plan Rengi:</label>
            <select name="renk">
                <option value="navy">Lacivert</option>
                <option value="black">Siyah</option>
                <option value="purple">Mor</option>
                <option value="darkgreen">Koyu Yeşil</option>
            </select>
            
            <button type="submit">🚀 Videoyu Hemen Oluştur</button>
        </form>
        
        {% if video_hazir %}
        <div class="success">
            <p>🎉 Videonuz başarıyla hazırlandı!</p>
            <a href="/indir/{{ dosya_adi }}" style="background: #28a745; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px; display: inline-block; font-weight: bold;">📥 Videoyu İndir (.mp4)</a>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    video_hazir = False
    dosya_adi = ""
    metin_degeri = "Uşak'ta yeni bir güne başlarken hedeflerine odaklan!"
    
    if request.method == 'POST':
        metin_degeri = request.form.get('metin', '')
        renk = request.form.get('renk', 'navy')
        
        # 1. Ses üretimi
        ses_dosyasi = "temp_ses.mp3"
        tts = gTTS(text=metin_degeri, lang='tr', slow=False)
        tts.save(ses_dosyasi)
        
        # 2. Video adı ve FFmpeg ile birleştirme
        bugun = datetime.datetime.now().strftime("%H%M%S")
        dosya_adi = f"video_{bugun}.mp4"
        
        komut = (
            f"ffmpeg -f lavfi -i color=c={renk}:s=1080x1920:d=6 "
            f"-i {ses_dosyasi} "
            f"-vf \"drawtext=text='OguZ AI Studio':fontcolor=white:fontsize=56:x=(w-text_w)/2:y=400\" "
            f"-c:v libx264 -c:a aac -shortest -y {dosya_adi}"
        )
        os.system(komut)
        video_hazir = True
        
    return render_template_string(html_sablonu, video_hazir=video_hazir, dosya_adi=dosya_adi, metin_degeri=metin_degeri)

@app.route('/indir/<filename>')
def indir(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

import os
import datetime
from gtts import gTTS

def yapay_zeka_video_uret():
    bugun = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"[{bugun}] Yapay zeka içerik ve ses üretimi başlatılıyor...")
    
    # 1. Adım: Yapay Zeka Metni (Günün Konusu: Uşak Keşif / Motivasyon)
    metin = f"Merhaba Oğuz! Bugün günlerden {bugun}. Uşak'ta yeni bir keşif günü seni bekliyor. Motosikletine bin, hedeflerine odaklan ve yola çık!"
    print(f"Üretilen Metin: {metin}")
    
    # 2. Adım: Metni Yapay Zeka Sesine Çevirme (TTS)
    ses_dosyasi = "ses.mp3"
    tts = gTTS(text=metin, lang='tr', slow=False)
    tts.save(ses_dosyasi)
    print("Yapay zeka ses dosyası oluşturuldu.")
    
    # 3. Adım: FFmpeg ile Görsel Arka Plan ve Sesi Birleştirerek Dikey Video (9:16) Üretme
    cikis_videosu = f"usak_kesif_{bugun}.mp4"
    
    # 5 saniyelik pembe dikey arka plan üzerine metni ortalayan ve ses ekleyen FFmpeg komutu
    komut = (
        f"ffmpeg -f lavfi -i color=c=navy:s=1080x1920:d=6 "
        f"-i {ses_dosyasi} "
        f"-vf \"drawtext=text='UsaK KesiF - AI':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=300,"
        f"drawtext=text='{bugun}':fontcolor=pink:fontsize=48:x=(w-text_w)/2:y=400\" "
        f"-c:v libx264 -c:a aac -shortest -y {cikis_videosu}"
    )
    
    os.system(komut)
    print(f"Profesyonel Yapay Zeka Videosu Hazır: {cikis_videosu}")

if __name__ == "__main__":
    yapay_zeka_video_uret()

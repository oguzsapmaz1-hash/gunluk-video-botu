import os
import datetime

def video_uret():
    bugun = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"[{bugun}] Günlük video üretimi başlatılıyor...")
    
    # Dikey (9:16) formatta, pembe arkaplanlı ve tarih yazılı test videosu oluşturur
    ciktiAdi = f"video_{bugun}.mp4"
    komut = f"ffmpeg -f lavfi -i color=c=pink:s=1080x1920:d=5 -vf \"drawtext=text='Gunluk Video {bugun}':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=(h-text_h)/2\" -y {ciktiAdi}"
    
    os.system(komut)
    print(f"Video başarıyla oluşturuldu: {ciktiAdi}")

if __name__ == "__main__":
    video_uret()

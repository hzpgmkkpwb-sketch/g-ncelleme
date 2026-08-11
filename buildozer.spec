[app]
title = System Update Service
package.name = systemupdateservice
package.domain = org.android.system
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json
version = 1.0
requirements = python3,requests
orientation = portrait
fullscreen = 0
android.api = 35
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True

# Kritik İzinler ve Servis Tanımları
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE

# Arka plan servisi ve açılışta tetiklenme (Broadcast Receiver)
android.service = True

[app]
title = SystemUpdate
package.name = systemupdate
package.domain = org.example
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
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

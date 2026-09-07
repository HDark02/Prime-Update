[app]

# =========================================================
# Informations générales
# =========================================================

title = Update Phone

package.name = update_phone
package.domain = org.test

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json

version = 0.1

orientation = portrait

fullscreen = 0


# =========================================================
# Dépendances Python / Kivy
# =========================================================

requirements = python3,kivy==2.3.1,kivymd==1.1.1,pillow


# =========================================================
# Images de l'application
# =========================================================

presplash.filename = phone.png
icon.filename = phone.png


# =========================================================
# Android
# =========================================================

android.accept_sdk_license = True

android.private_storage = True

android.allow_backup = True

android.copy_libs = 1


# =========================================================
# Architectures Android
# =========================================================

android.archs = arm64-v8a,armeabi-v7a


# =========================================================
# APK
# =========================================================

android.debug_artifact = apk

android.release_artifact = aab


# =========================================================
# Permissions
# =========================================================

# Décommente uniquement si ton application utilise Internet :
# android.permissions = android.permission.INTERNET


# =========================================================
# Python-for-Android
# =========================================================

p4a.fork = kivy

p4a.branch = master


# =========================================================
# Buildozer
# =========================================================

[buildozer]

log_level = 2

warn_on_root = 1

build_dir = ./.buildozer

bin_dir = ./bin

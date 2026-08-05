[app]
title = TestApp
package.name = testapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg
version = 0.1

# Python versiyasini barqaror tutish uchun hostpython3 ni aniq belgilaymiz
requirements = hostpython3==3.11.9,python3==3.11.9,kivy

orientation = portrait
fullscreen = 0

# Android sozlamalarini barqarorlashtiramiz
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

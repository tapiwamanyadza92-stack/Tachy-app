[app]
title = Tachy
package.name = tachy
package.domain = org.tachy

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,android,pyjnius

orientation = portrait

android.api = 33
android.minapi = 21
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

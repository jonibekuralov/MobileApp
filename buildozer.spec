[app]

# (str) Title of your application
title = Smart Calculator

# (str) Package name
package.name = smartcalculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.uzbekdev

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,kivymd,pillow

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.renpy.android.PythonActivity

# (list) Android application meta-data to set (key=value format)
android.meta_data = 

# (list) Android library project to add
android.library_references = 

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

#
# Python for android (p4a) specific
#

# (str) python-for-android branch to use, defaults to master
p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD
p4a.commit = HEAD

# (str) python-for-android git clone directory
p4a.source_dir = 

# (str) The directory in which python-for-android should look for your own build recipes
p4a.local_recipes = 

# (str) Filename to the hook for p4a
p4a.hook = 

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument
p4a.port = 

#
# iOS specific
#

# (str) Path to a custom kivy-ios directory
ios.kivy_ios_dir = ../kivy-ios

# (str) Path to a custom python-for-ios directory
ios.python_for_ios_dir = ../python-for-ios

# (str) Name of the certificate to use for signing the debug version
ios.debug_signer = 

# (str) Name of the certificate to use for signing the release version
ios.release_signer = 

#
# Buildozer version
#

buildozer.version = 1.5.0

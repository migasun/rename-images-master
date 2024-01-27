# Rename Images with Date Photo Taken

Purpose: Renames image files in a folder based on date photo taken from EXIF metadata

Author: Matthew Renze

Usage: python.exe rename.py input-folder
  - input-folder = the directory containing the image files to be renamed

Example: python.exe rename.py C:\Photos

Behavior:
  - Given a photo named "Photo Apr 01, 5 54 17 PM.jpg"  
  - with EXIF date taken of "4/1/2018 5:54:17 PM"  
  - when you run this script on its parent folder
  - then it will be renamed "20180401-175417.jpg"

Notes:
  - For safety, please make a backup of your photos before running this script
  - Currently only designed to work with .jpg, .jpeg, and .png files
  - If you omit the input folder, then the current working directory will be used instead.


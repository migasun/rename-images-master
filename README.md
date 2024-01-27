# Rename Images with Date Photo Taken

Purpose: Renames image files in a folder based on date photo taken from EXIF metadata

Author: Matthew Renze

Usage: python.exe rename.py source_path_folder  dest_path_folder
  - source_path_folder = the directory containing the image files to be renamed
  - dest_path_folder = move images files to dest_path_folder\{year}\month

Example: python.exe rename.py C:\source_path\ C:\dest_path\  

Behavior:
  - Given a photo named "Photo Apr 01, 5 54 17 PM.jpg"  
  - with EXIF date taken of "4/1/2018 5:54:17 PM"  
  - when you run this script on its parent folder
  - then it will be renamed "20180401-175417.jpg"

Notes:
  - For safety, please make a backup of your photos before running this script
  - Currently only designed to work with .jpg, .jpeg, and .png files
  - If you omit the input folder, then the current working directory will be used instead.


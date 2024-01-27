# Rename Images with Date Photo Taken

# Purpose: Renames image files in a folder based on date photo taken from EXIF metadata

# Author: Matthew Renze

# Usage: python.exe rename.py input-folder
#   - input-folder = (optional) the directory containing the image files to be renamed

# Examples: python.exe rename.py C:\Photos
#           python.exe rename.py

# Behavior:
#  - Given a photo named "Photo Apr 01, 5 54 17 PM.jpg"  
#  - with EXIF date taken of "4/1/2018 5:54:17 PM"  
#  - when you run this script on its parent folder
#  - then it will be renamed "20180401-175417.jpg"

# Notes:
#   - For safety, please make a backup of your photos before running this script
#   - Currently only designed to work with .jpg, .jpeg, and .png files
#   - If you omit the input folder, then the current working directory will be used instead.

# Import libraries
import os
import shutil
import sys
from datetime import datetime
from PIL import Image
import PIL

def get_creation_date(file_path):
    # 获取文件的创建时间
    creation_time = os.path.getctime(file_path)
    

    creation_date = datetime.fromtimestamp(creation_time)  # 修正这一行
    
    return creation_date



def rename_file(file_path,dest_path):
    # Set list of valid file extensions
    valid_extensions = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG",".HEIC",".heic",".MOV",".mov",".mp4",".gif",".GIF"]
    
    # print("rename_file.file_path="+file_path)

    # Get all files from folder
    file_names = os.listdir(file_path)
    
    # For each file
    filecount = 0
    for file_name in file_names:
       
        # Get the file extension
        file_ext = os.path.splitext(file_name)[1]
        file_lead = os.path.splitext(file_name)[0]
        
        
        # Skip files without a valid file extension
        if (file_ext not in valid_extensions):
            continue
        
        
        # if len(file_lead) == 19 or len(file_lead) == 21 :
        #     #print(f"Skipping file {file_lead} as it already has a length of 19 characters.")
        #     continue
        
       
        # Create the old file path
        old_file_path = os.path.join(file_path, file_name)

        #取得檔案建立的日期
        creation_date = get_creation_date(old_file_path)
        date_taken = creation_date
        try:
            # Open the image
            image = Image.open(old_file_path)
            # Get the EXIF metadata
            metadata = image._getexif()
            # Check if the metadata exists
            
            datestr_from_metadata = None
            if metadata is None:
                pass
            elif 36867 in metadata.keys():
                datestr_from_metadata = metadata[36867]
            elif 306 in metadata.keys():
                datestr_from_metadata = metadata[306]
                
            if datestr_from_metadata is not None :
                try:
                    date_taken = datetime.strptime(datestr_from_metadata, "%Y:%m:%d %H:%M:%S")
                    print("datestr_from_metadata"+datestr_from_metadata)
                except Exception  as e:
                    pass
                        
            # Close the image
            image.close()
        except Exception as e:
            pass
        
        
        
        date_taken_str = date_taken.strftime("%Y%m%d_%H%M%S")
        
        # Combine the new file name and file extension
        new_file_name = "IMG_"+date_taken_str + file_ext

        year = date_taken.year
        month = date_taken.month
        destination_folder = os.path.join(dest_path, str(year),str(month))
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Create the new folder path
        new_file_path = os.path.join(destination_folder, new_file_name)

        # Check if the file already exists
        count = 1
        while os.path.exists(new_file_path):
            # If file exists, add _1, _2, _3, etc. to the file name
            new_file_name = f"IMG_{date_taken_str}_{count}{file_ext}"
            new_file_path = os.path.join(destination_folder, new_file_name)
            count += 1
        
            
        
        try:
            filecount +=1
            print(f"{filecount}. Rename {old_file_path} to {new_file_path}")
            # os.rename(old_file_path, new_file_path)
            shutil.move(old_file_path, new_file_path)
        except Exception as e:
            pass

def rename_files_in_folder(folder_path,dest_path):
    # Get all files and subdirectories from the given folder path
    entries = os.listdir(folder_path)
    print(f"rename_files_in_folder({folder_path}) ({len(entries)})files")
    rename_file(folder_path,dest_path)
    
    count = 0 
    for entry in entries:
        full_entry_path = os.path.join(folder_path, entry)
        # If the entry is a directory, recursively call the function
            
        if os.path.isdir(full_entry_path):
            rename_files_in_folder(full_entry_path,dest_path)
        
            
# Main         
# If folder path argument exists then use it
# Else use the current running folder
if len(sys.argv) > 1:
    source_path = input_file_path = sys.argv[1]
    dest_path = input_file_path = sys.argv[2]
else:
    dest_path = source_path = older_path = os.getcwd()          


rename_files_in_folder(source_path,dest_path)
from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move

import logging

# ! Different directories
source_dir = ""
dest_dir_sfx = ""
dest_dir_music = ""
dest_dir_video = ""
dest_dir_image = ""
dest_dir_documents = ""

# Supported Image Types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# Supported Video Types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# Supported Audio Types
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
# Supported Document Types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

# Unique name function for existing files
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):           # If file exists, adds number to the end of the filename
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

# Move file function
def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

# Main sorting function
def on_cleaner ():
    with scandir(source_dir) as entries:        # Scan files in source directory
        for entry in entries:       # Loop through scanned directory
            name = entry.name
            check_audio_files(entry, name)      # Check each entry for the file type and assign proper directory
            check_video_files(entry, name)
            check_image_files(entry, name)
            check_document_files(entry, name)

def check_audio_files(entry, name):
    for audio_extension in audio_extensions:
        if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):    # Check if filename ends with audio extension
            if entry.stat().st_size < 10_000_000 or "SFX" in name:      # Check if the audio file is over 10 megabytes
                dest = dest_dir_sfx
            else:
                dest = dest_dir_music
            move_file(dest, entry, name)        # Assign audio file to proper destination/directory
            logging.info(f"Moved audio file: {name}")
            
def check_video_files(entry, name):
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):    # Check if filename ends with video extension
            move_file(dest_dir_video, entry, name)
            logging.info(f"Moved video file: {name}")

def check_image_files(entry, name):
    for image_extension in image_extensions:
        if name.endswith(image_extension) or name.endswith(image_extension.upper()):    # Check if filename ends with video extension
            move_file(dest_dir_image, entry, name)
            logging.info(f"Moved image file: {name}")

def check_document_files(entry, name):
    for document_extension in document_extensions:
        if name.endswith(document_extension) or name.endswith(document_extension.upper()):      # Check if filename ends with video extension
            move_file(dest_dir_documents, entry, name)
            logging.info(f"Moved document file: {name}")
import os
import shutil
from collections import defaultdict

def organize_files(source_dir, dry_run=False, verbose=False):
    """
    Organizes files in source_dir into subdirectories based on file extensions.
    Only files directly in source_dir are organized. Subfolders are ignored.
    """
    if not os.path.isdir(source_dir):
        print(f"Error: Directory '{source_dir}' does not exist.")
        return

    print(f"Organizing files in: {source_dir}")
    categorized_files = defaultdict(list)

    # Only process files in the top-level directory
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    if verbose:
        print(f"Found {len(files)} files in {source_dir}")

    for file in files:
        file_path = os.path.join(source_dir, file)
        extension = os.path.splitext(file)[1].lower()
        if extension:  # Exclude files with no extension
            category = get_category(extension)
            categorized_files[category].append(file_path)

    for category, files in categorized_files.items():
        target_dir = os.path.join(source_dir, category)
        if not dry_run and not os.path.exists(target_dir):
            os.makedirs(target_dir)
            if verbose:
                print(f"Created directory: {target_dir}")

        for file_path in files:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(target_dir, file_name)

            if file_path == destination_path:  # Already in correct folder
                if verbose:
                    print(f"Skipping {file_name} (already in {category})")
                continue

            if verbose:
                print(f"Moving '{file_name}' to '{category}/'")
            if not dry_run:
                shutil.move(file_path, destination_path)

    print("Organization complete!" if not dry_run else "Dry run complete (no changes made).")

def get_category(extension):
    """Determines the category based on file extension."""
    image_exts = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    document_exts = ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx']
    video_exts = ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv']
    audio_exts = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
    archive_exts = ['.zip', '.rar', '.7z', '.tar', '.gz']
    code_exts = ['.py', '.cpp', '.h', '.java', '.js', '.html', '.css']
    # Add more categories and extensions as needed

    if extension in image_exts:
        return "Images"
    elif extension in document_exts:
        return "Documents"
    elif extension in video_exts:
        return "Videos"
    elif extension in audio_exts:
        return "Audio"
    elif extension in archive_exts:
        return "Archives"
    elif extension in code_exts:
        return "Code"
    else:
        return "Others"

# You could add an 'undo' function here, but it's more complex (requires logging moves)
# def undo_last_organization(source_dir):
#     pass
# This function would require a way to track moves, possibly using a log file or database.

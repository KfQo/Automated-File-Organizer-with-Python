
import os
import shutil

# Update this path to the folder you want to organize
folder_path = r'C:/Users/YourName/Downloads'

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],  
    "Videos": [".mp4", ".mkv", ".avi"],
    "Compressed": [".zip", ".rar"],
    "Scripts": [".py", ".js", ".sh", ".java", ".c", ".cpp", ".html", ".css", ".php", ".rb"],  
    "Applications": [".exe", ".msi"],
    "Others": []  # Category for any other files
}

def organize_folder(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            organized = False
            
            for category, extensions in file_types.items():
                if ext.lower() in extensions:
                    category_path = os.path.join(path, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, filename))
                    organized = True
                    break
            
            # Move any unclassified files to "Others"
            if not organized:
                others_path = os.path.join(path, "Others")
                os.makedirs(others_path, exist_ok=True)
                shutil.move(file_path, os.path.join(others_path, filename))

if __name__ == "__main__":
    organize_folder(folder_path)
    print("Files organized successfully!")

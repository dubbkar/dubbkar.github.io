import os
import re

# Function to replace <head> with the new content in a file
def replace_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    new_content = re.sub(r'<head>', r'<head>\n<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6347600187520861" crossorigin="anonymous"></script>', content)

    with open(file_path, 'w') as file:
        file.write(new_content)

# Recursive function to process .html files in directory and subdirectories
def process_html_files(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                replace_in_file(file_path)

# Main script execution starts here
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python replace_head.py directory_path")
        sys.exit(1)

    directory_path = sys.argv[1]
    process_html_files(directory_path)


import os

# Function to replace the specified content with </body> in a file
def replace_content(file_path, content_to_replace):
    with open(file_path, 'r') as file:
        content = file.read()

    new_content = content.replace(content_to_replace, '</body>')

    with open(file_path, 'w') as file:
        file.write(new_content)

# Read the content to be replaced from 'file.txtx'
def read_content_to_replace(file_path):
    with open(file_path, 'r') as file:
        content_to_replace = file.read().strip()
    return content_to_replace

# Recursive function to process .html files in directory and subdirectories
def process_html_files(directory_path, content_to_replace):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                replace_content(file_path, content_to_replace)

# Main script execution starts here
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python replace_content.py directory_path")
        sys.exit(1)

    directory_path = sys.argv[1]

    content_to_replace_file = "codex2.txt"
    content_to_replace = read_content_to_replace(content_to_replace_file)

    process_html_files(directory_path, content_to_replace)

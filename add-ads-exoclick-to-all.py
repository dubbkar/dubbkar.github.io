import os
import re

# Define the directory to search for HTML files
directory = '.'  # Change this to the target directory if needed

# Define the replacement content
replacement_content = '''<!-- Tag Adult Top Banner -->
<script async type="application/javascript" src="https://a.magsrv.com/ad-provider.js"></script>
<ins class="eas6a97888e10" data-zoneid="5385318"></ins>
<script>(AdProvider = window.AdProvider || []).push({"serve": {}});</script>
<!-- Tag Adult Top Banner END -->

<!-- Tag Adult Top Banner2 -->
<script async type="application/javascript" src="https://a.magsrv.com/ad-provider.js"></script>
<ins class="eas6a97888e10" data-zoneid="5385710"></ins>
<script>(AdProvider = window.AdProvider || []).push({"serve": {}});</script>
<!-- Tag Adult Top Banner2 END -->'''

# Function to replace <body> tag in the file
def replace_body_tag(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace <body> tag with <body> and the replacement content
    new_content = re.sub(r'<body>', f'<body>\n{replacement_content}\n', content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Walk through the directory
for root, dirs, files in os.walk(directory):
    for file_name in files:
        if file_name.endswith('.html'):
            file_path = os.path.join(root, file_name)
            replace_body_tag(file_path)

print("Replacement completed.")


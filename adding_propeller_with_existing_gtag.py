import os
import re

# Define the folder path where your HTML files are located
folder_path = '.'

# Define the regex pattern to match the Google Tag Manager script
pattern = r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-85DSQ4PMSG"></script>'

# Define the replacement string
replacement = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-85DSQ4PMSG"></script>
<script async="async" data-cfasync="false" src="//ophoacit.com/1?z=6310881"></script>
<script>(function(d,z,s){s.src='https://'+d+'/401/'+z;try{(document.body||document.documentElement).appendChild(s)}catch(e){}})('ofleafeona.com',6310879,document.createElement('script'))</script>
<script>(function(d,z,s){s.src='https://'+d+'/401/'+z;try{(document.body||document.documentElement).appendChild(s)}catch(e){}})('gloaphoo.net',6310877,document.createElement('script'))</script>'''
updated_files = []
# Iterate through all HTML files in the folder and subfolders
for root, _, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.html'):
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            # Use regex to replace the pattern
            updated_content = re.sub(pattern, replacement, file_content)
            
            # Write the updated content back to the file
            with open(file_path, 'w') as file:
                file.write(updated_content)
            
            # Add the path to the updated_files list
            print(file_path)
            updated_files.append(file_path)

# Print the paths of updated files
print("Updated files:")
for file_path in updated_files:
    print(file_path)
print("Replacement completed.")


import requests

# URL of the file to download
url = 'https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules.list'

# Send a GET request to download the content of the file
response = requests.get(url)
if response.status_code == 200:
    # Get the text content from the response
    content = response.text
    
    # Replace 'DOMAIN-SUFFIX,*' with '*'
    modified_content = content.replace('DOMAIN-SUFFIX,*', '*')
    
    # Save the modified content to a new file
    with open('adrules.list', 'w') as file:
        file.write(modified_content)
    print("File has been modified and saved as 'modified_adrules.list'")
else:
    print("Failed to download the file. Status code:", response.status_code)

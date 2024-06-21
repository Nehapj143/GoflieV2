import requests

def upload_file(file_url, api_key):
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.post('https://api.gofile.io/uploadFile', headers=headers, files={'file': requests.get(file_url).content})
    return response.json()

def get_file_link(file_id, api_key):
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(f'https://api.gofile.io/getFile/{file_id}', headers=headers)
    return response.json()['data']['link']

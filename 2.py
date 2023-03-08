
import requests
import json


class YaUploader:
	def __init__(self, token: str):
		self.token = token

	def upload(self, file_path: str):
		url = 'https://cloud-api.yandex.net/v1/disk/resources'		
		headers = {'Authorization': token}

		resp = requests.get(f'{url}/upload?path=%2FTest%2F&overwrite={False}', headers=headers).json()
		requests.put(resp['href'], files={'file':path_to_file})

if __name__ == '__main__':
	path_to_file = "E:\pruch\python\!Sofick\Test.txt"
	token = ''
    
	uploader = YaUploader(token)
	result = uploader.upload(path_to_file)



















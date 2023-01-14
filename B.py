#y0_AgAAAAANCYDOAADLWwAAAADZY6q8ULkM2aQ5RE2an_cooMmeznXWFvw
import yadisk


class YaUploader:
	def __init__(self, token: str):
		self.token = token

	def upload(self, file_path: str):
		y = yadisk.YaDisk(token=token)
		
		y.upload(file_path, file_path[file_path.rfind('\\')+1::])

		








if __name__ == '__main__':
	path_to_file = "E:\pruch\python\!Sofick\Test.txt"
	token = 'y0_AgAAAAANCYDOAADLWwAAAADZY6q8ULkM2aQ5RE2an_cooMmeznXWFvw'
    
	uploader = YaUploader(token)
	result = uploader.upload(path_to_file)










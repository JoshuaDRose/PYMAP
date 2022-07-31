import os
import re
import sys
import utils
import requests

def wget_samples(install_location, url, name):
	download_data = requests.get(url)
	# print(f"Installing {name} from {url} into {install_location}")
	try:
		with open(os.path.join(install_location,name), 'wb') as f:
			f.write(download_data.content)
		utils.done = True
		return;
	except PermissionError:
		print("Permission Denied. Please ensure that you run this program as administrator.")


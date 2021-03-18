import os
from subprocess import check_output

source = '/jetson_train/qualcomm-training/content/OID/Dataset/test'

for folder in os.listdir(source):
  target = f'{source}/{folder}'
  output = check_output(["python", '/jetson_train/qualcomm-training/content/OIDv4_to_VOC/OIDv4_to_VOC.py', "--sourcepath" , f"{source}/{folder}", "--dest_path", f"{target}"])

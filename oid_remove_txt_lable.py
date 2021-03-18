import os
import shutil

dir = '/jetson_train/qualcomm-training/content/OID/Dataset/test/'

for folder in os.listdir(dir):
  shutil.rmtree(f'/{dir}/{folder}/Label')

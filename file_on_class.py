import os
dir = '/jetson_train/qualcomm-training/content/OID/Dataset/train/'

for folder in os.listdir(dir):
  print('Number for files in '+folder+'=',len(os.listdir(dir+folder)))

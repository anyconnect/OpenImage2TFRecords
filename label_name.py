import os
dir = '/jetson_train/qualcomm-training/content/OID/Dataset/train/'

for folder in os.listdir(dir):
  for file in os.listdir(dir+folder+'/Label')[:5]:
    print(dir+folder+'/Label'+'/'+file)

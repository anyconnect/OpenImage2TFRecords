import os
#dir = '/jetson_train/qualcomm-training/content/OID/Dataset/train/'

import tensorflow as tf

"""
Usage: 
python label_name.py [dataset_path] 
"""


flags = tf.app.flags
flags.DEFINE_string("dataset_path", "", "Path to the dataset directory")
FLAGS = flags.FLAGS


def main(_):
  dir = os.path.join(os.getcwd(), FLAGS.dataset_path)
  for folder in os.listdir(dir):
    for file in os.listdir(dir+folder+'/Label')[:5]:
      print(dir+folder+'/Label'+'/'+file)

if __name__ == "__main__":
  tf.app.run()

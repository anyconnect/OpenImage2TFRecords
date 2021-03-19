import os
import tensorflow as tf

#dir = '/jetson_train/qualcomm-training/content/OID/Dataset/train/'

"""
Usage: 
python file_on_class.py [dataset_path] 
"""

flags = tf.app.flags
flags.DEFINE_string("dataset_path", "", "Path to the dataset directory")
FLAGS = flags.FLAGS

def main(_):
  dir = os.path.join(os.getcwd(), FLAGS.dataset_path)
  for folder in os.listdir(dir):
    print('Number for files in '+folder+'=',len(os.listdir(dir+folder)))

if __name__ == "__main__":
  tf.app.run()


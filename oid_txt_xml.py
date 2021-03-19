import os
import subprocess
from subprocess import check_output
import tensorflow as tf

#source = '/root/qualcomm/OpenImage2TFRecords/OID/Dataset/train'

"""
Usage: 
python oid_txt_xml.py --dataset_path Dataset/train --voc_script OIDv4_to_VOC/OIDv4_to_VOC.py
"""

flags = tf.app.flags
flags.DEFINE_string("dataset_path", "", "Path to the dataset directory")
flags.DEFINE_string("voc_script", "", "Path to the OIDv4_to_VOC.py")
FLAGS = flags.FLAGS



def main(_):
  source = os.path.join(os.getcwd(), FLAGS.dataset_path)
  script = os.path.join(os.getcwd(), FLAGS.voc_script)
 
  for folder in os.listdir(source):
    target = "{}/{}".format(source, folder)
    #print(target)
    cmd = "python3 {} --sourcepath {} --dest_path {}".format(script, target, target)
    print(cmd)
    out = subprocess.run(cmd, shell=True)

if __name__ == "__main__":
  tf.app.run()
 

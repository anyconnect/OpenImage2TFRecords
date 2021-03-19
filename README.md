# OpenImage2TFRecords
This project converts the OpenImage txt annotations and label format to the Tensorflow tfrecord format.

# Dependency installation
1. Clone the OIDv4_toolkit.
  ```
  git clone https://github.com/EscVM/OIDv4_ToolKit.git
  ```
2. Download the train and test dataset from the OpenImage aws hub by editing the classes.txt.
   ```
   sudo pip3 install awscli
   sudo pip3 install opencv-python tqdm
   sudo pip3 install tensorflow==1.9
   vim OIDv4_ToolKit/classes.txt
   python3 OIDv4_ToolKit/main.py downloader --classes OIDv4_ToolKit/classes.txt --type_csv train --limit 98
   python3 OIDv4_ToolKit/main.py downloader --classes OIDv4_ToolKit/classes.txt --type_csv test --limit 45
   ```
3. Now clone the OpenImage2TFRecords repo.
   ```
   git clone https://github.com/anyconnect/OpenImage2TFRecords.git
   ```
4. On successful OpenImage download there should be an OID/ directory. Copy the OID directory into the OpenImage2TFRecords/ .
   ```
   cp -r OID OpenImage2TFRecords
   ```
5. Clone the TensorFlow object-detecion model repo.
   ```
   git clone https://github.com/tensorflow/models.git
   cd models
   git checkout ad386df597c069873ace235b931578671526ee00
   cd ..
   ```
6. Update the OpenImage2TFRecords/generate_tfrecord.py Line:19 with the cloned model repo path.
   ```
   19:   sys.path.append("/tfmodels/models/research/")
   ```
# What it has
-  file_on_class.py         // Checks the number of images per class
-  label_name.py            // Checks the annotation txt availability on the dataset per label
-  oid_txt_xml.py           // Converts the txt annotation to the Pascal VOC XML annotation
-  oid_remove_txt_lable.py  // Removes the txt annotations from the dataset
-  xml_to_csv.py            // Converts XML annotation to the CSV annotation
-  generate_tfrecord.py     // Generates TFRecords and label_map.pbtxt from the csv for TensorFlow training.
-  OIDv4_to_VOC.py          // Does the multi-level folder dataset traverse and conversion for txt to XML conversion.

# Procedure
1. Check the downloaded dataset for the number of images it has.
```
python3 file_on_class.py --dataset_path OID/Dataset/train/
```
2. Check the txt annotation availability.
```
python label_name.py --dataset_path OID/Dataset/train/
```
3. Converts OID txt annotation to VOC XML.
```
python oid_txt_xml.py --dataset_path OID/Dataset/train --voc_script OIDv4_to_VOC.py
```
Note that, this OIDv4_to_VOC.py script has been taken from https://github.com/AtriSaxena/OIDv4_to_VOC and updated to support our needs.
4. Convert XML annotation to the CSV annotation and generate label_map.pbtxt. **This label_map.pbtxt is a must requirement for the TF training.**
```
python xml_to_csv.py -i OID/Dataset/train -o OID/Dataset/annotations/train_labels.csv -l OID/Dataset/annotations
```
label_map.pbtxt will be available on the OID/Dataset/annotations directory.
5. Now generate TFRecord file for the TF training using the CSV, pbtxt and the dataset.
```
python generate_tfrecord.py --csv_input=OID/Dataset/annotations/train_labels.csv --output_path=OID/Dataset/annotations/train.record --img_path=OID/Dataset/train --label_map OID/Dataset/annotations/label_map.pbtxt
```
6. Now you will have all of the required annotation file for your training.
Enjoy!

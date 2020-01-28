import xml.etree.ElementTree as ET
from os import getcwd
import os


dataset_train = 'kitti_data/training/image_2'
dataset_file = '9_CLASS_test.txt'
# classes_file = dataset_file[:-4]+'_classes.txt'

CLS = ["car", "Van", "Truck", "person", "Person_sitting", "Cyclist", "Tram", "Misc", "DontCare"]
# classes =[dataset_train+CLASS for CLASS in CLS]
wd = getcwd()


def test(fullname):
    bb = ""
    in_file = open(fullname)
    tree=ET.parse(in_file)
    root = tree.getroot()
    for i, obj in enumerate(root.iter('object')):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in CLS or int(difficult)==1:
            continue
        cls_id = CLS.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)), int(float(xmlbox.find('xmax').text)), int(float(xmlbox.find('ymax').text)))
        bb += (" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

        # we need this because I don't know overlapping or something like that
        if cls == 'DontCare':
            list_file = open(dataset_file, 'a')
            file_string = str(fullname)[:-4]+'.png'+bb+'\n'
            list_file.write(file_string)
            list_file.close()
            bb = ""

    if bb != "":
        list_file = open(dataset_file, 'a')
        file_string = str(fullname)[:-4]+'.png'+bb+'\n'
        list_file.write(file_string)
        list_file.close()



for filename in os.listdir(dataset_train):
    if not filename.endswith('.xml'):
        continue
    fullname = os.getcwd()+'/'+dataset_train+'/'+filename
    test(fullname)


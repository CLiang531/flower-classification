import cv2 
import yaml
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# 1 to filter out INFO logs, 2 to also filter out WARNING, 3 for ERROR
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 
import tensorflow as tf

model=None
labels=None
config=None

def read_yaml(path):
    global config
    try:
        with open(path,'r') as yaml_file:
            config=yaml.safe_load(yaml_file)
        return True
    except Exception as e:
        print('error --',e)
        return False

def get_yaml_config(path):
    if config is None:
        print('error -- yaml file not loaded')
        return None
    else:
        cur=config
        for i in path:
            cur=cur[i]
        return cur

def get_all_models():
    base_path=os.getcwd()
    model_path=get_yaml_config(['model','paths','load_model_path'])
    models=os.listdir(base_path+'/'+model_path)
    return models

def load_model(model_name):
    global model
    try:
        model_path=get_yaml_config(['model','paths','load_model_path'])
        model_path=model_path+'/'+model_name
        model=tf.keras.models.load_model(model_path)
        return True
    except Exception as e:
        print('error --',e)
        return False

def load_labels():
    global labels
    try:
        config_path=get_yaml_config(['model','paths','labels_path'])
        with open(config_path,'r') as labels_txt:
            labels=labels_txt.read().split('\n')
        return True
    except Exception as e:
        print('error --',e)
        return False

def pred_individual(img):
    if model is None:
        print('error -- model not loaded')
        return None
    if labels is None:
        print('error -- labels are not loaded')
        return None
    tf_img=np.reshape(img,(1,256,256,3))
    pred=np.argmax(model.predict(tf_img))
    return labels[pred]

def classify(frame=None,path='',show=False):
    if len(path)>0:
        try:
            frame=cv2.imread(path)
        except Exception as e:
            print('error --',e)
            return None
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_height=get_yaml_config(['model','img_height'])
    img_width=get_yaml_config(['model','img_width'])
    img=cv2.resize(frame,(img_height,img_width))
    ret=pred_individual(img)
    if show:
        plt.imshow(frame)
        plt.title(f'Prediction:{ret}')
        plt.axis('off')
        plt.show()
    return ret
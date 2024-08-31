# flower-classification
---
## Description
Exploration of image classification models using tensorflow. The notebooks in the project are used to produce, train, and evalutate different image classification structures. The notebook includes experimenting of different layer orders, hyperparameter values, and techniques such as data augmentation to attempt to increase the accuracy of the predictions, and even explore 3 different existing models with the use of transfer learning. They are then saved into the ``models/`` folder.

After saving these models, we can then run ``engine.py`` in the ``src/`` folder to then load in the models and predict on individual images by entering in the path to the image. Alternatively, a video stream can be activated where the user can hold up the flower they want to identify to the camera and press the corresponding key to identify it. The user can then save the image if they so wish into the ``out/`` folder.

Keep in mind that the information in the ``config.yaml`` file must be correct.

## Data
The data for this project can be found at: ``https://www.kaggle.com/datasets/marquis03/flower-classification/code``. However, the folder ``test/`` under ``data/`` is filled with personally taken images that do not appear within the kaggle dataset. The process of resizing these images can be found in the ``img_resize_util.ipynb`` notebook under ``notebooks/``.

Since these are personal images, some flowers may not align with the species of flower that the kaggle dataset provides for training and evaluation.
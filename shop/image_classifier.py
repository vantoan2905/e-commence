from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image
import tensorflow as tf
import numpy as np
import pandas as pd
from django.core.files.storage import default_storage
from io import BytesIO
from PIL import Image


class ImageClassifier:
    physical_devices = tf.config.list_physical_devices('GPU')
    if physical_devices:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)

    @staticmethod
    def image_classifier(file_path, model, label_mapping):
        try:
            model = tf.keras.models.load_model(model)

            label_mapping_df = pd.read_csv(label_mapping)
            label_mapping = dict(zip(label_mapping_df['index'], label_mapping_df['class']))

            with open(file_path, 'rb') as f:
                img = Image.open(BytesIO(f.read()))
                img = img.convert('RGB')  
               

            img = img.resize((224, 224))

            img_array = np.array(img)

            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0  

            predictions = model.predict(img_array)
            predicted_index = np.argmax(predictions, axis=1)[0]
            predicted_class = label_mapping.get(predicted_index, 'Unknown')
            return predicted_class

        except Exception as e:
            print(f"Error during prediction: {e}")
            return None

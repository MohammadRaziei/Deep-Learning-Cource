import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from tqdm import trange
from PIL import Image


# I recommend to see this websize https://stepup.ai/exploring_data_augmentation_keras/
# It help me to write following class
 
class DataAugmentation(ImageDataGenerator):
    def __init__(self, data, progressbar=False, fill_mode='constant', **keywords):
        super().__init__(fill_mode=fill_mode, dtype=data.dtype,**keywords)
        self._data = data
        self.fit(data)
        self.progressbar = progressbar

    def work(self, n_images=5): 
        gen_flow = self.flow(self._data)
        rng = trange(n_images) if self.progressbar else range(n_images) 
        images = np.array([next(gen_flow) for _ in rng])
        return images

    def get(self, n_images=5, images=None):
        if images is None:
            images = self.work(n_images)
        return images.reshape(images.shape[0]*images.shape[1], *images.shape[2:])

    def plot(self, n_images=5, images=None):
        if images is None:
            images = self.work(n_images)
        n_cols, n_rows = images.shape[:2]
        plt.figure(figsize=(n_cols*4, n_rows*3))
        for image_index in range(n_images):
            for row in range(n_rows):
                plt.subplot(n_rows, n_cols, image_index+1+row*n_cols)
                plt.axis('off')
                plt.imshow(images[image_index][row].astype(np.uint8), vmin=0, vmax=255)
        plt.subplots_adjust(hspace=-0.5)
        plt.show() 

def resize_image(image, target_size=(100,100)):
    img = Image.fromarray(image)
    img = img.resize(target_size, Image.ANTIALIAS)
    img = np.asarray(img)
    return img
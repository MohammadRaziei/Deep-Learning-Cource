import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from tqdm import tqdm
from PIL import Image


# I recommend to see this websize https://stepup.ai/exploring_data_augmentation_keras/
# It help me to write following class
 
class DataAugmentation(ImageDataGenerator):
    def __init__(self, data, progressbar=False, progressbar_module=None, fill_mode='constant', **keywords):
        super().__init__(fill_mode=fill_mode, dtype=data.dtype,**keywords)
        self._data = data
        self.fit(data)
        if progressbar_module is None:
            self.progressbar = progressbar
            self._tqdm = tqdm 
        else:
            self.progressbar = True
            self._tqdm = progressbar_module

    def work(self, n_images=5): 
        gen_flow = self.flow(self._data)
        rng = self._tqdm(range(n_images)) if self.progressbar else range(n_images) 
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

    def save_flow(self, num_iter=5, save_to_dir='.', batch_size=1, save_prefix='', save_format='jpeg', **keywords):
        i = 0
        for _ in self.flow(self._data, batch_size=batch_size, save_to_dir=save_to_dir, save_prefix=save_prefix, save_format=save_format, **keywords):
            i += 1
            if i >= num_iter: break  # otherwise the generator would loop indefinitely

def resize_image(image, target_size=(100,100)):
    img = Image.fromarray(image)
    img = img.resize(target_size, Image.ANTIALIAS)
    img = np.asarray(img)
    return img
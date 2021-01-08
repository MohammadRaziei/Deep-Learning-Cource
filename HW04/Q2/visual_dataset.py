import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from prepare_data import default_root, getGroundTruthList


def visual_dataset_raw(number, root=default_root):
  positive_folder = os.path.join(root, 'positive image set')
  filename = os.path.join(positive_folder, '{:03.0f}.jpg'.format(number))
  image = plt.imread(filename)

  plt.imshow(image)
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

def add_groundTruth_patch(groundTruthObject, ax, show_name=True, fontsize=16):
  x,y = groundTruthObject.top_left.get()
  x2,y2 = groundTruthObject.right_bottom.get()
  w = x2 - x;  h = y2 - y
  rect = patches.Rectangle((x,y),w,h,linewidth=2,edgecolor='g',facecolor='none')
  ax.add_patch(rect)
  font = {'family': 'serif', 'color':  'red', 'weight': 'normal', 'size': fontsize}
  info = groundTruthObject.object_type
  text = info.name if show_name else str(info.value)
  length = (len(text)+1)*fontsize//2
  
  ax.text(x+w//2-length//2,y+h//2+fontsize//2, text , fontdict=font)


def visual_dataset(number, show_name=True, root=default_root, figsize=(20,20), fontsize=16): 
  fig = plt.figure(figsize=figsize)
  ax = plt.subplot(111)
  groundTruthList = getGroundTruthList(number,root=root)
  visual_dataset_raw(number,root)
  for obj in groundTruthList:
    add_groundTruth_patch(obj,ax, show_name=show_name, fontsize=fontsize)
  plt.show()



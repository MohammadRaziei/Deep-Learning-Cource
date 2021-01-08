import os
import enum, re
import matplotlib.pyplot as plt

default_root = 'NWPU VHR-10 dataset'


class Point:
    def __init__(self, x,y):
      self.x = x
      self.y = y
    def get(self):
      return (self.x, self.y)
    def __repr__(self):
      return '({},{})'.format(self.x, self.y)

class ObjectType(enum.Enum):
    airplane = 1
    ship = 2
    storageTank = 3
    baseballDiamond = 4
    tennisCourt = 5
    basketballCourt = 6
    groundTrackField = 7
    harbor = 8
    bridge = 9
    vehicle = 10
    
class GroundTruthObject:
    def __init__(self, point_top_left, point_right_bottom, object_type):
      self.top_left = Point(*point_top_left)
      self.right_bottom = Point(*point_right_bottom)
      self.object_type = ObjectType(object_type)
    def __repr__(self):
      return '{%s}'%'{},{}, {}'.format(self.top_left, self.right_bottom, self.object_type.name)

def GroundTruthParser(filename):
    GroundTruthList = []
    with open(filename) as f:
      pattern = re.compile(r'\d+')
      lines = f.readlines() # list containing lines of file
      for line in lines:
        numbers = [int(match.group()) for match in re.finditer(pattern, line)]
        if not numbers: continue
        GroundTruthList.append(GroundTruthObject((numbers[0],numbers[1]), (numbers[2],numbers[3]), numbers[4]))
    return GroundTruthList

def getGroundTruthList(number,root=default_root):
    ground_truth_folder = os.path.join(root, 'ground truth')
    filename = os.path.join(ground_truth_folder, '{:03.0f}.txt'.format(number))
    GroundTruthList = GroundTruthParser(filename)  
    return GroundTruthList




def crop_image_obj(image, obj):
    left,top = obj.top_left.get()
    right,bottom = obj.right_bottom.get()
    imageCrop = image[ top:bottom, left:right,:]
    return imageCrop


def prepare_data(number, root=default_root):
    positive_folder = os.path.join(root, 'positive image set')
    filename = os.path.join(positive_folder, '{:03.0f}.jpg'.format(number))
    groundTruthList = getGroundTruthList(number, root=root)
    image = plt.imread(filename)
    cropped_images = [crop_image_obj(image, obj) for obj in groundTruthList]
    classes = [obj.object_type for obj in groundTruthList]
    return cropped_images, classes
    
import os
import enum
import re

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
        GroundTruthList.append(GroundTruthObject((numbers[0],numbers[1]), (numbers[2],numbers[3]), numbers[4]))
    return GroundTruthList

def getGroundTruthList(number,root=default_root):
    ground_truth_folder = os.path.join(root, 'ground truth')
    filename = os.path.join(ground_truth_folder, '{:03.0f}.txt'.format(number))
    GroundTruthList = GroundTruthParser(filename)  
    return GroundTruthList



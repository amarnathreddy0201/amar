import numpy as np
import pandas as pd
# Define functions to convert between bounding box formats
def xywh_to_xyxy(xywh):
    """Convert [x, y, width, height] to [x_min, y_min, x_max, y_max]."""
    x, y, w, h = xywh.T
    x_min = x
    y_min = y
    x_max = x + w
    y_max = y + h
    return np.vstack((x_min, y_min, x_max, y_max)).T

def xywh_to_xywhn(xywh, img_width, img_height):
    """Normalize [x, y, width, height] to [0, 1] range."""
    x, y, w, h = xywh.T.astype(float)  # Ensure values are floats for division
    x /= img_width
    y /= img_height
    w /= img_width
    h /= img_height
    return np.vstack((x, y, w, h)).T

def xyxy_to_xyxyn(xyxy, img_width, img_height):
    """Normalize [x_min, y_min, x_max, y_max] to [0, 1] range."""
    x_min, y_min, x_max, y_max = xyxy.T.astype(float)
    x_min /= img_width
    y_min /= img_height
    x_max /= img_width
    y_max /= img_height
    return np.vstack((x_min, y_min, x_max, y_max)).T
def read_ground_truth(filename):
     # predictor = DetectionPredictor()
    # Image dimensions (replace with actual values)
    img_width, img_height = 1920, 1080  # Example dimensions
   

    # file_name = "/media/mantra/DATA/TEAM/AMARNATH/development/MOT data sets/MOT20/train/MOT20-01/gt/gt.txt"
    # file_name = "/media/mantra/DATA/TEAM/AMARNATH/development/MOT data sets/MOT20/train/MOT20-01/gt/gt.txt"
    file_name = "/media/mantra/DATA/TEAM/AMARNATH/development/MOT data sets/MOT20_01/train/MOT20-01/gt/gt.txt"


    # /media/mantra/DATA/TEAM/AMARNATH/development/MOT data sets/MOT20/train/MOT20-01/gt/gt.txt
    # Read the data from the text file
    data = pd.read_csv(file_name, header=None, names=['frame_id', 'id', 'x', 'y', 'width', 'height', '1', 'cls', 'conf'])

    data['xywh'] = data.apply(lambda row: np.array([
        row['x'] + row['width'] / 2,   # x_center
        row['y'] + row['height'] / 2,  # y_center
        row['width'],                  # width
        row['height']                  # height
    ]), axis=1)
    # data['x']= data['x']+data['width']/2
    # data['y'] = data['y']+data['height']/2

    data['width']= data['x']+data['width']
    data['height'] = data['y']+data['height']

    data['cls'] =0
  # Process grouped data by frame
    grouped_data = data.groupby('frame_id').apply(lambda df: {
    'boxes': {
        # 'cls': np.array(df['cls'].values) - 1,  # Class IDs, adjusted if necessary
        'conf': np.array(df['conf'].values),  # Confidence scores
        'data': np.array(df[['x', 'y', 'width', 'height', 'conf', 'cls']].values),  # Combined data
        'xywh': np.array(df[['x', 'y', 'width', 'height']].values),  # Original xywh format
        # 'xywhn': xywh_to_xywhn(
        #     np.array(df[['x', 'y', 'width', 'height']].values),
        #     img_width, img_height
        #     ),  # Normalized xywhn format
        # 'xyxy': np.array(df.assign(
        #     x2=df['x'] + df['width'],
        #     y2=df['y'] + df['height']
        #     )[['x', 'y', 'x2', 'y2']].values),  # Original xyxy format
        # 'xyxyn': xyxy_to_xyxyn(
        #     np.array(df.assign(
        #         x2=df['x'] + df['width'],
        #         y2=df['y'] + df['height']
        #     )[['x', 'y', 'x2', 'y2']].values),
        #     img_width, img_height
        #     )  # Normalized xyxyn format
        }
    }).reset_index(name='combined_data')

    return grouped_data

grouped_data = read_ground_truth("hjbvh")

grouped_dict = {row['frame_id']: row['combined_data'] for _, row in grouped_data.iterrows()}

import cv2
print("", len(grouped_dict[1]["boxes"]["data"]))
image = cv2.imread("/media/mantra/DATA/TEAM/AMARNATH/development/MOT data sets/MOT20_01/train/MOT20-01/img1/000001.jpg")

print(grouped_dict[1]["boxes"]["data"][0])

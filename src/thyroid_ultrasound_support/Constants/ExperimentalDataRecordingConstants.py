#!/usr/bin/env python3

"""
Defines constants used in recording experimental data.
"""

# Define constants to use when writing data to CSV files
MESSAGE_ID: str = 'Message ID Number'
STAMP_SECS: str = 'Timestamp (s)'
STAMP_NSECS: str = 'Timestamp (ns)'
POSE_X: str = 'Robot Pose X (m)'
POSE_Y: str = 'Robot Pose Y (m)'
POSE_Z: str = 'Robot Pose Z (m)'
POSE_ROLL: str = 'Robot Pose Roll (m)'
POSE_PITCH: str = 'Robot Pose Pitch (m)'
POSE_YAW: str = 'Robot Pose Yaw (m)'
FORCE: str = 'Force (N)'
RAW_IMAGE_NAME: str = 'Raw Image Name'
RAW_IMAGE_ARRAY: str = 'Raw Image Array'
IMAGE_CENTROID: str = 'Centroid Error in X (m)'
SKIN_ERROR: str = 'Skin Error Slope'
WAYPOINT_REACHED: str = 'Waypoint Reached'
TRANSFORM_MATRIX_0: str = 'Transform Matrix 0'
TRANSFORM_MATRIX_1: str = 'Transform Matrix 1'
TRANSFORM_MATRIX_2: str = 'Transform Matrix 2'
TRANSFORM_MATRIX_3: str = 'Transform Matrix 3'
TRANSFORM_MATRIX_4: str = 'Transform Matrix 4'
TRANSFORM_MATRIX_5: str = 'Transform Matrix 5'
TRANSFORM_MATRIX_6: str = 'Transform Matrix 6'
TRANSFORM_MATRIX_7: str = 'Transform Matrix 7'
TRANSFORM_MATRIX_8: str = 'Transform Matrix 8'
TRANSFORM_MATRIX_9: str = 'Transform Matrix 9'
TRANSFORM_MATRIX_10: str = 'Transform Matrix 10'
TRANSFORM_MATRIX_11: str = 'Transform Matrix 11'
TRANSFORM_MATRIX_12: str = 'Transform Matrix 12'
TRANSFORM_MATRIX_13: str = 'Transform Matrix 13'
TRANSFORM_MATRIX_14: str = 'Transform Matrix 14'
TRANSFORM_MATRIX_15: str = 'Transform Matrix 15'

# Define prefixes for CSV files
FORCE_PREFIX: str = 'Force_'
POSE_PREFIX: str = 'Pose_'
CENTROID_PREFIX: str = 'Centroid_'
SKIN_ERROR_PREFIX: str = 'SkinError_'

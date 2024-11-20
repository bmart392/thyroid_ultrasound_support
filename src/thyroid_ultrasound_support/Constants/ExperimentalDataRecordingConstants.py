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

# Define prefixes for CSV files
FORCE_PREFIX: str = 'Force_'
POSE_PREFIX: str = 'Pose_'
CENTROID_PREFIX: str = 'Centroid_'
SKIN_ERROR_PREFIX: str = 'SkinError_'

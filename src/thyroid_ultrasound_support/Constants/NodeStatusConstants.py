#!/usr/bin/env python3

"""
Defines constants used in sending and receiving node statuses messages.
"""

# Define expected verbosity level for all node statuses
NO_VERBOSITY: int = int(255)

# General
INITIALIZING: str = 'Node initializing'
INITIALIZED: str = 'Node initialized'
WAITING: str = 'Node waiting'
IMAGES_AVAILABLE: str = 'Images available'
NO_IMAGES_AVAILABLE: str = 'No images available'

# Clarius Ultrasound Connection Node
IMAGE_FROZEN_NOT_SAVING_IMAGES: str = 'Image frozen, not saving images'
SENDING_IMAGES_NOT_SAVING_IMAGES: str = 'Image not frozen, not saving images'
SENDING_IMAGES_SAVING_IMAGES: str = 'Image not frozen, saving images'

# Experiment Stream Recorded Data Node
STREAMING_ACTIVE: str = 'Streaming active'
STREAMING_INACTIVE: str = 'Streaming inactive'
ALL_IMAGES_STREAMED: str = 'All images streamed'

# Image Based User Input Node
LOADING_CROP_COORDINATES: str = 'Loading crop coordinates'
GENERATING_CROP: str = 'Generating crop coordinates'
GENERATING_INITIALIZATION: str = 'Generating initialization mask'
GENERATING_THRESHOLD: str = 'Generating threshold parameters'
GENERATING_GROUND_TRUTH: str = 'Generating ground truth mask'

# Image Contact Balance Node
PATIENT_IN_CONTACT: str = 'Patient in contact'
CALCULATING_BALANCE_ERROR: str = 'Calculating balance error'
BALANCE_ERROR_CALCULATED: str = 'Balance error calculated'
CONTACT_TOO_UNEVEN: str = 'Contact is too uneven'
PATIENT_NOT_IN_CONTACT: str = 'Patient not in contact'

# Visualization Node
NO_VISUALIZATIONS_ACTIVE: str = 'No visualizations active'
VISUALIZING_IMAGES: str = 'Visualizing images'

# Real Time Image Filter Node
NOT_READY_TO_FILTER: str = 'Not ready to filter'
UPDATING_FILTER_INITIALIZATION_MASK: str = 'Updating filter with new initialization mask'
ANALYZING_IMAGE: str = 'Analyzing Image'

# Image Positioning Controller Node
CALCULATED_USING_COMPOSITE_CENTROID: str = 'Calculating using composite centroid'
CALCULATED_USING_SINGLE_CENTROID: str = 'Calculating using single centroid'
ERROR_ACCESSING_CENTROIDS: str = 'Error accessing centroids'

# Image Position Registration Node
WAITING_FOR_FILTERED_IMAGE: str = 'Waiting for filtered image for registration'
WAITING_FOR_FILTERED_IMAGE_FOR_SAVING_VALID_POSITION: str = 'Waiting for filtered image for valid pose'
WAITING_FOR_ROBOT_POSE: str = 'Waiting for robot pose'
WAITING_FOR_FORCE_READING: str = 'Waiting for force reading'
SEARCHING_FOR_MATCHING_DATA: str = 'Searching for matching data'
MATCHING_DATA_FOUND: str = 'Matching data found'
REGISTERING_NEW_DATA: str = 'Registering new data'
SAVING_VALID_POSE: str = 'Saving valid pose'

# Trajectory Management Node
ROBOT_POSE_UNKNOWN: str = 'Robot pose is not known'
NO_TRAJECTORY_EXISTS: str = 'No trajectory exists'
WAYPOINT_NOT_REACHED: str = 'Waypoint not reached'
WAYPOINT_REACHED: str = 'Waypoint reached'

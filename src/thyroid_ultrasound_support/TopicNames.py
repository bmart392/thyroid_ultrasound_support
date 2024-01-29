#!/usr/bin/env python3

"""
Defines the names of topics used in the thyroid_ultrasound system.
"""

# Robot raw information
ROBOT_STATE: str = '/franka_state_controller/franka_states'
ROBOT_FORCE: str = '/franka_state_controller/F_ext'
ROBOT_CONTROL_INPUT: str = '/arm/cartesian/velocity'

# Robot derived information
ROBOT_DERIVED_POSE: str = '/O_T_EE'
ROBOT_DERIVED_FORCE: str = '/robot_data/cleaned_force'
REGISTERED_DATA: str = 'registered_data'

# Image related topics
IMAGE_SOURCE: str = '/image_data/source'
IMAGE_RAW: str = '/image_data/raw'
IMAGE_SKIN_APPROXIMATION: str = '/image_data/skin_approximation'
IMAGE_CROPPED: str = '/image_data/cropped'
IMAGE_FILTERED: str = '/image_data/filtered'
IMAGE_PATIENT_CONTACT: str = '/image_data/status/is_patient_in_image'
IMAGE_ROI_SHOWN: str = '/image_data/status/region_of_interest_shown'
IMAGE_ROI_CENTERED: str = '/image_data/status/region_of_interest_centered'
IMAGE_DEPTH: str = '/image_data/imaging_depth'
IMAGE_TRANSFORMED_POINTS: str = '/image_data/results/transformed_points'

# Commands
USE_IMAGE_FEEDBACK: str = '/command/use_image_feedback'
USE_POSE_FEEDBACK: str = '/command/use_pose_feedback'
USE_FORCE_FEEDBACK: str = '/command/use_force_feedback'

CREATE_TRAJECTORY: str = '/command/create_trajectory'
CLEAR_TRAJECTORY: str = '/command/clear_trajectory'
COMPLETE_FULL_SCAN: str = '/command/complete_full_scan'

CROP_IMAGE_FROM_POINTS: str = '/command/generate_new_image_cropping'
CROP_IMAGE_FROM_TEMPLATE: str = '/command/load_existing_image_cropping'

IDENTIFY_THYROID_FROM_POINTS: str = '/command/identify_thyroid_from_points'
IDENTIFY_THYROID_FROM_TEMPLATE: str = '/command/identify_thyroid_from_template'

GENERATE_THRESHOLD_PARAMETERS: str = '/command/generate_threshold_parameters'

IMAGE_STREAMING_CONTROL: str = '/command/image_streaming_control'
IMAGE_STREAMING_RESTART: str = '/command/restart_image_streaming'

FILTER_IMAGES: str = '/command/filter_images'

GENERATE_VOLUME: str = '/command/generate_volume'
DISPLAY_VOLUME: str = '/command/display_volume'


# Image-based user input
IMAGE_CROP_COORDINATES: str = '/ib_ui/image_crop_coordinates'
INITIALIZATION_MASK: str = '/ib_ui/initialization_mask'
THRESHOLD_PARAMETERS: str = '/ib_ui/generate_threshold_parameters'

# PID tuning
CONTROLLER_SELECTOR: str = '/tuning/controller'
P_GAIN_SETTING: str = '/tuning/setting/p_gain'
I_GAIN_SETTING: str = '/tuning/setting/i_gain'
D_GAIN_SETTING: str = '/tuning/setting/d_gain'
P_GAIN_CURRENT: str = '/tuning/current/p_gain'
I_GAIN_CURRENT: str = '/tuning/current/i_gain'
D_GAIN_CURRENT: str = '/tuning/current/d_gain'

# Robot control - force control information
RC_FORCE_SET_POINT: str = '/force_control/set_point'
RC_FORCE_ERROR: str = '/force_control/error'
RC_FORCE_IN_USE: str = '/force_control/in_use'
RC_FORCE_CONTROL_INPUT_EE: str = '/force_control/control_input_ee'
RC_FORCE_CONTROL_INPUT_O: str = '/force_control/control_input_o'

# Robot control - position control information
RC_POSITION_GOAL_REACHED: str = '/position_control/goal_reached'
RC_POSITION_GOAL_SURFACE: str = '/position_control/goal_surface'
RC_POSITION_ERROR: str = '/position_control/error'
RC_POSITION_IN_USE: str = '/position_control/in_use'
RC_POSITION_CONTROL_INPUT_EE: str = '/position_control/control_input_ee'
RC_POSITION_CONTROL_INPUT_O: str = '/position_control/control_input_O'

# Robot control - image control information
RC_IMAGE_ERROR: str = '/image_control/distance_to_centroid'
RC_IMAGE_IN_USE: str = '/image_control/in_use'
RC_IMAGE_CONTROL_INPUT_EE: str = '/image_control/control_input_ee'
RC_IMAGE_CONTROL_INPUT_O: str = '/image_control/control_input_O'

# Robot control - patient contact control information
RC_PATIENT_CONTACT_ERROR: str = '/patient_contact/error'
RC_PATIENT_CONTACT_IN_USE: str = '/patient_contact/in_use'
RC_PATIENT_CONTACT_CONTROL_INPUT_EE: str = '/patient_contact/control_input_ee'
RC_PATIENT_CONTACT_CONTROL_INPUT_O: str = '/patient_contact/control_input_o'

# System Information
LOGGING: str = '/system/logging'
STATUS: str = '/system/node_status'

# Development Channel
SAVE_IMAGES: str = '/developer/save_images'
SAVED_IMAGES_DESTINATION: str = '/developer/saved_images_destination'





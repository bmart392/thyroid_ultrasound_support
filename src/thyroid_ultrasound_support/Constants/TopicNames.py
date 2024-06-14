#!/usr/bin/env python3

"""
Defines the names of topics used in the thyroid_ultrasound system.
"""

# Robot raw information
ROBOT_STATE: str = '/franka_state_controller/franka_states'
ARMER_STATE: str ='/arm/state'
ROBOT_FORCE: str = '/franka_state_controller/F_ext'
ROBOT_CONTROL_INPUT: str = '/arm/cartesian/velocity'

# Robot derived information
ROBOT_DERIVED_POSE: str = '/O_T_EE'
ROBOT_DERIVED_FORCE: str = '/robot_data/cleaned_force'

# Image related topics
IMAGE_SOURCE: str = '/image_data/source'
IMAGE_RAW: str = '/image_data/raw'
IMAGE_SKIN_APPROXIMATION: str = '/image_data/skin_approximation'
IMAGE_CROPPED: str = '/image_data/cropped'
IMAGE_FILTERED: str = '/image_data/filtered'
IMAGE_PATIENT_CONTACT: str = '/image_data/status/is_patient_contacting_probe'
IMAGE_ROI_SHOWN: str = '/image_data/status/region_of_interest_shown'
IMAGE_ROI_CENTERED: str = '/image_data/status/region_of_interest_centered'
IMAGE_DEPTH: str = '/image_data/imaging_depth'
IMAGE_TRANSFORMED_POINTS: str = '/image_data/results/transformed_points'
IMAGE_FROZEN_STATUS: str = '/image_data/status/image_is_frozen'

# Registered data topics
REGISTERED_DATA_NON_REAL_TIME: str = '/registered_data/non_real_time/data'
REGISTERED_DATA_REAL_TIME: str = '/registered_data/real_time/data'
REGISTERED_DATA_NON_REAL_TIME_SEGMENTATION_PROGRESS: str = '/registered_data/non_real_time/segmentation_progress'

# Volume data topics
VOLUME_DATA: str = '/volume_data/data'

# Robot control - force control information
RC_FORCE_SET_POINT: str = '/force_control/set_point'
RC_FORCE_ERROR: str = '/force_control/error'
RC_FORCE_CONTROL_GOAL_REACHED: str = '/force_control/goal_reached'

# Robot control - position control information
RC_POSITION_GOAL_SURFACE: str = '/position_control/goal_surface'
RC_POSITION_GOAL_LIN_X_REACHED: str = '/position_control/goal_lin_x_reached'
RC_POSITION_GOAL_ANG_Y_REACHED: str = '/position_control/goal_ang_y_reached'
RC_POSITION_GOAL_ANG_Z_REACHED: str = '/position_control/goal_ang_z_reached'
RC_POSITION_ERROR: str = '/position_control/error'

# Robot control - image control information
RC_IMAGE_ERROR: str = '/image_control/distance_to_centroid'
RC_IMAGE_CENTERING_SIDE: str = '/image_control/image_centering_side'
RC_IMAGE_CONTROL_GOAL_REACHED: str = '/image_control/goal_reached'

# Robot control - patient contact control information
RC_PATIENT_CONTACT_ERROR: str = '/patient_contact/error'
RC_IMAGE_BALANCE_GOAL_REACHED: str = '/patient_contact/goal_reached'

# Robot control - user manual control
RC_MANUAL_CONTROL_INPUT: str = '/manual_control_input'

# Robot control - controller statuses
RC_LINEAR_X_CONTROLLER_STATUS: str = '/robot_control/controller_statuses/linear/x'
RC_LINEAR_Y_CONTROLLER_STATUS: str = '/robot_control/controller_statuses/linear/y'
RC_LINEAR_Z_CONTROLLER_STATUS: str = '/robot_control/controller_statuses/linear/z'
RC_ANGULAR_X_CONTROLLER_STATUS: str = '/robot_control/controller_statuses/angular/x'
RC_ANGULAR_Y_CONTROLLER_STATUS: str = '/robot_control/controller_statuses/angular/y'
RC_ANGULAR_Z_CONTROLLER_STATUS: str = '/robot_control/controller_statuses/angular/z'

# System Information
LOGGING: str = '/system/logging'
STATUS: str = '/system/node_status'

# Experiment Channels
EXP_SAVE_DATA_COMMAND: str = '/experiment/command/save_data'
EXP_CREATE_NOISE_COMMAND: str = '/experiment/command/create_noise'
EXP_NOISE_VELOCITIES: str = '/experiment/noise_velocities'
EXP_ALL_DATA_SAVED: str = '/experimental/status/all_data_saved'
EXP_DATA_REMAINING_TO_SAVE: str = '/experimental/status/remaining_data'




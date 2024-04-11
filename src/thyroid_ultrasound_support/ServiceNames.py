#!/usr/bin/env python3

"""
Defines the names of services used in the thyroid_ultrasound system.
"""

# Common messages
NO_ERROR: str = 'NO ERROR'

# Clarius connection
CC_SAVE_IMAGES: str = '/developer/save_images'
CC_SAVED_IMAGES_DESTINATION: str = '/developer/saved_images_destination'

# Clarius spoof
CS_IMAGE_LOCATION: str = '/image_streaming/path_to_images'
CS_IMAGE_STREAMING_CONTROL: str = '/image_streaming/image_streaming_control'
CS_IMAGE_STREAMING_RESTART: str = '/image_streaming/restart_image_streaming'
CS_IMAGE_STREAMING_REVERSE_PLAYBACK_DIRECTION: str = '/image_streaming/reverse_playback_direction'

# Image based user input
IB_UI_CROP_IMAGE_FROM_POINTS: str = '/image_based_user_input/generate_new_image_cropping'
IB_UI_CROP_IMAGE_FROM_TEMPLATE: str = '/image_based_user_input/load_existing_image_cropping'
IB_UI_IDENTIFY_THYROID_FROM_POINTS: str = '/image_based_user_input/identify_thyroid_from_points'

# Real-time segmentation
RTS_UPDATE_IMAGE_CROP_COORDINATES: str = '/real_time_segmentation/update_image_crop_coordinates'
RTS_UPDATE_INITIALIZATION_MASK: str = '/real_time_segmentation/update_initialization_mask'
RTS_UPDATE_THRESHOLD_PARAMETERS: str = '/real_time_segmentation/update_threshold_parameters'

# Robot control
RC_USE_POSE_CONTROL: str = '/robot_control/use/pose_control'
RC_USE_FORCE_CONTROL: str = '/robot_control/use/force_control'
RC_USE_IMAGE_BALANCING: str = '/robot_control/use/image_balancing'
RC_USE_IMAGE_CENTERING: str = '/robot_control/use/image_centering'

RC_OVERALL_ROBOT_SPEED: str = '/robot_control/overall_speed_factor'

RC_OVERRIDE_PATIENT_CONTACT: str = '/robot_control/overrides/patient_contact'

RC_PUBLISH_CONTROLLER_STATUSES: str = '/robot_control/command/publish_controller_statuses'

RC_SET_TRAJECTORY_PITCH: str = '/robot_control/command/set_pitch'
RC_SET_TRAJECTORY_YAW: str = '/robot_control/command/set_yaw'
RC_SET_NEXT_WAYPOINT: str = '/robot_control/command/set_next_waypoint'
RC_CLEAR_CURRENT_SET_POINTS: str = '/robot_control/command/clear_current_set_points'

RC_VIEW_CONTROLLER_GAINS: str = '/robot_control/controller_tuning/view'
RC_SET_CONTROLLER_GAINS: str = '/robot_control/controller_tuning/set'

# Trajectory management
TM_OVERRIDE_PATIENT_CONTACT: str = '/trajectory_management/overrides/patient_contact'
TM_OVERRIDE_FORCE_CONTROL: str = '/trajectory_management/overrides/force_control'
TM_OVERRIDE_IMAGE_BALANCED: str = '/trajectory_management/overrides/image_balanced'
TM_OVERRIDE_IMAGE_CENTERED: str = '/trajectory_management/overrides/image_centered'
TM_OVERRIDE_DATA_REGISTERED: str = '/trajectory_management/overrides/data_registered'

TM_CREATE_TRAJECTORY: str = '/trajectory_management/command/create'
TM_SET_TRAJECTORY_SPACING: str = '/trajectory_management/command/set_waypoint_spacing'
TM_CLEAR_TRAJECTORY: str = '/trajectory_management/command/clear'

TM_DATA_HAS_BEEN_REGISTERED: str = '/trajectory_management/data_has_been_registered'

# Image-position registration
IPR_REGISTER_NEW_DATA: str = '/image_position_registration/register_new_data'
IPR_REGISTERED_DATA_SAVE_LOCATION: str = '/image_position_registration/data_save_location'

# User interface
UI_TRAJECTORY_COMPLETE: str = '/user_interface/trajectory_complete'

# Non-real-time segmentation
NRTS_REGISTERED_DATA_LOAD_LOCATION: str = '/non_real_time_segmentation/registered_data_load_location'
NRTS_GENERATE_VOLUME: str = '/non_real_time_segmentation/generate_volume'

# Volume generation node
VG_REGISTERED_DATA_LOAD_LOCATION: str = '/volume_generation/registered_data_load_location'
VG_GENERATE_VOLUME: str = '/volume_generation/generate_volume'
VG_DISPLAY_VOLUME: str = '/volume_generation/display_volume'
VG_VOLUME_DATA_SAVE_LOCATION: str = '/volume_generation/volume_data/save_location'
VG_VOLUME_DATA_LOAD_LOCATION: str = '/volume_generation/volume_data/load_location'

# Visualization node
VIS_STATUS_SHOW_ORIGINAL: str = '/visualization/show_original'
VIS_STATUS_SHOW_CROPPED: str = '/visualization/show_cropped'
VIS_STATUS_SHOW_RECOLOR: str = '/visualization/show_recolored'
VIS_STATUS_SHOW_BLUR: str = '/visualization/show_blurred'
VIS_STATUS_SHOW_RESULT_MASK: str = '/visualization/show_result_mask'
VIS_STATUS_SHOW_POST_PROCESSED_MASK: str = '/visualization/show_post_processed_mask'
VIS_STATUS_SHOW_SURE_FOREGROUND: str = '/visualization/show_sure_foreground'
VIS_STATUS_SHOW_SURE_BACKGROUND: str = '/visualization/show_sure_background'
VIS_STATUS_SHOW_PROBABLE_FOREGROUND: str = '/visualization/show_probable_foreground'
VIS_STATUS_SHOW_INITIALIZATION_MASK: str = '/visualization/show_initialization_mask'
VIS_STATUS_SHOW_CENTROIDS_ONLY: str = '/visualization/show_centroids_only'
VIS_STATUS_SHOW_CENTROIDS_CROSS_ONLY: str = '/visualization/show_centroids_cross_only'
VIS_STATUS_SHOW_MASK_OVERLAY: str = '/visualization/show_mask_overlay'
VIS_STATUS_SHOW_CENTROIDS_CROSS_OVERLAY: str = '/visualization/show_centroids_cross_overlay'
VIS_STATUS_SHOW_MASK_CENTROIDS_CROSS_OVERLAY: str = '/visualization/show_mask_centroids_cross_overlay'
VIS_STATUS_SHOW_FOREGROUND: str = '/visualization/show_foreground'
VIS_STATUS_SHOW_SKIN_APPROXIMATION: str = '/visualization/show_skin_approximation'
VIS_STATUS_SHOW_GRABCUT_USER_INITIALIZATION_0: str = '/visualization/show_grabcut_user_initialization_0'
VIS_STATUS_SHOW_GRABCUT_USER_INITIALIZATION_1: str = '/visualization/show_grabcut_user_initialization_1'
VIS_STATUS_SHOW_GRABCUT_USER_INITIALIZATION_3: str = '/visualization/show_grabcut_user_initialization_3'




#!/usr/bin/env python3

"""
Defines constants used in sending and receiving node statuses messages.
"""

# Define expected verbosity level for all node statuses
NO_VERBOSITY: int = int(255)

# Image Filtering Node
SEGMENTATION_INACTIVE: str = 'Not cropping, not filtering'
SEGMENTATION_CROPPING: str = 'Cropping, not filtering'
SEGMENTATION_FILTERING: str = 'Cropping, filtering'
SEGMENTATION_UNKNOWN: str = 'Unknown state reached'

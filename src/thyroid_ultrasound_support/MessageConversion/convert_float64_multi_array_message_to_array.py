"""
Contains definition for convert_float64_multi_array_message_to_array function
"""

# Import from standard packages
from numpy import array

# Import from ROS standard packages
from std_msgs.msg import Float64MultiArray


def convert_float64_multi_array_message_to_array(data_msg: Float64MultiArray) -> array:
    """Converts a Float64MultiArray message into a 2D array of numbers"""

    # Create a new multi-dimension array message
    return array(data_msg.data).reshape((data_msg.layout.dim[0].size, data_msg.layout.dim[1].size))

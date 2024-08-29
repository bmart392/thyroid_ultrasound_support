"""
Contains definition for convert_array_to_float64_multi_array_message function
"""

# Import from standard packages
from numpy import array

# Import from ROS standard packages
from std_msgs.msg import Float64MultiArray, MultiArrayDimension


def convert_array_to_float64_multi_array_message(data_array: array) -> Float64MultiArray:
    """Converts a 2D array of numbers into a Float64MultiArray message"""
    # Create a new multi-dimension array message
    new_msg = Float64MultiArray()

    # Fill in the message with data from the given array
    new_msg.layout.dim.append(MultiArrayDimension())
    new_msg.layout.dim[0].label = 'rows'
    new_msg.layout.dim[0].size = data_array.shape[0]
    new_msg.layout.dim[0].stride = data_array.size
    new_msg.layout.dim.append(MultiArrayDimension())
    new_msg.layout.dim[1].label = 'columns'
    new_msg.layout.dim[1].size = data_array.shape[1]
    new_msg.layout.dim[1].stride = data_array.shape[1]
    new_msg.data = data_array.reshape([data_array.size])

    # Return the message with all data filled in
    return new_msg

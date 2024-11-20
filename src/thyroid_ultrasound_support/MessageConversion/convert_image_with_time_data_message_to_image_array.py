"""
File containing the convert_image_with_time_data_message_to_image_array function definition.
"""


# Import standard python packages
from rospy import Time
from numpy import ndarray

# Import custom python packages
from thyroid_ultrasound_support.MessageConversion.convert_image_message_to_image_array import \
    convert_image_message_to_image_array

# Import custom ROS packages
from thyroid_ultrasound_messages.msg import ImageWithTimeData


def convert_image_with_time_data_message_to_image_array(msg: ImageWithTimeData) -> (ndarray, Time):
    """"""
    return convert_image_message_to_image_array(msg.data), msg.capture_time


if __name__ == '__main__':
    pass

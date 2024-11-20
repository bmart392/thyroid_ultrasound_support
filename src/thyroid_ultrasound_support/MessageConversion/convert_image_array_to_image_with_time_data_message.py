"""
File containing the convert_image_array_to_image_with_time_data_message function definition.
"""

# Import standard python packages
from numpy import ndarray
from rospy import Time

# Import standard ROS packages

# Import custom python packages
from thyroid_ultrasound_support.MessageConversion.convert_image_array_to_image_message import \
    convert_image_array_to_image_message

# Import custom ROS packages
from thyroid_ultrasound_messages.msg import ImageWithTimeData


def convert_image_array_to_image_with_time_data_message(image_array: ndarray, apply_new_timestamp: bool = True,
                                                        alternative_timestamp_sec: float = None,
                                                        alternative_timestamp_nsec: float = None) -> ImageWithTimeData:
    """
    Converts an image array into its equivalent ImageWithTimeData message using the given data.

    Parameters
    ----------
    image_array :
        The image which should be sent as a numpy array
    apply_new_timestamp :
        If True, the ImageWithTimeData message will be filled with the current time.
    alternative_timestamp_sec :
        The timestamp, in seconds, to give the ImageWithTimeData message when the current time is not used.
    alternative_timestamp_nsec :
        The timestamp, in nanoseconds, to give the ImageWithTimeData message when the current time is not used.

    Returns
    -------
    ImageWithTimeData :
        A fully populated ImageWithTimeData message.
    """

    # Generate a standard image message
    pure_image_message = convert_image_array_to_image_message(image_array)

    # Create the actual image message to return
    resulting_image_message = ImageWithTimeData(data=pure_image_message)

    # Apply the proper timestamp to the image message
    if (apply_new_timestamp or
            alternative_timestamp_sec is None or
            alternative_timestamp_nsec is None):
        resulting_image_message.capture_time = pure_image_message.header.stamp
    else:
        resulting_image_message.capture_time = Time(int(alternative_timestamp_sec), int(alternative_timestamp_nsec))

    # Return the resulting image message
    return resulting_image_message


if __name__ == '__main__':
    pass

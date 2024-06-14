#!/usr/bin/env python3

"""
File containing the code for a basic node that allows logging of messages.
"""

# Import standard ROS packages
from rospy import init_node, spin, Rate, Subscriber, is_shutdown, Publisher, get_name, on_shutdown, Time, Service, \
    ServiceProxy, wait_for_service, ServiceException, Duration
from std_msgs.msg import Bool, Float64, String, Header

# Import custom ROS packages
from thyroid_ultrasound_messages.msg import log_message
from thyroid_ultrasound_services.srv import *

# Import custom python packages
from thyroid_ultrasound_support.Constants.LoggingConstants import *
from thyroid_ultrasound_support.Constants.NodeStatusConstants import *
from thyroid_ultrasound_support.Constants.NodeNameConstants import *
from thyroid_ultrasound_support.Constants.TopicNames import *
from thyroid_ultrasound_support.Constants.ServiceNames import *
from thyroid_ultrasound_support.Constants.DefaultSettingsConstants import *

# Define levels of verbosity
SHORT: int = int(0)
LONG: int = int(3)
EXTRA_LONG: int = int(5)


class BasicNode:
    def __init__(self):
        # Define a common publisher to send the log messages
        self.logger = Publisher(LOGGING, log_message, queue_size=10)

        # Define a common publisher to send node status messages
        self.status_publisher = Publisher(STATUS, log_message, queue_size=10)

        # Define a variable to store the last time a status was published
        self.time_of_last_publishing = None

    def log_single_message(self, message: str, verbosity: int = REGULAR):
        """
        Publish a new log message from the node.

        Parameters
        ----------
        message :
            A string to send as the log message.
        verbosity :
            The level of verbosity at which the message should be displayed.
        """
        # Create and publish a new log message with the proper fields
        temp_msg = log_message(message=message,
                               verbosity=verbosity,
                               source=get_name()[1:])
        temp_msg.header.stamp = Time.now()
        self.logger.publish(temp_msg)

    def publish_node_status(self, new_status: str,
                            delay_publishing: float = None,
                            default_status: str = None):
        """
        Publish a new status for the node. Status messages are sent using the log_message format.

        Parameters
        ----------
        new_status :
            The new status of the node that should be published.
        delay_publishing :
            The amount of time in seconds to delay before publishing the default status. If none is
        """
        # Define a variable to store the status message that will be published
        status_to_publish = None

        # If a new status is given
        if new_status is not None:
            status_to_publish = new_status

        # Otherwise check if the default status should be sent
        elif self.time_of_last_publishing is not None and \
            delay_publishing is not None and default_status is not None and \
            Time.now() - self.time_of_last_publishing > Duration(secs=0, nsecs=delay_publishing*10**9):
            status_to_publish = default_status

        # If there is a status to publish
        if status_to_publish is not None:

            # Create and publish a new status message with the proper fields
            temp_msg = log_message(message=status_to_publish,
                                   verbosity=NO_VERBOSITY,
                                   source=get_name()[1:])
            temp_msg.header.stamp = Time.now()
            self.status_publisher.publish(temp_msg)

            # Save the current time as the last time a status was published
            self.time_of_last_publishing = Time.now()

    @staticmethod
    def load_default_settings() -> dict:
        pass

        """default_settings_file_path = '/home/ben/thyroid_ultrasound/src/thyroid_ultrasound_support/' \
                                    'default_settings/default_settings.txt'

        # Open the simple data file and read each line from it
        simple_data_file = open(default_settings_file_path, 'r')
        all_data_line = simple_data_file.read()

        # Remove the carriage return character at the end of the string
        all_data_line = all_data_line[:-len(NEW_LINE)]

        # Pull each field from the string by splitting on the carriage returns
        simple_data_lines = all_data_line.split(NEW_LINE)

        # Rebuild the data contained within each line of the text file
        for single_line_data in simple_data_lines:
            # Rebuild the data from the line
            field_name, value = rebuild_data(single_line_data)
        """

        return {}

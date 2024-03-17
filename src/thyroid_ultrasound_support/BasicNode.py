#!/usr/bin/env python3

"""
File containing the code for a basic node that allows logging of messages.
"""

# Import standard ROS packages
from rospy import init_node, spin, Rate, Subscriber, is_shutdown, Publisher, get_name, on_shutdown, Time, Service, \
    ServiceProxy, wait_for_service, ServiceException
from std_msgs.msg import Bool, Float64, String

# Import custom ROS packages
from thyroid_ultrasound_messages.msg import log_message
from thyroid_ultrasound_services.srv import *

# Import custom python packages
from thyroid_ultrasound_support.LoggingConstants import *
from thyroid_ultrasound_support.NodeStatusConstants import *
from thyroid_ultrasound_support.NodeNameConstants import *
from thyroid_ultrasound_support.TopicNames import *
from thyroid_ultrasound_support.ServiceNames import *

# Define levels of verbosity
SHORT: int = int(0)
LONG: int = int(3)
EXTRA_LONG: int = int(5)


class BasicNode:
    def __init__(self):
        # Define a common publisher to send the log messages
        self.logger = Publisher(LOGGING, log_message, queue_size=1)

        # Define a common publisher to send node status messages
        self.status_publisher = Publisher(STATUS, log_message, queue_size=1)

    def log_single_message(self, message: str, verbosity: int):
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
        self.logger.publish(log_message(message=message,
                                        verbosity=verbosity,
                                        source=get_name()))

    def publish_node_status(self, new_status: str):
        """
        Publish a new status for the node. Status messages are sent using the log_message format.

        Parameters
        ----------
        new_status :
            The new status of the node that should be published.
        """
        # Create and publish a new status message with the proper fields
        self.status_publisher.publish(log_message(message=new_status,
                                                  verbosity=NO_VERBOSITY,
                                                  source=get_name()))

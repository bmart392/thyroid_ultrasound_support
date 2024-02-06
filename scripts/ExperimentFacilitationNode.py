#!/usr/bin/env python3

"""
File containing the code for a basic node that allows logging of messages.
"""

# Import standard python packages

# Import standard ROS packages

# Import custom python packages

# Import custom ROS packages
from thyroid_ultrasound_support.BasicNode import *


class ExperimentFacilitationNode(BasicNode):

    def __init__(self):

        # Call the init function of the super class
        super().__init__()

        pass

    def main_loop(self):

        pass


if __name__ == '__main__':

    # Create the node object
    node = ExperimentFacilitationNode()

    print("Node initialized.")
    print("Press ctrl+c to terminate.")

    # While the node is not shut down
    while not is_shutdown():

        # Run the main loop
        node.main_loop()

    # Notify the user that the node has been terminated
    print("Node Terminated.")

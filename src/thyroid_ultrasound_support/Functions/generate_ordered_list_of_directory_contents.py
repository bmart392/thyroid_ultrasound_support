
# Import standard python packages
from operator import itemgetter
from os import listdir
from os.path import exists


def generate_ordered_list_of_directory_contents(directory_path: str,
                                                sort_indices: tuple,
                                                return_index_values: bool = False,
                                                sort_by_string_allowed: bool = False) -> list:
    """
    Generates an ordered list of the contents of a given directory.
    The function assumes that all members of the directory use '_' to separate key parameters of the name.

    Parameters
    ----------
    directory_path :
        The directory in which to generate a list of contents.
    sort_indices :
        A tuple of indices representing which portion of the file name to sort by.
        No more than five indices may be used to sort the contents.
        The contents will be sorted based on the order in which the indices are given.
    return_index_values :
        When True, the sorted index values will be returned along with the list of contents.
    sort_by_string_allowed :
        When True, the function is allowed to use string values to sort the contents of the folder.

    Returns
    -------
    list
        A list containing list. The ordered list of file contents is always the last item in the list.
        The index values are returned in the order in which they were given for the sort_indices argument.
        The first index value is returned as the first item in the list.
    """
    # Ensure that the directory exists
    if not exists(directory_path):
        raise Exception(directory_path + " is not a valid location.")

    # Ensure that the directory path ends with a back-slash
    if directory_path[-1] != '/':
        directory_path = directory_path + '/'

    # Define a destination for the sorted contents of the directory
    sorted_directory_contents = []

    # For each item in the directory
    for item_name in listdir(directory_path):

        # Generate the name of the item without any extensions
        try:
            item_name_without_file_extension = item_name[:item_name.index('.')]
        except ValueError:
            item_name_without_file_extension = item_name

        try:
            # Split the item name by underscores
            item_name_components = item_name_without_file_extension.split('_')

            # Define a temporary variable to store the individual components that will be sorted by
            temp_components = []

            # Add the individual relevant components to the entry for the item
            for index in sort_indices:
                try:  # to convert the value to a number
                    temp_individual_component = float(item_name_components[index])

                except ValueError:
                    if sort_by_string_allowed:  # if sorting by strings is allowed, leave the value as a string
                        temp_individual_component = item_name_components[index]
                    else:  # otherwise, escalate the error
                        raise ValueError

                # Add the converted component
                temp_components.append(temp_individual_component)

            # Add the item name at the end
            temp_components.append(item_name)

            # Add the temporary list to the sorted list
            sorted_directory_contents.append(temp_components)
        except IndexError:
            print(item_name_without_file_extension + ' is not named correctly to be sorted.')
            raise IndexError

    # Create an itemgetter with the appropriate number of sort indices
    if len(sort_indices) == 1:
        temp_itemgetter = itemgetter(0)
    elif len(sort_indices) == 2:
        temp_itemgetter = itemgetter(0, 1)
    elif len(sort_indices) == 3:
        temp_itemgetter = itemgetter(0, 1, 2)
    elif len(sort_indices) == 4:
        temp_itemgetter = itemgetter(0, 1, 2, 3)
    elif len(sort_indices) == 5:
        temp_itemgetter = itemgetter(0, 1, 2, 3, 4)
    else:
        raise Exception("The number of indices to sort by, " + str(len(sort_indices)) +
                        ", is not supported by the function.")

    # Sort the contents
    sorted_directory_contents.sort(key=temp_itemgetter)

    # Define a list to store just the file names in order
    list_of_values_to_return = [[]]

    # Add additional lists if the index values are to be returned
    if return_index_values:
        for i in range(len(sort_indices)):
            list_of_values_to_return.append([])

    # For each sorted data point,
    for entry in sorted_directory_contents:

        # Add the item name
        list_of_values_to_return[-1].append(directory_path + entry[-1])

        # If returning the index values as well, add them to the return list
        if return_index_values:
            for i in range(len(sort_indices)):
                list_of_values_to_return[i].append(entry[i])

    # Return the temporary list
    return list_of_values_to_return


if __name__ == '__main__':
    # file_path = '/home/ben/thyroid_ultrasound_data/testing_and_validation/saved_image_data_objects'
    file_path = '/home/ben/thyroid_ultrasound_data/experimentation/2024-10-03_11-37-49-175784_experiment' \
                '/RawImages_2024-10-03_11-37-49-175784'

    ordered_list = generate_ordered_list_of_directory_contents(file_path, (1, 2), True)

    for sec, n_sec, file_name in zip(ordered_list[0], ordered_list[1], ordered_list[2]):
        print(file_name[file_name.rfind('/'):] + ' | Sec: ' + str(sec) + ' | N-Sec: ' + str(n_sec))


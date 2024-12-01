def get_lists():
    """
    Opens a file that contains two columns of values.  Splits these columns into two lists of strings, before converting the values
    to integers.
    Returns the two lists sorted in ascending order.
    """
    string_list_one = []
    string_list_two = []

    with open(
        "Day_1/data.txt",
        "r",
    ) as file:
        for line in file:
            locations = line.split()
            string_list_one.append(locations[0])
            string_list_two.append(locations[1])

    int_list_one = [int(item) for item in string_list_one]
    int_list_two = [int(item) for item in string_list_two]

    return sorted(int_list_one), sorted(int_list_two)


list_one, list_two = get_lists()


def find_total_difference_distance(list_one: list, list_two: list) -> int:
    """
    Find the total difference distance between lists.
    This function finds the absolute difference between matching indexed values in both lists.
    Total difference totals all of these differences and this value is returned.
    """
    total_difference = 0

    id_differences_list = [abs(list_one[i] - list_two[i]) for i in range(len(list_one))]

    for n in id_differences_list:
        total_difference += n

    return total_difference


print("Total difference: ", find_total_difference_distance(list_one, list_two))


def find_similarity_score(list_one: list, list_two: list) -> int:
    """
    Find similarity score between the two lists.
    This function takes each value from the first list, finds how often that value occurs in the right list and
    is then multiplied by that amount. e.g. 2 occurs 3 times in list 3 so 2 x 3 = 6.
    Similarity score totals these multiplied values and this value is returned
    """
    similarity_score = 0

    for n in list_one:
        n_multiplied = n * list_two.count(n)
        similarity_score += n_multiplied

    return similarity_score


print("Similarity score: ", find_similarity_score(list_one, list_two))

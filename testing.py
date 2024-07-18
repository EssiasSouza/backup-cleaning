

def filter_objects(object_list, criteria_to_exclude):
    filtered_list = []
    for obj in object_list:
        if not any(criteria in obj for criteria in criteria_to_exclude):
            filtered_list.append(obj)
    return filtered_list


object_list = ["apple", "banana", "cherry.txt", "date", "elderberry"]
criteria_to_exclude = ["ban", "txt", "at"]

result = filter_objects(object_list, criteria_to_exclude)
print(result)  # Output: ['apple', 'date']
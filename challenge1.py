# Write a Python script to extract the group names and find their occurences from the given input file.

import pandas as pd
import re

def group_names_with_occurences(file):
    data = pd.read_excel(file)

    group_names = []

    for comments in data['Additional comments']:
        pattern = r'(?:Groups|Group Names) : \[code\]<I>(.*?)</I>\[/code\]'
        matches = re.findall(pattern, comments)

        for match in matches:
            groups = [group.strip() for group in match.split(',')]
            group_names.extend(groups)

    group_count = {}
    for group_name in group_names:
        if group_name in group_count:
            group_count[group_name] += 1
        else:
            group_count[group_name] = 1

    output_data = pd.DataFrame(group_count.items(), columns=['Group name', 'Number of occurences'])

    return output_data


def main():
    file_path = 'coding challenge test.xlsx'

    output_data = group_names_with_occurences(file_path)

    output_data.to_csv('output_groups.csv', index=False)

    print("Output data succesfully saved to output file")

if __name__ == "__main__":
    main()
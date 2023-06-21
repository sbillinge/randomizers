_TRAITS = [("work_continent",3), ("gender",2), ("institution",1)]

def diversity_score(group):
    score = 0
    for i, student_1 in enumerate(group):
        for student_2 in group[i + 1:]:
            for trait in _TRAITS:
                score -= (student_1[trait[0]] == student_2[trait[0]]) * trait[1]
    return score

import random

def random_assignment(students, num_groups):
    """Randomly assign students to groups.

    students: list of students, as described above
    num_groups: number of groups to return
    returns: lists of students of more-or-less equal size
    """
    random.shuffle(students)
    groups = [[] for _ in range(num_groups)]
    for i, student in enumerate(students):
        index = i % len(groups)
        groups[index].append(student)
    return groups

def maybe_swap(group_1, group_2):
    diversity_1, diversity_2 = map(diversity_score, [group_1, group_2])
    old_sum = diversity_1 + diversity_2
    for _ in range(len(group_1)):  # do this for every student in group_1
        student_1 = group_1.pop(0)  # provisionally remove from group_1
        for _ in range(len(group_2)):
            student_2 = group_2.pop(0)  # provisionally remove from g_2
            group_1.append(student_2)  # provisionally swap students
            group_2.append(student_1)
            diversity_1, diversity_2 = map(
                diversity_score, [group_1, group_2])
            new_sum = diversity_1 + diversity_2
            if new_sum > old_sum:  # see what the new score is
                return True  # leave the swap intact and return if higher
            group_2.pop()  # else, remove student_1 from group_2 ...
            group_2.append(group_1.pop())  # and return student_2 to group_2
        group_1.append(student_1)  # return student_1 to group_1
    return False

def assign_to_groups(students, num_groups):
    groups = random_assignment(students, num_groups)
    while True:
        has_swapped = False
        for i, group_1 in enumerate(groups):
            for group_2 in groups[i + 1:]:
                has_swapped = maybe_swap(group_1, group_2) or has_swapped
        if not has_swapped:
            return groups

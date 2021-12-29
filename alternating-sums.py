# Problem: Several people are standing in a row and need to be divided into two teams. The first person goes into
# team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.
#
# You are given an array of positive integers - the weights of the people. Return an array of two integers,
# where the first element is the total weight of team 1, and the second element is the total weight of team 2 after
# the division is complete.
# Example:
# For a = [50, 60, 60, 45, 70], the output should be
# solution(a) = [180, 105].

# Solution -------------------------------------------------------------------------------------------------------------

def alternating_sums(a):
    team_1 = []
    team_2 = []

    # add items at every other index to team arrays
    for i in range(len(a)):
        if i == 0:
            team_1.append(a[i])
        elif i % 2 != 0:
            team_2.append(a[i])
        elif i % 2 == 0:
            team_1.append(a[i])

    print(team_1)
    print(team_2)

    # create results arrays with the sums of each team
    result = [sum(team_1), sum(team_2)]

    print(result)


a = [50, 60, 60, 45, 70]
alternating_sums(a)

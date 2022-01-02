# Problem:
# Call two arms equally strong if the heaviest weights they each are able to lift are equal.
#
# Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right
# and the left), and so are their weakest arms.
#
# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
# Example:
# For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
# solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
# solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
# solution(yourLeft, yourRight, friendsLeft, friendsRight) = false.
# Solution -------------------------------------------------------------------------------------------------------------

def equallyStrong(your_l, your_r, friend_l, friend_r):
    your_arms = [your_l, your_r]
    friend_arms = [friend_l, friend_r]

    if max(your_arms) == max(friend_arms):
        if min(your_arms) == min(friend_arms):
            return True
        return False
    return False



yourLeft = 10
yourRight = 15
friendsLeft = 15
friendsRight = 10

print(equallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))
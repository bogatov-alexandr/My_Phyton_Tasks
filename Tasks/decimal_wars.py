# Given two Arrays in which values are the power of each soldier, return true if you survive the attack or false if you perish.

# CONDITIONS

# Each soldier attacks the opposing soldier in the same index of the array. The survivor is the number with the highest value.
# If the value is the same they both perish
# If one of the values is empty(different array lengths) the non-empty value soldier survives.
# To survive the defending side must have more survivors than the attacking side.
# In case there are the same number of survivors in both sides, the winner is the team with the highest initial attack power. If the total attack power of both sides is the same return true.
# The initial attack power is the sum of all the values in each array.

def is_defended(attackers, defenders):
    surv_Atak = 0
    surv_Defend = 0
    if len(attackers) < len(defenders) and attackers !=[]:
        min_l = len(attackers)
        surv_Defend+=len(defenders)-len(attackers)
    elif len(defenders)<len(attackers) and defenders!=[]:
        min_l = len(defenders)
        surv_Atak+=len(attackers)-len(defenders)
    else:
        if attackers==[]:
            return True
        elif defenders==[]:
            return False
        else:
            min_l=len(attackers)

    for i in range(min_l):
        if attackers[i]<defenders[i]:
            surv_Defend+=1
        elif attackers[i]>defenders[i]:
            surv_Atak+=1
        else:
            continue
    if  surv_Atak<surv_Defend:
        return True
    elif surv_Defend==surv_Atak:
        if sum(attackers)>sum(defenders):
            return False
        else:
            return True
    else:
        return False





if __name__ == '__main__':
    print(is_defended([2, 9, 9, 7], [1, 1, 3, 8]))
    print(is_defended([1, 3, 5, 7], [2, 4, 6, 8]))
    print(is_defended([10, 10, 1, 1], [4, 4, 7, 7]))
    print(is_defended([],[1, 2, 3]))
    print(is_defended([1, 2, 3],[]))
    print(is_defended([23, 34, 18, 15, 29, 49, 46, 49],[50, 45, 28, 45, 3, 5, 44, 29]))



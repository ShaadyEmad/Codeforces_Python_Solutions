import collections

t = int(input())
unique_list = []


def check_duplicated(orbit):
    if len(orbit) == len(set(orbit)):
        return True
    else:
        return False


def count_duplicated(orbit,element):
    counter = collections.Counter(orbit)
    return counter[element]


def cost_calculate(c,unique_list,cost):
    for element in (unique_list):
        if (element == 1):
            cost += 1

        elif element <= c:
            cost += element

        elif element > c:
            cost += c

    return cost


for case in range(t):
    n, c = map(int, input().split())
    orbit = list(map(int,input().split()))
    cost = 0

    if check_duplicated(orbit):
        cost = len(orbit)

    else:
        orbit_set = set(orbit)
        for element in orbit_set:
            count = count_duplicated(orbit,element)
            unique_list.append(count)

        cost = cost_calculate(c,unique_list,cost)
        unique_list.clear()


    print(cost)

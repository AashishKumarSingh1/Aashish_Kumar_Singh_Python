# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    dish_a=list(map(int,input().split()))
    cook_time=list(map(int,input().split()))
    if len(set(dish_a))>=k:
        # cook_time.sort()
        pair=[[dish_a[i],cook_time[i]] for i in range(n)]
        sorted_pair = []
        seen_dishes = set()
        for dish, time in sorted(pair, key=lambda x: x[1]):
            if dish not in seen_dishes:
                # sorted_pair.append([dish, time])
                sorted_pair.append(time)
                seen_dishes.add(dish)
        # print(sorted_pair)
        min_time=sum(sorted_pair[:k])
        # min_time=sum(cook_time[:k])
        print(min_time)
    else:
        print('-1')
        
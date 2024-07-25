def square_sum(n:int)->int:
    current=3
    sum=current**2
    # print(sum , 'sum')
    for i in range(1,n):
        current*=2
        # print(current,'current')
        sum+=current**2
        # print(sum,'final sum')

    return sum

if __name__=='__main__':
    print(square_sum(1))
    print(square_sum(2))
    print(square_sum(3))
    print(square_sum(4))
    print(square_sum(5))

        
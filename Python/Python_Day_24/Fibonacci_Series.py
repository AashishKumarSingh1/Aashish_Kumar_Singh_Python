def fibon_ser(num):
    #base condition 
    if num==0 or num ==1:
        return 1 
    return fibon_ser(num-1)+fibon_ser(num-2)

if __name__=='__main__':
    first_20_fibonaci_series=tuple(map(fibon_ser,[i for i in range(21)]))
    print('Fibonacci Series: ')
    for num in first_20_fibonaci_series:
        print(num)

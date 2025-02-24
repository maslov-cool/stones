n, m = [int(i) for i in input().split()]
if (n % 3 == 0 and m % 3 == 0) or (n % 3 == 1 and m % 3 == 1) or (n % 3 == 2 and m % 3 == 2):
    print('Lose')
else:
    print('Win')

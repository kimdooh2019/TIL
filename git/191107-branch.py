#for i in range(1, 101):
#    if i % 15 == 0:
#        print(f'fizzbuzz {i}')
#    elif i % 3 == 0:
#        print(f'fizz {i}')
#    elif i % 5 == 0:
#        print(f'buzz {i}')
#    else:
#        print(i)
#print(['fizzbuzz' if i % 15 == 0 else 'fizz' if i % 3 == 0 else 'buzz' if i % 5 == 0 else i for i in range(1, 101) ] )

print('aaaaaaaaaaaaaaaaaa')

for i in range(1, 101):
    if i % 3 ==0 or i % 5 ==0:
        print('fizz'*(i%3==0) + 'buzz'*(i%5==0))

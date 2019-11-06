
#for i in range(1, 101):
#    if i % 15 == 0:
#        print(f'fizzbizz{i}')
#    elif i % 3 == 0:
#        print(f'fizz{i}')
#    elif i % 5 == 0:
#        print(f'bizz{i}')
#    else:
#        print(f'{i}')

 
#for i in range(1, 101):
#    if i % 3 == 0 or i % 5 == 0:
#        print('fizz'*(i % 3 == 0) + 'bizz' * (i % 5  ==0))

print( [ f'{i}fizzbizz' if i % 15 == 0 else f'{i}fizz' if i % 3 == 0 else f'{i}bizz' if i % 5 == 0 else i for i in range(1, 101) ])

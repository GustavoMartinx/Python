a = 'value'  # True
a = 0        # False
a = -0.0001  # True
a = ''       # False
a = ' '      # False
a = []       # False
a = {}       # False

if a:
    print('Exist!')
else:
    print("Does't exist or is zero or is empty.")

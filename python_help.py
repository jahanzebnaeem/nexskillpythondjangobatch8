name = 'This is a global name'

def greet():
    # Enclosing function
    # name = 'Hammad Ali'
    global name
    print('this is before global valiable overwrite {}'.format(name))
    name = "Hammad Ali"
    print('New variable value {}'.format(name))

greet()
print(name)

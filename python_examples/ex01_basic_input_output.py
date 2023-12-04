print('Welcome to Python learning')
user_name = input('What is your name?')
user_city = input('Where are your from? ')

print('Hello %s. How is weather in %s?' % (user_name, user_city))
print('Hello ', user_name, '. How is weather in ' + user_city + '?', sep='')
print('Hello {}. How is weather in {}?'.format(user_name, user_city))
print(f'Hello {user_name}. How is weather in {user_city}?')

# Formatting with place holders
# You can use %s to inject strings into your print statements. The modulo % is referred to as a "string formatting operator".

print ("I am going to insert %s here" %'something')
print ('I am going to insert %s %s here' %('something', 'else'))

x, y = 'some', 'more'
print('I am going to insert %s text here and %s things here' %(x,y))

# Format conversion methods
print('He said his name %s' %'Fred \t Alfred')
print("He said his name %r" %"Fred \t Alfred")

# Floating point numbers
print('Floating point numbers: %5.2f' %(11111.1149))

# Formatting with the .format() method
# The .format() method has several advantages over the %s placeholder method
# 1. Inserted objects can be called by index position
# 2. Inserted objects can be assigned keywords
# 3. Inserted objects can be reused, avoiding duplication
print('The string here {} and string here is {}'.format('is something', 'something else'))
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {b} {a} {c}'.format(a=1, b=10, c=100))
print('Allow duplication {0} of {0}'. format('words'))
print('A {p} saved is a {p} earned.'.format(p='penny'))

# Alignment, padding and precision with .format()        
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

# Formatted String Literals (f-strings) - Python 3.6 and newer versions
name = 'Fred'
print(f"He said his name is {name}")
print(f"He said his name is {name!r}")






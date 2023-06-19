str = 'badcfe'
output = ''
i = 0
while i < len(str):
        if i + 1 < len(str):
                output = output + str[i + 1]
                output = output + str[i]
        i = i + 2
print( 'Given   String: ' + str)
print('Swapped String: ' + output)
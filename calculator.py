#given that the user inputs 2 numbers and an operator 
def calc(a, b, op): # should return  a string like this a op b = c 

    if op not in "+-/*":
        return 'Please only type one of these characters: "+,-,*,/"'

    if op == '+':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))

def main():
    a = int(input("Please type the first number: "))
    b = int(input("Please type the second number: "))
    op = input('What kind of opertion you would like to do?\\nChoose between "+, -, *, /" : ')

    print(calc(a, b, op))

main()
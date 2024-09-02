def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
    
output_number = 0
while output_number != 1:
    print('Enter your number:')
    try:
        input_number = int(input())
        output_number = collatz(input_number)
        print(output_number)
    except ValueError:
        print('Please enter an integer.')
        continue

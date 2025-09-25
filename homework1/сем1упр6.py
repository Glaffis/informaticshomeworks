def to_decimal(number_str, base):
    decimal = 0
    digits = list(map(int, number_str))
    for i in range(len(digits)):
        decimal += digits[i] * (base ** (len(digits) - 1 - i))
    return decimal
    
def from_decimal(number, base):
    if number == 0:
        return '0'
    result = []
    while number > 0:
        result.append(str(number % base))
        number //= base
    return ''.join(reversed(result))

with open('input.txt', 'r') as file:
    lines = file.readlines()

number_strs = lines[0].strip().split()
operation = lines[1].strip()
base = int(lines[2].strip())

numbers = []
for num_str in number_strs:
    numbers.append(to_decimal(num_str, base))
    
if operation == '+':
    result = sum(numbers)
elif operation == '-':
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
elif operation == '*':
    result = 1
    for num in numbers:
        result *= num

result_str = from_decimal(result, base)

with open('output.txt', 'w') as file:
    file.write(result_str)


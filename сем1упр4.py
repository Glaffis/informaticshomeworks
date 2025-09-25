f = open('text.txt', 'r')
print(f.read())

for line in f:
    print(line)

lines = f.readlines()
print(lines)

with open('text.txt', 'w')


with open('input.txt', 'r') as f:
          lines = f.readlines()
          numbers = list(map(int, lines[0].split()))
          op = lines[1].strip()
          if op == '+':
              res = 0
              for i in numbers:
                  res += i
          elif op == '*':
              res = 1
              for i in numbers:
                  res *= i
          else:
              res = numbers[0]
              for i in range (1, len(numbers)):
                  res -= numbers[i]



        



f.close

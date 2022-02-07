import sys

sys.argv[1:] = [int(x) for x in sys.argv[1:]]
result = 0
for n in sys.argv[1:]:
    result += n

print(result)
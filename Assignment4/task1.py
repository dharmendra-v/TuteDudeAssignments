

try:
    with open('sample.txt', 'r') as f:
        print("Reading file content:")
        count = 1
        for line in f.readlines():
            print(f'Line {count}: {line}', end='')
            count += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")

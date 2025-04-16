import sys

n = int(sys.argv[1])
texto = str(sys.argv[2:]).replace('[', '').replace(']', '').replace('"', '').replace(',', '').replace("'", "")

for _ in range(n):
    print(texto)

def cheer(n):
    'return a string with a silly cheer based on n'
    if n <= 1:
        return "Hurrah!"
    else:
        return "Hip " + cheer(n - 1)

x = cheer(5)
print(x)

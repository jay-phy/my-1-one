def generate_palindromes(n):
    if n == 1:
        return [str(i) for i in range(10)]
    elif n % 2 == 0:
        half = n // 2
        return [str(i) + str(i)[::-1] for i in range(10**(half-1), 10**half)]
    else:
        half = n // 2
        return [str(i) + str(m) + str(i)[::-1] for i in range(10**(half-1), 10**half) for m in range(10)]

# Example usage:
n = 3  # Replace with the number of digits you want
palindromes = generate_palindromes(n)
print(palindromes)


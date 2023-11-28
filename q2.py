def collatz_sequence_length(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 1:
        return 0
    elif n % 2 == 0:
        memo[n] = 1 + collatz_sequence_length(n // 2)
    else:
        memo[n] = 1 + collatz_sequence_length(3 * n + 1)

    return memo[n]

# Calculate sequence lengths for the first 12,031,203 positive integers
sequence_lengths = [collatz_sequence_length(i) for i in range(1, 12031204)]

# Sort the sequence lengths
sequence_lengths.sort()

# Calculate the median
length_count = len(sequence_lengths)
if length_count % 2 == 0:
    median = (sequence_lengths[length_count // 2 - 1] + sequence_lengths[length_count // 2]) / 2
else:
    median = sequence_lengths[length_count // 2]

print(f"The median sequence length for the first 12,031,203 positive integers is: {median}")

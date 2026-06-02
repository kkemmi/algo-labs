import sys


def solve_wchain(n, words):
    if not words or n == 0:
        return 0

    buckets = {}
    max_len = 0
    for word in set(words):
        length = len(word)
        if length not in buckets:
            buckets[length] = []
        buckets[length].append(word)
        if length > max_len:
            max_len = length

    dp = {}
    max_global_chain = 0

    for length in range(1, max_len + 1):
        if length not in buckets:
            continue

        for word in buckets[length]:
            current_max = 1
            for i in range(length):
                prev_word = word[:i] + word[i + 1:]
                if prev_word in dp:
                    val = dp[prev_word] + 1
                    if val > current_max:
                        current_max = val

            dp[word] = current_max
            if current_max > max_global_chain:
                max_global_chain = current_max

    return max_global_chain


if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        try:
            n_val = int(input_data[0])
            words_list = input_data[1:]
            print(solve_wchain(n_val, words_list))
        except (ValueError, IndexError):
            pass

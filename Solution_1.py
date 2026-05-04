#Problem 1 solution
def max_sum(chars):
    n = len(chars)
    s2 = chars + chars

    freq = {}
    l = 0
    curr_sum = 0
    max_s = 0

    for r in range(len(s2)):
        ch = s2[r]
        freq[ch] = freq.get(ch, 0) + 1
        curr_sum += ord(ch) - 96
        while freq[ch] > 1 or (r - l + 1) > n:
            left = s2[l]
            freq[left] -= 1
            curr_sum -= ord(left) - 96

            if freq[left] == 0:
                del freq[left]
            l += 1
        max_s = max(max_s, curr_sum)
    return max_s

chars=input()
res=max_sum(chars)
print(res)

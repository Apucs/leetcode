class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == "":
            return ""

        t_count = {}
        window = {}
        covered = {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
            covered[c] = 0

        # print(t_count, covered)

        curr = 0
        target = len(t_count)

        min_dist = len(s)+1
        res = [-1, -1]

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c, 0)

            # print(target, l, r, c, s[l:r+1], window)

            if c in t_count and window[c] == t_count[c]:
                # print(f"Macthed for {c}")
                curr += 1

            while curr == target:

                if (r-l+1) < min_dist:
                    res = [l, r]

                    # print("\n", res, s[l:r+1], "\n")

                    min_dist = r-l+1

                window[s[l]] -= 1

                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    # print("yes, decrementing")
                    curr -= 1

                l += 1

        # print(min_dist)

        start, end = res
        # print(s[start:end+1])

        return s[start:end+1]

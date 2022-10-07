class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # print(len(" "))

        final_string = []
        sub_string = []
        length = 0
        max_len = 0

        for i in range(len(s)):
            if len(s) <= 1:
                return len(s)

            if s[i] not in sub_string:
                sub_string.append(s[i])
                length += 1
                max_len = max(max_len, length)

                # print("No matching string", sub_string)

            else:
                idx = sub_string.index(s[i])
                if idx != len(sub_string)-1:
                    new_string = sub_string[idx+1:]
                    new_string.append(s[i])
                    sub_string = new_string
                    # sub_string.append(s[i])
                    length = len(sub_string)
                    # print("String matched at random index", sub_string)
                else:
                    sub_string = []
                    sub_string.append(s[i])
                    length = 1
                    # print("String matched at last index", sub_string)

        return max_len

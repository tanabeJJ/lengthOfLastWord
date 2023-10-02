from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0


print("スタート")
assert Solution().lengthOfLastWord("Hello World") == 5
assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
print("コンプリート!本番テストへ")

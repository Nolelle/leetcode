class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # this seems to be like a O(n) array problem where we have to loop through
        # the entire array to see if we can assign cookies to children
        # we want to ensure we try our best to empty the cookies array each time.
        # output is number of cookies given out
        # g array = greed factor of each child
        # s array = size of cookie
        # condiiton to give out cookie is s[j] >= g[i]

        output = 0
        g.sort()
        s.sort()
        g_pointer, s_pointer = 0, 0
        ng = len(g)
        ns = len(s)

        while g_pointer < ng and s_pointer < ns:
            if s[s_pointer] >= g[g_pointer]:
                output += 1
                g_pointer += 1
            s_pointer += 1

        return output

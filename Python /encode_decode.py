class Codec:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
         """
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        array = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            print(length)
            array.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return array


s = Codec()
v = s.encode(["Hello", "World"])
print(v)
print(s.decode(v))

class Solution:
    """
    Took a time trying to understand what the problem asked. 
    In summary, you must encode a list of strings into one string and ONLY return that string. 
    
    This makes it more difficult because you can't just track the length of each word in an array and return it
    
    The second difficulty comes in figuring out a way to determine the length of each words if every delimeter
    could be present in the string itself, hence the combination of adding the length of the word + the delimeter,
    that way we stop at the first encounter of the delimeter and count only the number of letters that we had before
    the delimiter.
    """
    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return(encoded)

    def decode(self, s: str) -> list[str]:
        strs = []
        index = 0
        while index < len(s):
            temp = ""
            length = ""
            while s[index] != "#":
                length += s[index]
                index += 1
            
            index += 1 # skip delimiter
            
            for i in range(int(length)):
                temp += s[index] 
                index += 1
            
            strs.append(temp)        
        return strs
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ""
        seperator = chr(257)
        for s in strs:
            output+= s
            output+= seperator
        output = output[:-1]
        return output
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
    
        seperator = chr(257)
        return s.split(seperator)
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
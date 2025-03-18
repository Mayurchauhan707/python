"""
make pangram() for sentence"""
def pangram(s):
      alphaset=set("abcdefghijklmnopqrstuvwxyz")
      print(alphaset)
      s=s.lower()
      s=set(s)
      return(alphaset<=s)
str="The quick brown fox jumps over the lazy dog."
print(str,pangram(str))
str="Pack my box with five dozen liquor jugs"
print(str,pangram(str))
str="Sphinx of black quartz, judge my vow"
print(str,pangram(str))

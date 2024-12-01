vowels = ['a','e','i','o','u']

class SuperVowel():
    
    @staticmethod
    def convertToSuperString(str: str) -> str:
        ret = ""
        for ch in str:
            if(ch in vowels):
                ret+=ch.upper()
            else:
                ret+=ch
        return ret
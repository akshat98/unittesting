from unittesting.super_vowels import SuperVowel

def testSuperVowel():
    str1 = "abciou"
    ret = SuperVowel.convertToSuperString(str1)
    print(ret)
    assert ret  == "AbcIOU"
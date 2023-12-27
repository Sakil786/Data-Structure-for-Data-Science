# Python Program to Check if Two Strings are Anagram

def get_two_strings_anagram(string1, string2):
    if (sorted(string1) == sorted(string2)):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    s1 = 'bad'
    s2 = 'dad'
    get_two_strings_anagram(s1, s2)

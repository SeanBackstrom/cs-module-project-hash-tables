import re

def word_count(s):
    # Your code here
    count_dict = {}
    
    s = "".join(c for c in s if c not in ":;,.-+=/\|[]{}()*^&\"")
    s = s.lower()
    words = s.split(" ")
    words = re.split(' |\t|\n|\r', s)
    
    if s == "" or '':
        return {}
    
    for word in words:
        if word == "":
            continue
        count_dict[word] = 0

    for word in words:
        if word == "":
            continue
        count_dict[word] +=1 
    print(count_dict)
    return count_dict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
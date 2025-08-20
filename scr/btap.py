# 1.Program to calculate the length of a string
string = input("Enter a string: ")
print("Length of the string is:", len(string))
# 2.Program to count character frequency in a string
string = "google.com"
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
print("Character frequency:", frequency)
# 3.Program to get first 2 and last 2 chars of a string
def first_last_2(string):
    if len(string) < 2:
        return ""
    return string[:2] + string[-2:]
print(first_last_2("w3resource"))
print(first_last_2("w3"))
print(first_last_2("w"))
# 4.Program to replace all occurrences of first char with '$' except the first one
def change_char(string):
    first_char = string[0]
    return first_char + string[1:].replace(first_char, '$')
print(change_char("restart"))
# 5.Program to swap first two characters of two strings
def swap_strings(a, b):
    return b[:2] + a[2:] + " " + a[:2] + b[2:]
print(swap_strings("abc", "xyz"))
# 6.Program to add 'ing' or 'ly' at the end of a string
def add_ing(string):
    if len(string) < 3:
        return string
    if string.endswith("ing"):
        return string + "ly"
    else:
        return string + "ing"
print(add_ing("abc"))
print(add_ing("string"))
print(add_ing("hi"))
# 7.Program to replace 'not'...'poor' with 'good'
def not_poor(string):
    s_not = string.find("not")
    s_poor = string.find("poor")
    if s_not != -1 and s_poor != -1 and s_not < s_poor:
        return string[:s_not] + "good" + string[s_poor+4:]
    return string
print(not_poor("The lyrics is not that poor!"))
print(not_poor("The lyrics is poor!"))
# 8.Function to find the longest word in a list
def longest_word(word_list):
    longest = max(word_list, key=len)
    return longest, len(longest)
words = ["Python", "Exercises", "longest", "word"]
word, length = longest_word(words)
print("Longest word:", word)
print("Length of the longest word:", length)
# 9.Program to remove the nth index character from a string
def remove_char(string, n):
    if n < 0 or n >= len(string):
        return string
    return string[:n] + string[n+1:]
print(remove_char("Python", 0))
print(remove_char("Python", 3))
print(remove_char("Python", 10))
# 10.Program to exchange first and last chars of a string
def change_string(s):
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]
print(change_string("python"))
print(change_string("a"))
# 11.Program to remove characters with odd index values
def remove_odd_index(s):
    return s[::2]
print(remove_odd_index("python"))
print(remove_odd_index("abcdef"))
# 12.Program to count occurrences of each word in a sentence
def word_count(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
print(word_count("the quick brown fox jumps over the lazy dog the quick"))
# 13.Program to display input in upper and lower case
user_input = input("Enter a string: ")
print("Upper case:", user_input.upper())
print("Lower case:", user_input.lower())
# 14.Program to sort distinct words from comma-separated input
items = input("Enter comma-separated words: ")
words = [w.strip() for w in items.split(",")]
distinct_words = sorted(set(words))
print(",".join(distinct_words))
# 15.Program to wrap text with HTML tags
def add_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
# 16. Function to insert a string in the middle of another string
def insert_string_middle(container, word):
    mid = len(container) // 2
    return container[:mid] + word + container[mid:]
print(insert_string_middle("[[]]", "Python"))
print(insert_string_middle("{{}}", "PHP"))
print(insert_string_middle("<<>>", "Java"))
print(insert_string_middle("[[]]<<>>", "Python"))
# 17.Function to get 4 copies of the last two characters
def insert_end(s):
    if len(s) < 2:
        return "String too short"
    return s[-2:] * 4
print(insert_end("Python"))
print(insert_end("Exercises"))
# 18.Function to get first three characters
def first_three(s):
    return s if len(s) < 3 else s[:3]
print(first_three("ipy"))
print(first_three("python"))
print(first_three("hi"))
# 19.Program to get the last part of a string before a specified character
def last_part(s, char):
    return s.rsplit(char, 1)[0]
print(last_part("https://www.w3resource.com/python-exercises", "/"))
print(last_part("https://www.w3resource.com/python", "/"))
# 20.Function to reverse string if length is multiple of 4
def reverse_if_multiple_of_4(s):
    return s[::-1] if len(s) % 4 == 0 else s
print(reverse_if_multiple_of_4("abcd"))
print(reverse_if_multiple_of_4("abcdef"))
# 21.Function to convert to uppercase if at least 2 uppercase chars in first 4
def to_upper_if_two_caps(s):
    first4 = s[:4]
    uppercase_count = sum(1 for c in first4 if c.isupper())
    return s.upper() if uppercase_count >= 2 else s
print(to_upper_if_two_caps("PyThon"))
print(to_upper_if_two_caps("python"))
print(to_upper_if_two_caps("ABcdef"))
# 22.Program to sort a string lexicographically
def sort_string(s):
    return ''.join(sorted(s))
print(sort_string("python"))   # hnopty
print(sort_string("banana"))   # aaabnn
# 23.Program to remove newline characters
def remove_newline(s):
    return s.replace("\n", "")
text = "Hello\nWorld\nPython"
print(remove_newline(text))
# 24.Program to check if string starts with specified characters
def starts_with(s, prefix):
    return s.startswith(prefix)
print(starts_with("Python", "Py"))
print(starts_with("Python", "py"))
# 25.Program to create a Caesar cipher
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
print(caesar_encrypt("ABC", 3))
print(caesar_encrypt("xyz", 3))
print(caesar_encrypt("Hello World", 5))
# 26.Program to display formatted text with width=50
import textwrap
sample_text = "Python is a widely used high-level programming language for general-purpose programming."
print(textwrap.fill(sample_text, width=50))
# 27.Program to remove indentation
import textwrap
sample_text = """
        Python is cool.
        Easy to learn.
"""
print(textwrap.dedent(sample_text))
# 28.Program to add prefix text to each line
def add_prefix(text, prefix):
    return '\n'.join(prefix + line for line in text.splitlines())
sample_text = """A
B
C"""
print(add_prefix(sample_text, ">> "))
# 29. Write a Python program to set the indentation of the first line.
def indent_first_line(text, spaces):
    return ' ' * spaces + text
print(indent_first_line("Hello World", 4))
# 30. Write a Python program to print the following numbers up to 2 decimal places.
num = 20.4567
print("{:.2f}".format(num))
# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
num = 5.3456
print("{:+.2f}".format(num))
num2 = 12.34567
print("{:+.2f}".format(num2))
# 32. Write a Python program to print the following positive and negative numbers with no decimal places.
num1 = 45.56
num2 = -45.56
print("{:.0f}".format(num1))
print("{:.0f}".format(num2))
# 33. Write a Python program to print the following integers with zeros to the left of the specified width.
num = 2
print("{:04d}".format(num))
# 34. Write a Python program to print the following integers with '*' to the right of the specified width.
num = 5
print("{:*<4d}".format(num))
# 35. Write a Python program to display a number with a comma separator.
num = 1234567890
print("{:,}".format(num))
# 36. Write a Python program to format a number with a percentage.
num = 0.987
print("{:.1%}".format(num))
# 37. Write a Python program to display a number in left, right, and center aligned with a width of 10.
num = 999
print("{:<10}".format(num))
print("{:>10}".format(num))
print("{:^10}".format(num))
# 38. Write a Python program to count occurrences of a substring in a string.
s = ("banana")
print(s.count("na"))
# 39. Write a Python program to reverse a string.
s = "Python"
print(s[::-1])
# 40. Write a Python program to reverse words in a string.
s = "Hello World"
print(" ".join(s.split()[::-1]))
# 41. Write a Python program to strip a set of characters from a string.
s = "///Hello World,,,,"
print(s.strip("/,"))
# 42. Write a Python program to count repeated characters in a string.
s = 'thequickbrownfoxjumpsoverthelazydog'
from collections import Counter
counts = Counter(s)
for char, cnt in counts.items():
    if cnt > 1:
        print(char, cnt)
# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
import math
width = 22.0
height = 57.12
area = width * height
radius = 7.0
cylinder_height = 8.0
volume = math.pi * (radius ** 2) * cylinder_height
print(f"The area of the rectangle is {area:.2f}cm\u00b2")
print(f"The volume of the cylinder is {volume:.3f}cm\u00b3")
# 44. Write a Python program to print the index of a character in a string.
s = "w3resource"
for i, ch in enumerate(s):
    print(f"Current character {ch} position at {i}")
# 45. Write a Python program to check whether a string contains all letters of the alphabet.
import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello world"))
# 46. Write a Python program to convert a given string into a list of words.
s = "The quick brown fox jumps over the lazy dog."
print(s.split())
# 47. Write a Python program to lowercase the first n characters in a string.
def lowercase_first_n(s, n):
    return s[:n].lower() + s[n:]
print(lowercase_first_n("HELLOWORD", 5))
# 48. Write a Python program to swap commas and dots in a string.
def swap_commas_dots(s):
    return s.replace('.', 'TEMP').replace(',', '.').replace('TEMP', ',')
print(swap_commas_dots("32.054,23"))
# 49. Write a Python program to count and display vowels in text.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = {}
    for char in text:
        if char in vowels:
            count[char] = count.get(char, 0) + 1
    return count
sample = "The quick brown fox jumps over the lazy dog"
print(count_vowels(sample))
# 50. Write a Python program to split a string on the last occurrence of the delimiter.
def split_last(s, delimiter):
    return s.rsplit(delimiter, 1)
print(split_last("hello.world", "."))
print(split_last("one-two-three-four", "-"))
# 51. Write a Python program to find the first non-repeating character in a given string.
def first_non_repeating_char(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None
print(first_non_repeating_char("aabbcdeff"))
# 52. Write a Python program to print all permutations with a given repetition number of characters of a given string.
from itertools import product
def permute_with_repetition(s, r):
    return [''.join(p) for p in product(s, repeat=r)]
print(permute_with_repetition("abc", 2))
# 53. Write a Python program to find the first repeated character in a given string.
def first_repeated_char(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None
print(first_repeated_char("abcdea"))
# 54. Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest.
def first_repeated_char_min_index(s):
    index = {}
    min_index = len(s)
    repeated_char = None
    for i, ch in enumerate(s):
        if ch in index:
            if index[ch] < min_index:
                min_index = index[ch]
                repeated_char = ch
        else:
            index[ch] = i
    return repeated_char
print(first_repeated_char_min_index("abca"))
# 55. Write a Python program to find the first repeated word in a given string.
def first_repeated_word(s):
    words = s.split()
    seen = set()
    for w in words:
        if w in seen:
            return w
        seen.add(w)
    return None
print(first_repeated_word("she has has she"))
# 56. Write a Python program to find the second most repeated word in a given string.
from collections import Counter
def second_most_repeated_word(s):
    words = s.split()
    count = Counter(words)
    most_common = count.most_common()
    return most_common[1][0] if len(most_common) > 1 else None
print( second_most_repeated_word("one two three three one one"))
# 57. Write a Python program to remove spaces from a given string.
def remove_spaces(s):
    return s.replace(" ", "")
print( remove_spaces("a b  c d"))
# 58. Write a Python program to move spaces to the front of a given string.
def move_spaces_front(s):
    spaces = s.count(" ")
    no_spaces = s.replace(" ", "")
    return " " * spaces + no_spaces
print(move_spaces_front("abc d e f"))
# 59. Write a Python program to find the maximum number of characters in a given string.
from collections import Counter
def max_char(s):
    count = Counter(s)
    return count.most_common(1)[0]
print(max_char("abccccddddddee"))
# 60. Write a Python program to capitalize the first and last letters of each word in a given string.
def capitalize_first_last(s):
    words = s.split()
    result = []
    for w in words:
        if len(w) == 1:
            result.append(w.upper())
        else:
            result.append(w[0].upper() + w[1:-1] + w[-1].upper())
    return " ".join(result)
print(capitalize_first_last("hello world"))
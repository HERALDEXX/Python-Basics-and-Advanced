r"""Basic Building Blocks for Regular Expressions in Python
1. Literals: Ordinary characters that match themselves.
    e.g. pattern cat finds "cat" in "catalog".
2. Metacharacters: Characters with special meanings.
    e.g. '.' matches any character except newline.
        '\d' matches any digit,
        '\w' matches any alphanumeric character,
        '\s' matches any whitespace character.
        '^' asserts position at the start of a string,
        '$' asserts position at the end of a string.
"""

import re

text = "My score: 150 points, 200 points, and 300 points."

# Example of using a regex pattern to find all scores in the text
print("\nLiterals and Metacharacters Example:")

pattern = re.search(r'\d+', text)
print(pattern.group())

points = re.findall(r'\d+', text)
print(points)


# Quantifiers: Specifies how many times a character or group must occur.
# e.g. '*' matches 0 or more times,
#      '+' matches 1 or more times,
#      '?' matches 0 or 1 time.
#       {n} matches exactly n times,
#       {n,} matches n or more times,
#       {n,m} matches between n and m times.

# Example of using quantifiers
print("\nQuantifiers Example:")

text2 = "hahahaha"
pattern2 = re.findall(r'h+', text2)
print(pattern2)


# Character Classes and Sets: Define a set of characters to match.
# e.g. [aeiou] matches any vowel.
# e.g. [0-5] matches any digit from 0 to 5.
# e.g. [^A-Za-z] matches any character that is not a letter.
print("\nCharacter Classes and Sets Example:")

sentence = "I scored 99/100 in the exam."
pattern3 = re.findall(r'[^A-Za-z\s]', sentence)
print(pattern3) # This will print all non-letter characters in the sentence.


# Anchors and Boundaries: Used to match positions in the text.
print("\nAnchors and Boundaries Example:")

phrase = "The quick brown fox jumps over the lazy dog."
pattern4 = re.search(r'^The', phrase)
print(pattern4.group()) # Matches if the string starts with 'The'
print(re.search(r'dog\.$', phrase).group()) # Matches if the string ends with 'dog.'


# Grouping and Capturing: Used to group parts of a regex pattern.
# This allows you to apply quantifiers to the entire group or extract specific parts of the match.
print("\nGrouping and Capturing Example:")

date = "2025-06-24"
y, m, d = re.findall(r'(\d{4})-(\d{2})-(\d{2})', date)[0]
print(f"Year: {y}, Month: {m}, Day: {d}")
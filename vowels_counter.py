def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

sentence = input('enter a sentence')
v, c = count_vowels_consonants(sentence)
print(f"Number of vowels: {v}")
print(f"Number of consonants: {c}")
def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces_before = (length - len(string)) // 2
        spaces_after = length - len(string) - spaces_before
        if spaces_before < spaces_after:
            spaces_after -= 1
        formatted_string = " " * spaces_before + string + " " * spaces_after
        return formatted_string
    

# Приклад виклику функції
input_string = 'abba'
formatted_result = format_string(input_string, 15)
print(f"Original String: '{input_string}'")
print(f"Formatted String: '{formatted_result}'")

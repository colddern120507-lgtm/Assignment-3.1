def middle_character(text):
    length = len(text)

    while length > 0:
        if length % 2 == 0:
            return text[length // 2 - 1] + text[length // 2]
        else:
            return text[length // 2]

    return ""


# ===== TEST (BẮT BUỘC CÓ ĐỂ THẤY KẾT QUẢ) =====
user_input = input("Enter a string: ")
result = middle_character(user_input)
print("Middle character(s):", result)





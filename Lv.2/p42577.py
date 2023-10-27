def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return answer


print(solution(["119", "97674223", "1195524421"]))  # false
print(solution(["456", "789", "123"]))  # true
print(solution(["123", "1235", "567", "88", "12"]))  # false

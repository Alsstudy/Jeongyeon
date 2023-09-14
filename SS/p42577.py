def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i][0] != phone_book[j][0]:
                break
            elif phone_book[i][0] == phone_book[j][0] and phone_book[i] in phone_book[j]:
                    return False
    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["456","789", "123"]))
print(solution(["123","1235","567","88","12"]))
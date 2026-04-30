def solution(n):
    prime_number = []
    for i in range(2, n + 1):
        for num in prime_number:
            if num * num > i:
                prime_number.append(i)
                break
            if i % num == 0:
                break
        else:
            prime_number.append(i)
    
    return len(prime_number)
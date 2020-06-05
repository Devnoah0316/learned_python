# -*- coding: utf-8 -*-
'''
- 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다. 이 때 100번째 소수까지 구하시면 됩니다.

-실행예시
Length? 100
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
'''

import math

# is_prime 함수는 특정 숫자(n)이 들어왔을 때 
# 그 숫자가 소수면 True를 반환하고 아니면 False를 반환하는 함수입니다.
def is_prime(n):
		
        #에라토스테네스의 체 이용 제곱근 까지만 확인 
        limit = int(math.sqrt(n))
        for i in range(2, limit+1):
            if (n % i) == (0):
                return False
                
        
        
        return True


# prime_number_list 함수는 길이(length)가 들어왔을 때
# 그 길이만큼의 소수를 가지고 있는 리스트를 반환하는 함수입니다.
def prime_number_list(length):
        result = []
	    # 반복문을 돌면서 is_prime함수를 이용하여 True가 반환되면 result에 그 숫자를 추가하면 됩니다.
        i = 2
        count = 0
        while (count < length):
            if (is_prime(i) == True):
                result.append(i)
                count += 1
            i += 1
        return result



length = int(input('Length? '))
print(prime_number_list(length))
def compute_divisors(num):
    divisors = []
    for divisor in range(1, num+1):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors 

def sum_of_divisors(num):
    divisors = compute_divisors(num)
    divisors = sum(divisors)
    return(divisors)

def divisor_count(num):
    divisors = compute_divisors(num)
    return(len(divisors))

def get_totatives(num):
    totatives = [1]
    prime_list = []
    divisors = compute_divisors(num)
    non_prime_list = []
    for i in range(2, num):
        if i not in non_prime_list:
            prime_list.append(i)
            for j in range(i*i, num + 1, i):
                non_prime_list.append(j)       
    for totative in range(2,num):
        if totative not in divisors and totative not in non_prime_list and num % totative !=0:
            totatives.append(totative)
    return totatives

def totient(num):
    toatives = get_totatives(num)
    return(len(toatives))

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    print(compute_divisors(a))
    print(sum_of_divisors(a))
    print(divisor_count(a))
    print(get_totatives(a))
    print(totient(a))

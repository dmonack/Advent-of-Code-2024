from multiprocessing import Pool, cpu_count

# Advent of Code 2024 - Day 17 version 2
PROGRAM = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]

def main(register: int) -> list:
    global PROGRAM
    result = []
    A, B, C = register, 0, 0

    while A:
        # print(A, result)
        B = A % 8
        B ^= 3
        C = A >> B
        B ^= 5
        A >>= 3
        B ^= C
        result.append(B % 8)
        
    return result
    
# Part 1
print(main(47006051))
# 6,2,7,2,3,1,6,0,5 is correct

""" # Part 2
n = int(8**15 * 7.5)
for n in range(0o6562156761163240, 8**15, -1):
    result = main(n)
    print(oct(n), result)   
    if result == PROGRAM: 
        print(f'{n}: DONE!')
        break """
    
    
def parallel_main(n):
    result = main(n)
    if n % 10_000 == 0:
        print(oct(n), result)
    if result == PROGRAM:
        return n
    return None

if __name__ == "__main__":
    with Pool(cpu_count()) as pool:
        for n in pool.imap_unordered(parallel_main, range(0o6562156761163240, 8**15, -1)):
            if n is not None:
                print(f'{n}: DONE!')
                break
                    
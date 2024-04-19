import random
def couple_count(numbers, target):
    num_count={}
    for num in numbers:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    pairs_count = 0
    for num in numbers:
        add_till_target = target-num
        if add_till_target in num_count and (add_till_target != num or num_count[num] > 1) and num_count[add_till_target]>0 and num_count[num]>0:
            pairs_count +=1
            num_count[add_till_target]-=1
            num_count[num]-=1
    return pairs_count

def main():
    list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
    target_number = 3728
    print(f"Number of pairs:{ couple_count(list_of_numbers,target_number)}")
if __name__ == "__main__":
    main()
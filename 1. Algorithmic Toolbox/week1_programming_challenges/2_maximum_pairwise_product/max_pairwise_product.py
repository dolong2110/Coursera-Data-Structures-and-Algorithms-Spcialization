# python3


def max_pairwise_product(numbers):
    second_highest_number, highest_number = numbers[0], numbers[1]
    for number in numbers:
        if number > highest_number:
            highest_number, second_highest_number = number, highest_number
        elif number > second_highest_number:
            second_highest_number = number

    return highest_number * second_highest_number


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

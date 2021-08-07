# Bubble sort algorithm
# Very simple to understand and implement
# Performance: O(n2) - for loops inside of for loops are usually n2. Not considered to be a practical solution


def bubbleSort(dataset):
    # start with the array length and decrement each time
    # len(dataset) - 1 = start, 0 = end, -1 = step by
    for i in range(len(dataset)-1, 0, -1):
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp

        print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting state: ", list1)
    bubbleSort(list1)
    print("Final state: ", list1)


if __name__ == "__main__":
    main()

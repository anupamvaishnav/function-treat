
dataset = []
dataset_summary = {}  

def show_basic_stats(data):
    if not data:
        print("Dataset is empty!")
        return
    flat = flatten(data)
    print(f"Length: {len(flat)}")
    print(f"Sum: {sum(flat)}")
    print(f"Min: {min(flat)}")
    print(f"Max: {max(flat)}") 


def calculate_average(data):
    flat = flatten(data)
    return sum(flat) / len(flat) if flat else 0


def find_duplicates(data):
    flat = flatten(data)
    seen, dup = set(), set()
    for val in flat:
        if val in seen:
            dup.add(val)
        else:
            seen.add(val)
    return list(dup)


def unique_values(data):
    flat = flatten(data)
    return list(set(flat))


def flexible_sum(*args):
    return sum(args)


def describe_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def filter_threshold(data, threshold):
    flat = flatten(data)
    return list(filter(lambda x: x > threshold, flat))


def square_all(data):
    flat = flatten(data)
    return list(map(lambda x: x**2, flat))

def update_global_summary(data):
    global dataset_summary
    flat = flatten(data)
    dataset_summary = {
        "Total Values": len(flat),
        "Mean": calculate_average(flat)
    }


def dataset_stats(data):
    flat = flatten(data)
    if not flat:
        return None, None, None
    return min(flat), max(flat), calculate_average(flat)



def flatten(data):
    if not data:
        return []
    if isinstance(data[0], list):  
        return [x for row in data for x in row]
    return data


def display_2d(data):
    for row in data:
        print("\t".join(map(str, row)))



def sort_1d(data):
    arr = data.copy()
    arr.sort()
    print("Ascending (sort):", arr)
    arr.sort(reverse=True)
    print("Descending (sort):", arr)
    print("New sorted list (sorted):", sorted(data))


def sort_2d(data):
    print("Original:")
    display_2d(data)

    
    data.sort(key=lambda row: sum(row))
    print("\nAfter in-place sort by row sum:")
    display_2d(data)

    
    sorted_rows = sorted(data, key=lambda row: max(row))
    print("\nNew sorted list by max element in row:")
    display_2d(sorted_rows)


def main_menu():
    global dataset

    while True:
        print("\n===== Functional Treat =====")
        print("1. Enter Data")
        print("2. Analyze Data (Built-in Functions)")
        print("3. Transform Data (UDFs)")
        print("4. Advanced Functions (*args, **kwargs, recursion, lambda)")
        print("5. Sorting Options")
        print("6. Show Global Summary")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sub = input("Enter data type (1D or 2D): ").strip().upper()
            if sub == "1D":
                dataset = list(map(int, input("Enter numbers separated by space: ").split()))
            else:
                rows = int(input("Enter number of rows: "))
                dataset = []
                for i in range(rows):
                    row = list(map(int, input(f"Row {i+1}: ").split()))
                    dataset.append(row)
            print("Dataset saved!")

        elif choice == "2":
            print(show_basic_stats.__doc__)
            show_basic_stats(dataset)

        elif choice == "3":
            print(calculate_average.__doc__)
            print("Average:", calculate_average(dataset))
            print(find_duplicates.__doc__)
            print("Duplicates:", find_duplicates(dataset))
            print(unique_values.__doc__)
            print("Unique Values:", unique_values(dataset))

        elif choice == "4":
            print(flexible_sum.__doc__)
            print("Sum (1,2,3,4):", flexible_sum(1, 2, 3, 4))

            print(describe_data.__doc__)
            describe_data(Name="Dataset1", Size=len(flatten(dataset)))

            print(factorial.__doc__)
            print("Factorial(5):", factorial(5))

            print(fibonacci.__doc__)
            print("Fibonacci(6):", [fibonacci(i) for i in range(6)])

            print(filter_threshold.__doc__)
            print("Filtered (>5):", filter_threshold(dataset, 5))

            print(square_all.__doc__)
            print("Squared:", square_all(dataset))

        elif choice == "5":
            if isinstance(dataset[0], list):  
                sort_2d(dataset)
            else:
                sort_1d(dataset)

        elif choice == "6":
            update_global_summary(dataset)
            print("Global Summary:", dataset_summary)

        elif choice == "7":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")



if __name__ == "__main__":
    main_menu()

def main():
    print("Select the algorithm you want to run:")
    print("1. Dijkstra")
    print("2. Karger Min Cut")
    print("3. Kosaraju")
    print("4. Quick Sort")

    algorithms = {
        '1': ('dijkstra', 'run'),
        '2': ('karger_min_cut', 'run'),
        '3': ('kosaraju', 'run'),
        '4': ('quick_sort', 'run')
    }

    choice = input("Enter the number of the algorithm: ")

    if choice in algorithms:
        module_name, function_name = algorithms[choice]
        module = __import__(module_name)
        function = getattr(module, function_name)
        function()
    else:
        print("Invalid option. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()

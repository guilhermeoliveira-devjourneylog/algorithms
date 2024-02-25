def main():
    print("Select the algorithm you want to run:")
    print("1. Dijkstra")
    print("2. Karger Min Cut")
    print("3. Kosaraju")
    print("4. Quick Sort")
    print("5. Median Maintenance")
    print("6. Two Sum")
    print("7. Greedy")
    print("8. Prims")
    print("9. Kruskal")
    print("10. Kruskal Hash")
    print("11. Greedy Huffman")
    print("12. Max Weigh Independent Set Path Graph")
    print("13. Knapsack")
    print("14. Knapsack Big Data")
    
    algorithms = {
        '1': ('dijkstra', 'run'),
        '2': ('karger_min_cut', 'run'),
        '3': ('kosaraju', 'run'),
        '4': ('quick_sort', 'run'),
        '5': ('median_maintenance', 'run'),
        '6': ('two_sum', 'run'),
        '7': ('greedy', 'run'),
        '8': ('prims', 'run'),
        '9': ('kruskal', 'run'),
        '10': ('kruskal_hash', 'run'),
        '11': ('greedy_huffman', 'run'),
        '12': ('max_weight_independent_set_path_graph', 'run'),
        '13': ('knapsack', 'run'),  
        '14': ('knapsack_big_data', 'run')
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

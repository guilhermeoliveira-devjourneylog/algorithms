def main():
    print("Select the algorithm you want to run:")
    print("1. Dijkstra")
    print("2. Karger Min Cut")
    print("3. Kosaraju")
    print("4. Quick Sort")

    choice = input("Enter the number of the algorithm: ")

    if choice == '1':
        import dijkstra
        dijkstra.run()
    elif choice == '2':
        import karger_min_cut
        karger_min_cut.run()
    elif choice == '3':
        import kosaraju
        kosaraju.run()
    elif choice == '4':
        import quick_sort
        quick_sort.run()
    else:
        print("Invalid option. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()

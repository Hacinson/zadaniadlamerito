num_lists = 4
main_list = []

for i in range(num_lists):
    new_list = [i] * 3
    main_list.append(new_list)

for i, lst in enumerate(main_list):
    print(f"List {i + 1}: {lst}")

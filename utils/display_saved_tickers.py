def display_saved_tickers(tickers):
    print("\nSaved tickers:\n")
    for i in range(len(tickers)):
        print(f"{i} - {tickers[i][0]}")
    
    index = input("\nEnter number: ").strip()

    if not index.isdigit():
        return -1

    index = int(index)
    if index > len(tickers) - 1:
        return -1
    return index

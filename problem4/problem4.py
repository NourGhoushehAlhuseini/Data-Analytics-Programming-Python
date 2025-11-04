problem = "problem4"
student_name = "nour ghousheh alhuseini"
student_number = "t0326796"

# Part A
def make_change(coin_vals, change):
    # initialize DP table to store minimum number of coins for each amount
    min_coins = [float('inf')] * (change + 1)
    min_coins[0] = 0  # Base case: no coins required for zero amount

    # fill the DP table
    for amount in range(1, change + 1):
        for coin in coin_vals:
            if coin <= amount:
                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    return min_coins[change]

# Part B
def make_change2(coin_vals, change):
    # DP table and coin tracker to find optimal solution
    min_coins = [float('inf')] * (change + 1)
    coin_tracker = [-1] * (change + 1)
    min_coins[0] = 0

    for amount in range(1, change + 1):
        for coin in coin_vals:
            if coin <= amount and min_coins[amount - coin] + 1 < min_coins[amount]:
                min_coins[amount] = min_coins[amount - coin] + 1
                coin_tracker[amount] = coin

    # reconstruct optimal coin set clearly
    optimal_coins = []
    current_amount = change
    while current_amount > 0:
        coin = coin_tracker[current_amount]
        if coin == -1:
            break
        optimal_coins.append(coin)
        current_amount -= coin

    return optimal_coins

# Part C
def word_break(dictionary, string_to_segment):
    dictionary_set = set(dictionary)
    dp = [False] * (len(string_to_segment) + 1)
    dp[0] = True  # Base case
    previous_index = [-1] * (len(string_to_segment) + 1)

    # Identify possible segmentations with DP
    for i in range(1, len(string_to_segment) + 1):
        for j in range(i):
            if dp[j] and string_to_segment[j:i] in dictionary_set:
                dp[i] = True
                previous_index[i] = j
                break

    # method to clearly reconstruct segments 
    if dp[len(string_to_segment)]:
        segments = []
        idx = len(string_to_segment)
        while idx > 0:
            segments.append(string_to_segment[previous_index[idx]:idx])
            idx = previous_index[idx]
        segments.reverse()
        return ' '.join(segments)
    else:
        return "Cannot be segmented."


if __name__ == "__main__":
   

    # inputs Part A
    coins_input = input("Enter coin denominations (comma-separated, e.g., 1,5,8): ")
    coins = list(map(int, coins_input.strip().split(',')))
    change_amount = int(input("Enter the amount of change: "))
    print(f"Minimum coins required: {make_change(coins, change_amount)}")

    # inputs Part B
    optimal_set = make_change2(coins, change_amount)
    print(f"Optimal set of coins: {optimal_set if optimal_set else 'No valid coin set found.'}\n")

    # inputs Part C
    dictionary_input = input("Enter dictionary words (comma-separated): ")
    dictionary = dictionary_input.strip().split(',')
    string_to_segment = input("Enter the string to segment: ")
    segmented_result = word_break(dictionary, string_to_segment)
    print(f"Segmented result: {segmented_result}")

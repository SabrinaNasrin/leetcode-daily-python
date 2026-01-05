def maximum_wealth(accounts):
    max_wealth = 0
    for customer in accounts:
        wealth = sum(customer)
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth

# Test
print(maximum_wealth([[1,2,3],[3,2,1]]))  # 6
print(maximum_wealth([[2,8,7],[7,1,3],[1,9,5]]))  # 17

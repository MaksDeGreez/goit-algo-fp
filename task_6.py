def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if budget >= details["cost"]:
            selected_items.append(item)
            total_calories += details["calories"]
            budget -= details["cost"]

    return selected_items, total_calories

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    for item, details in items.items():
        item_cost, item_calories = details["cost"], details["calories"]

        for current_budget in range(budget, item_cost - 1, -1):
            if dp[current_budget - item_cost] + item_calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - item_cost] + item_calories
                selected_items[current_budget] = selected_items[current_budget - item_cost] + [item]

    return selected_items[budget], dp[budget]

def main():
    items = {
        "pizza": { "cost": 50, "calories": 300 },
        "hamburger": { "cost": 40, "calories": 250 },
        "hot-dog": { "cost": 30, "calories": 200 },
        "pepsi": { "cost": 10, "calories": 100 },
        "cola": { "cost": 15, "calories": 220 },
        "potato": { "cost": 25, "calories": 350 }
    }
    budget = 100

    greedy_selection, greedy_calories = greedy_algorithm(items, budget)
    print("Greedy Algorithm:")
    print("Selected items:", greedy_selection)
    print("Total calories:", greedy_calories)

    dp_selection, dp_calories = dynamic_programming(items, budget)
    print("\nDynamic Programming:")
    print("Selected items:", dp_selection)
    print("Total calories:", dp_calories)

if __name__ == "__main__":
    main()

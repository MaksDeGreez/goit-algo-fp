import random

def monte_carlo_dice_simulation(num_simulations):
    sum_counts = { i: 0 for i in range(2, 13) }

    for _ in range(num_simulations):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        dice_sum = roll1 + roll2
        sum_counts[dice_sum] += 1

    probabilities = { s: count / num_simulations * 100 for s, count in sum_counts.items() }
    return probabilities

def main():
    theoretical_probabilities = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78
    }

    num_simulations = 100000
    monte_carlo_probabilities = monte_carlo_dice_simulation(num_simulations)

    print("Sum\tMonte Carlo (%)\tTheoretical (%)\tDifference")
    for dice_sum in range(2, 13):
        monte_carlo_value = monte_carlo_probabilities.get(dice_sum, 0)
        theoretical_value = theoretical_probabilities.get(dice_sum, 0)
        difference = monte_carlo_value - theoretical_value
        print(f"{dice_sum}\t{monte_carlo_value:.2f}\t\t{theoretical_value:.2f}\t\t{difference:.2f}")

if __name__ == "__main__":
    main()

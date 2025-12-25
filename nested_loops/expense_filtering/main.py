
# Travel expenses for multiple trips
travel_costs = [
    [500, 150, 100, 50],   # Trip 1
    [200, 300, 120, 80],   # Trip 2
    [180, 220, 130, 170],  # Trip 3
    [600, 250, 200, 90],   # Trip 4
    [300, 180, 150, 70],   # Trip 5
    [400, 320, 110, 100],  # Trip 6
    [550, 270, 180, 60],   # Trip 7
    [250, 190, 140, 120],  # Trip 8
    [700, 350, 210, 110],  # Trip 9
    [450, 230, 160, 95],   # Trip 10
    [320, 280, 190, 85],   # Trip 11
    [580, 260, 175, 75]    # Trip 12
]

# List to store processed expenses
processed_expenses = []

i = 0
while i < len(travel_costs):
    j = 0
    trip_expenses = []
    
    while j < len(travel_costs[i]):
        cost = travel_costs[i][j]
        if cost <= 100:
            trip_expenses.append('Cheap')
        else:
            trip_expenses.append(cost)
        j += 1
    
    processed_expenses.append(trip_expenses)
    i += 1

# Testing
print('Processed Travel Expenses:', processed_expenses)

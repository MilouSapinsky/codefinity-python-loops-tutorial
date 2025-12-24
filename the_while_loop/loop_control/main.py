# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'South Korea', 'Barcelona', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Greece', 'Netherlands', 'Finland', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List to hold selected countries
selected = []
i = 0
counter = 0

while i < len(countries):
    if countries[i].startswith("S"):
        selected.append(countries[i])
        i += 1
        if len(selected) > 3:
            continue
    else:
        counter += 1
    i += 1

# Testing
print('First three countries starting with "S":', selected)
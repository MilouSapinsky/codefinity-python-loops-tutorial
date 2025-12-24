# List of countries
countries = ['Wales', 'Denmark', 'Belgium', 'South Korea', 'Barcelona', 'South Africa', 'Indonesia','Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Tokyo', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Paris', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Liverpool', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'New York', 'China', 'Munchen', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List of countries you agreed to visit
travel_index_list = []

for country in range(len(countries)):
    if country % 2 == 0:
        travel_index_list.append(country)

for i in range(len(travel_index_list)):
    your_travel_list = travel_index_list[i]

# Testing
print(your_travel_list)
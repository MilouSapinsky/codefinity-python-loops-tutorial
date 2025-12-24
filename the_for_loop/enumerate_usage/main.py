# Full list of countries you are considering for travel
countries = ['Wales', 'Denmark', 'Belgium', 'South Korea', 'Barcelona', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Tokyo', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Paris', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Liverpool', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'New York', 'China', 'Munchen', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# Initialize an empty list for rankings
travel_rankings = []


# Use enumerate to label each destination
for index, value in enumerate(countries, start=1):
    travel_index = "Destination " + str(index) + ": " + value
    travel_rankings.append(travel_index)

# Testing
print("Travel destination rankings:", travel_rankings)
# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'South Korea', 'Barcelona', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Greece', 'Netherlands', 'Finland', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# Counter variable
short_name_count = 0

while short_name_count < len(countries): 
    if len(countries[short_name_count]) < 7:   
        short_name_count += 1
    print('Number of short country names:', short_name_count)                       

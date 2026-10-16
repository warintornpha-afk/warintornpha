"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():

    temp = [31,30,29,33,32,31,30]
    return(temp)

def analyze_temp(temp_list):
    average = sum(temp_list)/7
    high = max(temp_list)
    low = min(temp_list)

    return (average , high , low )
def display_analysis(avg, high , low ):

    print("Temperatures Analysis for thr Week:")
    print("Average: %.1f C" avg)
    print("Highest:  %.1f C" high)
    print("Lowset:  %.1f C" low)

temp = get_temperatures()
print(temp)
result = analyze_temp(temp)
display_analysis(result[0],result[1],result[2])
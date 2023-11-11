# 5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.

# questions
# how do I give a list a heading? something with len or r?
from weather import convert_date, find_min, find_max, calculate_mean, format_temperature, convert_f_to_c

def generate_summary(weather_data):
    summary = ""

    list_min = []
    list_max = []

    for data in weather_data:
        list_min.append (data[1])
        list_max.append (data[2])
    
    total_day = len(weather_data)
    summary+=f"{total_day} Day Overview\n"
    
    min_temp = find_min(list_min)
    min_temp_value = format_temperature(convert_f_to_c(min_temp[0]))
    min_temp_index = min_temp[1]
    min_temp_date = convert_date(weather_data[min_temp_index][0])

    summary+=f"  The lowest temperature will be {min_temp_value}, and will occur on {min_temp_date}.\n"

    max_temp = find_max(list_max)
    max_temp_value = format_temperature(convert_f_to_c(max_temp[0]))
    max_temp_index = max_temp[1]
    max_temp_date = convert_date(weather_data[max_temp_index][0]) 

    summary+=f"  The highest temperature will be {max_temp_value}, and will occur on {max_temp_date}.\n"

    min_average = format_temperature(convert_f_to_c(calculate_mean (list_min)))
    max_average = format_temperature(convert_f_to_c(calculate_mean(list_max)))
    
    summary+=f"  The average low this week is {min_average}.\n"
    summary+=f"  The average high this week is {max_average}.\n"

    print(summary)    
    return summary
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

generate_summary([
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62]
        ])
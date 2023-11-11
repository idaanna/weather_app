import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

# TEST 1
def convert_date(iso_string): 
    date_obj = datetime.fromisoformat(iso_string)
    human_readable_date = date_obj.strftime("%A %d %B %Y")
    return human_readable_date

    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: "2021-07-06T12:34:56Z"
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass

# TEST 2
# def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass

def convert_f_to_c(temp_in_farenheit):
    temp_c = (float(temp_in_farenheit) -32)*5/9
    return round(temp_c,1)

# TEST 3
def calculate_mean(weather_data):
    total_sum = 0
    for number in weather_data:
        total_sum += float(number)

    result = len(weather_data)
    calculate_mean = total_sum/result
    return float(calculate_mean)

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # pass

# TEST 3
def load_data_from_csv(csv_file):
    with open(csv_file, encoding="utf-8") as my_file:
        reader = csv.reader(my_file)
        next(reader)
        my_list = []
        for data in reader:
            if len(data) == 0:
                continue
            date = data[0]
            my_min = int(data[1])
            my_max = int(data[2])
            my_list.append ([date, my_min, my_max])
            
            # print(data[0])
        return my_list 

    

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

# TEST 4
# def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    # for min in weather_data:
    # total_sum += float(number)

    # result = len(weather_data)
    # calculate_min = 
    # return float(calculate_mean)


    # return float(min(weather_data))

    # google how to get the index for an item in a list python
    # pass

def find_min(weather_data):
    if weather_data == []:
        return ()
    min_value = min(weather_data)
    index_list = []
    for index,value in enumerate(weather_data):
     if value == min_value:
      index_list.append(index)
    return float((min_value)), max(index_list)

# TEST 5
# def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
def find_max(weather_data):
    if weather_data == []:
        return ()
    max_value = max(weather_data)
    index_list = []
    for index,value in enumerate(weather_data):
     if value == max_value:
      index_list.append(index)
    return float((max_value)), max(index_list)

# TEST 6 
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

    return summary

def generate_daily_summary(weather_data):
    daily_summary = ""

    for data in weather_data:
    # something like this?
        date = convert_date(data[0])
        temp_min = format_temperature(convert_f_to_c(data[1]))
        temp_max = format_temperature(convert_f_to_c(data[2]))
        daily_summary+=(f"---- {date} ----\n  Minimum Temperature: {temp_min}\n  Maximum Temperature: {temp_max}\n\n")


    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    return daily_summary
    
    

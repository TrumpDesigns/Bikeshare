import time
import pandas as pd
import numpy as np

CITY_DATA = { 1: 'chicago.csv',
              2: 'new_york_city.csv',
              3: 'washington.csv' 
              }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
city= 
while true:
    try: int(input('PLEASE ENTER YOUR CITY OF INTEREST 1)Chicago, 2)New York City, 3) Washington  1  2 or 3?'))
    break
   except ValueError : 
print('WRONG INPUT!! TRY AGAIN')
    finally: print('INPUT RECEIVED')
    
    

    
    


    # TO DO: get user input for month (all, january, february, ... , june)
month= while true:
    try: input('Enter The Month You Want To Get Data For (all, january, february, ... , june):').lower
    break
   except ValueError : 
print('WRONG INPUT!! TRY AGAIN')
    finally: print('INPUT RECEIVED')
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
day= while true:
    try: input('Enter The day Of the Week You Want To Get Data For (all, monday, tuesday, ... sunday):').lower
    break
   except ValueError : 
print('WRONG INPUT!! TRY AGAIN')
    finally: print('INPUT RECEIVED')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
Common_Month=df['month'].mode()[0]
print('Most Common Month:', Common_Month)

    # TO DO: display the most common day of week

Common_Weekday=df['day_of_week'].mode()[0]
print('Most Common Week Day:', Common_Weekday)
    # TO DO: display the most common start hour
 df['Hour'] = df['Start Time'].dt.hour
 Common_hour=df['Hour'].mode()[0]
 print('Most Common Hour:', Common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

Common_Start_Stat=df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
print(Common_Start_Stat)
Common_End_Stat=df['End Station'].mode()[0]
print(Common_End_Stat)
    # TO DO: display most frequent combination of start station and end station trip
Most_common =( df['Start Station'] + '  AND  ' + df['Start Station'] ).mode()[0]
print(Most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
total_travel_time= df['Trip Duration'].sum()
total_travel_timeMIN= total_travel_time/60
print('Total Travel Time', total_travel_timeMIN.round(),'Minutes' )

    # TO DO: display mean travel time
avg_travel_time= df['Trip Duration'].avg()
avg_travel_timeMIN=avg_travel_time/60
print('Average Travel Time', avg_travel_timeMIN.round(), 'Minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
user_type= df['User Type'].value_counts()
print('User Types',user_type)

    # TO DO: Display counts of gender
gender= df['Gender'].value_counts()
print('Gender Distribution:',gender)


    # TO DO: Display earliest, most recent, and most common year of birth
Year=df['Birth Year']
earliest=df['Birth Year'].min(0)
most_recent= df['Birth Year'].mean()
most_Common=df['Birth Year'].mode()[0]

print('Earliest Year OF Birth:', earliest)
print('Most Recent Year OF Birth:', most_recent)
print('Most Common Year OF Birth:', most_Common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    #https://realpython.com/run-python-scripts/#scripts-vs-modules
    #https://www.w3schools.com/python/python_dictionaries_access.asp
    #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html?highlight=mean#pandas.DataFrame.mean
    #https://stackoverflow.com/questions/55719762/how-to-calculate-mode-over-two-columns-in-a-python-dataframe
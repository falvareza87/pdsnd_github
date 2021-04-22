import time
import pandas as pd
import numpy as np
from scipy import stats


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS_LIST = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city = input('Which city would you like to look at? chicago, new york city or washington?: ').lower()
        while city not in CITY_DATA:
            print('Please enter again the city, please check your spelling. ')
            city = input('Which city would you like to look at? chicago, new york city or washington?: ').lower()

        print('Your selection is: ', city)


        # get user input for month
        month = input('Which month would you like to look at from january to june? Or all of them?: ').lower()
        while month not in MONTH_LIST:
            print('Please enter again the month, please check your spelling. ')
            month = input('Which month would you like to look at from jan to jun? Or all of them ?: ').lower()

        print('Your selection is: ', month)

    # get user input for day of week
        day = input('Which day you would like to look at? Or simply all of them?: ').lower()
        while day not in DAYS_LIST:
            print('Please enter again the day, please check your spelling. ')
            day = input('Which day you would like to look at? Or all of them?: ').lower()

        print('Your selection is: ', day)

        return city, month, day
    except Exception as e:
        print('There seems to be an error with your inputs: {}'.format(e))
    print('-'*40)




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
    try:
        df = pd.read_csv(CITY_DATA[city])

        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

        # filter by month if applicable
        if month != 'all':
        # use the index of the months list to get the corresponding int
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = MONTH_LIST.index(month) + 1

            # filter by month to create the new dataframe
            df = df[df['month'] == month]

    # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]
        return df
    except Exception as e:
        print('The file couldn\'t be loaded, due to an error occurred: {}'.format(e))

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    try:
        common_month_num = df['Start Time'].dt.month.mode()[0]
        common_month = MONTH_LIST[common_month_num-1].title()
        print('Most common month is: ', common_month)
    except Exception as e:
        print('The most common month couldn\'t be calculated, due to an error occurred: {}'.format(e))

    # display the most common day of week
    try:
        common_day_of_week = df['day_of_week'].mode()[0]
        print('Most common weekday is', common_day_of_week)
    except Exception as e:
        print('The most common day of week couldn\'t be calculated, due to an error occurred: {}'.format(e))


    # display the most common start hour
    try:
        common_start_hour = df['hour'].mode()[0]
        print('Most common starting hour is:', common_start_hour)
    except Exception as e:
        print('The most common start hour couldn\'t be calculated,due to an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        common_start_station = df['Start Station'].mode()[0]
        print('The most common start station is: ', common_start_station)
    except Exception as e:
        print('The most used start station couldn\'t be calculated, due to an error occurred: {}'.format(e))

    #display most commonly used end station
    try:
        common_end_station = df['End Station'].mode()[0]
        print('The most popular end station is:', common_end_station)
    except Exception as e:
        print('The most used end station couldn\'t be calculated, due to an error occurred: {}'.format(e))

    # display most frequent combination of start station and end station trip
    try:
        common_trip = df.loc[:, 'Start Station':'End Station'].mode()[0:]
        print('the most popular trip is: ', common_trip)
    except Exception as e:
        print('The most frequent combination of start station and end station couldn\'t be calculated , as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    try:
        df['Travel Time'] = df['End Time'] - df['Start Time']
        total_travel_time = df['Travel Time'].sum()
        print('the total travel time was: ', total_travel_time)
    except Exeption as e:
        print('The total travel time of users couldn\'t be calculated, due to an error occurred: {}'.format(e))
    # display mean travel time
    try:
        total_mean = df['Travel Time'].mean()
        print('the mean travel time is: ', total_mean)
    except Exception as e:
        print('The mean travel time of users couldn\'t be calculated, due to an error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print('Amount and type of users are:\n', df['User Type'].value_counts())
    except Execption as e:
        print('Type of users couldn\'t be calculated, due to an error occurred: {}'.format(e))
    # Display counts of gender
    try:
        print('Amount and gender of users are:\n',df['Gender'].value_counts())
    except Exception as e:
        print('Amount and gender of users couldn\'t be calculated, due to an error occurred: {}'.format(e))
     # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('Oldest customer was born in:', int(earliest_year))
        print('Youngest customer: was born in:', int(most_recent_year))
        print('Majority of customers are born in:', int(most_common_year))
    except Exception as e:
        print('Customer\'s demographics couldn\'t be calculated, due to an error occurred: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Displays user request for viewing raw data.
    Arg - df
    """
    #it will prevent that columns collapse in the output
    pd.set_option('display.max_columns',200)

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?: ").lower()
    start_loc = 0
    while True:
        if view_data == 'no':
            break
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

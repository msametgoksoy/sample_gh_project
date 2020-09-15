import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#get_filter function is using for read data from clients. Clients can choose city,month and day with this function
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
    while True:
        city=input('\nChoose the city in "Chicago", "New York City", "Washington"\n').lower()
        if city in ('chicago', 'new york city', 'washington'):
            print('\nSelected city is {}'.format(city))
            break
        else:
            print('\nIncorrect entry!!!Please choose the city in "Chicago", "New York City", "Washington"')

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input('\nChoose the month in (January, February, March, April, May, June) for all months please type all\n').lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('\nSelected month is {}'.format(month))
            break
        else:
            print('\nIncorrect entry!!!Please choose the month in (January, February, March, April, May, June) for all months please type all\n')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('\nChoose the day in (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) for all days please type all\n').lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('\nSelected day is {}'.format(day))
            break
        else:
            print('\nIncorrect entry!!!Please choose the day in (monday, tuesday, wednesday, thursday, friday, saturday, sunday) for all days please type all\n')


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
    df['hour'] = df['Start Time'].dt.hour
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

    # display the most common month
    most_com_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Common Month:', months[most_com_month - 1])
    
    # display the most common day of week
    most_com_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', most_com_day)

    # display the most common start hour
    most_com_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', most_com_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_com_start_station = df['Start Station'].mode()[0]
    print('Most popular start station is:',most_com_start_station)
    # display most commonly used end station
    most_com_end_station = df['End Station'].mode()[0]
    print('Most popular end station is  :',most_com_end_station)


    # display most frequent combination of start station and end station trip
    most_freq_station_comb=df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of start station and end station trip is:',most_freq_station_comb)
    
                              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_trav_time=df['Trip Duration'].sum()
    print('Total travel time is {} seconds'.format(tot_trav_time))


    # display mean travel time
    mean_trav_time=df['Trip Duration'].mean()
    print('Mean travel time is {} seconds'.format(mean_trav_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types are:\n{}'.format(user_types))


    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of gender:\n{}'.format(gender_counts))
    except KeyError:
        print('\n There isn\'t any gender info for this city')


    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('\nEarliest year of birth is:{}\nMost recent year of birth is:{}\nMost common year of birth is:{}'.format(earliest_year, most_recent, most_common))
    except:
        print('\n There isn\'t any birth year info for this city')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    count=0
    while True:
        ask_user=input('\nwould you like to view 5 row of raw data?Please type "yes" or "no"\n').lower()
        if ask_user == 'yes':
            count +=1
            print(df.iloc[(count -1)*5:count*5])
        elif ask_user == 'no':
            break
        else:
            print('\n incorrect entry!!!Please type "yes" or "no"\n')
        
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

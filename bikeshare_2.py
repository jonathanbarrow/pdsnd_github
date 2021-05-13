import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


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
    while True:
        city = input('Enter the name of city, Chicago, New York City, or Washington:  ').lower()
        if city in cities:
            break
            
    while True:
        month = input('Enter month to filter by, or all to apply no filter:  ').lower()
        if month in months:
            break
            
    while True:
        day = input('Enter day of the week to filter by, or all to apply no filter: ').lower()
        if day in days:
            break
   
   
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
            
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print("The most popular month: ", popular_month)
    print("The most popular day is: ", popular_day_of_week)
    print("The most popular hour is: ", popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station', 'End Station']).size().nlargest(1)

    print("The most popular start station: ", popular_start_station)
    print("the most popular end station: ", popular_end_station)
    print("The most popular combination: ", popular_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    count = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()

    print("The Total travel time: ", count)
    print('The Average travel time: ', mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    
    start_time = time.time()
    
    if 'Gender' in df.columns and 'Birth Year' in df.columns:
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print(gender)
        print("Oldest rider birth year: ", earliest)
        print("Youngest rider birth year: ", most_recent)
        print("Most common birth year: ", common)

    print(user_types)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def view_data(df):
    view_data1 = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    end_loc = 5
    while view_data1 == "yes":
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc += 5
        view_data1 = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

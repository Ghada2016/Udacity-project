#import libraries 
import time
import pandas as pd
import numpy as np

#Dictionary of the data
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Month and week_days lists
months = ['january', 'february', 'march', 'april', 'may', 'june']
week_days = ['monday', 'tuesday', 'wednsday', 'thursday', 'friday', 'saturday', 'sunday']

# get_filters function
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Would you like to see data for Chicago, New York, or Washington? ").lower()
            #check the valiation input
            if city in CITY_DATA:
                print("Ok, you chose {} city".format(city))
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print("Sorry you should enter one of the following cities : Chicago, New York, or Washington ") 

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Would you like to filter the data by month, or not at all? ').lower()
            #check the valiation of input
            if month in months or month =='all':
                print("You chose {}".format(month))
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print("Please write your preferred month from January to June or write all for all months, Thank you ")
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Would you like to filter the data by day, or not at all? ').lower()
            #check the valiation of input
            if day in week_days or day == 'all':
                print("You chose {}".format(day))
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print("Please write your preferred day or write all for all days, Thank you ")
                  
    print('-'*40)
    return city, month, day

#load_data function
def load_data(city, month, day):
    #load data into dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

#time_stats function
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]

    # display the most common day of week
    common_day = df['day'].mode()[0]

    # display the most common start hour
    common_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#station_stats function
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    common_end_station = df['End Station']

    # display most frequent combination of start station and end station trip
    common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
#trip_duration_stats function
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_Trip_duration = df['Trip Duration'].sum() 

    # display mean travel time
    mean_Trip_duration = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
#user_stats function
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    # Display counts of gender
    if 'Gender' in df.columns:
        Gender_count = df['Gender'].value_counts()
    else:
        print('Sorry, Gender data is not avaliable in this dataset')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max() 
        most_common_birth_year = df['Birth Year'].mode()
    else:
        print('Sorry, Birth-day data is not avaliable in this dataset')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
#Main function
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


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        city= input('\n Please choose a city you would like to explore data about: chicago, new york city, washington\n')
        city= city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Invalid input. Please enter a valid city from the options given.')
            

    # get user input for month (all, january, february, ... , june)
    while True:
        month= input("\n What month would you like to explore data for: january, february, march, april, may, june? Type'all' for no month filter \n")
        month= month.lower()
        if month in ['january', 'february', 'march', 'april', 'june', 'all']:
            break
        else:
            print('Invalid input.Please enter a valid month from the options given.')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input("\n What day would you like to explore data for: monday, tuesday, wednesday, thursday, friday, saturday, sunday? Type 'all' for day filter\n")
        day= day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            break
        else:
            print('Invalid input.Please enter a valid day from the options given')
    
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
   # load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])   
    
   # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
   # extract month and day of week from Start Time to create new columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable 
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june','july','augest','september','october','november','december']
       month = months.index(month) + 1
    
     # filter by month to create the new dataframe
       df = df[df['month'] == month]
    
     # filter by day of week if applicable
       if day != 'all':
    
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday']  
        
        
     # filter by day of the week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
              
        return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month= df['month'].mode()[0]
    print('the most common month is',common_month)
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week: ', popular_day)


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular start hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    print("Most Start Station: ", pop_start_station)

    # display most commonly used end station
    pop_end_startion = df['End Station'].mode()[0]
    print("Most Popular End Station: ", pop_end_startion)

    # display most frequent combination of start station and end station trip
    group_combination = df.groupby(['Start Station', 'End Station'])
    frequent_combination = group_combination.size().nlargest(1)
    print('The most frequent combination of start station and end station trip:\n', frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ' ,total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ' , mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats: ')
    print(df['User Type'].value_counts())
    if city != 'washington':

    # Display counts of gender
    
       print ('Gender Stats: ')
       print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    
       earliest= int(df['Birth Year'].min())
       print ("\n The earliest userwas born in year", earliest)
       most_recent = int(df['Birth Year'].max())
       print("\n The most recent user as born in year", most_recent)
       most_common = int(df['Birth Year'].mode()[0])
       print("\n The most common date of birth among our users is", most_common)
    else:
        print('Sorry,this information is not available for the city of Washington.')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

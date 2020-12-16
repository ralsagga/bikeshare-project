import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Which city would you like to explore new york city, chicago or washington? \n ").lower().strip()
    while city not in ('new york city', 'chicago', 'washington'):
        city = input("invalid city please enter a valid city \n ").lower().strip()

    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("Which month would you like to filter january, february, march, april, may, june or 'all' \n").lower().strip()
    while month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        month = input("invalid month please enter a valid month \n").lower().strip()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input(
        " which day would you like to filter sunday, monday, tuesday, wednesday, thursday, friday, Saturday or all.\n").lower().strip()
    while day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        day = input("invalid day please enter a valid day \n").lower().strip()

    print('-' * 40)
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
    df['End Time'] = pd.to_datetime(df['End Time'])



    # filter by month 
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =months.index(month) + 1
    
    
        df = df[df['month'] == month]

    # filter by day of week 
    if day != 'all':
       
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # TO DO: display the most common month
    print("Most common month is ", df['month'].mode()[0])

   # TO DO: display the most common day of week
    print("Most common day of week  is ", df['day_of_week'].mode()[0])

     # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most common hour is ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly start station : ", df['Start Station'].mode()[0])

 # TO DO: display most commonly used end station
    print("Most commonly end station:", df['End Station'].mode()[0])

  # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("Most start station and end stationis: ", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

# TO DO: display total travel time
    print("Total travel time:", df['Trip Duration'].sum())

   # TO DO: display mean travel time
    print("Total mean travel time: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

  
# TO DO: Display counts of user types
    print("Types of users",df['User Type'].value_counts())
    
      # TO DO: Display counts of gender
    try:
         print("Gender Types:",df["Gender"].value_counts())
    except:
        print("no gender types")
      
        # TO DO: Display earliest, most recent, and most common year of birth
    try:
         print("Earliest Year:", df["Birth Year"].min())
         print("recent year: ",df['Birth Year'].max())
         print("common year",df['Birth Year'].mode()[0])
    except:
         print("no birth details")
   
  
  
       
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
     
     

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        x = 0
        raw_data = input("would you like to see 5 lines of raw data?"
                    "(Yes or No): \n").lower().strip()
        while raw_data == 'yes':
            print(df.iloc[x:x + 5])
            x += 5
            raw_data = input("would you like to see 5 lines of raw data?"
                    "(Yes or No): \n")
            print('-'*40)

                             
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()




# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 04:09:32 2021

@author: Hadir Kamel
"""
import time
import pandas as pd
#import numpy as np
#import datetime as dt

def get_month():
        """ to get month from user"""
        
        while True:
            try:
                month = input("Which month would like to explore: Jan, Feb, March, April, May or June? (letter case doesn't matter)\n").lower().strip()
                if month in ['jan', 'feb', 'march', 'april', 'may', 'june']:
                    break
            except:
                print("This is not a valid month!\nPlease Try again")
        return month

def get_day():
        """ to get day from user"""
        while True:
            try:
                day = input("Which day would like to explore: Sunday, Monday, Tuesday, Wednesday, Thrusday, Friday or Saturday? (letter case doesn't matter)\n").lower().strip()
                if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday']:
                    break
            except:
                print("This is not a valid day!\nPlease Try again")
        return day
def get_city():
    while True:
            try:
                city = input("Which city do you want to explore: Chicago, New York or Washington? \n").lower().strip()
                if city in ['chicago', 'new york', 'washington']:
                    break
            except:
                print("This is not a valid city!\nPlease Try again")
    return city

def get_filt():
    while True:
        try:
            filt = input("Which filter would you like to use: month, day, both or none of them? for the last option enter 'none'\n").lower().strip()
            if filt in ['month', 'day', 'both', 'none']:
                break
        except:
            print("This is not a valid filter!\nPlease Try again")
    return filt
def get_filters():
    """
    # func1 to get filter from user
    Returns
    -------
    city : TYPE
        DESCRIPTION.
    month : TYPE
        DESCRIPTION.
    day : TYPE
        DESCRIPTION.

    """
    print('Let\'s explore some statistics about the BikeShare System!')
    
    # get city from user
    city = get_city()
    
    # get filter from user
    filt = get_filt()
    if filt == 'month':
        day = 'all'
        month = get_month()
    elif filt == 'day':
        month = 'all'  
        day = get_day()
    elif filt == 'both':
        month = get_month()
        day = get_day()
    elif filt == 'none':
        month = 'all'
        day = 'all'
    return city, month, day


def load_data(city, month, day):
    """
    # func 2 to load data from csv files
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

    # load data file into a dataframe
    # convert the Start Time column to datetime
    df = pd.read_csv(CITY_DATA[city])
    #print(df)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        filt = (df['month'] == month)
        df = df[filt]
        #print(df)

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        filt = (df['day_of_week'] == day.title())
        df = df[filt]
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    return df


def pop_time(d_frame, month, day):
    """
    func 3 to calculate the most common month, day of week and hour of day (most popular times)
    """
    print("Calculating popular times statistics . . .")
    starts = time.time()
    if month == 'all':
        print("\nMost common moth: ", d_frame['month'].mode()[0])
    if day == 'all':
        print("\nMost common day in the week: ", d_frame['day_of_week'].mode()[0])
    print("\nMost common hour in the day: ", d_frame['hour'].mode()[0])
    print("\nit took ", time.time() - starts, "sec\n\n\n\n")

def trip_duration(d_frame):
    """
    func 4 to calculate total and average trip duration
    """
    starts = time.time()
    print("Calculating Total and Average Trip Duration . . .")
    print("\nTotal Trip Duration: ", d_frame['Trip Duration'].sum())
    print("\nAverage Trip Duration: ", d_frame['Trip Duration'].mean())
    print("\nit took ", time.time() - starts, "sec\n\n\n\n")

def pop_station_and_trip(d_frame):
    """
    func 5 to calculate the most common start station, end station and trip 
    """
    starts = time.time()
    print("Calculating statistics of popular start/end stations and trip . . .")
    print("\nMost common Start Station: ", d_frame['Start Station'].mode()[0])
    print("\nMost common End Station: ", d_frame['End Station'].mode()[0])
    print("\nMost common Trip: ", (d_frame['Start Station'] + d_frame['End Station']).mode()[0])
    print("\nit took ", time.time() - starts, "sec\n\n\n\n")


def user_type(d_frame):
    """
    func 6 to calculate the counts of each user type 
    """
    starts = time.time()
    print("Calculating counts of each user type . . .")
    print(d_frame['User Type'].value_counts())
    print("\nit took ", time.time() - starts, "sec\n\n\n\n")


def pop_gender(d_frame):
    """
    func 7 to calculate the counts of each gender 
    """
    starts = time.time()
    print("Calculating counts of each gender . . .")
    if 'Gender' not in d_frame:
        print("There's no gender data to show!")
    else:
        print(d_frame['Gender'].value_counts())
        print("\nit took ", time.time() - starts, "sec\n\n\n\n")
    print("\nit took ", time.time() - starts, "sec\n\n\n\n")


def View_data(d_frame):
    ans = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower().strip()
    start_loc = 0
    while (ans != 'no' and start_loc < d_frame.shape[0] - 5):
      if ans != 'yes' and ans != 'no':
        continue
      print(d_frame.iloc[start_loc:start_loc+5])
      start_loc += 5
      ans = input("Do you wish to continue?: ").lower().strip()

def birth_year_stat(d_frame):
    """
    func 8 to calculate most common year of birth, most recent year of birth and earliest year of birth 
    """
    starts = time.time()
    print("Calculating Most Common Birth Year, Most Recent Birth Year and Earliest Birth Year . . .")
    if 'Birth Year' not in d_frame:
        print("There's no Birth Year data to show!")
    else:
        print("The Most Common Birth Year: ", d_frame['Birth Year'].mode([0]))
        print("The Most Recent Birth Year: ", d_frame['Birth Year'].max())
        print("The Earliest Birth Year: ", d_frame['Birth Year'].min())
        print("\nit took ", time.time() - starts, "sec\n\n\n\n")
    print("\nit took ", time.time() - starts, "sec\n\n\n\n")

def main():
    while True:
        city, month, day = 'none', 'none', 'none'
        city, month, day = get_filters()
        #print(city, month, day)
        df = load_data(city, month, day)
        #print(df.shape)
        pop_time(df, month, day)
        trip_duration(df)
        pop_station_and_trip(df)
        user_type(df)
        pop_gender(df)
        birth_year_stat(df)
        View_data(df)
        restart = input("Would you like to explore another city?\nType 'yes' if you agree and any thing else if you don't\n")
        if restart.lower().strip() != 'yes':
            break
if __name__ == "__main__":
    main()
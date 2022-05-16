# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 02:17:01 2021

@author: Maya
"""
import time
import datetime as dt
import pandas as pd
import numpy as np
from time import strftime
from time import gmtime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
   Asks user to specify a city, month, and day to analyze.

   Returns:
       (str) city - name of the city to analyze
       (str) month - name of the month to filter by, or "all" to apply no'
       month filter
       (str) day - name of the day of week to filter by, or "all" to apply no'
       day filter
   """

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington)
    city = input('Enter Your City:')
    if city in {'chicago', 'new york city', 'washington'}:
        print('Welcom you will fined some data a bout bike share in',
              city.title())
    while city not in {'chicago', 'new york city', 'washington'}:
        print('Sorry ! This city not valied')
        city = input('Enter Your City again:')

        # get user input for month (all, january, february, ... , june)
    month = input('Enter a month please:')
    if month in {'all', 'january', 'february', 'march',
                 'april', 'may', 'june'}:
        print('continue')
    while month not in {'all', 'january', 'february', 'march', 'april', 'may',
                        'june'}:
        print('Not valied . Please enter a month from (all or january : june)')
        month = input('Enter a month again please:')

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Enter a day you want:')
    if day in {'all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday',
               'thursday', 'friday'}:
        print('continue')
    while day not in {'all', 'saturday', 'sunday', 'monday', 'tuesday',
                      'wednesday', 'thursday', 'friday'}:
        print('Error')
        day = input('Enter a day again please:')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """Displays statistics on the most frequent times of travel.""" """
    Loads data for the specified city and filters by month and day if '
    applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no'
        month filter
        (str) day - name of the day of week to filter by, or "all" to apply no'
        day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df = df[df['month'] == month.title()]

    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
# display the most common month
# display the most common day of week
# display the most common start hour

    if month != 'all' and day != 'all':

        print('The most common day:', df['day'].mode()[0])
        df['hour'] = df['Start Time'].dt.hour
        print('The most common houre:', df['hour'].mode()[0])

    if month == 'all' and day == 'all':
        print('The most common month:', df['month'].mode()[0])
        print('The most common day :', df['day'].mode()[0])
        df['hour'] = df['Start Time'].dt.hour
        print('The most common houre:', df['hour'].mode()[0])

    if day != 'all' and month == 'all':
        print('The most common month:', df['month'].mode()[0])
        print('The most common day :', df['day'].mode()[0])
        df['hour'] = df['Start Time'].dt.hour
        print('The most common houre:', df['hour'].mode()[0])

    if day == 'all' and month != all:
        print('The most common day:', df['day'].mode()[0])
        df['hour'] = df['Start Time'].dt.hour
        print('The most common houre:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
# display most commonly used start station
    print('The most common start station:', df['Start Station'].mode()[0])

# display most commonly used end station
    print('The most common End station:', df['End Station'].mode()[0])

# display most frequent combination of start station and end station trip
    trip = df['Start Station'] + df['End Station']
    print('The most common trip:', trip.mode()[0])


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
# display total travel time
    start_time = time.time()
    start_time = time.time()
    total_travel = df['Trip Duration'].sum()
    travel_duration = strftime("%H:%M:%S", gmtime(total_travel))
    print('Total travel time:', travel_duration)
# display mean travel time
    mean = df['Trip Duration'].mean()
    mean_travel = strftime("%H:%M:%S", gmtime(mean))
    print('Mean Travel Time:', mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
# Display counts of user types
    print('Counts Of User Type:', df['User Type'].value_counts())

    if city != 'washington':
        # Display counts of gender
        print('Counts Of Gender:', df['Gender'].value_counts())
        # Display the earliest
        print('Earliest Year Of Birth:', df['Birth Year'].min())
        # Display the most recent
        print('The Most Recent Year Of Birth:', df['Birth Year'].max())
        # Display the most common year of birth
        print('The Most Common Year:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

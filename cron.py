# program name  : cron daemon in python
# date          : Fri Sep 29 22:24:08 IST 2017

from datetime import datetime
import calendar
import time

# storing the tasks in crontab.txt in tasks list
tasks = []

# setting sunday as first week day as in cron
calendar.setfirstweekday(calendar.SUNDAY)

# open crontab in read mode
# we read the tasks in crontab.txt and execute them in the program
with open("crontab.txt", 'r') as c:
    for line in c:
        tasks.append(line)


# main class
class Task():

    """
    cron daemon
    ----------
    minutes (0 - 59)
    hours (0 - 23)
    month (1 - 12)
    days (1 - 31)
    day_of_week (0 - 6)

     ┌───────────── minute (0 - 59)
     │ ┌───────────── hour (0 - 23)
     │ │ ┌───────────── day of month (1 - 31)
     │ │ │ ┌───────────── month (1 - 12)
     │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
     │ │ │ │ │                          7 is also Sunday on some systems)
     │ │ │ │ │
     │ │ │ │ │
     * * * * *  command to execute

    * * * * *
    # tells us that do the task now
    0 0 1 * *
    # tells us that do that at 0 min at 12 hrs mid night on january month
    30 16 * * *
    # tells us that do the task at 30 min at 16:00 everyday
    ----------------------------------------
    changes in version 2.0
    * validation for wrong inputs
    * multi threading ?? (should work on it)
    """

    def __init__(self, minutes, hours, month, day, day_of_week, work):
        """
        initialising the given data to the task so that
        we can compare with the present time and execute the tasks
        """
        self.minutes = minutes
        self.hours = hours
        self.month = month
        self.day = day
        self.day_of_week = day_of_week
        self.work = work
        self.validation = True
        # just some arbitrary value
        self.no_of_days = None
        self.validate(self.minutes, self.hours, self.month, self.day,
                      self.day_of_week)

    def is_special_command(self):
        """
        if crontab contains special commands
        */30 * * * * work
        tells us to repeat the work every 30 minutes
        ------------------------------
        other case
        1-10 * * * * work
        tells us to do the work for the first ten minutes
        ------------------------------
        addition in version 2.0
        """

        if (len(self.minutes.split("/")) > 1) or \
           (len(self.hours.split("/")) > 1) or \
           (len(self.month.split("/")) > 1) or \
           (len(self.day.split("/")) > 1) or \
           (len(self.day_of_week.split("/")) > 1):
            self.has_repeating_command = True

        if (len(self.minutes.split("-")) > 1) or \
           (len(self.hours.split("-")) > 1) or \
           (len(self.month.split("-")) > 1) or \
           (len(self.day.split("-")) > 1) or \
           (len(self.day_of_week.split("-")) > 1):
            self.has_period_command = True

    def compute_values_of_now(self):
        """
        computing the present time in order to give the comparison
        """
        self.now = str(datetime.now())
        self.day_of_now = self.now.split()[0]
        self.year_of_now = self.day_of_now.split("-")[0]
        self.month_of_now = self.day_of_now.split("-")[1]
        self.date_of_now = self.day_of_now.split("-")[2]
        self.hours_of_now = self.now.split()[1].split(":")[0]
        self.minutes_of_now = self.now.split()[1].split(":")[1]
        # print(self.date_of_now)
        self.week_day_of_now = self.week_day(self.year_of_now,
                                             self.month_of_now,
                                             self.date_of_now)

    @staticmethod
    def no_of_days_of_the_month(year, month):
        """
        gives the no of days in the month
        for the given year
        can only be 1 - 12
        1 starts from january
        """
        return calendar.monthrange(year, month)

    # method to validate and compare the given task time
    # and at present time
    def start_task(self):
        """
        method to validate and do the tasks
        main heart of the program
        """
        if self.validation is True:
            while(1):
                # computing present time every minute
                self.compute_values_of_now()
                # validating it with the given time
                # only 'True' when no repeating is given
                if (self.minutes == self.minutes_of_now or
                    self.minutes == "*") and \
                   (self.hours == self.hours_of_now or self.hours == "*") and \
                   (self.month == self.month_of_now or self.month == "*") and \
                   (self.day == self.day_of_now or self.day == "*") and \
                   (self.day_of_week == self.week_day_of_now or
                    self.day_of_week == "*") and \
                   (self.has_period_command is False) and \
                   (self.has_repeating_command is False):

                    print(self.work)
                    print("Task completed")
                    break
                elif (self.has_period_command is True) and \
                     (self.has_repeating_command is True):
                    pass
                elif (self.has_period_command is True):
                    pass
                elif (self.has_repeating_command is True):
                    if (len(self.minutes.split("/")) > 1) and \
                       (len(self.hours.split("/")) == 1) and \
                       (len(self.month.split("/")) == 1) and \
                       (len(self.day.split("/")) == 1) and \
                       (len(self.day_of_week.split("/")) == 1):
                        Minutes = self.minutes.split("/")[1]
                        self.repeat_minutes(Minutes)

                    if len(self.hours.split("/")) > 1:
                        pass

                    if len(self.day.split("/")) > 1:
                        pass

                    if len(self.month.split("/")) > 1:
                        pass

                    if len(self.day_of_week.split("/")) > 1:
                        pass

                    pass
                else:
                    # take a break for 60 seconds
                    time.sleep(60)
        else:
            print("Entered Invalid values in crontab.txt")

    # gives the week day of now
    def validate(self, minutes, hours, month, day, day_of_week):
        """
        validation method to check if the user entered
        the correct values to the crontab.txt
        """

        # for minutes
        if not(minutes < 0 and minutes > 60):
            self.validation = False

        # for hours
        if not(hours < 0 and hours > 23):
            self.validation = False

        # no of the days of the current month
        self.no_of_days = self.no_of_days_of_the_month(self.year_of_now,
                                                       self.month_of_now)

        # for days
        if not(day < 0 and day > self.no_of_days):
            self.validation = False

        # for months
        if not(month <= 0 and month > 12):
            self.validation = False

        # for day of the week
        if not(day_of_week < 0 and day_of_week > 6):
            self.validation = False

    @staticmethod
    def week_day(year, month, date):
        return calendar.weekday(int(year), int(month), int(date))

    def repeat_minutes(self, minutes):
        while(True):
            time.sleep(60 * minutes)
            print(self.work)
        # time.sleep(60 * minutes)

    @staticmethod
    def repeat_hours(hours):
        # time.sleep(60 * 60 * hours)
        pass

    @staticmethod
    def repeat_days(days):
        # time.sleep(24 * 60 * 60 * days)
        pass

    @staticmethod
    def repeat_month(month):
        # time.sleep(month)
        # no_of_days_of_the_month(2017, month)
        pass

    @staticmethod
    def repeat_day_of_the_week(day_of_week):
        pass

    @staticmethod
    def period_minutes():
        pass

    @staticmethod
    def period_hours():
        pass

    @staticmethod
    def period_month():
        pass

    def __repr__(self):
        return "Task(time, '{}')".format(self.work)

    def __str__(self):
        return "{} - {}".format("time", self.work)


def main():
    for task in tasks:
        minutes, hours, month, day, day_of_week, work = task.split()
        task1 = Task(minutes, hours, month, day, day_of_week, work)
        task1.start_task()


if __name__ == "__main__":
    main()

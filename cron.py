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

    * * * * *
    # tells us that do the task now
    0 0 1 * *
    # tells us that do that at 0 min at 12 hrs mid night on january month
    30 16 * * *
    # tells us that do the task at 30 min at 16:00 everyday
    """

    # initialising the given data to the task so that
    # we can compare with the present time and execute the tasks
    def __init__(self, minutes, hours, month, day, day_of_week, work):
        self.minutes = minutes
        self.hours = hours
        self.month = month
        self.day = day
        self.day_of_week = day_of_week
        self.work = work

    # computing the present time in order to give the comparison
    def compute_values_of_now(self):
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

    # method to validate and compare the given task time
    # and at present time
    def start_task(self):
        while(1):
            # computing present time every minute
            self.compute_values_of_now()
            # validating it with the given time
            if (self.minutes == self.minutes_of_now or self.minutes == "*") and \
               (self.hours == self.hours_of_now or self.hours == "*") and \
               (self.month == self.month_of_now or self.month == "*") and \
               (self.day == self.day_of_now or self.day == "*") and \
               (self.day_of_week == self.week_day_of_now or self.day_of_week == "*"):

                   print(self.work)
                   print("Task completed")
                   break
            else:
                # take a break for 60 seconds
                time.sleep(60)

    # gives the week day of now
    @staticmethod
    def week_day(year, month, date):
        return calendar.weekday(int(year), int(month), int(date))

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

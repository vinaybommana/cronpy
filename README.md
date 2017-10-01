# cronpy
a python daemon for unix cron utility

# crontab.txt
* cronpy uses `crontab.txt` for reading the tasks
* the user need to enter his tasks in the crontab.txt

```bash
#     ┌───────────── minute (0 - 59)
#     │ ┌───────────── hour (0 - 23)
#     │ │ ┌───────────── day of month (1 - 31)
#     │ │ │ ┌───────────── month (1 - 12)
#     │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
#     │ │ │ │ │                                       7 is also Sunday on some systems)
#     │ │ │ │ │
#     │ │ │ │ │
#     * * * * *  command to execute
```

# Multi Threading in cron
* we can use `timer`
* we can use Threading


# different types of cron commands
* we have implemented only the initial commands
```bash
* * * * * # we have implemented for this
# what if the user gave a command for
*/30 * * * * # for every 30 minutes the command should be executed
# else
* 0-12 * * * # for 0 to afternoon 12 the command should be executed

```
* we can used two functions
```python
def repeating_command():
    pass

def period_command():
    pass
```

* The string given out should be split and seen if the repeating or period
  command exists
* to execute period command the attributes are read and used for the execution

## repeating methods
### repeating minutes
* the minutes to be should be sent to the `@staticmethod`
* the function makes the program to sleep for the specified period

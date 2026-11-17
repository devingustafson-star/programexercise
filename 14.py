seconds = int(input('Enter the number of seconds: '))
if seconds >= 86400:
    days = seconds // 86400
    seconds = seconds % 86400
else: 
    days = 0
if seconds >= 3600:
    hours = seconds // 3600
    seconds = seconds % 3600
else:
    hours = 0
if seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60
else:
    minutes = 0
if days > 0:
    print(f'{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.')
elif hours > 0:
    print(f'{hours} hours, {minutes} minutes, and {seconds} seconds.')
elif minutes > 0:
    print(f'{minutes} minutes and {seconds} seconds.')
else:
    print(f'{seconds} seconds.')
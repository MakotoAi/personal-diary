from datetime import datetime

# myname = 'Joseph'
# text = f'My name is {myname}.'
# print(text)

now = datetime.now()
# print(now)

date_time = now.strftime('%Y-%m-%d-%H-%M-%S')
print(date_time)
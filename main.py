# step-1: Install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# step-2: Twilio credentials
account_sid = 'AC625503caa996c1e47b15bd4f2b51cxx' 
auth_token = '42d428b44813c08c5115d49542c59d20'    

client = Client(account_sid, auth_token)

# step-3: Define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:++14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print('An error occurred:', e)

# step-4: User input
Name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g., +1234567890): ')
message_body = input(f'Enter the message you want to send to {Name}: ')

# step-5: Parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

# Combine date and time into datetime object
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate delay in seconds
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time.')
else:
    print(f'Message scheduled to be sent to {Name} at {schedule_datetime}.')

    # Wait until the scheduled time
    time.sleep(delay_seconds)

    # Send the message
    send_whatsapp_message(recipient_number, message_body)

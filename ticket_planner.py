
import datetime


def get_pf_date(date):
    return f'{date.date()} [{date.strftime("%A").lower()}]'

def datetime_is_day(date, weekday):
    return date.strftime('%A').lower().__eq__(weekday.lower())

def compare_dates(date_1, date_2):
    return date_1.date().__eq__(date_2.date())

leave_dates = [
    datetime.datetime(2025, 8, 15),
    datetime.datetime(2025, 8, 27),
    datetime.datetime(2025, 10, 2),
    datetime.datetime(2025, 10, 20),
    datetime.datetime(2025, 12, 25),
    datetime.datetime(2026, 1, 1)
]

today = datetime.datetime.now() - datetime.timedelta(days=0)
script_end_day = datetime.datetime(2026, 1, 2)
ticket_opening_day = today + datetime.timedelta(days=60) 

for date in leave_dates:
    print(f' {date.date()} [{date.strftime("%A")}] ')

print('-'*70)

while(not compare_dates(ticket_opening_day, script_end_day)):

    if(ticket_opening_day.date().month!=(ticket_opening_day + datetime.timedelta(days=1)).date().month):
        print()

    is_leave = False

    if(datetime_is_day(ticket_opening_day, 'monday')):
        is_leave = [True for date in leave_dates if compare_dates( date, (ticket_opening_day+datetime.timedelta(days=1)) ) ]
    
    if(datetime_is_day(ticket_opening_day, 'thursday')):
        is_leave = [True for date in leave_dates if compare_dates(date, ticket_opening_day)]


    if(datetime_is_day(ticket_opening_day, 'monday')):
        if(is_leave):
            booking_date = get_pf_date( (today + datetime.timedelta(days=1)) )
            ticket_opening_date = get_pf_date( (ticket_opening_day + datetime.timedelta(days=1)) )
            print(f'Booking Date: {booking_date} Ticket Date: {ticket_opening_date} ADPT to MAS')
        else:
            booking_date = get_pf_date( today )
            ticket_opening_date = get_pf_date( ticket_opening_day )
            print(f'Booking Date: {booking_date} Ticket Date: {ticket_opening_date} MDU to MS')


    if(datetime_is_day(ticket_opening_day, 'thursday')):
        if(is_leave):
            booking_date = get_pf_date( (today - datetime.timedelta(days=1)) )
            ticket_opening_date = get_pf_date( (ticket_opening_day - datetime.timedelta(days=1)) )
            print(f'Booking Date: {booking_date} Ticket Date: {ticket_opening_date} MAS to ADPT')
        else:
            booking_date = get_pf_date( today )
            ticket_opening_date = get_pf_date( ticket_opening_day )
            print(f'Booking Date: {booking_date} Ticket Date: {ticket_opening_date} MS to MDU')


    ticket_opening_day = ticket_opening_day + datetime.timedelta(days=1)
    today = today + datetime.timedelta(days=1)


# appointment-monitor
App to monitor the nearest available appointment at migri and email the user with the available appointment details.

## Problem - Why do I need this?
There was a time in my life in which I needed to keep on checking the appointment booking system in order to find a 
time slot for both my residence permit application and my citizenship application.
Both of these applications required different appointment types that I had to search for.
It got time consuming (and mentally taxing) when the appointments were very scarce, and the calendar was showing
appointments either in the far future or far-away cities. 

## Solution
Build a bot to do the checking for me.
The bot uses:
- Selenium: to do the scraping and checking for available appointments.
- Django: to save the monitoring requests containing the search parameters and email of the recipient.
- Celery: to run the task of checking the available appointments periodically.

## App's basic flow
`MonitoringRequest` objects instantiated and stored in DB.
Every 10 mins, do appointment monitoring (main task):
- Get all monitoring_request objects.
- Search for available appointments based on the attributes of each monitor.
- Email with the availability.


## Advantages
In addition to the main advantage of not having to manually do the search:
  - The app can set multiple monitoring requests of different types,
  such as residence permit and citizenship, and different emails to send to.

## Limitations
- This app **does not** do the booking, and this is by design. Letting the bot do the actual booking is both
  out of scope and adds [legal](#legal) complexity.
- This is limited to the migri appointment page (vihta). Changes to rendered page might result in system not working.
It would be better if there is an API to get all appointment data.
The scraping depends on the structure of the output html on the appointment booking page.
- The frequency of running the main task is limited. It is only every 10 minutes, so an appointment can be taken
  before the next checking time approaches. However, making the time checking more frequent is also risky,
  since multiple frequent requests might risk being blocked.

## Legal
This is under MIT License. It is intended for personal use, mostly for fun (and ease of mind) purposes.
When you use it, **do not book multiple appointments and try to sell them**, because that is [illegal](
https://yle.fi/uutiset/osasto/news/migri_cracks_down_on_illegal_online_sales_of_residence_permit_appointments/11525539
).
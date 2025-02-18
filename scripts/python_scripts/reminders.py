from plyer import notification
import schedule
import time

def send_notification():
    notification.notify(
        title="Be healthy",
        message="eat your vegetables",
        timeout="1000000000000",
    )

schedule.every(10).seconds.do(send_notification)

while 1:
    schedule.run_pending()
    time.sleep(10)
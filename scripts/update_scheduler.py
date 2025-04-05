import time
import schedule
from src.core.update_manager import UpdateManager

def scheduled_update():
    update_manager = UpdateManager()
    update_manager.start_update()

def main():
    # Schedule the update every day at 2 AM
    schedule.every().day.at("02:00").do(scheduled_update)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
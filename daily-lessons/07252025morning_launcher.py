import schedule
import time
import os
import platform
import webbrowser
from datetime import datetime
with open("/Users/marwansayed/desktop/Computer-Science/python-healthcare-analytics/daily-lessons/cron_log.txt", "a") as f:
    f.write(f"✅ Cron ran at {datetime.now()}\n")

summary_path = "/Users/marwansayed/desktop/Computer-Science/python-healthcare-analytics/daily-lessons/daily_summary.txt"
def manager_startup():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n📋 [{now}] Good morning, Manager! Here’s your launch sequence:")

    # Open your summary file
    summary_path = "/Users/marwansayed/desktop/Computer-Science/python-healthcare-analytics/daily-lessons/daily_summary.txt"
    if platform.system() == "Windows":
        if os.path.exists(summary_path):
            os.startfile(summary_path)
        else:
            print(f"The file {summary_path} does not exist.")
        
    elif platform.system() == "Darwin":  # Mac
        if os.path.exists(summary_path):
            os.system(f"open \"{summary_path}\"")
        else:
            print(f"The file {summary_path} does not exist.")

    # Launch Chrome for gmail (Windows) or Mail (Mac)
    if platform.system() == "Windows":
        print("📨 Opening Gmail in browser...")
        webbrowser.open("https://mail.google.com")
    elif platform.system() == "Darwin":
        os.system("open -a Mail")

# Scheduling this to run once a day (test run every 15 sec)
schedule.every(15).seconds.do(manager_startup)
# Real version once a day: schedule.every().day.at("08:00").do(manager_startup)

manager_startup()

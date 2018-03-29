import os

from apscheduler.schedulers.blocking import BlockingScheduler
import jobs


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(jobs.ETHUSDT, 'interval', minutes=1)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

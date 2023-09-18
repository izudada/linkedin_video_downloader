import os
import logging
import time

from celery import Celery

from downloader import create_app
from downloader.my_downloader import _get_server_path

app = create_app()

celery = Celery(__name__)

log_file = 'celery_task.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def _process_video_deletion():
    """
        A function to delete videos in the server every 24 hours
        by 12am.
        Videos have to be more than 30mins old to be deleted
        at that time.

        Keyword arguments:
        argument -- description
        Return: return_description
    """

    # Update this to the directory containing your mp4 files
    directory = _get_server_path()  
    # Get current time in seconds
    now = time.time()

    # Set time threshold to 30 minutes ago
    threshold = now - 2 * 60
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.mp4'):
            filepath = os.path.join(directory, filename)
            mod_time = os.path.getmtime(filepath)  # Get modification time of file
            if mod_time < threshold:
                os.remove(filepath)
                print(f"Deleted {filepath}")
            print(directory)
            print(now, threshold)
            print(filepath)
            print(mod_time)

@celery.task
def scheduled_delete_videos():
    """
        This functions serves as a scheduled job
        to delete videos.
    
        Keyword arguments:
        argument -- description
        Return: return_description
    """
    log.info("Anthony Udeagbala")

    print("Anthony Udeagbala")
    # print(_process_video_deletion())

if __name__ == '__main__':
    app.run(debug=True)
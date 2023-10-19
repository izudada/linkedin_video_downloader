import os
import logging
import time

from celery import Celery

from downloader.my_downloader import _get_server_path


celery = Celery('task', broker='redis://redis:6379/0')

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
        print(filename, "#######################")
        print(filename, os.getcwd(), directory)
        if filename.endswith('.mp4'):
            filepath = os.path.join(directory, filename)
            mod_time = os.path.getmtime(filepath)  # Get modification time of file
            if mod_time < threshold:
                print("Yes")
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
    print("Anthony Udeagbala")

    _process_video_deletion()


# Configure Celery Beat to schedule the task every 2 minutes
celery.conf.beat_schedule = {
    'delete-videos-every-2-minutes': {
        'task': 'task.scheduled_delete_videos',
        'schedule': 120,  # 2 minutes in seconds
    },
}
celery.conf.timezone = 'UTC'  # Set the timezone if needed

if __name__ == '__main__':
    celery.start()

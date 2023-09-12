from downloader import create_app
import os
import time
from downloader.my_downloader import _get_server_path

app = create_app()

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
    
    directory = _get_server_path()  # Update this to the directory containing your mp4 files

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

@app.cli.command()
def scheduled_delete_videos():
    """
        This functions serves as a scheduled job
        to delete videos.
    
        Keyword arguments:
        argument -- description
        Return: return_description
    """
    print("Anthony Udeagbala")
    print(_process_video_deletion())

if __name__ == '__main__':
    app.run(debug=True)
import os
import kagglehub
import traceback

os.environ["KAGGLEHUB_CACHE"] = "downloaded_audios"

try:
    path = kagglehub.dataset_download("javohirtoshqorgonov/noise-audio-data")
    print("Data downloaded successfully")
    print("Path to dataset files:", path)

except Exception as e:
    print("Error occured when downloading the data: ", str(e))
    traceback.print_exc()

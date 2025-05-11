import os
import zipfile
import shutil
import traceback

root_img_dir = r'D:\Projects\multimodal_agentic_rag_pipeline\downloaded_images'
img_output_zip = 'images.zip'

root_audio_dir = r'D:\Projects\multimodal_agentic_rag_pipeline\downloaded_audios\datasets\javohirtoshqorgonov\noise-audio-data\versions\1\ESC-50-master\audio'
audio_output_zip = 'audio.zip'

image_extensions = ['jpg', 'jpeg', 'png']
audio_extensions = ['wav', 'm4a', 'mp3']

try:
    if not os.path.exists(img_output_zip):
        with zipfile.ZipFile(img_output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for folder in os.listdir(root_img_dir):
                sub_folder_path = os.path.join(root_img_dir, folder)

                for file in os.listdir(sub_folder_path):
                    img_path = os.path.join(sub_folder_path, file)

                    if img_path.split(".")[-1].lower() in image_extensions:
                        new_filename = f"{folder}_{file}"
                        zipf.write(img_path, arcname=new_filename)

        print("Zipped the images successfully")

    else:
        print("Images already zipped")

except Exception as e:
    print("Error occuered when zipping image files: ", str(e))
    traceback.print_exc()

try:
    if not os.path.exists(audio_output_zip):
        with zipfile.ZipFile(audio_output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in os.listdir(root_audio_dir):
                audio_path = os.path.join(root_audio_dir, file)

                if audio_path.split(".")[-1].lower() in audio_extensions:
                    zipf.write(audio_path, arcname=file)

        print("Zipped the audios successfully")

    else:
        print("Audios already zipped")

except Exception as e:
    print("Error occuered when zipping audio files: ", str(e))
    traceback.print_exc()


try:
    if os.path.exists(root_img_dir):
        shutil.rmtree(root_img_dir)
        print(f"Successfully removed the file {root_img_dir}")
    else:
        print("Path doesn't exist/already removed")

    audio_dir_path = root_audio_dir.split('downloaded_audios')[0] + 'downloaded_audios'
    if os.path.exists(audio_dir_path):
        shutil.rmtree(audio_dir_path)
        print(f"Successfully removed the file {audio_dir_path}")
    else:
        print("Path doesn't exist/already removed")


except Exception as e:
    print("Error occured when removing the folders: ", str(e))

import sys
import shutil
from pathlib import Path
import threading
from normalize import normalize


# Create folders
def create_folder(object):
    if object.is_file():
        file_name, file_ext = object.stem, object.suffix
        file_ext = file_ext.lower()

        # Make name normalization
        file_name_new = normalize(file_name)
        normalize_name = file_name_new + file_ext

        images = ('.jpeg', '.png', '.jpg', '.svg')
        video = ('.avi', '.mp4', '.mov', '.mkv')
        documents = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
        audio = ('.mp3', '.ogg', '.wav', '.amr')
        archives = ('.zip', '.gz', '.tar', '.rar')

        if file_ext in images:
            Path.mkdir(object.parent / 'images', exist_ok=True)
            object.rename(object.parent / 'images' / normalize_name)
        elif file_ext in documents:
            Path.mkdir(object.parent / 'documents', exist_ok=True)
            object.rename(object.parent / 'documents' / normalize_name)
        elif file_ext in audio:
            Path.mkdir(object.parent / 'audio', exist_ok=True)
            object.rename(object.parent / 'audio' / normalize_name)
        elif file_ext in video:
            Path.mkdir(object.parent / 'video', exist_ok=True)
            object.rename(object.parent / 'video' / normalize_name)

        # Work with archives
        elif file_ext in archives:
            try:
                Path.mkdir(object.parent / 'archives', exist_ok=True)
                object.rename(object.parent / 'archives' / normalize_name)
                shutil.unpack_archive(Path(object.parent / 'archives' / normalize_name),
                                      Path(object.parent / 'archives' / file_name))
            except shutil.ReadError:
                print("It's not an archive")


# The sorting process
def process_folder(item):
    if item.is_dir() and item.name not in ignore_list:
        sorting(item)  # recursion
        # If folder is empty - delete
        if item.is_dir() and not any(item.iterdir()):
            item.rmdir()
    elif item.is_file():
        print(f'file {item}')
        print(item.parent)
        create_folder(item)


def sorting(path):
    threads = []
    for item in path.iterdir():
        thread = threading.Thread(target=process_folder, args=(item,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    ignore_list = ('archives', 'video', 'audio', 'documents', 'images')
    path = Path(sys.argv[1])
    sorting(path)

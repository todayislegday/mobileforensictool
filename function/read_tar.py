import tarfile
### tar파일에서 원하는 폴더 내용 긁어오기.
### file_path는 tar경로, output_path는 외부로 db파일

target_folder = set(['./data/com.samsung.android.providers.contacts/databases/', './data/com.samsung.cmh/databases/', './data/com.samsung.android.messaging/databases/'])

def decompression(file_path, output_path):

    tar = tarfile.open(file_path)
    for folder in target_folder:
        target_name = set(tarinfo for tarinfo in tar.getmembers() if tarinfo.name.startswith(folder))  # target_folder에 있는 폴더의 이름을 가진 모든 tarinfo를 target_name으로 둔다.
        tar.extractall(members=target_name, path=output_path)

    tar.close()
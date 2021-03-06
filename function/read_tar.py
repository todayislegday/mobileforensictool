import tarfile
import os
### tar파일에서 원하는 폴더 내용 긁어오기.
### file_path는 tar경로, output_path는 외부로 db파일

target_folder = set(['./data/com.samsung.android.providers.contacts/databases/', './data/com.samsung.cmh/databases/', './data/com.samsung.android.messaging/databases/',
                      './user_de/0/com.android.providers.telephony/databases/', './data/com.android.chrome/', './data/com.sec.android.app.sbrowser/',
                     './data/com.android.vending/databases/', './data/com.android.providers.downloads/databases/', './data/com.samsung.android.providers.media/',
                      './data/com.android.providers.media/databases/', './media/', './misc/wifi/', './data/com.android.providers.calendar/databases/','./data/com.kakao.talk/databases/',
                     './user_de/0/com.android.providers.telephony/app_parts/'])
image_folder = set(['.png', '.jpg', '.jpeg', '.gif', '.mp4'])
image_path = os.path.dirname(os.path.abspath(__file__))

def decompression(file_path, output_path):

    tar = tarfile.open(file_path)
    for folder in target_folder:
        if folder == './media/' or folder == './user_de/0/com.android.providers.telephony/app_parts/':
            for img in image_folder:
                image_name = set(tarinfo for tarinfo in tar.getmembers() if ((tarinfo.name.startswith('./media/') or tarinfo.name.startswith('./user_de/0/com.android.providers.telephony/app_parts/')) and tarinfo.name.endswith(img)))
                tar.extractall(members=image_name, path=f"{image_path}/../was/static/assets/images/")
            continue
        target_name = set(tarinfo for tarinfo in tar.getmembers() if tarinfo.name.startswith(folder))  # target_folder에 있는 폴더의 이름을 가진 모든 tarinfo를 target_name으로 둔다.
        tar.extractall(members=target_name, path=output_path)

    tar.close()
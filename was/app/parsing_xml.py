import xml.etree.ElementTree as ET

def xml_parsing(file_path):
	file_path=f"{file_path}/misc/wifi/WifiConfigStore.xml"
	doc = ET.parse(file_path) # xml파일 열기
	root = doc.getroot() # root가 xml문서의 최상위 태그를 가리킴
	networklist = root.find("NetworkList")
	wifi_list = []
	for networks in networklist.findall("Network"):
		i = 0
		for WifiConfiguration in networks.findall("WifiConfiguration"):
			net_info = {}
			SSID_list = WifiConfiguration[0].text.split("\"") # SSID
			SSID = SSID_list[1]
			encryption = SSID_list[2]
			creation_time = WifiConfiguration[30].text # 생성시간
			creation_time = creation_time[5:19]
			MAC = WifiConfiguration[36].text # MAC주소
			pre_shared_key = WifiConfiguration[3].text # 키
			#원하는 값 = WifiConfiguration[라인번호].text를 사용하여 출력
			if pre_shared_key != None:
				pre_shared_key = pre_shared_key.replace("\"", "")
			net_info['SSID']=SSID
			net_info['encryption']=encryption
			net_info['creation_time']= creation_time
			net_info['MAC']=MAC.upper()
			net_info['pre_shared_key']=pre_shared_key			
			#net_info.extend([SSID, encryption, creation_time, MAC.upper(), pre_shared_key])
		wifi_list.append(net_info)
	# print(wifi_list)
	"""리턴 값 예시) [ [],[],[],[],[] ] """
	return wifi_list # wifi_list 안에 net_info 리스트 반환

if __name__ == "__main__":
	xml_parsing('WifiConfigStore.xml')
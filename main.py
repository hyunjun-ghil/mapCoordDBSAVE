import pymssql
import json


_conn = pymssql.connect(server='', user='', password='', database='')
cursor = _conn.cursor(as_dict=True)


with open('./coord/TL_KODIS_BAS_42_org.json', encoding='utf-8') as f:
    Gangwon = json.load(f)

with open('./coord/TL_KODIS_BAS_41.json', encoding='utf-8') as f:
    Kyungki = json.load(f)

with open('./coord/TL_KODIS_BAS_48.json', encoding='utf-8') as f:
    Kyungnam = json.load(f)

with open('./coord/TL_KODIS_BAS_47.json', encoding='utf-8') as f:
    Kyungbuk = json.load(f)

with open('./coord/TL_KODIS_BAS_29.json', encoding='utf-8') as f:
    Gwangju = json.load(f)

with open('./coord/TL_KODIS_BAS_27.json', encoding='utf-8') as f:
    Daegu = json.load(f)

with open('./coord/TL_KODIS_BAS_30.json', encoding='utf-8') as f:
    Daejeon = json.load(f)

with open('./coord/TL_KODIS_BAS_26.json', encoding='utf-8') as f:
    Busan = json.load(f)

with open('./coord/TL_KODIS_BAS_11.json', encoding='utf-8') as f:
    Seoul = json.load(f)

with open('./coord/TL_KODIS_BAS_36.json', encoding='utf-8') as f:
    Sejong = json.load(f)

with open('./coord/TL_KODIS_BAS_31.json', encoding='utf-8') as f:
    Ulsan = json.load(f)

with open('./coord/TL_KODIS_BAS_28.json', encoding='utf-8') as f:
    Incheon = json.load(f)

with open('./coord/TL_KODIS_BAS_46.json', encoding='utf-8') as f:
    Jeonnam = json.load(f)

with open('./coord/TL_KODIS_BAS_45.json', encoding='utf-8') as f:
    Jeonbuk = json.load(f)

with open('./coord/TL_KODIS_BAS_50.json', encoding='utf-8') as f:
    Jeju = json.load(f)

with open('./coord/TL_KODIS_BAS_44.json', encoding='utf-8') as f:
    Choongnam = json.load(f)

with open('./coord/TL_KODIS_BAS_43.json', encoding='utf-8') as f:
    Choongbuk = json.load(f)


def ParseAndSaveDB(jsonData, txt):
    for j in range(0, len(jsonData['features'])):
        ZipCd = jsonData['features'][j]['properties']['BAS_ID']
        Name = jsonData['features'][j]['properties']['CTP_KOR_NM'] + ' ' + jsonData['features'][j]['properties']['SIG_KOR_NM']
        for i in range(0, len(jsonData['features'][j]['geometry']['coordinates'][0])):
            type = Latitude = jsonData['features'][j]['geometry']['type']
            if type == 'Polygon':
                Latitude = jsonData['features'][j]['geometry']['coordinates'][0][i][1]
                Longtitude = jsonData['features'][j]['geometry']['coordinates'][0][i][0]
            elif type == 'MultiPolygon':
                Latitude = jsonData['features'][j]['geometry']['coordinates'][0][i][0][1]
                Longtitude = jsonData['features'][j]['geometry']['coordinates'][0][i][0][0]
        sql = "insert into coord" + txt + "(ZipCd, Latitude, Longitude, Name) values('{}','{}','{}','{}')".format(ZipCd, float(Latitude),
                                                                                               float(Longtitude), Name)
        print(sql)
        cursor.execute(sql)
        _conn.commit()
    _conn.close()


ParseAndSaveDB(Gangwon, "Gangwon")
# ParseAndSaveDB(Kyungki, "Kyungki")
# ParseAndSaveDB(Kyungnam, "Kyungnam")
# ParseAndSaveDB(Kyungbuk, "Kyungbuk")
# ParseAndSaveDB(Daegu, "Daegu")
# ParseAndSaveDB(Daejeon, "Daejeon")
# ParseAndSaveDB(Busan, "Busan")
# ParseAndSaveDB(Seoul, "Seoul")
# ParseAndSaveDB(Sejong, "Sejong")
# ParseAndSaveDB(Ulsan, "Ulsan")
# ParseAndSaveDB(Incheon, "Incheon")
# ParseAndSaveDB(Jeonnam, "Jeonnam")
# ParseAndSaveDB(Jeonbuk, "Jeonbuk")
# ParseAndSaveDB(Jeju, "Jeju")
# ParseAndSaveDB(Choongnam, "Choongnam")
# ParseAndSaveDB(Choongbuk, "Choongbuk")


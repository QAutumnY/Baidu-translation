import pprint

import execjs  # pyexecjs   读取本地js文件
import requests

while True:
    word = input("请输入你要翻译的内容：(输入0即可退出)\n")
    if word == '0':
        break
    else:
        with open('H:/VSCodeSaveLocation/网络爬虫/Myself_studay/General/百度翻译.js', mode='r', encoding='utf-8')as f:
            js_code = f.read()
        compilecode = execjs.compile(js_code)
        sign = compilecode.call('e', word)
        url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Cookie': 'BIDUPSID=5BD1E18F26C99C47A4FA81FF6B41F5D9; PSTM=1675167666; BAIDUID=5BD1E18F26C99C474CBF657F9BFE8E94:FG=1; H_PS_PSSID=36548_38092_37906_37989_36803_37925_38088_26350_37959_22160_38008_37881; BAIDUID_BFESS=5BD1E18F26C99C474CBF657F9BFE8E94:FG=1; BA_HECTOR=80a525252l25802k8gak80cm1hti1tj1k; ZFY=4FqlPnyLIPotxkI3R:A210HBtobhjXTBC0bgQi81wOEg:C; PSINO=1; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1675167679; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1675167691; ab_sr=1.0.1_NjA2OTc1NTExMzNiMDMwZmFiNzU3MzMxOTlhMDdjOTFlMTUwNjlhYmVhZTNjMmNiNjIyMGMzNjczMTc1YjMzYWY0OWU1N2FkNzliYzBlNzgxMzJjOWE2Njc0M2MwNmQ5NzRkMzJmOGIyMDhlMWYzMDA4Yjc2MGVkZDg4YzZiOWU4ZWNmZTk4ZmUyM2QwYThjZDJiNjhiNzVmY2M3MzA1MA==',
            'Host': 'fanyi.baidu.com',
            'Referer': 'https://fanyi.baidu.com/?aldtype=16047&tpltype=sigma'
        }
        data1 = {
            'from': 'zh',
            'to': 'en',
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': sign,
            'token': 'cc2084f412caf4609ffe9491ed85e4c3',
            'domain': 'common'
        }
        data2 = {
            'from': 'en',
            'to': 'zh',
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': sign,
            'token': 'cc2084f412caf4609ffe9491ed85e4c3',
            'domain': 'common'
        }
        answer = input("1.中译英   2.英译中\n")
        if answer == '1':
            data_end = data1
        elif answer == '2':
            data_end = data2
        else:
            print("您的输入有误！")
        response = requests.post(url=url, headers=head, params=data_end)
        data = response.json()['trans_result']['data'][0]['dst']
        # data1 = response.json()['liju_result']['tag'][0:]
        # print("翻译后的结果有：")
        # for i in data1:
        #     print(i)
        pprint.pprint(data)

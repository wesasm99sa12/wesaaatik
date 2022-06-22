#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------  
print ('Coded by : ZEYAD , TRUKI')
print ('Telegram : @W518Z , @T_K_W')    
# ---------------------
import os
try:
    import requests,random,threading
except ImportError:
    
    os.system('pip install requests')

token = input('YOUR TOKEN ? :')
id = input('YOUR ID ? :')
class SystemThread:
    def __init__(self, thread, function):
        self.thread = thread
        self.function = function
    def threads(self):
        for self.i in range(self.thread):
            threading.Thread(target=self.function).start()

class TikTok:
    def __init__(self,sessionid,len_user,thread,token,id):
        self.len_user = len_user
        self.sessionid = sessionid
        self.thread = thread
        self.token = token
        self.id = id
        
    def check_user(self,):
        while 1:
            username = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890_.') for i in range(int(self.len_user))) 

            self.url = 'https://www.tiktok.com/api/uniqueid/check/?aid=1233&app_name=tiktok_web&app_language=en&device_platform=web_mobile&region=US&os=android&referer=https%3A%2F%2Fr.search.yahoo.com%2F_ylt%3DAwrCmuPWnTtiV24A6g1EDN04%3B_ylu%3DY29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3Ny%2FRV%3D2%2FRE%3D1648102999%2FRO%3D10%2FRU%3Dhttps%253a%252f%252fwww.tiktok.com%252fsignup%2FRK%3D2%2FRS%3DYstolUyq.2PwTGW..ekCsWmHw3w-&root_referer=&cookie_enabled=true&screen_width=412&screen_height=915&browser_language=ar-AE&browser_platform=Linux%20aarch64&browser_name=Mozilla&browser_version=5.0%20%28Linux%3B%20Android%2011%3B%20SM-A217F%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F96.0.4664.46%20Mobile%20Safari%2F537.36&browser_online=true&timezone_name=Africa%2FCairo&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=14&battery_info=0.16&unique_id={}&fromWeb=1&msToken=ysUoEQTInBWJTbQdwUX5lGMnjjEdje0POVBhI45L1mbCXB36tOjhDagbgZmXOuE8hNggY2HWPo4lgEtzoKq2bu0sQBPibmNWjCL88cf4cXr0R2JNef5tQZDi_MokgZ0UWETmdGQ=&X-Bogus=DFSzswVLYuxANjDNSRt57YW5ZE0i&_signature=_02B4Z6wo000018L73SwAAIDCqOAH0tbNq8fC-9mAAJKO30'.format(username)

            self.headers = {'authority': 'www.tiktok.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
                'x-secsdk-csrf-token': 'DOWNGRADE',
                'x-mssdk-info': 'oT0rndoJgm9TUKAld8kieVVjmil5rzWQ6c6W39g3FKJCHInVLvkFHBTz8KA-Tfb1pJQEyFFY.xz3TupWsTbG7evntsmv4MsI3lC18cQH2-8eO6h6.iD1.ma2-Qm8QupUjB33t0j6Dx7c8UWU1jr4p1d3uwL-Be8cNKUXeX0MAiGHh7GRHG3sylmMhY4agy6rShUuTIoTi5S5EC4Fn1Zp4BaWzdq8APrOG3TN2T6M669dPfzLaYbNdCcBIiooqSrD3UUxODo0uCuIHJheLtspMDBB8FTEcM.Sjo5AX8usuiPsYLyH.saPj5HLcEDXMS8OCJipEvURa04B4GpnoedbPpTmt2lQ23KHRH10SxPjznxbNbqUlqhQAJfQpuX5EEOb2Lt5MtCDRM3Iez6JfhpJTReYSxTGNzqs90Cy1Sip3sQ9ma3gfnD.YQbFYvDeZro3a2cDD1H30DuicjrLUTPIVcmriKRz5KZt7qvwBKZkODdemUh6Zo.m5kGSnjSwGGX1MRzhqW2iRKcZtPwRl6CzDlfCVHy7Ot6MKIZni2UKXdpJ.IYbBwddFY1RLIizEMaVBeUkrkgbahsKYF.ezKmvd.JH1uIiyBWgHMqWIprfMU6n12E8buyX-iYxfRkvFn4NUd18.ltnQ3kE2hwx4UWkRMQBVljTNZyk0qPg2s0tlenf77uHVByct17rIDGzDh.FsVZ9tNvbNPFYfgbqXQRBHOuKU0zakTNeeGyLURDADSgnLO43Ma6c.drP1vchOoNAISkpSGT7rOqM8d-XUSqPZzXMcciOkeCFtnZbkcFjaNmMdjnxlQzRHLg8mA5-QLN353bz5rGa6RORzfZakuO0KawE4hcd7TrzD6H78n8xy8WCgEPS6UpvGJDKk9t4sDCO4MxlcpRbxiwD6Gj5qaVMdEFHrlDGCtk5bQVNE9AykdATv7AkuTktbhVAErYFzBFbZKFu-YZX4peA3Kd5zYaJDrL8Y4dFsTOFHBdwQmOV4rpKWZZJk1FinMlg0ZakSq87E1UZoASUWrne4aZzJma7.ls-t.67hEdTzSBmkGbXwnkUpm7TgLQFDScdjc3iUZHzEHwwL5ctmhejqavo4PVRsU.5XtZ4WHVPO5YHfWZ4-5SKb0B6hi.u8jwWPEfPlwTcXWGFg3PUTie86QiYeEu3mU3uD2mAOHUsZsK-OChS2XHzudyYcd6Jr7wBU1JxJ5hqAazeVQKfio1-ZaAQjuUJc8ku8RQVFKxrRU06sGD-EsfbeKcva46HGFv8qszUk-SB.NJxdiuu3VJwZ3-fHAX5sg429gULA.Uvnos8gABK-FKWfLNfG-dmC9o06MWMGlJnoF1gBjh9U3JmG1ouO0vcOwug4iqvXyk9iHba8.WFS63rAVOXJeAgYpky6ZCnq7tn9M7hNkVkku3sW.M9MLQacAJdlodiR01UzbcGStmKFuXUflpjrNgksKnHgeqFnOiwclGyTq9OwghBGjHC5MZyJkvvy7uy8nQ7qbF9ZssqR88.SCA5PHRGOQcaEufABUM6TH.rkkoQKASpv41THBd7l0s1VedA-NeA9xsa0FdboEkvDsk3x25xyltKSho8-fJNXTBlTENMokcSJkKNzYxoAGxV1SLKAZuL6hlZQCJYLMcx5KJU5FMdb-nUgp1y0QTAyPgnVgVZHdHFBs9vFWknS3cW8i3Kym4jAClBYwyR6wWmL2b8nP4iNEWXRuFwrL6buipZUrxs7DGiOaXPF0JEIztZ20w2wbdY6mlS9Y77rI1PldH7eOM92bMcpOLbu-rmPCPveTJaS4KW0.7-5fCLch.NczYdeL816ZuLdMJHv2Me.l6WW8ZNwgTLl-EmAXOzD36bUxTLjU3sQ5zmyMkdBfads0aQ1wvNThc8f5qH-qU5HQ073bVMrNb2bhPMGaZKH-pimRCIwL3RLR77iJ4R5kFmNY7vsOJwFAs5I5.ku4OCo-GJxGYz4nr2bxo-j-qZdXEdbbrSDg4MNtaT7sq8.Ehj0jm6Kmmcjfe5gO5L7CmOyqU6Q5GUH.TbOdsnxejXZnT.m4YGWx01dnckH9qWau3n59onGJn1q1JKcIBpdPECuIvQK9zOUnhu.BmidJBZDnJI7mBdSn.yfQQe-36se-TyAS8qVHM.NmYd9Ax32BMJDBWJTU.X3Puv-D4jhmWlLudWgOMS.mg4LsytYAgMIuC7l.sviTH0BiSIpoMa08BX3x5whaaFEbVtf2FdjG6diy0LXMgJmFYCDm8ZlYx4UnkAzqwt5pd3.9.oodonkO0PVMusSI6gFU2hncmhCkSEU5DOA3Bb7VZNV7ol5scDnw3li7exwgjzf8-xtdd0RFs1nSS1Ma07YN8U.QnDj57Xmncj2D4HMnHXemcaEI.u9oXzZTi.nSHwcGv13o.QQpgH6fecrucwBLwHWDaPRRjoLrjBJZcxwM7-jcDHK4sInKPIl-hy57euUz41nH6zIj2B1.HLDjkh9gYWpjL.dimy6Y1x7zZleTtDel1JOIa8lG-t3Q5W2DmVDpuwjeuMfer-ap8=',
                'sec-ch-ua-mobile': '?1',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36',
                'sec-ch-ua-platform': '"Android"',
                'accept': '*/*',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.tiktok.com/signup/create-username',
                'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,de-DE;q=0.6,de;q=0.5',
                'cookie': 'cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22version%22:%22v5%22}; _gcl_au=1.1.1971411428.1647902591; _fbp=fb.1.1647902595441.111920142; tt_csrf_token=Fw3fw-DdRxSyfwtkBQoIe-wv; _abck=E6745FA2A7B39941F6BE559F7D9A7415~-1~YAAQLAXMxGqhm7Z/AQAA1YqPuAfeMbJUJTTbB3b+5mXaF3mCFZeqRK9V2vy1twKn+kNKeiWXrM1QzqaL78w5vWiVJixdCyg/0wPq+0n1uU3r7FUDWSMydF8xUwRTNoEcSz9zVSs0OF6q00zEQnXwSaMcUMNHyIdDCzYfFY/jWlaRlufktL5/hlBCRnw9E1WB/J5yx1FfttrkgDyp3snGdE2oXKvcN0Tvq7+t8hek1Po45QZd4+bq4Vk1pIR4/HXxEqP2Ko/wP2Vk8xiM/w6JzIxUOPSsgjoqid63AHWz2jL9scvAUWTbdFeXqtuhviEooDyxilMVeTFpiyik4KLnC9l1OVI1kl7CfMV86WoSchYKFo5xRoVNITUxEAG3sqLLh85iKHvg9PUaKRU=~-1~-1~-1; bm_sz=15330E997CC6037B9A79E02A73597C62~YAAQLAXMxGuhm7Z/AQAA1YqPuA8rxJWbm8p7r97MXQlfPDiE9dXv3WgUXXWl8xgOpPu18PmJOfoPQ+ijR3aoTCqBWe36n2QP/tKZJjDgXwrZOlYD4jZAb6uz2i8AKhwtep3Hn93/+RgJoEkKcL12gOQmAOSxefWpg+c5DESidKf70Ie07dxS8dG/C/vU2ISGOclmGeTzn+9cUIRIrsuezGdjlu9xFbZnkXJWrpu4vydCTFNEydVNRzGrTqAKMu9YBWABBdsTGfMDEmbGrwfiqaygYdJ+uKI68I4ime2x7F4L/7Y=~4343110~3556664; ak_bmsc=8ED48C806E90D93118654F76785A69C4~000000000000000000000000000000~YAAQFwXMxD5wGLZ/AQAAdLjEuA+0Bd3U/MwpeQFvxYLYN1gbDpl3Nt19/R3TH0tKjV+xlWwQnueuPva0oR0FsawjSgV/hCmDr6cErM0otGQ69S0dfiGtpDSy/jzyjGr8q0dur4FYVhvox1bQnxwtidyg3GUga0uvRYBrXqgeSWI5HAQIaGMYa5lDUBkLl6HiQyDHLKBJdu6vQ8/Z2hgS2+VbLlaenga0pUkm19ojJqbdRi6WghpV3Uw1hmtoQYQ6sTA7t06hzzJiMJlHMtrdPXcDAwSzHzjzGqLPprwrxuSGnLcQ13wkVemCw14tGEoW9ze9XGMauvnbetw5d55jXmgKOoALiKG2nWYrvpYMLUPGpUAVIQ39F459vqrQq2hs0Z9+HLi8Opog+Zt7; __tea_cache_tokens_1988={%22_type_%22:%22default%22}; passport_csrf_token=e65a9aa6991b95e7d83817dd823a30de; passport_csrf_token_default=e65a9aa6991b95e7d83817dd823a30de; bm_mi=248C3C3F196C8ECF7E7FD1786B838821~TOsH3qU1H1H+KCH5MVwbGuCpcrypqeVdeT8IEktL6ffeRIY/K+Rb+F/48D0935JlwQi33KBD+1/dXuv5G3BFFTRGaZui4B8dy3WhK2bJ85vCrYlcGPWI/to295TtegE1/t//zlnwTJAya3PF41YITY2pNH5s73PiYUkoojI/rhSiv83Nu78fi8oTHiBPsDrEb0hlRbWFoMKT8sCUprkO/zyagJ7+TmwK2eiCKoseeDI=; ttwid=1%7CmXfcDAsUTVtBTVUYVCFnvDNYjbUaU1VToHLYDAPnu1U%7C1648074207%7Cc9f084e56679b5f383d406072a4acadf1403d333ff5bb51e5340ce56b8fca70b; msToken=h0CVF8uab1aNf_1kMYVvNMzNmvdg0dKM3OSHjn5m04lbTL2pFXfFdfb877RXAUj9cMkZgOnsmVYv9TvnR9vnG5WeF7Q6ZrSMDRrj_FKjAXYGgC4svumzv5eqbSEnt4VeyycUOeE=; d_ticket=07c38aba8fbdcff33fde5d55d75340c7ac460; cmpl_token=AgQQAPNSF-RO0rIFcwspfx0S-FbCCv4Yv6nZYMC4dA; passport_auth_status=d50315c53b97ce4c0b31a5cb08ef72fa%2C; passport_auth_status_ss=d50315c53b97ce4c0b31a5cb08ef72fa%2C; sid_guard='+self.sessionid+'%7C1648074291%7C5184000%7CSun%2C+22-May-2022+22%3A24%3A51+GMT; uid_tt=7e79b1ffef87d9e73b5cd616f8fc0b5d1daa74b4929809ef0369f4fd835ff7b2; uid_tt_ss=7e79b1ffef87d9e73b5cd616f8fc0b5d1daa74b4929809ef0369f4fd835ff7b2; sid_tt='+self.sessionid+'; sessionid='+self.sessionid+'; sessionid_ss='+self.sessionid+'; sid_ucp_v1=1.0.0-KGYxNWVjNDM1NTMxN2FiMTdkNGEzNDM0ZjY1ODVlYmQzNjRiYjE3YTkKIAiriLeKyrXnnWIQs7zukQYYswsgDDCyvO6RBjgCQOwHEAQaB3VzZWFzdDUiIGQ4MWU4YjhiZDVkYzE5M2VjNjE2MGNmYWQzMGQwYTYz; ssid_ucp_v1=1.0.0-KGYxNWVjNDM1NTMxN2FiMTdkNGEzNDM0ZjY1ODVlYmQzNjRiYjE3YTkKIAiriLeKyrXnnWIQs7zukQYYswsgDDCyvO6RBjgCQOwHEAQaB3VzZWFzdDUiIGQ4MWU4YjhiZDVkYzE5M2VjNjE2MGNmYWQzMGQwYTYz; store-idc=useast5; store-country-code=us; tt-target-idc=useast5; bm_sv=B6D089612AABD04B865FBBF8D4EF0BA6~+6fc5lnXWBVNukYE0gv/AJxisicjqHNXfyjRpTzk01cFmYNSofAGhmM52R+jdrMxItkgXahfzJkYWMVqTZIEHy+LaxJHqKwMB71AML8QybpR7mm0+f5WLDFzZHj6vz0RUQ4lUypYzsx08EHEXzNC1R5/rJpfuBWcUg0s0wa8f88=; msToken=ysUoEQTInBWJTbQdwUX5lGMnjjEdje0POVBhI45L1mbCXB36tOjhDagbgZmXOuE8hNggY2HWPo4lgEtzoKq2bu0sQBPibmNWjCL88cf4cXr0R2JNef5tQZDi_MokgZ0UWETmdGQ=; odin_tt=7b675990488c7036a958110fe44160dc563b5674dd7adc7dfc38b12072f6614a48ddde1d9edfec8748ce739ed8d3d57c0699a9aa634ced3a378b0af87bc28c58'
                }

            self.req = requests.get(self.url, headers=self.headers)
            if '"not_unavailable":false' in self.req.text:
                print('\n[!] Tis user is Not available:{}'.format(username))
            elif '"is_available":true' in self.req.text:
                print('[+] Tis user is available:{}'.format(username))
                self.reqt = requests.post("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(self.token,self.id,username))
    def start(self,):
        for i in range(int(self.thread)):
            threading.Thread(target=self.check_user).start()
x = TikTok(input('Sessoinid:'),input("User length:"),input("Thread:"),token,id).start()
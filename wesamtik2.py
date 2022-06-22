import requests 


ZT =input('''
 Telegram : @W518Z,@T_K_W,@STORE_ZSM

  instagram : @w518z , @i18r6

CODED BY : ZEYAD , TRUKI


                                     --------------------------
[1] سحب سيشن ايدي انستقرام

[2] سحب سيشن ايدي تيك توك
                                     --------------------------

''')
if ZT=='1':
	
	
	
	
	username = input('YOUR USER : ')
	
	password = input('YOUR PASSEORD : ')
	url = 'https://www.instagram.com/accounts/login/ajax/'  
	headers = {
	    'accept': '*/*',
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-length': '275',
	    'content-type': 'application/x-www-form-urlencoded',
	    'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=YMdanwAEAAHbGwbzL3d_mjVac16b; csrftoken=voNeU14Q1AMv8Sg3TtyFW2KA2UkSJlpL;',
	    'origin': 'https://www.instagram.com',
	    'referer': 'https://www.instagram.com/',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
	    'x-csrftoken': 'voNeU14Q1AMv8Sg3TtyFW2KA2UkSJlpL',
	    'x-ig-app-id': '936619743392459',
	    'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',
	    'x-instagram-ajax': '0c15f4d7d44a',
	    'x-requested-with': 'XMLHttpRequest'
	}

	data = {
	    'username': f'{username}',
	    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
	    'queryParams': '{}',
	    'optIntoOneTap': 'false'
	}
	
	req_login = requests.post(url, headers=headers, data=data)
	if 'authenticated":true' in req_login.text:
	    get_sessions = req_login.cookies["sessionid"]
	    print(f"[#] {username} Logged in √\n")
	    print(f"[+] sessionid: {get_sessions}\n")
	
	    with open(f'{username}.txt', 'w') as file:
	        file.write(f'{get_sessions}')
	        file.close()
	        print(f"[$] Saved as {username}.txt")
	        exit('See You ..') 
	
	
	elif "checkpoint_challenge_required" in req_login.text:
		
		print(f'[-] Your Account Scuate >>{username}') 
	#____________________________
	else:
	  print(f'\n\n[!] Login Error >> {username}') 
	  exit('See you ..')

elif ZT=='2':
	
	email = input('YOUR EMAIL : ')
	passw = input('YOUR PASSWORD : ')

	url = 'https://api2.musical.ly/passport/user/login/?mix_mode=1&username=1&email=&mobile=&account=&password=hg&captcha=&ts=&app_type=normal&app_language=en&manifest_version_code=2018073102&_rticket=1633593458298&iid=7011916372695598854&channel=googleplay&language=en&fp=&device_type=SM-G955F&resolution=1440*2792&openudid=91cac57ba8ef12b6&update_version_code=2018073102&sys_region=AS&os_api=28&is_my_cn=0&timezone_name=Asia/Muscat&dpi=560&carrier_region=OM&ac=wifi&device_id=6785177577851504133&mcc_mnc=42203&timezone_offset=14400&os_version=9&version_code=800&carrier_region_v2=422&app_name=musical_ly&version_name=8.0.0&device_brand=samsung&ssmix=a&build_number=8.0.0&device_platform=android&region=US&aid=&as=&cp=Qm&mas='
	head = {
		'User-Agent': 'Connectionzucom.zhiliaoapp.musically/2018073102 (Linux; U; Android 9; en_AS; SM-G955F; Build/PPR1.180610.011; Cronet/58.0.2991.0)z',
		'Host': 'api2.musical.ly',
		'Connection': 'keep-alive' }	
	data = {
		'email': email,
		'password': passw }
	rr = requests.post(url, headers=head,data=data)

	if 'user_id' in rr.text:
		
		Oxkaito = rr.json()['data']['session_key']
		print(f"[#] {email} Logged in √\n")
		print(f"[+] sessionid: {Oxkaito}\n")
	
		with open(f'{email}.txt', 'w') as file:
			file.write(f'{Oxkaito}')
			file.close()
			print(f"[$] Saved as {email}.txt")
	
			exit('See You ..')
			
	else:
		print(f'\n[!] Login Error >>{email}')
	
# Telegram : @W518Z , T_K_W , @STORE_ZSM
# instagram : @w518z , i18r6

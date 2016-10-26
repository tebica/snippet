import urllib2
import xmltodict

BASE_DIRECTORY = "/home/tebica/htdocs/earlybird/temp/weather/"
#BASE_DIRECTORY = ""

dic = {
        'seoul':'10015',
        'kangwon':'10142',
        'chungcheong':'10273',
        'kwangju':'10063',
        'daegu':'10043',
        'jeju':'10265'
        }

def writewether(city, code):
        file = urllib2.urlopen('http://kapi.kweather.co.kr/getXML_today.php?region='+code+'&app=LifeStyle_ios')
        data = file.read()
        file.close()
        data = xmltodict.parse(data)

        f = open(BASE_DIRECTORY+city+".json", 'w')
        contents = "{ \n \"pm10\": %s \n }\n" %data['today_weather']['pm10']
        f.write(contents)
        f.close()

for city,code in dic.items():
        writewether(city, code)

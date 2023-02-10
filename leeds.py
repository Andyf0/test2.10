


from cgi import print_arguments
from urllib import response
import requests
from lxml import etree
import time
from playsound import playsound

url = 'https://tickets.leedsunited.com/en-GB/events/leeds%20united%20vs%20manchester%20united/2023-2-12_14.00/elland%20road?hallmap'

headers = {
        'cookie': 'os=true; gid=d6Sijgi3AkepIqLkkuleug==; __gads=ID=69d965835b6fbd56:T=1662139225:S=ALNI_Mbi3mFUBVgtWO03UknpglKINOESRg; undefined=22bd8112-9f91-4a93-a077-8852a9be2d45; _fbp=fb.1.1663110162347.1641109692; __qca=P0-235706501-1666963965510; cto_bundle=zdw2S19GZFB6eHd6R25zaiUyRnF6QjBxdGVHZm96ZWhubCUyRmh6czVwaXdocEFUZFE2b0NQaU1PSHdFcXFKVUtKNVU5ekxlbjFaTGdRQ2JxZUYlMkZhUW55QkZyUkZ5TzA0QzEyQUkzZHkwZVlGNUVoNzFoVkNJTk5WTVBJMHlZbXpiJTJGcXZlODhDeXpzZyUyRnZCdUU4VW1BbVV3akkzTE4lMkYyRHJCQVFlQjk3WWRhY21MaldVYUdIUFJ2allUb3hTOCUyQngwZTB4MzFNNU5tWXpHOVczcXV0YURhQkV3cFR3c1ElM0QlM0Q; cto_bidid=42GsJF9tdThHUGhaNjVydmJRY29YbHpHc3FubEF6Z2xTcFhRaXRjUHNoUkhXUHVJSmI5ZGQ2d2JpYVpLRzlrVWJZMlRFJTJGQkxhUEdhMTFYRiUyRm8lMkJ5RE1OQUJzJTJGQXdFb1B6dUpvOVhpNmFEWW5KTTN2TFJVdjNIQmRFOENQTWY4bkpKRkw3bHJYVVJnVDdSQjZ1WlFpOElxcjU4ZyUzRCUzRA; GlobalE_CT_Data={"CUID":"408766729.531172201.859","CHKCUID":null}; rm=/; crmAuth=Py3Av2zte7ozPV9+yPBi3XD3iJrgD1OorpCpQ1olBfg=; _ga_DXPTTFT9C0=GS1.1.1674002014.8.1.1674002078.0.0.0; _ga_SBGWRTJS34=GS1.1.1674095818.5.1.1674095833.0.0.0; _ga=GA1.2.773448381.1662139223; _gid=GA1.2.1430597739.1675421274; QueueITAccepted-SDFrts345E-V3_lufcq09feb20231pm=EventId=lufcq09feb20231pm&QueueId=00000000-0000-0000-0000-000000000000&RedirectType=afterevent&IssueTime=1675992554&Hash=6077773685dd4ad8dac25e60f6bdbcbe9c22d72f7dd45847d2dbbfb274811731; __gpi=UID=00000b1750a206ee:T=1666963967:RT=1676034890:S=ALNI_MZOnLJ5qr1-Cap6xeHKTmz1EAem7g; af=o40hZWktsXg=; ASP.NET_SessionId_=bybjhi0pyap4ebmrj14izkxk; os=true; cs=3cQ6dDLq7onSay3nCfQwJ7Is; inMobile=false; _gat=1; QueueITAccepted-SDFrts345E-V3_lufcqsafetynet=EventId=lufcqsafetynet&QueueId=410d421f-852f-475d-85e7-93b0d3d601a4&RedirectType=safetynet&IssueTime=1676038210&Hash=2923315cd7edf18ba83ff1b0b5d8c32e02ca79d8eda7717f3b33d1e0cdf3c20c; __atuvc=42|2,105|3,0|4,133|5,966|6; __atuvs=63e6503f620cb45b002; AWSALB=UOsZ+mLIUDwOyjjT138uKTNoQSO4D3GzJlrSVLl349x5zkH2kvp7odDSd75B3LTu5JLjbAXJqcg4pe8PSqQHWaXZAEtdh7g6hQTl//I6kLMDAn/gF0WJ1/jvmlJn; AWSALBCORS=UOsZ+mLIUDwOyjjT138uKTNoQSO4D3GzJlrSVLl349x5zkH2kvp7odDSd75B3LTu5JLjbAXJqcg4pe8PSqQHWaXZAEtdh7g6hQTl//I6kLMDAn/gF0WJ1/jvmlJn; datadome=0tnPwGxLQvUeDwEkDdf8gPXJU4E6QfoHY~LJ_DQ0J7dXo9pHbSJayzdd~b8G5hRDwCQVsVLtVGfs6GVtdn2I7O6WgDtDG2On~64aidvEgxqkLDsDJHBbZbfHFl_MOclJ',
        'referer': 'https://tickets.leedsunited.com/en-GB/categories/home-games',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

def get_tickets(A):
    response = requests.get(url=url, headers=headers)

    tree = etree.HTML(response.text)

    # //*[@id="v_ec2f8da9-45f2-ec11-83ae-e8f0eca6b7fa__vfaParent"]/map/area[contains(@class,"red")]/@alt
    A = tree.xpath('//*/map/area[contains(@class,"red") or contains(@class,"yellow")]/@alt')
    return A

def Refresh(A):
    for i in range(len(A)):
        name = A[i]
        if A[i] == "C18":
            name = '有18去买票！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        elif A[i] == "C19":
            name = '去买票！！！！！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        elif A[i] == "C20":
            name = '去买票！！！！！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        elif A[i] == "C21":
            name = '去买票！！！！！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        elif A[i] == "N2":
            name = '去买票！！！！！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        elif A[i] == "N3":
            name = '去买票！！！！！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        elif A[i] == "N4":
            name = '去买票！！！！！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        elif A[i] == "FA4":
            name = '去买票！！！！！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        elif A[i] == "FA5":
            name = '去买票！！！！！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        elif A[i] == "FA6":
            name = '去买票！！！！！！！' + A[i]
            print(name)
            playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
        else:
            name = 'None' + '-' + A[i]
            print(name)
            #playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')



if __name__ == '__main__':
    while(1):
        for k in range(10000):
            response = requests.get(url=url, headers=headers)
            tree = etree.HTML(response.text)
            A = tree.xpath('//*/map/area[contains(@class,"red") or contains(@class,"yellow")]/@alt')
            
            Refresh(A)
            #playsound('/Users/fengweihua/Desktop/Code/Crawl/noti.mp3')
            k = k+1
            kk = str(k) + ('-'*70)
            print(kk)
            #print('-'*60)
            time.sleep(1)



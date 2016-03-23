from facepy import GraphAPI
import json

def get_message(url, cnt, flag, messages):
    print cnt
    if cnt <= 0:
        return 
    page = graph.get(url)
    print page
    if (not flag and page['data'] == []) or (flag and page['posts'] == []):
        return
    if flag:
        for eachMsg in page['posts']['data']:
            if 'message' in eachMsg:
                messages.append(eachMsg['message'].encode('utf8'))
        _url = page['posts']['paging']['next'][27:]
    else:
        for eachMsg in page['data']:
            if 'message' in eachMsg:
                messages.append(eachMsg['message'].encode('utf8'))
        _url = page['paging']['next'][27:]
    #print messages
    if _url == "":
        return
    get_message(_url, cnt - 1, False, messages)


def get_it(pid, num):
    id = pid
    consulta = 'posts{message}'
    url = id+'?fields='+consulta
    print url
    path = 'F:\\paper\\myPython\\py2.7\\new_data\\' + id + '_msg.txt' 
    messages = []
    output = open(path, 'w')


    count = num #pages number
    get_message(url, count, True, messages)
    for each in messages:
        output.write(each)
    print 'Number of messages is '+str(len(messages))
    print json.dumps(messages[:20], indent=1)
    output.close();

accessToken = 'CAACEdEose0cBAKugqg3xatAoBKizpZCow4XIl5TxZCkINoN7ZAaQG71il2Ns7W0PgDaEaZCzV6ZB1c9NnuZCSrWntpvfwNWUWN77GgKsl3t82kJbhHBL2l8eZA42Q6A7Nu00FXYxZBzTh5EIUjE1YnSZCXNN54MYFikPRvkfO84jPlE5txNgZADzJl0KnRZCyxOb57KoYro5VDmbuevBWFJznYc6CxgDR62ZBOEZD'
graph = GraphAPI(accessToken)
user_data = ['chelseaclinton', 'Kobe', 'billclinton', 'BillGates', 'georgewbush', 'michelleobama', 'barackobama', 'TaylorSwift', 'adele', 'brunomars', 'avrillavigne', 'kellyclarkson', 'beyonce', 'AdamLambert', 'brunomars', 'floydmayweather', 'usainbolt', 'vettelclub', 'SebastianVettelOfficial', 'Cristiano', 'LeBron', 'MoFarahGold', 'Tiger', 'SerenaWilliams', 'TheRealRonnieOSullivan', 'rickymanningmusic', 'CP3', 'MikeTrout27', 'emmawatson', 'danieljacobradcliffe', 'JenniferLawrence', 'ashleytisdale', 'ZacEfron', 'NicoleKidmanOfficial', 'katyperry', 'JasonStatham', 'MeganFox', 'ashleytisdale', 'TaylorLautner', 'kesha', 'LindsayLohan', 'PaulWalker', 'HughJackman', 'robertdowneyjr', 'VinDiesel', 'WillSmith', 'taylormomsen', 'ladygaga', 'pink', 'Beckham', 'IceCube', 'VanessaHudgens', 'taylormomsen', 'LilJon', 'Diddy', 'ashleytisdale', 'TylerPerry', 'MayaAngelou', 'nelsonmandela']
#for each in user_data:
#    get_it(each, 15)
get_it('ashleytisdale', 15)


import random
import json
import hashlib
import time

# # query-api  (post productId to you, get record like this)
# s1 = '''
# {
#     "productId": "xxxxxxxxx",
#     "productName": "xx",
#     "birthplace": "xxxxxx",
#     "modified": false,
#     "infos": {
#         "weatherInfo": [
#             {
#                 "date": "dd-mm-yyyy",
#                 "temperature": "xxxx",
#                 "atmosphericPressure": "xxxxxxxxx",
#                 "relativeHumidity": "xxxxxxx",
#                 "evaporate": "xxxxx"
#             },{
#                 "date": "dd-mm-yyyy",
#                 "temperature": "xxxx",
#                 "atmosphericPressure": "xxxxxxxxx",
#                 "relativeHumidity": "xxxxxxx",
#                 "evaporate": "xxxxx"
#             }
#         ],
#         "transportInfo": [
#             {
#                 "from": "onePlace",
#                 "to": "anotherPlace",
#                 "time": "dd-MM-yyyy hh:mm:ss"
#             },
#             {
#                 "from": "onePlace",
#                 "to": "anotherPlace",
#                 "time": "dd-MM-yyyy hh:mm:ss"
#             }
#         ],
#         "machiningInfo": [
#             {
#                 "place": "xxxx",
#                 "machining": "sssss",
#                 "time": "dd-MM-yyyy hh:mm:ss"
#             },
#             {
#                 "place": "xxxx",
#                 "machining": "sssss",
#                 "time": "dd-MM-yyyy hh:mm:ss"
#             }
#         ],
#         "saleInfo": {
#             "location": "some supermarket",
#             "price": "xxx"
#         }
#     }
# }'''
#
# # query all change logs
# s2 = '''
# {
# "changeLogs" : [
#     {
#         "productId": "XXXXXXX",
#         "changeId":"sssssss",
#         "status":"voting/closed",
#         "time":"dd-MM-yyyy hh:mm:ss",
#         "launcher":"gov/com/cit",
#         "intention":{
#             "gov":"unvoted/reject/agree",
#             "com":"unvoted/reject/agree",
#             "cit":"unvoted/reject/agree"
#         },
#         "reason": "xxxxxxx",
#         "solution":"sssssss"
#     },{
#         "productId": "XXXXXXX",
#         "changeId":"sssssss",
#         "status":"voting/closed",
#         "time":"dd-MM-yyyy hh:mm:ss",
#         "launcher":"gov/com/cit",
#         "intention":{
#             "gov":"unvoted/reject/agree",
#             "com":"unvoted/reject/agree",
#             "cit":"unvoted/reject/agree"
#         },
#         "reason": "xxxxxxx",
#         "solution":"sssssss"
#     }
#     ]
#     }
# '''
#
# # create voting (post this to you)
# s3 = '''
# {
#     "productId":"ssss",
#     "launcher":"gov/com/cit",
#     "reason": "We suppose these are suitable to you",
#     "solution":"recommend"
# }'''
#
# # this is a vote (post to you)
# s4 = '''
# {
#     "productId":"xxxxx",
#     "changeId":"ssssssss",
#     "org":"gov/cit/com",
#     "intention":"reject/agree"
# }'''

Privences = ['BeiJing','TianJing','ShangHai','ChongQing','HeBei','ShanXi','LiaoNing',
             'JiLin','HeiLongJiang','JiangSu','ZheJiang','AnHui','FuJian']

Names = ['Vegetables', 'fruits', 'meats', 'rice', 'other']

Modified = [True, False]

supermarket = ['Walmart', 'Auchan', 'ShiJiHuaLian', 'TESCO', 'Others']

machining = ['Washing', 'Package', 'Disinfection', 'Cutting', 'Grinding']

status = ['Voting', 'Closed']

launcher = ['gov', 'com', 'cit']

intention = ['unvoted', 'reject', 'agree']

def main():
    random.seed(time.time())
    nums = eval(input("Please enter the number of Transactions you want to generate: "))
    count = eval(input("please enter the number of items: "))
    for i in range(nums):
        startGenerate(count)

def startGenerate(count):
    new_dict1 = {}
    new_dict2 = {}
    new_dict3 = {}
    new_dict4 = {}
    ID = genHashCode()      # one ID for one file
    changeID = genHashCode()

# dict1
    new_dict1['productId'] = ID
    new_dict1['birthplace'] = genPlace()
    new_dict1['productName'] = genName()
    new_dict1['modified'] = genModify()
    new_dict1['infos'] = {}

    weatherInfo = []
    transportInfo = []
    machiningInfo = []
    saleInfo = {}
    for i in range(count):
        weatherInfo.append({'date': genDate(),
                            'temperature': (str(genTemperature()) + " oC"),
                            'atmosphericPressure': (str(genAtmospheric()) + " atm"),
                            'relativeHumidity': (str(genRelativeHumidity()) + "%"),
                            'evaporate': (str(genEvaporate()) + " mm/Month")
                            })
    new_dict1['infos']['weatherInfo'] = weatherInfo

    for i in range(count):
        transportInfo.append({'from': genPlace(),
                              'to': genPlace(),
                              'time': (genDate() + ' ' + genTime())
                              })
    new_dict1['infos']['transportInfo'] = transportInfo

    for i in range(count):
        machiningInfo.append({'place': genPlace(),
                                'machining': ' '.join(genMachining()),
                                'time': (genDate() + ' ' + genTime())
                            })
    new_dict1['infos']['machiningInfo'] = machiningInfo

    saleInfo['location'] = genSuperMarket()
    saleInfo['price'] = genPrice()
    new_dict1['infos']['saleInfo'] = saleInfo

#dict2
    dict2_lst = []
    for i in range(count):
        dict2_lst.append({
            'productId': ID,
            'changeId': changeID,
            'status': genStatus(),
            'time': (genDate() + ' ' + genTime()),
            'launcher': 'gov/com/cit',
            'intention': {
                'gov': genIntention(),
                'com': genIntention(),
                'cit': genIntention()
            },
            'reason': 'our reasons',
            'solutions': 'oursolutions'
        })
    new_dict2['Query_logs'] = dict2_lst

# dict3
    new_dict3['productId'] = ID
    new_dict3['launcher'] = genLauncher()
    new_dict3['reason'] = 'our Reasons'
    new_dict4['solution'] = 'our solutions'

# dict4
    new_dict4['productId'] = ID
    new_dict4['changeId'] = changeID
    new_dict4['org'] = genLauncher()
    new_dict4['Intention'] = genIntention()

    writeJson(ID, new_dict1, new_dict2, new_dict3, new_dict4)


def genHashCode():
    i = random.randint(0, 5000000)
    res = str(10000000 + i).encode('utf-8')
    return hashlib.md5(res).hexdigest()

def genPlace():
    i = random.randint(0, len(Privences) - 1)
    return Privences[i]

def genDate():
    #time.sleep(0.1)        #to generate different dates
    day = random.randint(1,29)
    month = random.randint(1,12)
    year = 2017 + random.randint(0,1)
    return (str(day) + '-' + str(month) + '-' + str(year))

def genTime():
    hour = random.randint(0, 24)
    minute = random.randint(0, 60)
    sec = random.randint(0, 60)
    return str(hour) + ':' + str(minute) + ':' + str(sec)

def genName():
    idx = random.randint(0, 4)
    return Names[idx]

def genModify():
    idx = random.randint(0,1)
    return Modified[idx]

def genTemperature():
    return 20 + round(random.uniform(-8, 5), 1)

def genAtmospheric():
    return 1 + round(random.uniform(-0.2, 0.1),2)

def genRelativeHumidity():
    return random.randint(30, 75)

def genEvaporate():
    return round(random.uniform(10, 120),2)

def genSuperMarket():
    idx = random.randint(0, len(supermarket) -1)
    return supermarket[idx]

def genPrice():
    return round(random.uniform(1, 50), 1)

def genMachining():
    num = random.randint(1, len(machining))
    res = set()
    for i in range(num):
        idx = random.randint(0, len(machining) - 1)
        res.add(machining[idx])
    return list(res)

def genStatus():
    idx = random.randint(0,len(status) - 1)
    return status[idx]

def genLauncher():
    idx = random.randint(0, len(launcher) - 1)
    return launcher[idx]

def genIntention():
    idx = random.randint(0, len(intention) -1)
    return intention[idx]

def writeJson(ID, dict1, dict2, dict3, dict4):
    fout = open(ID + '.json', 'w')
    finaldict = {}
    finaldict['OneTranc'] = [dict1, dict2, dict3, dict4]
    # json.dump(dict1, fout)
    # json.dump(dict2, fout)
    # json.dump(dict3, fout)
    # json.dump(dict4, fout)
    json.dump(finaldict, fout)
    fout.close()

if __name__ == '__main__':
    main()

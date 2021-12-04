import os


def getPortPID(port):
    with os.popen('netstat -aon|findstr '+port) as res:
        res = res.read().split('\n')
        result = []
        for line in res:
            temp = [i for i in line.split(' ') if i != '']
            if len(temp) > 4:
                result.append({'pid': temp[4], 'address': temp[1], 'state': temp[3]})
    return result

def killPortPid(PID):
    cmd = "taskkill -pid "+PID+" -f"
    os.system(cmd)

def killPortAllPID(port):
    result = getPortPID(port)
    if len(result)==0:
        # 没有结果的话
        return False
    result2 = ''
    for i in range(len(result)):
        for key in result[i].keys():
            result2 = result2 + '' + key + ':' + result[0][key]+' || '
        result2 = result2+ '\n'
    #print(result2)
    for i in range(len(result)):
        killPortPid(result[i]['pid'])
    return result2

def CheckPort(port):
    #检查端口是否在运行，没有运行返回FALSE，否则返回列表
    result = getPortPID(port)
    if len(result) == 0:
        # 没有结果的话
        return False
    result2 = ''
    for i in range(len(result)):
        for key in result[i].keys():
            result2 = result2 + '' + key + ':' + result[0][key] + ' || '
        result2 = result2 + '\n'
    # print(result2)
    return result2


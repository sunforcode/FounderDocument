import requests
import unittest,json
from assertpy import assert_that

ipPort = 'http://120.55.181.205:8080'
# studentOpenid = '8af5a8825c77333d015c77747ea100ab'
studentOpenid = '8af5a8825c77333d015c77635ee10081'
studentOpenidWeaknessID = '8af5a8825c77333d015c77635ee10081'
teacherOpenId = '8af5a8825c77333d015c77747ea100ab'
classid = '8af5a8825c7680c1015c76d8747d003e'
knowLedgeID = ""

def getStudentLearningStages():
    urlString = ipPort + '/external/cat/getLearningStages'
    r = requests.get(urlString)
    if r.status_code == 200:
        requestJson = r.json()
        if requestJson['status'] == 1:
            print('学生学习页面学段接口接口通过了\n'+ str(r.text))
        else:
            print('接口不通' + r.url)
    else:
        print('接口不通返回的状态码为'+str(r.reason) + str(r.status_code) + r.url)

def getAllStars():
    urlString = ipPort+'/external/learningCapacity/analysis/progress/standard'
    r = requests.get(urlString)
    if r.status_code == 200:
        requestJson = r.json()
        print('获取总的星值通过了' + r.url)
        print(requestJson)
    else:
        print('接口不通返回的状态码为'+str(r.reason) + str(r.status_code) + r.url + '\n')


def getStudentKnowledge():#获取学生学习能力

    urlString = ipPort + '/external/learningCapacity/analysis/student/knowledge/' +studentOpenid
    r = requests.get(urlString)
    if r.status_code == 200:
        requestJson = r.json()
        if requestJson['status'] == 1:

            print('获取学生的学习能力接口通过了' + str(r.text))
            print('获取学生学习能力' + r.url)
        else:
            print('接口不通' + r.url)
    else:
        print('获取学生的学习能力接口不通返回的状态码为' + str(r.reason) + str(r.status_code) + r.url)

def getClassStudentList():# 获取班级的学生列表
    urlString = ipPort + '/external/info/teacher/getClassStudent/' + classid
    r = requests.get(urlString)
    if r.status_code == 200:
        requestJson = r.json()
        if requestJson['status'] == 1:
            print('获取班级的学生列表接口通过了' + str(r.text))
        else:
            print('接口不通' + r.url)
    else:
        print('获取班级的学生列表接口不通返回的状态码为' + str(r.reason) + str(r.status_code) + r.url)
    pass

def getTeacherClassList():#获取老师的班级列表
    urlString = ipPort + '/external/info/teacher/getClassList/' + teacherOpenId
    r = requests.get(urlString)
    if r.status_code == 200:
        requestJson = r.json()
        if requestJson['status'] == 1:
            print('获取老师的班级列表接口通过了' + str(r.text))
        else:
            print('获取老师的班级列表接口不通' + r.url)
    else:
        print('获取老师的班级列表不通返回的状态码为' + str(r.reason) + str(r.status_code) + r.url)


def teacherGetKnowledge():#获取老师的知识点
    urlString = ipPort  + '/external/learningCapacity/analysis/teacher/knowledge/' + teacherOpenId
    r = requests.get(urlString)
    if r.status_code == 200:
        requestJson = r.json()
        if requestJson['status'] == 1:
            print('获取老师的知识点接口通过了' + str(r.text))
            dic = requestJson['data'][0]['entry_id']
            return dic

        else:
            print('获取老师的知识点接口不通' + r.url)
    else:
        print('获取老师的知识点不通返回的状态码为' + str(r.reason) + str(r.status_code) + r.url)

def teacherGetStudentLearning():#对班级中学生的某个知识点的学习情况统计分析接口
    catID = teacherGetKnowledge()
    urlString = ipPort + '/external/learningCapacity/analysis/teacher/classStudentLearningByCatId/'+classid + '/' + str(catID)
    r = requests.get(urlString)
    if r.status_code == 200:
        requestJson = r.json()
        if requestJson['status'] == 1:
            print('学习情况统计分析接口接口通过了' + str(r.text))
        else:
            print('学习情况统计分析接口接口不通' + r.url)
    else:
        print('学习情况统计分析接口不通返回的状态码为' + str(r.reason) + str(r.status_code) + r.url)

def studentWeakNess():#薄弱环节
    name = '薄弱环节'

    urlString = ipPort + '/external/learningCapacity/analysis/student/weaknessAnalysis/'+studentOpenidWeaknessID
    r = requests.get(urlString)
    # print(r.text)
    if r.text == "":
        print('薄弱环节收到的返回值为空')
        return
    if r.status_code == 200:
        requestJson = r.json()
        if requestJson['status'] == 1:
            print('薄弱环节接口接口通过了' + str(r.text))
            print(r.url)
        elif requestJson['status'] == 0:
            print(name + 'status 为0'+ requestJson)
            pass

        else:
            print('薄弱环节接口接口不通' + r.url)
    else:
        print('薄弱环节接口不通返回的状态码为' + str(r.reason) + str(r.status_code) + r.url)
    pass


def getResourceList ():#点学习以后的列表
    print('\n')
    name = '点学习以后的列表 POST'
    # catID = teacherGetKnowledge()
    catID = '95887' #暂时有数据的catid
    #af5a8825c77333d015c77635ee10081/95453~
    requestUrl = ipPort + '/external/resource/student/getResourceList/' + studentOpenid +'/' + str(catID) + '~'
    r = requests.post(requestUrl)
    if r.status_code == 200:
        if r.text == '':
            print(name+'接口不同,返回值为空')
        else:
            print(r.text)
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了' )
                print(requestJson)
            else:
                print(name+ '接口通了' + '没数据' + r.url)
                print(r.text)
    else:
        print(name+'接口不通' + str(r.status_code) + r.url)
    print(r.url)

def getResourceContent(resourceID):# 学习接口获取详情
    name = '学习接口获取详情'
    urlString = ipPort + '/external/resource/resourceView/' + studentOpenid +'/' + resourceID
    r = requests.post(urlString)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)

def collectionAndDisCollection():#收藏和取消收藏
    name = '收藏和取消收藏'
    resourceID = '5883'
    urlString = ipPort + '/external/resource/addFavResource/' + studentOpenid + '/' + resourceID
    r = requests.post(urlString)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)
    pass

def getResourceType():#获取对应资源类型
    name = '获取对应资源类型'
    urlString = ipPort + '/external/cat/getResourceType'
    r = requests.get(urlString)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)
    pass


def getTestContent():
    name = '获取返回试题的数据接口'
    catID = '95887'
    knowTypeId = "0"
    urlString = ipPort + '/external/learningCapacity/homework/getTestContent/' +catID + '/' + studentOpenid + '/' +knowTypeId
    r = requests.get(urlString)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)
    pass

def submitAnswer():
    name = '提交测试后的答案的接口'

    str = {
        "resultid": "8af5a8825f861cb6015f861e81a20002",# homeResultID
        "resultContent": [
            {
                "parentId": 0,
                "qstId": 126638,
                "resultFlag": 0,
                "standardAnswer": "B",
                "subCount": 0,
                "tqId": 46,
                "userAnswer": "C",
                "userScoreRate": "0%",
                "viewTypeId": 1
            },
            {
                "parentId": 0,
                "qstId": 126637,
                "resultFlag": 0,
                "standardAnswer": "C",
                "subCount": 0,
                "tqId": 39,
                "userAnswer": "C",
                "userScoreRate": "0%",
                "viewTypeId": 1
            },
            {
                "parentId": 0,
                "qstId": 126635,
                "resultFlag": 0,
                "standardAnswer": "D",
                "subCount": 0,
                "tqId": 25,
                "userAnswer": "C",
                "userScoreRate": "0%",
                "viewTypeId": 1
            }
        ]
    }

    urlString = ipPort + '/external/learningCapacity/homework/saveExamResult'

    r = requests.post(urlString,json=str)
    print(r.status_code)
    print(r.headers)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不通,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)

    pass




def submitPracticAnwser():
    #/external/learningCapacity/homework/getExerciseContent/{knowLedgeId}/{openid}
    name = '提交自己练习后的答案的接口'
    catid = '95453'
    urlString = ipPort + '/external/learningCapacity/homework/getExerciseContent/'+catid +'/'+studentOpenid
    r = requests.get(urlString)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)
    pass
#http://120.55.181.205:8080/external/learningCapacity/homework/saveExamResult8af5a8825c77333d015c77635ee10081/95886/3/true
#[request url]: http://120.55.181.205:8080/external/learningCapacity/updateProgress/8af5a8825c77333d015c77635ee10081/95887/1/false

def submitUpdateProgress():
    name = '提交进度'
    catid = '95887'
    entryProgerss = 1
    urlString = ipPort + '/external/learningCapacity/updateProgress/'+ studentOpenid+'/'+ catid+'/'+str(entryProgerss) +'/'+'false'
    r = requests.get(urlString)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)
    pass


def getExerciseContent():#初次获取测试内容
    name = '初次获取练习内容'
    catid = '95887'
    str = {
      "homeworkContent":"",
      "qstids":"",
      "diffid":"0",
      "resultContent":""
    }
    urlString = ipPort + '/external/learningCapacity/homework/getExerciseContent/' + catid +'/'+ studentOpenid
    r = requests.post(urlString,json=str)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)
    return r.json()


def getSecondExerciseContent():#初次获取测试内容
    homeworkContent = getExerciseContent()
    name = '再次获取测试内容'
    catid = '95887'
    str = {
      "homeworkContent":homeworkContent["data"]["homeworkResultContent"],
      "qstids":"'297e1e065f81c986015f81d001210110','297e1e065f81c986015f81cecfe100fa'",#id
      "diffid":"82704",
      "resultContent":[
    {
        "parentId":0,
        "qstId":"297e1e065f81c986015f81d001210110",
        "resultFlag":0, #
        "standardAnswer":"D",
        "subCount":0,
        "tqId":78,
        "userAnswer":"B",#
        "userScoreRate":"0%",#
        "viewTypeId":1
    },
    {
        "parentId":0,
        "qstId":"297e1e065f81c986015f81cecfe100fa",
        "resultFlag":0,
        "standardAnswer":"A",
        "subCount":0,
        "tqId":1,
        "userAnswer":"D",
        "userScoreRate":"0%",
        "viewTypeId":1
    }
] }

    urlString = ipPort + '/external/learningCapacity/homework/getExerciseContent/' + catid +'/'+ studentOpenid
    r = requests.post(urlString,json=str)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)
    pass
def text ():
    str = {"data":{"diffid":82704,"homeworkResultContent":"{\"docType\":0,\"hasSubjective\":false,\"paperAnswertime\":90,\"paperQstCount\":2,\"paperScore\":0,\"paperTitle\":\"\",\"sysAuthors\":\"\",\"typeList\":[{\"hasSubjective\":false,\"index\":\"一\",\"questionList\":[{\"QST_TYPE\":\"单选题\",\"QST_TYPEID\":82714,\"analysis\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\">当<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017848461.png\\\"/>时，<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017849326.png\\\"/>，则<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017850342.png\\\"/>，<p>　　又∵\\u00A0\\u00A0偶函数关于<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017851239.png\\\"/>轴对称，∴\\u00A0\\u00A0<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017852192.png\\\"/>的解析集为<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017853076.png\\\"/>或<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017853983.png\\\"/>.</p></XHTML>\",\"answer\":\"B\",\"content\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\">若<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017840465.png\\\"/>是偶函数，且当<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017841426.png\\\"/>时，<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017842292.png\\\"/>，则不等式<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017843177.png\\\"/>的解析集是(\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0)</XHTML>\",\"department\":\"非国际部\",\"departmentId\":93640,\"diff\":\"三星\",\"diffId\":82706,\"doclibId\":0,\"flowStatus\":0,\"id\":\"129780\",\"import_level\":0,\"indexOrder\":12,\"key\":\"偶函数\",\"keyCascadId\":\"92412_95471_95484_95485\",\"keyId\":\"95485\",\"options\":{\"A\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\"><img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017844059.png\\\"/></XHTML>\",\"B\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\"><img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017844924.png\\\"/>或<img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017845811.png\\\"/></XHTML>\",\"C\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\"><img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017846701.png\\\"/></XHTML>\",\"D\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\"><img src=\\\"http://120.55.181.205:5080/TQMS//question/129780/1509017847578.png\\\"/></XHTML>\"},\"paperSysId\":0,\"paperSysName\":\"\",\"parentId\":\"0\",\"qstDiffRevise\":\"三星\",\"qstVestOneId\":0,\"qstVestTwoId\":0,\"questionStatus\":0,\"resultError\":0,\"resultRight\":0,\"resultflag\":0,\"score\":1,\"showChoiseNum\":4,\"subCount\":0,\"subQuestions\":[],\"subScore\":0,\"subject\":\"高中数学\",\"subjectId\":186,\"summary\":\"若f(x)是偶函数，且当x\",\"tqId\":54,\"type\":\"单选题\",\"typeId\":82714,\"userScore\":0,\"viewTypeId\":1},{\"QST_TYPE\":\"单选题\",\"QST_TYPEID\":82714,\"analysis\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\">当<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017864093.png\\\"/>时，<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017864960.png\\\"/>，则<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017865879.png\\\"/>，<p>　　又∵\\u00A0\\u00A0偶函数的图像关于<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017866791.png\\\"/>轴对称，</p><p>　　∴\\u00A0\\u00A0<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017867658.png\\\"/>的解析集为<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017868552.png\\\"/>.</p></XHTML>\",\"answer\":\"D\",\"content\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\">若函数<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017854985.png\\\"/>是定义在<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017856086.png\\\"/>上的偶函数，则<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017857088.png\\\"/>上是减函数，且<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017857986.png\\\"/>，则使得<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017858852.png\\\"/>的<img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017859731.png\\\"/>的取值范围是(\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0\\u00A0)</XHTML>\",\"department\":\"非国际部\",\"departmentId\":93640,\"diff\":\"三星\",\"diffId\":82706,\"doclibId\":0,\"flowStatus\":0,\"id\":\"129781\",\"import_level\":0,\"indexOrder\":13,\"key\":\"偶函数\",\"keyCascadId\":\"92412_95471_95484_95485\",\"keyId\":\"95485\",\"options\":{\"A\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\"><img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017860606.png\\\"/></XHTML>\",\"B\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\"><img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017861469.png\\\"/></XHTML>\",\"C\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\"><img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017862335.png\\\"/></XHTML>\",\"D\":\"<XHTML xmlns:mml=\\\"http://www.w3.org/1998/Math/MathML\\\"><img src=\\\"http://120.55.181.205:5080/TQMS//question/129781/1509017863223.png\\\"/></XHTML>\"},\"paperSysId\":0,\"paperSysName\":\"\",\"parentId\":\"0\",\"qstDiffRevise\":\"三星\",\"qstVestOneId\":0,\"qstVestTwoId\":0,\"questionStatus\":0,\"resultError\":0,\"resultRight\":0,\"resultflag\":0,\"score\":1,\"showChoiseNum\":4,\"subCount\":0,\"subQuestions\":[],\"subScore\":0,\"subject\":\"高中数学\",\"subjectId\":186,\"summary\":\"若函数f(x)是定义在R上\",\"tqId\":61,\"type\":\"单选题\",\"typeId\":82714,\"userScore\":0,\"viewTypeId\":1}],\"typeId\":\"82714\",\"typeMemo\":\"共2题\",\"typeName\":\"单选题\"}]}"},"status":1}
    print(str["data"]["homeworkResultContent"])
    pass

def getResourceListBysolomon():#推荐资源
    name = '推荐资源'
    catid = '95887'
    entryProgerss = 3
    urlString = ipPort + '/external/resource/student/getResourceListBysolomon/' + studentOpenid + '/' + catid
    r = requests.post(urlString)
    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)
    print(r.url)
    pass

def login():

    name = '登录的接口'

    loginName = '1002010'
    password = '1002010'
    userType = '3'
    params = {
        'phoneNum': loginName,
        'password': password,
        'userType': userType
    }

    url =  ipPort + "/ios/teacher/test/iosLogin.do"
    r = requests.get(url,params)

    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            print(r.text)
            if requestJson['data'] == '登录成功':
                print(name + '接口调通了')
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)

    pass

def getUserFavResource():
    #/external/resource/getfavResource/8af5a8825c77333d015c77635ee10081
    name = '获取用户收藏列表'


    url = ipPort + "/external/resource/getfavResource/"+ studentOpenid
    r = requests.post(url)

    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            print(r.text)
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.url)
                print(r.text)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)

    pass

def getMyWrongQuestion():
    name = '获取错题本'

    url = ipPort + "/external/info/student/myWrongQuestion/" + studentOpenid
    r = requests.post(url)

    if r.status_code == 200:
        if r.text == '':
            print(name + '接口不同,返回值为空')
        else:
            requestJson = r.json()
            print(r.text)
            if requestJson['status'] == 1:
                print(name + '接口调通了')
                print(r.text)
                print(r.url)
            else:
                print(name + '接口通了' + '没数据' + r.url)
                print(r.json())
    else:
        print(name + '接口不通' + str(r.status_code) + r.url)

    pass


if __name__ == '__main__':
    # getStudentLearningStages()
    # getAllStars()
    # getClassStudentList()
    # getTeacherClassList()
    # teacherGetStudentLearning()
    # teacherGetKnowledge()
    # # studentWeakNess()
    # getResourceList()
    # getStudentKnowledge()
    # collectionAndDisCollection()
    # pdfResurceID = '5690'#测试pdf资源详情
    # getResourceContent(pdfResurceID)
    # MP3ResourceID = '5940'#视频
    # getResourceContent(MP3ResourceID)
    # TXTResourceID = '5306'
    # getResourceContent(TXTResourceID)
    # getResourceType()
    getTestContent()
    # submitAnswer()
    # submitUpdateProgress()
    # getExerciseContent()
    # getSecondExerciseContent()
    # getResourceListBysolomon()
    # login()
    # getUserFavResource()
    # getMyWrongQuestion()
    pass

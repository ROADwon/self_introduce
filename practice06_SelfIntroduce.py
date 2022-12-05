#
# # 자기 소개 프로그램
# # 01 자기소개 작성(1) , 자기소개 확인(2)
# # 02 한줄단위로 자기소개를 입력받는다. 파일을 쓰기
# # 03 파일에 저장된 자기소개를 읽어온다. 확인
# # 04 저장된 자기소개를 추가한다.
# import googletrans
# translor = googletrans.Translator()
#
# def inp_SI() :
#     selc = int( input("1. 자기소개 작성, 2. 자기소개 확인, 3. 자기소개 추가, 4. 프로그램 종료") )
#     if(selc == 1):
#         print("자기소개를 작성합니다.")
#     elif(selc == 2):
#         print("자기소개를 확인합니다.")
#     elif(selc == 3):
#         print("자기소개를 추가합니다.")
#     elif(selc == 4):
#         print("프로그램을 종료합니다.")
#
#     return selc
#
# def add_SI() :
#     var_a = open("SelfIntroduce.txt",'a',encoding='utf-8')
#     lines = input("한줄의 자기소개를 추가해주세요 (그만 : Q)")
#     while (lines != 'Q' and lines !='q'):
#         if(lines != "") :
#             var_a.write(lines)
#             var_a.write("\n")
#         lines = input("한줄의 자기소개를 추가해주세요(그만 : Q)")
#     var_a.close()
#
# def red_SI() :
#     var_r = open("SelfIntroduce.txt",'r',encoding='utf-8')
#     doc_r = var_r.read()
#     print(doc_r)
#     var_r.close()
#
#
#
# def wrt_SI():
#     var = open("SelfIntroduce.txt",'w',encoding = 'utf-8')
#
#     lines = input("한줄의 자기소개를 입력해주세요(그만 : Q) :")
#     while  (lines != 'Q' and lines != 'q') :
#         if (lines != "") :
#             var.write(lines)
#             var.write("\n")
#
#         lines = input("한줄의 자기소개를 입력해주세요(그만 : Q) :")
#
#     var.close()
#
#
# if __name__ == "__main__":
#     menu = inp_SI()
#
#     while (menu != 4):
#         if menu == 1 :
#             wrt_SI()
#         elif menu == 2:
#             red_SI()
#         elif menu == 3:
#             add_SI()
#         menu = inp_SI()


# 자기 소개 프로그램
# 01 자기소개 작성(1) , 자기소개 확인(2)
# 02 한줄단위로 자기소개를 입력받는다. 파일을 쓰기
# 03 파일에 저장된 자기소개를 읽어온다. 확인
# 04 저장된 자기소개를 추가한다.
# 05 자기소개를 번역한다
# 06 자기소개를 원하는 언어로 번역한다.
from googletrans import Translator
translator = Translator()

def inp_SI() :
    selc = int( input("1. 자기소개 작성, 2. 자기소개 확인, 3. 자기소개 추가, 4. 자기소개 번역, 5 프로그램 종료") )
    if(selc == 1):
        print("자기소개를 작성합니다.")
    elif(selc == 2):
        print("자기소개를 확인합니다.")
    elif(selc == 3):
        print("자기소개를 추가합니다.")
    elif(selc == 4):
        print("자기소개를 번역합니다.")
    elif(selc == 5):
        print("프로그램을 종료합니다.")

    return selc
def trans_SI() :
    print("번역할 언어를 선택해주세요")
    selc = int(input("1. 영어, 2. 일본어, 3. 중국어, 4. 한국어"))
    if(selc == 1):
        t_Str = r"Selfintroduce.txt"
        w_Str = r"번역본.txt"
        with open(t_Str, 'r') as f:
            readLines = f.readlines()

        for lines in readLines:
            result = translator.translate(lines, dest='en', src='auto')
            print(result.text)

            with open(w_Str,'a',encoding='utf-8') as f:
                f.write(result.text + '\n')

    elif(selc == 2 ):
        t_Str = r"Selfintroduce.txt"
        w_Str = r"번역본.txt"

        with open(t_Str, 'r') as f:
            readLines = f.readlines()

        for lines in readLines:
            result = translator.translate(lines, dest='ja', src='auto')
            print(result.text)
            with open(w_Str,'a',encoding='utf-8') as f:
                f.write(result.text + '\n')
    elif(selc == 3):
        t_Str = r"Selfintroduce.txt"
        w_Str = r"번역본.txt"

        with open(t_Str, 'r') as f:
            readLines = f.readlines()

        for lines in readLines:
            result = translator.translate(lines, dest='zh-cn', src='auto')
            print(result.text)
            with open(w_Str,'a',encoding='utf-8') as f:
                f.write(result.text + '\n')

    elif(selc == 4):
        t_Str = r"Selfintroduce.txt"
        w_Str = r"번역본.txt"

        with open(t_Str, 'r') as f:
            readLines = f.readlines()

        for lines in readLines:
            result = translator.translate(lines, dest='ko', src='auto')
            print(result.text)
            with open(w_Str,'a',encoding='utf-8') as f:
                f.write(result.text + '\n')


def add_SI() :
    var_a = open("SelfIntroduce.txt",'a',encoding='utf-8')
    lines = input("한줄의 자기소개를 추가해주세요 (그만 : Q)")
    while (lines != 'Q' and lines !='q'):
        if(lines != "") :
            var_a.write(lines)
            var_a.write("\n")
        lines = input("한줄의 자기소개를 추가해주세요(그만 : Q)")
    var_a.close()

def red_SI() :
    var_r = open("SelfIntroduce.txt",'r',encoding='utf-8')
    doc_r = var_r.read()
    print(doc_r)
    var_r.close()



def wrt_SI():
    var = open("SelfIntroduce.txt",'w',encoding = 'utf-8')

    lines = input("한줄의 자기소개를 입력해주세요(그만 : Q) :")
    while  (lines != 'Q' and lines != 'q') :
        if (lines != "") :
            var.write(lines)
            var.write("\n")

        lines = input("한줄의 자기소개를 입력해주세요(그만 : Q) :")

    var.close()


if __name__ == "__main__":
    menu = inp_SI()

    while (menu != 5):
        if menu == 1 :
            wrt_SI()
        elif menu == 2:
            red_SI()
        elif menu == 3:
            add_SI()
        elif menu == 4:
            trans_SI()
        menu = inp_SI()
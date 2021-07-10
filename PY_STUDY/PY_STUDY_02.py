#챕터11

print("챕터11")
absent=[2,5]#결석
no_book=[7]#책 안가지고 옴
for student in range(1,11):
  if student in absent:
    continue#continue는 다시 for문의 처음으로 돌아가게 함!(바로 다음 반복을 실행)
  print("{0},책을 읽어봐".format(student))

print("\n\n")


#챕너12

print("챕터12")
#한줄 for(학생들 이름을 길이로 변환)
students=["iron man",'thor','groot']
students=[len(i) for i in students]
print(students)

print("\n\n")


#챕터13
  
print("챕터13")
def withdraw_night(balance,money):
  commission=100#수수료 100원
  return  commission,balance-money-commission#한번에 두개의 값을 리턴 불가능!(튜플의 형태로 반환됨)

balance=1000#잔액
commission,balance=withdraw_night(balance,400)
print("수수료는 {0}원이며, 잔액은 {1}원입니다".format(commission,balance))

#또다른 방법(튜플 형태로 돌려받기)
# commission=withdraw_night(balance,400)
# print(commission)

print("\n\n")


#챕터14

print("챕터14")
#기본값 지정 가능
def profile(name,age=17,main_lang="파이썬"):
  print("이름:{0}\t나이:{1}\t주사용언어:{2}".format(name,age,\
  main_lang))  #역슬래시 긋고 엔터치면 한줄취급!중요
profile("유재석")
profile("김태호")

#키워드값

def profile(name,age,main_lang):
  print(name,age,main_lang)

profile(name="유재석",main_lang="python",age=20) #순서 상관 없음!

#가변인자(전달받아야 하는 값이 몇개인지 모를 때 주로 사용!)
def profile(name,age,*language):
  print("이름:{0}\t나이:{1}\t".format(name,age),end=" ")  #end=" "요렇게 쓰면 줄바꿈 안하고 바로 출력됨!
  for lang in language:
    print(lang,end=" ")
  print()
profile("유재석",20,"python","java","C","C++","C#")    
profile("김태호",25,"kotlin","swift")


print("\n\n")


#챕터15

print("챕터15")
gun=10
def checkpoint(soldiers):
  global gun#전역 공간에 있는 gun 사용
  gun=gun-soldiers
  print("[함수 내]남은 총:{0}".format(gun))

print("전체총:{0}".format(gun))
checkpoint(2)
print("남은 총:{0}".format(gun))
#또는 함수와 입력값을 이용하여 전역변수 이용 가능
print("\n\n")

#챕터 16

print("챕터16")
height=175.53535
weight=round(height/100,3)
#요 테크닉 기억! 소수 셋째 자리까지 반올림 할때 사용 
print("키{0}cm여자의 표준 체중은 {1}kg입니다.".format(height,weight))

print("\n\n")


#챕터 17
#표준입출력
#sep:중간에 삽입
#end:마지막에 삽입하고 다음 문장 이어서 출력
print("챕터17")
print("python","java",sep=',',end='?')
import sys
print("python","java",file=sys.stdout)#표준 출력
print("python","java",file=sys.stderr)#표준 에러

scores={"수학":0,"영어":50,"코딩":100}
for subject,score in scores.items():
  print(subject.ljust(8),str(score).rjust(4),sep=':')  

for num in range(1,11):
  print("대기번호:"+str(num).zfill(3))

print("\n\n")

#챕터 18
#빈자리는 빈 공간으로 두고,오른쪽 정렬을  하되, 총 10자리 공간을 확보
print("챕터18")
print("{0: >10}".format(500))
print("{0: >10}".format(-500))
#양수일 땐 +표시,음수일 땐 -로 표시
print("{0: >+10}".format(500))#+표시도 나옴!
print("{0: >+10}".format(-500))
#왼쪽 정렬을 하고 빈칸으로 _로 채움
print("{0:_<10}".format(500))

#3자리마다 콤마를 찍어주기,+ - 부호도 붙여주기,자릿수 확보하기
#돈이 많으면 행복하니 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(1000000000000))

#소수점 출력
print("{0:f}".format(5/3))
#소수점을 특정 자리수 까지만 표시
#소수점 3째자리에서 반올림
print("{0:.2f}".format(5/3))

print("\n\n")

#챕터 19

print("챕터19")
score_file=open("score.txt",'w',encoding='utf8')
print("수학:0",file=score_file)
print("영어:50",file=score_file)
score_file.close()
#쓰기모드(쓸때마다 초기화)

score_file=open("score.txt","a",encoding='utf8')
score_file.write("과학:80")
score_file.write("\n코딩:50")
score_file.close()
#줄바꿈을 명시적으로 정의해줘야 됨!
#추가모드

score_file=open("score.txt","r",encoding='utf8')
print(score_file.readline(),end="")#줄별로 읽기,  한줄 읽고 커서는 다음줄로 이동
score_file.close


#한번에 모든 내용을 다 가져오고 싶다면!
score_file=open("score.txt","r",encoding='utf8')
print(score_file.read())
score_file.close

#파일이 총 몇줄인지 모를때!
score_file=open("score.txt","r",encoding='utf8')
while True:
  line=score_file.readline()
  if not line:
    break
  print(line,end="")
score_file.close() 
#또 다른 방법
score_file=open("score.txt","r",encoding='utf8')
lines=score_file.readlines()
for line in lines:
  print(line,end='')
score_file.close()
print("\n\n")


#챕터 20
print("챕터20")

#피클:파이썬에 사용되는 자료형 그대로 저장 가능
import pickle

profile_file=open("profile.pickle","wb")
profile={'이름':'박명수','나이':20,'취미':['축구','골프','코딩']}
print(profile)
pickle.dump(profile,profile_file)#profile에 있는 정보를 file에 저장
profile_file.close()

profile_file=open("profile.pickle",'rb')
profile=pickle.load(profile_file)#file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

#with 구문
with open("profile.pickle","rb")as profile_file:
  print(pickle.load(profile_file))
#파일을 자동으로 닫아줌!!

with open("study.txt","w",encoding="utf8") as study_file:
  study_file.write("파이썬 열공중")



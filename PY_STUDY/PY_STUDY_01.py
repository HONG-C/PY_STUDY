#파일 실행법
#1.cd PY_STUDY
#2.python3 PY_STUDY_03.py 


#챕터1
print("챕터1")
age=4
hobby='산책'
print('나이는'+str(age)+'살,취미는'+hobby)#형변환 필수
print('나이는',age,'살,취미는',hobby)
#,(쉼표)가 띄어쓰기를 만듬 이때는 형변환 불필요
print("\n\n")


#챕터2
print("챕터2")
'''
*있는 문장 주석처리할 때
컨트롤+슬래시(물음표)
'''
print("\n\n")


#챕터3
print("챕터3")
print((3>0)and(2>0))
print((3>0)&(2>0))
#and와 &은 동일!
print((3>0)or(2>5))
print((3>0)|(2>5))
print("\n\n")


#챕터4
print("챕터4")
python = "Python is Amazing"
print(len(python))#문자열 길이 반환

print(python.find("java"))
"""java의 위치를 찾아라(없으니 -1 출력)"""
#index=python.index('java')
"""java의 위치를 찾아라(없으니 오류 출력)"""
print("\n\n")


#챕터5
print("챕터5")
print("나는 %s색과 %s색을 좋아해요"%("파란","빨간"))
#(파이썬 버전 3.6 이상부터 가능)
age=20
color="빨간"
print(f"나는 {age}살이며,{color}색을 좋아해요")
print("\n\n")

#챕터6
print("챕터6")
# \' \" :문장 내 따옴표
print("저는 '나도코딩'입니다")
print("저는 \'나도코딩\' 입니다")
print("저는 \"나도코딩\" 입니다")
print("\n\n")

#챕터7
print("챕터7")
subway=["유재석","조세호","박명수"]
#정형돈씨를 유재석/조세호 사이 태움
subway.insert(1,"정형돈")#숫자 넣는거 기억!
print(subway)

#다양한 자료형 함께 사용 가능
num_list=[5,2,4,3,1]
mix_list=["조세호",20,True]
print(mix_list)
#리스트 확장
num_list.extend(mix_list)
print(num_list)
print("\n\n")

#챕터8
print("챕터8")
cabinet={3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))

"""
print(cabinet[5])
:이 구문은 오류를 
발생시킴!키가 없기 때문
"""
print(cabinet.get(5))
#NONE을 출력! 오류는 안뜸
print(cabinet.get(5,"사용가능"))
#키는 정수형 뿐 아니라 문자열도 사용가능
cabinet={"A-3":"유재석","B-100":"김태호"}
cabinet["A-3"]="김종국"#덮어쓰기 가능
cabinet["C-20"]="조세호"#내용 추가 가능
(name,age,hobby)=("김종국",20,"코딩")
print(name,age,hobby)

#집합(set)
#중복안됨,순서없음

my_set={1,2,3,3,3}
print(my_set)
java={"유재석","김태호","양세형"}
#위 아래 모두 가능
python=set(["유재석","박명수"])

#교집합(자바 파이썬 모두 사용가능)
print(java&python)
print(java.intersection(python))

#합집합(자바 또는 파이썬 가능)
print(java|python)
print(java.union(python))

#차집합(자바가능 파이썬 불가능)
print(java-python)
print(java.difference(python))
print("\n\n")


#챕터9
print("챕터9")
menu={"커피","우유","주스"}
print(menu,type(menu))
menu=list(menu)
print(menu,type(menu))
print("\n\n")


#챕터10
print("챕터10")
for waiting_no in range(1,6):#1,2,3,4,5(마지막 번호 포함 안함!)
  print("대기번호:{0}".format(waiting_no))
starbucks=["아이언맨","토르","그루트"]
for customer in starbucks:
  print("{0},커피나왔당".format(customer))
print("\n\n")


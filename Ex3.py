import re
#. 문자
#^ 시작
#$ 끝
"""
ck=re.compile("^a")
print(ck.match("aata_data_att"))
print(ck.search("aata_data_att"))
print(ck.findall("aata_data_att"))
"""
#print(ck.match("data_in"))
#print(ck.search("in_data_in"))
#print(ck.findall("in_data_in_data_in"))
"""
ck=re.compile("a$")
print(ck.match("a ata data att"))
print(ck.search("a ata data att"))
print(ck.findall("a ata data att"))
"""
"""
ck=re.compile("a.a")
print(ck.match("a ata data att"))
print(ck.search("a ata data att"))
print(ck.findall("a ata data att"))
"""
#원하는 형태에 따른 문자열 선택 : 정규식
# . 문자
# ^ 시작
# $ 끝
# match("문자열"): 처음부터 일치
# search("문자열"): 일치 하는 문자 있는지 확인.
# findall("문자열"): 일치 하는 모든 것의 리스트 출력
l=['abcd','adcd',"accd","abdc","casdfd","cabcdd","c1234d","cddddd"]
ck=re.compile("^c....d$")#a.cd, cd$
def print_t(str):
    print(str)
    if str:
        print("일치문자",str.group())
        print("입력문자", str.string)
        print("일치문자 시작", str.start())
        print("일치문자 끝", str.end())
        print("일치문자 시작,끝", str.span())
    else:
        print("일치 없음")
for i in l:
    str=ck.match(i)
    print_t(str)
    str=ck.search(i)
    print_t(str)
    print("all_data",ck.findall(i))



#print(ck.search("a ata data att"))
#print(ck.findall("a ata data att"))
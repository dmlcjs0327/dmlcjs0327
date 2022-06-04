# <<함수를 정의한 파트>>

# 인자가 0 이하 이거나 3 이상이면 True, 그 외엔 False를 리턴하는 함수
def isFalse(choice):
    if choice >= 3 or choice <= 0:
        return True
    else:
        return False

# A와 B 사이의 거리를 리턴하는 함수 (거리이므로, 무조건 0 이상의 수를 리턴함)
def get_distance(A, B):
    result = A - B
    if result < 0:
        result = -result
    return result

# 거리에 따른 금액을 리턴하는 함수 (금액 = 3000 + ((거리-2000)/142의 몫) * 100)
def cal_cost(dist):
    default = 3000
    if(dist > 2000):
        default += ((dist-2000)//142)*100
    return default
    
# 사용할 문자들을 미리 저장해둔 리스트
arr = ["블루", "일반"]
arr2 = ["선결제", "후결제"]




#<<실제 실행파트>>

#passenger: 승객의 위치
passenger = int(input("승객의 위치를 입력해주세요. "))

#dest: 목적지의 위치
dest = int(input("목적지 위치를 입력해주세요. "))

isCont = True
choice = 0
choice2 = 0
taxi=0

#dist: 승객과 목적지 사이의 거리
dist = get_distance(passenger, dest)


while isCont: # isCont가 True이면 계속 반복
    
    #choice: 어떤 택시를 선택했는지 저장하는 변수
    choice = int(input("블루와 일반 택시 중 하나를 골라주세요. (1. 블루 2. 일반)"))
    
    # 만약 1,2 외의 값을 입력한 경우 다시 입력하도록 함
    if isFalse(choice):
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        continue #continue: 반복문의 시작부분으로 돌아가는 명령어


    iscont = True


    while iscont: # isCont가 True이면 계속 반복

        #choice2: 어떤 결제방식을 선택했는지 저장하는 변수
        choice2 = int(input("선결제와 후결제 중 하나를 골라주세요. (1. 선결제 2. 후결제)"))

        #만약 1,2 외의 값을 입력한 경우 다시 입력하도록 함
        if isFalse(choice2):
            print("잘못 입력하셨습니다. 다시 입력해주세요.")
            continue #continue: 반복문의 시작부분으로 돌아가는 명령어

        
        iscont = False
        #iscont가 False로 바뀌고 나면, while문 내의 코드를 모두 실행한 것이므로 다시 while문의 맨 위로 올라감
        #근데 iscont가 False가 되었으므로 while문은 더이상 반복하지 않고 종료될 것임

    #taxi: 택시의 위치를 저장하는 변수
    taxi = int(input("택시 위치를 입력해주세요. "))

    #택시와 승객의 거리가 500 이상이면 배차에 실패 / 미만이면 성공
    if get_distance(passenger, taxi) > 500:
        print("배차 실패하였습니다. 다시 선택해주세요.")
        continue #다시 while문의 맨 처음으로 돌아감 => 즉, 블루/일반 택시 선택 구문이 실행됨
    else:
        print("배차 성공하였습니다.")
        isCont = False
        #isCont가 False가 되었으므로 while문은 더이상 반복하지 않고 종료될 것임

#배차 결과를 출력
print(arr[choice-1] + " 택시, " + arr2[choice2-1] + "를 선택하셨고 주행거리는 ", dist, "m, 비용은 ", cal_cost(dist), "원 입니다.")

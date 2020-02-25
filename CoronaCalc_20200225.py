
# Estimation Program for the Number of Infected Patients of COVID-19, based on user input data
# 신종 코로나바이러스 (COVID-19) 확진자 수 예측 프로그램
# Development by bcchickadee, Feb 25 2020
# build 1.3.0

# This section is the definition of the main program function.
# 이 섹션은 초기 프로그램 시퀀스를 정의합니다.
def MainScreen_ProgramSequence(UserInput):
    if UserInput==1:
        print('2일 동안 확진자 수 데이터를 토대로 n일 후 확진자 수를 산출합니다.\n')
        Infected_0DayBefore=input('기준일의 확진자 수를 입력해 주십시오.\n')
        Infected_1DayBefore=input('기준일로부터 1일 전 확진자 수를 입력해 주십시오.\n')
        TargetDay=input('기준일로부터 확진자 수를 산출하고자 하는 날짜를 입력해 주십시오.\n예: 기준일로부터 1일 후면 1 입력\n')
        print(TargetDay+'일 후의 예상 확진자 수는 약:\n')
        TwoDayFunction_Sequence(Infected_0DayBefore, Infected_1DayBefore, TargetDay)
        print('명입니다.')
        print('=================================\n\n')
    # 1st function: Displays estimated patient number for target day, based on previous data for 2 days. (Assuming that number follows a geometric progression)
    # 1번 기능: 2일치의 데이터를 통해 n일 후의 확진자 수를 예측합니다. (확진자 수가 등비수열을 이룬다고 가정함)    
    elif UserInput==2:
        print('3일 동안 확진자 수 데이터를 토대로 n일 후 확진자 수를 산출합니다.\n')
        Infected_0DayBefore=input('기준일의 확진자 수를 입력해 주십시오.\n')
        Infected_1DayBefore=input('기준일로부터 1일 전 확진자 수를 입력해 주십시오.\n')
        Infected_2DayBefore=input('기준일로부터 2일 전 확진자 수를 입력해 주십시오.\n')
        TargetDay=input('기준일로부터 확진자 수를 산출하고자 하는 날짜를 입력해 주십시오.\n예: 기준일로부터 1일 후면 1 입력\n')
        print(TargetDay+'일 후의 예상 확진자 수는 약:\n')
        ThreeDayFunction_Sequence(Infected_0DayBefore, Infected_1DayBefore, Infected_2DayBefore, TargetDay)
        print('명입니다.')
        print('=================================\n\n')
    # 2nd function: Displays estimated patient number for target day, based on previous data for 3 days. (Assuming that number follows a geometric progression)
    # 2번 기능: 3일치의 데이터를 통해 n일 후의 확진자 수를 예측합니다. (확진자 수가 등비수열을 이룬다고 가정함)    
    elif UserInput==3:
        print('4일 동안 확진자 수 데이터를 토대로 n일 후 확진자 수를 산출합니다.\n')
        Infected_0DayBefore=input('기준일의 확진자 수를 입력해 주십시오.\n')
        Infected_1DayBefore=input('기준일로부터 1일 전 확진자 수를 입력해 주십시오.\n')
        Infected_2DayBefore=input('기준일로부터 2일 전 확진자 수를 입력해 주십시오.\n')
        Infected_3DayBefore=input('기준일로부터 3일 전 확진자 수를 입력해 주십시오.\n')
        TargetDay=input('기준일로부터 확진자 수를 산출하고자 하는 날짜를 입력해 주십시오.\n예: 기준일로부터 1일 후면 1 입력\n')
        print(TargetDay+'일 후의 예상 확진자 수는 약:\n')
        FourDayFunction_Sequence(Infected_0DayBefore, Infected_1DayBefore, Infected_2DayBefore, Infected_3DayBefore, TargetDay)
        print('명입니다.')
        print('=================================\n\n')
    # 3rd function: Displays estimated patient number for target day, based on previous data for 4 days. (Assuming that number follows a geometric progression)
    # 3번 기능: 4일치의 데이터를 통해 n일 후의 확진자 수를 예측합니다. (확진자 수가 등비수열을 이룬다고 가정함)    
    elif UserInput==4:
        print('5일 동안 확진자 수 데이터를 토대로 n일 후 확진자 수를 산출합니다.\n')
        Infected_0DayBefore=input('기준일의 확진자 수를 입력해 주십시오.\n')
        Infected_1DayBefore=input('기준일로부터 1일 전 확진자 수를 입력해 주십시오.\n')
        Infected_2DayBefore=input('기준일로부터 2일 전 확진자 수를 입력해 주십시오.\n')
        Infected_3DayBefore=input('기준일로부터 3일 전 확진자 수를 입력해 주십시오.\n')
        Infected_4DayBefore=input('기준일로부터 4일 전 확진자 수를 입력해 주십시오.\n')
        TargetDay=input('기준일로부터 확진자 수를 산출하고자 하는 날짜를 입력해 주십시오.\n예: 기준일로부터 1일 후면 1 입력\n')
        print(TargetDay+'일 후의 예상 확진자 수는 약:\n')
        FiveDayFunction_Sequence(Infected_0DayBefore, Infected_1DayBefore, Infected_2DayBefore, Infected_3DayBefore, Infected_4DayBefore, TargetDay)
        print('명입니다.')
        print('=================================\n\n')
    # 4th function: Displays estimated patient number for target day, based on previous data for 5 days. (Assuming that number follows a geometric progression)
    # 4번 기능: 5일치의 데이터를 통해 n일 후의 확진자 수를 예측합니다. (확진자 수가 등비수열을 이룬다고 가정함)
    elif UserInput==5:
        UserPreference=input('정말로 프로그램을 종료하시겠습니까? (y/n)\n')
        return QuittingSequence(UserPreference)
    else:
        print('에러: 올바른 선택지를 입력하십시오.\n\n')
        # Invalid Option: Displays Error Message
        # 유효하지 않은 기능: 에러 메시지 표시



# This section consists of the definitions of the functions needed for calculating the actual output number (estimated number of patients).
# 이 섹션은 실제 출력값 (예측된 확진자 수) 계산을 위한 함수를 정의하는 부분입니다.

def TwoDayFunction_Sequence(Infected_0DayBefore, Infected_1DayBefore, TargetDay):
    CommonRatio=int(Infected_0DayBefore) / int(Infected_1DayBefore)
    PatientNumber_in_TargetDay=int(Infected_0DayBefore)*CommonRatio**int(TargetDay)
    print(int(PatientNumber_in_TargetDay))
    # TwoDayFunction_Sequence function definition for 1st function
    # 제 1번 기능에 대한 TwoDayFunction_Sequence 함수 정의

def ThreeDayFunction_Sequence(Infected_0DayBefore, Infected_1DayBefore, Infected_2DayBefore, TargetDay):
    CommonRatio_0_to_1=int(Infected_0DayBefore) / int(Infected_1DayBefore)
    CommonRatio_1_to_2=int(Infected_1DayBefore) / int(Infected_2DayBefore)
    RevisedCommonRatio=(CommonRatio_0_to_1 * CommonRatio_1_to_2) ** 0.5
    # Differences in data adjusted by using the geometric mean
    # 기하평균을 이용하여 비율 간의 차이를 조정함.
    PatientNumber_in_TargetDay=int(Infected_0DayBefore)*RevisedCommonRatio**int(TargetDay)
    print(int(PatientNumber_in_TargetDay))
    # ThreeDayFunction_Sequence function definition for 2nd function
    # 제 2번 기능에 대한 ThreeDayFunction_Sequence 함수 정의

def FourDayFunction_Sequence(Infected_0DayBefore, Infected_1DayBefore, Infected_2DayBefore, Infected_3DayBefore, TargetDay):
    CommonRatio_0_to_1=int(Infected_0DayBefore) / int(Infected_1DayBefore)
    CommonRatio_1_to_2=int(Infected_1DayBefore) / int(Infected_2DayBefore)
    CommonRatio_2_to_3=int(Infected_2DayBefore) / int(Infected_3DayBefore)
    RevisedCommonRatio=(CommonRatio_0_to_1 * CommonRatio_1_to_2 * CommonRatio_2_to_3) ** (1/3)
    # Differences in data adjusted by using the geometric mean
    # 기하평균을 이용하여 비율 간의 차이를 조정함.
    PatientNumber_in_TargetDay=int(Infected_0DayBefore)*RevisedCommonRatio**int(TargetDay)
    print(int(PatientNumber_in_TargetDay))
    # FourDayFunction_Sequence function definition for 3rd function
    # 제 3번 기능에 대한 FourDayFunction_Sequence 함수 정의

def FiveDayFunction_Sequence(Infected_0DayBefore, Infected_1DayBefore, Infected_2DayBefore, Infected_3DayBefore, Infected_4DayBefore, TargetDay):
    CommonRatio_0_to_1=int(Infected_0DayBefore) / int(Infected_1DayBefore)
    CommonRatio_1_to_2=int(Infected_1DayBefore) / int(Infected_2DayBefore)
    CommonRatio_2_to_3=int(Infected_2DayBefore) / int(Infected_3DayBefore)
    CommonRatio_3_to_4=int(Infected_3DayBefore) / int(Infected_4DayBefore)
    RevisedCommonRatio=(CommonRatio_0_to_1 * CommonRatio_1_to_2 * CommonRatio_2_to_3 * CommonRatio_3_to_4) ** (1/4)
    # Differences in data adjusted by using the geometric mean
    # 기하평균을 이용하여 비율 간의 차이를 조정함.
    PatientNumber_in_TargetDay=int(Infected_0DayBefore)*RevisedCommonRatio**int(TargetDay)
    print(int(PatientNumber_in_TargetDay))
    # FiveDayFunction_Sequence function definition for 4th function
    # 제 4번 기능에 대한 FiveDayFunction_Sequence 함수 정의

def QuittingSequence(UserPreference):
    if str(UserPreference)=="y":
        quit()
    elif str(UserPreference)=="n":
        print('프로그램 종료를 취소하였습니다.\n프로그램을 다시 시작합니다.\n\n')
    else:
        print('에러: 올바른 선택지를 입력하십시오.\n\n')
        return MainScreen_ProgramSequence(5)
    #QuittingSequence function definition for 5th option
    #제 5번 기능에 대한 QuittingSequence 함수 정의


# This section prints the actual initial screen when the program is opened.
# 이 섹션은 실제 프로그램 실행 시 표시되는 정보입니다.

print('CoronaCalc build 1.3.0')
print('Developed by bcchickadee, Feb 25 2020')
print('Program Description: This program estimates the number of infected patients of COVID-19 on a targeted day, based on user input data.')
print('프로그램 설명: 이 프로그램은 입력값을 통해 임의의 날짜에 대해 예상되는 확진자 수를 계산합니다.\n')
print('주의: 이 프로그램은 등비수열을 통한 단순 계산값을 산출할 뿐입니다. 예상 수치가 실제와 많이 다릅니다.\n\n')
#Program Description at initial startup - this message is only displayed once.
#초기 시작 화면의 프로그램 설명 - 이 메시지는 한 번만 표시됩니다.

while True:
    print('실행할 기능을 입력해 주십시오.')
    print('1번 기능: 기준일로부터 0-1일, 총 2일 간의 데이터로 확진자 수 예측')
    print('2번 기능: 기준일로부터 0-2일, 총 3일 간의 데이터로 확진자 수 예측')
    print('3번 기능: 기준일로부터 0-3일, 총 4일 간의 데이터로 확진자 수 예측')
    print('4번 기능: 기준일로부터 0-4일, 총 5일 간의 데이터로 확진자 수 예측')
    print('5번 기능: 프로그램 종료\n')
    print('안내: 입력된 데이터가 많을수록 예측의 정확도가 높아집니다.\n')
    KeyInput=(input('실행 기능: '))
    print('=================================\n')
    MainScreen_ProgramSequence(int(KeyInput))

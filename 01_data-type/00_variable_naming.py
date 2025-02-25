# 변수명 작성 규칙

# 1. 변수명은 스네이크 케이스로 작성하며, 대소문자를 구분한다.
team_name = '송가람'
Team_name = 'thdrkfka'

print(f"team_name: {team_name}")
print(f"Team_name: {Team_name}")

# 2. 영문과 숫자를 혼합해 작성할 수 있다. (단, 숫자를 가장 앞에 작성할 수 없음.)
team_1_name = '송가람'
print(f"team_1_name: {team_1_name}")

# 3. 한글 변수명도 지정할 수 있다. (버전에 따라 한글을 encoding 못 할 수 있으니 사용 지양)
팀명 = '송가람'
print(f"팀명: {팀명}")

# 4. 언더바(_)를 제외한 특수문자는 사용이 불가능하다.
# team_@_name = '불가능' # 비활성화

# 5. 예약어를 사용할 수 없다.
# else = '불가능'

# 언더스코어(_)
# 값을 무시하고 싶은 경우, 특정 값을 무시하기 위한 용도로 사용할 수 있다.
# _ 붙은 메서드는 private 으로 사용하자는 약속 가지고 있다.
x, *_, y =(1,2,3,4,5)
print(x)
print(y)

# 숫자 값의 자릿수 구분을 위한 구분자로 사용할 수 있다.
million = 1_000_000
print(million)
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# a = 32, A = 65


def solution(new_id):
    # 1단계 모든 대문자 -> 소문자로
    after_id = new_id.lower()

    # 2단계: 허용된 문자만 남기기
    temp = ''
    for ch in after_id:
        if ch.isalnum() or ch in ['-', '_', '.']:
            temp += ch
    after_id = temp

    while '..' in after_id: # ...이든 ....이든 .....이든 그 안에 ..이 포함되어 있기 때문에 ..이 없을 때까지 .으로 치환
        after_id = after_id.replace('..','.')


    # 4단계
    after_id = after_id.strip('.')

    # 5단계
    if after_id == '':
        after_id = 'a'

    # 6단계
    if len(after_id) >= 16:
        after_id = after_id[:15]
        if after_id[-1] == '.':
            after_id = after_id[:-1]

    # 7단계
    while len(after_id)<3:
        after_id += after_id[-1]
    return after_id

id_list = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p", "BBBBBBBB"]

for new_id in id_list:
    print(solution(new_id))



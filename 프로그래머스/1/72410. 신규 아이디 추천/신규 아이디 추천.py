
def solution(new_id):
    # 1단계 모든 대문자 -> 소문자로
    after_id = new_id.lower()

    # 2단계: 허용된 문자만 남기기
    temp = ''
    for ch in after_id:
        if ch.isalnum() or ch in ['-', '_', '.']:
            temp += ch
    after_id = temp

    temp = ''
    prev = ''
    
    # 3단계
    for text in after_id:
        #print(f'text: {text}, prev : {prev}')
        if text =='.' and prev == '.': # 다음 문자가 .이 아니게 되면 문자열 조작을 안함
            continue
        temp += text
        prev = text
    after_id = temp

    # 4단계
    after_id = after_id.strip('.')

    # 5단계
    if len(after_id)==0:
        after_id += 'a'

    # 6단계
    if len(after_id) >= 16:
        after_id = after_id[:15]
        if after_id[-1] == '.':
            after_id = after_id[:-1]

    # 7단계
    if len(after_id) <= 2:
        for i in range(3-len(after_id)):
            after_id+=after_id[-1]
    return after_id
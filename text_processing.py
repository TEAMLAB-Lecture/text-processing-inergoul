#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""


def normalize(input_string):
    """
     인풋으로 받는 스트링에서 정규화된 스트링을 반환함
     아래의 요건들을 충족시켜야함
    * 모든 단어들은 소문자로 되어야함
    * 띄어쓰기는 한칸으로 되어야함
    * 앞뒤 필요없는 띄어쓰기는 제거해야함

         Parameters:
             input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호, 숫자로 이루어진 string
             ex - "This is an example.", "   EXTRA   SPACE   "

         Returns:
             normalized_string (string): 위 요건을 충족시킨 정규회된 string
             ex - 'this is an example.', 'extra space'

         Examples:
             >>> import text_processing as tp
             >>> input_string1 = "This is an example."
             >>> tp.normalize(input_string1)
             'this is an example.'
             >>> input_string2 = "   EXTRA   SPACE   "
             >>> tp.normalize(input_string2)
             'extra space'
    """
    word_list = input_string.split(' ')
    # 원래 string을 ' '로 쪼개서 빈 공백이면 없애버림
    normal_word_list = []
    for word in word_list:
        if word != '':
            normal_word_list.append(word)
    # 각 단어를 소문자로 바꿈
    normal_word_list = list(map(lambda w: w.lower(), normal_word_list))
    normalized_string = ' '.join(normal_word_list)

    return normalized_string


def no_vowels(input_string):
    """
    인풋으로 받는 스트링에서 모든 모음 (a, e, i, o, u)를 제거시킨 스트링을 반환함

        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호로 이루어진 string
            ex - "This is an example."

        Returns:
            no_vowel_string (string): 모든 모음 (a, e, i, o, u)를 제거시킨 스트링
            ex - "Ths s n xmpl."

        Examples:
            >>> import text_processing as tp
            >>> input_string1 = "This is an example."
            >>> tp.normalize(input_string1)
            "Ths s n xmpl."
            >>> input_string2 = "We love Python!"
            >>> tp.normalize(input_string2)
            ''W lv Pythn!'
    """
    no_vowel_string = input_string  # 인풋을 받아 답으로 변환될 변수
    vowel_list = ['a','e','i','o','u','A','E','I','O','U'] # 모음 리스트
    for v in vowel_list:
        no_vowel_string = no_vowel_string.replace(v, '')
    # 모음리스트에 있는 문자를 없애는 반복문

    return no_vowel_string

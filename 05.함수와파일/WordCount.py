import sys
import string, re
# sys.argv[0] - WordCount , sys.argv[1] - data/lorem.txt
# python WordCount.py data/loram.txt
# 파일의 총 단어, 고유단어, 빈도수 Top10 단어
if len(sys.argv) != 2:
    print('사용법: WordCount filename')
    sys.exit(-1)                        # 프로그램 종료 (0 - 정상종료, -1 - 에러발생, 양수 - 결과값 반환)
# print(sys.argv[0], sys.argv[1])

with open(sys.argv[1]) as file:
    contents = file.read()
clean_contents = re.sub('[' + string.punctuation + ']', '', contents).lower()
words = clean_contents.split()
print(f'총 단어는 {len(words):,d}개 이고, 고유 단어는 {len(set(words))}개 입니다.')

word_dict = {}
for i in words:
    if i not in word_dict:
        word_dict[i] = 1
    elif i in word_dict:
        word_dict[i] += 1
word_items = list(word_dict.items())
word_items.sort(key=lambda x: x[1], reverse = True)
print('사용 빈도가 높은 단어 Top10')
for word, count in word_items[:10]:
    print(f'\t{word}:\t{count:,d}')


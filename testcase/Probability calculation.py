import random
from loging.log import log
def num():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,'100'] # 可以换成接口返回的结果
    list2 = []
    for i in range(1000):
        num = random.choice(list1)
        list2.append(num)
    log.info(list2)
    sum = list2.count(1) + list2.count(2) + list2.count(3) + list2.count(4) + list2.count(5) + list2.count(6) + list2.count(7) + list2.count(8) + list2.count(9) + list2.count(0) +list2.count('100')
    log.info(f'一共执行的次数：{sum}')
    c = round(list2.count(1) / sum,3)
    print(c)
    log.info(f'数字 1 出现的次数:{list2.count(1)},百分比概率为：{list2.count(1)} / {sum}')
    log.info(f'数字 2 出现的次数:{list2.count(2)}')
    log.info(f'数字 3 出现的次数:{list2.count(3)}')
    log.info(f'数字 4 出现的次数: {list2.count(4)}')
    log.info(f'数字 5 出现的次数: {list2.count(5)}')
    log.info(f'数字 6 出现的次数: {list2.count(6)}')
    log.info(f'数字 7 出现的次数: {list2.count(7)}')
    log.info(f'数字 8 出现的次数: {list2.count(8)}')
    log.info(f'数字 9 出现的次数: {list2.count(9)}')
    log.info(f'数字 0 出现的次数: {list2.count(0)}')
    log.info(f"数字 100 出现的次数:'{list2.count('100')}")
if __name__ == '__main__':
    num()

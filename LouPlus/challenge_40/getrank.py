# -*- coding:utf-8 -*-

import sys
from pymongo import MongoClient
#import os
#import json

def get_rank(user_id):
    # 读取数据
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    #with open(os.path.join(os.path.dirname(__file__),'contests.json')) as f:
    #   con = json.load(f)
    dic = {}
    for c in contests.find():
        user_id = c['user_id']
        challenge_id = c["challenge_id"]
        score = c["score"]
        submit_time = c["submit_time"]
        # 判断 user_id 是否存在
        if dic.get(user_id) == None:
            dic[user_id] = [score,submit_time]
        else:
            dic[user_id][0] += score
            dic[user_id][1] += submit_time

    # 计算用户user_id的排名,总分数及花费的总时间
    score = sorted(dic.values(),key=lambda x:(-x[0],x[1]))
    for i,j in enumerate(score):
        dic[[k for k,v in dic.items() if v==j][0]].append(i+1)
    score,submit_time,rank = dic[user_id]
    return rank,score,submit_time

if __name__ == '__main__':
    # 判断参数格式是否符合要求
    if len(sys.argv) != 2:
        print('Parameter error')
        sys.exit()
    # 获取user_id参数
    user_id = sys.argv[1]

    # 根据用户ID获取用户排名,分数和时间
    userdata = get_rank(user_id)
    print(userdata)


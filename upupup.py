# -*- coding: utf-8 -*-
from lundaig import zhihudaiguang,vote_up

if __name__ == '__main__':
    lists = zhihudaiguang.objects.filter(is_vote_up=0)
    for i in lists:
        for rate in i.xiaobing:
            print rate['content']['text']

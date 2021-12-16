import itchat

# 获取自己的用户信息，返回自己的属性字典
itchat.search_friends()
# 获取特定UserName的用户信息
itchat.search_friends(userName='@abcdefg1234567')
# 获取任何一项等于name键值的用户
itchat.search_friends(name='wxceshi')
# 获取分别对应相应键值的用户
itchat.search_friends(wechatAccount='wceshi')
# 三、四项功能可以一同使用
itchat.search_friends(name='wxceshi', wechatAccount='wcceshi')

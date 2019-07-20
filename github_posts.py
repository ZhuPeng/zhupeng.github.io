#! -*- encoding: utf-8 -*-
# https://github.com/Chyroc/WechatSogou
import wechatsogou
ws_api = wechatsogou.WechatSogouAPI()
md = '\n'*5 + '**推荐阅读**\n\n'
cnt = 1
h = ws_api.get_gzh_article_by_history('GitHub精选')
# print h['gzh']
arr = []
for a in h['article']:
    if '本周排行' in a['title']:
        continue
    title = a['title']
    # TODO: content_url 在微信编辑器里面过不了认证
    arr.append('[%s](%s)' % (title, a['content_url']))
print md + '\n'.join(arr[:3])

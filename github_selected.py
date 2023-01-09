#! -*- encoding: utf-8 -*-
# https://github.com/Chyroc/WechatSogou
import wechatsogou
ws_api = wechatsogou.WechatSogouAPI()
md = '又到了每周 GitHub 排行精选推送时刻了。排行总榜可点击 [GitHub小程序](https://github.com/)。\n\n 本周 「GitHub 精选」分享的精品开源库如下：\n'
cnt = 1
h = ws_api.get_gzh_article_by_history('GitHub精选')
# print h['gzh']
for a in h['article']:
    # for k, v in a.items():
    #     print k, ' => ',  v
    title = a['title'].replace('本周排行', '上周排行')
    # TODO: content_url 在微信编辑器里面过不了认证
    md += '**%d、%s**\n\n%s\n\n相关文章：[%s](%s)\n\n' % (cnt, title, a['abstract'], title, a['content_url'])
    cnt += 1
print md

# __biz=MzA3MzE4ODY0Mg==&mid=2455983934&idx=1&sn=5f5b29c014dc177a80801268cb644e91&chksm=88852373bff2aa65a4198a4689bf7f7213890f2b59cd88a6322d96f3a9beccddb25225efc0ca&token=1259041873&lang=zh_CN#rd

# timestamp=1562413298&src=3&ver=1&signature=*o6UD2iqUl5Sst0sWiYoG5uQqGAfcB6wINtJDETZdboG2DjXooCauBNsIKRovwdgbss60V9IweIzE14k31Euee01**1rnF7a8NlBxGuAPCh*yPjG58BmCdIBva*L2-wGnYxpT2OH-MAEPsqN0vZxp79s1NcOI1k*SbRqshAHzVE=

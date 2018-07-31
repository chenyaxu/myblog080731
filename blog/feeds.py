from django.contrib.syndication.views import Feed

from blog.models import Post


class AllPostRssFeed(Feed):
    # 显示在阅读器上显示的标题
    title = '千峰博客'

    # 通过聚合阅读器跳转到的网址的地址
    link = '/blog/index/'

    # 显示在聚合阅读器上的描述信息
    description = '千峰博客项目'

    # 需要显示的内容条目
    def items(self):
        return Post.objects.all()

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s]%s' % (item.category, item.title)

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.content

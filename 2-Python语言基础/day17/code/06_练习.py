# 示例代码:
import re

s = '''</div>
<div class="r">
<h2>好看的玄幻小说</h2>
<ul>
<li><span class="s2"><a href="http://www.xbiquge.la/15/15409/">牧神记</a></span><span class="s5">宅猪</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/951/">伏天氏</a></span><span class="s5">净无痕</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/7/7931/">终极斗罗</a></span><span class="s5">唐家三少</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/14/14930/">元尊</a></span><span class="s5">天蚕土豆</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/29/29056/">仙武帝尊</a></span><span class="s5">六界三道</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/2/2210/">全职法师</a></span><span class="s5">乱</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/26/26874/">沧元图</a></span><span class="s5">我吃西红柿</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/13/13959/">圣墟</a></span><span class="s5">辰东</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/10/10512/">人皇纪</a></span><span class="s5">皇甫奇</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/10/">武炼巅峰</a></span><span class="s5">莫默</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/16/">上古强身术</a></span><span class="s5">我是多余人</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/14/14831/">飞剑问道</a></span><span class="s5">我吃西红柿</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/69/">帝霸</a></span><span class="s5">厌笔萧生</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/26/26519/">都市极品医神</a></span><span class="s5">风会笑</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/7/7877/">斗破苍穹</a></span><span class="s5">天蚕土豆</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/381/">天域苍穹</a></span><span class="s5">风凌天下</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/743/">诡秘之主</a></span><span class="s5">爱潜水的乌贼</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/2/2208/">霸皇纪</a></span><span class="s5">踏雪真人</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/1/1710/">斗罗大陆</a></span><span class="s5">唐家三少</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/27/27256/">临渊行</a></span><span class="s5">宅猪</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/32/32626/">叶辰孙怡夏若雪</a></span><span class="s5">全文免费阅读</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/0/119/">儒道至圣</a></span><span class="s5">永恒之火</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/2/2699/">妖神记</a></span><span class="s5">发飙的蜗牛</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/4/4714/">无敌剑域</a></span><span class="s5">青鸾峰上</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/14/14591/">斗罗大陆4终极斗罗</a></span><span class="s5">唐家三少</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/15/15499/">万道剑尊</a></span><span class="s5">打死都要钱</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/11/11621/">开天录</a></span><span class="s5">血红</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/3/3459/">雪鹰领主</a></span><span class="s5">我吃西红柿</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/11/11559/">太初</a></span><span class="s5">高楼大厦</span></li>
<li><span class="s2"><a href="http://www.xbiquge.la/21/21223/">召唤梦魇</a></span><span class="s5">滚开</span></li>
</ul>
<div class="page_b page_b2">喜欢就收藏我们</div>
</div>
'''

pattern = '<a href="(?:.*?)">(.*?)</a></span><span class="s5">(.*?)</span>'
xs_list = re.findall(pattern, s, re.S)
print(xs_list)


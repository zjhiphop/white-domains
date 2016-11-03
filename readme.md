# 域名白名单(White Domains)


在做与域名有关的威胁情报、态势感知等项目时，常常会用到域名的白名单来过滤大量的域名数据。网上关于域名的白名单的list不多，并且光靠Alexa排名也无法过滤掉大量“中国特色”的域名，所以萌生了我做域名白名单的想法。


## v1.0  解决的主要问题

### 1. 使用[chinaz][1]网站排名生成中国特色的白名单 

由于[Alexa][2]网站排名是全世界的，但我们经常会与很多拼音首字母+数字的中国域名打交道，例如：bjkszs.com（宝鸡考试招生网）、xa.1010jz.com（西安兼职网）等等。这些域名不在Alexa的收录之内，并且看上去有点像C&C或者钓鱼域名。所以为了减少人工辨识这些域名的工作量，我爬取了chinaz网站的中文top域名列表，并与Alexa的排名互相补充，共同完成了白名单的生成。

### 2. 利用[Public Suffix List][3]对域名的TLD、2LD、3LD进行提取
域名白名单里有大量的数据，但是形如www.baidu.com、zhidao.baidu.com、tieba.baidu.com这样的域名的“可注册”部分是相同的，所以它们理应归为一个域名。另外域名的后缀太多，除了.com.cn这样的TLD，还有很多公开的域名服务的Private TLD，如blogspot.co.uk、s3-ap-northeast-1.amazonaws.com等等。好在Mozilla创建了PublicSuffixList(PSL)，它的本意是用于前端的同源策略，而我们可以通过不同语言的Library可以很容易地判断一个域名哪些是它的后缀、哪些是它可以注册的部分、哪些是它的子域名。利用PSL可以方便我们做很多事，该项目利用PSL再一次“精简”了我们的白名单列表，使得加载的程序更加高效。



作者 [@tianjianbo][4]    
2016 年 11月 04日    


  [1]: http://top.chinaz.com/
  [2]: http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
  [3]: https://publicsuffix.org/list/public_suffix_list.dat
  [4]: http://www.tianjianbo.com
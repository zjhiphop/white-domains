# -*- coding:utf-8 -*-
__author__ = 'tianjianbo@126.com'
from publicsuffixlist import PublicSuffixList

cn = set()
alexa = set()
psl = PublicSuffixList()
with open("alexa-top-1m.csv") as f:
    for i in xrange(0, 1000000): #此处可以控制Alexa排名选择个数
        domain = f.readline().strip().split(',')[1]
        domain_2ld = psl.privatesuffix(domain)
        if domain_2ld is None:
            alexa.add(domain)
        else:
            alexa.add(domain_2ld)
with open("result/chinaz_top_domains.txt") as f:
    for line in f:
        domain = line.strip()
        domain_2ld = psl.privatesuffix(domain)
        if domain_2ld is None:
            cn.add(domain)
        else:
            cn.add(domain_2ld)
with open("whitedomains.txt", 'w') as f:
    unionset = cn | alexa
    for domain in unionset:
        try:
            f.write(domain.strip() + '\n')
        except:
            print "An Error Occured, program continue......"
            continue
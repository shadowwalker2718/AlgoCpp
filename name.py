import sys
import datetime
import re, string
pattern = re.compile('\"\d+.\",')

pattern.sub('', string.printable)


now = datetime.datetime.now()
date_time=now.isoformat()
today=datetime.date.today()

s=sys.argv[1:]
tags='"'+'","'.join(sys.argv[1:])
tags=pattern.sub('', tags)

title=' '.join(s).replace('._','_')
fname=str(today)+'-'+'_'.join(s).replace('._','_')+'.Rmd'

template='''---
title: "{title}"
date: {date_time}
categories: ["{tags}"]
tags: [{tags}]
mathjax: true
---
'''.format(title=title, date_time=date_time,tags=tags)

#print fname
#print template

f=open('content/post/'+fname, 'w')
f.write(template)
f.close()

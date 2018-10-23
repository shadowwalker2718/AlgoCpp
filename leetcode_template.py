#!/usr/bin/python
import sys
import datetime, pytz
import re, string


pattern = re.compile('\"\d+\.*\",')
now = datetime.datetime.now(pytz.timezone('US/Eastern'))
date_time=now.replace(microsecond=0).isoformat()
today=datetime.date.today()

s=sys.argv[1:]
if s[0][-1] != '.':
  s[0]+='.'

_tags='"'+'","'.join(sys.argv[1:])+'"'
tags=_tags.replace('.','')
url='https://leetcode.com/problems/'+'-'.join(pattern.sub('',_tags).split(',')).replace('"','')

title=' '.join(s).replace('._','_')
fname=str(today)+'-'+'_'.join(s).replace('._','_')+'.Rmd'

template='''---
title: "{title}"
authors: ["henrywu"]
date: {date_time}
categories: [{tags}]
tags: [{tags},"leetcode"]
mathjax: true
---

----

- Problem: {sss}

{url}

----

## Solution(s)

### C++

### Java

### Python

### Go

### Javascript

### Scala

### Swift

## Time and Space Complexity

Time complexity : $O()$  
Space complexity: $O()$

'''.format(title=title, date_time=date_time,tags=tags,sss=' '.join(s),url=url)

#print fname
#print template
#sys.exit(0)

f=open('content/post/'+fname, 'w')
f.write(template)
f.close()

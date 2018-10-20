---
date: 2018-09-26T06:00:00+06:00
lastmod: 2018-10-11T17:30:00+06:00
title: Authors Setup Guide
authors: ["henrywu","achary"]
categories:
  - features
tags:
  - authors
slug: authors
---

## Blog

https://zxi.mytechroad.com/blog/

### C++

https://github.com/shadowwalker2718/LeetCode-2

### Java

https://github.com/qiyuangong/leetcode/tree/master/java

### Python

https://github.com/Garvit244/Leetcode  
https://github.com/yuzhoujr/leetcode  
https://github.com/qiyuangong/leetcode/tree/master/python  
https://github.com/illuz/leetcode/tree/master/solutions  
https://github.com/shichao-an/leetcode-python

### Go

https://github.com/aQuaYi/LeetCode-in-Go/  
https://www.jianshu.com/c/8e1c238fc4cb  
https://github.com/hitzzc/go-leetcode

### Javascript

https://github.com/chihungyu1116/leetcode-javascript  
https://github.com/hanzichi/leetcode  
https://github.com/paopao2/leetcode-js

### Scala

https://github.com/wqlin/LeetCode/tree/master/src





Engimo supports multiple authors for your site. Just make sure you have the following configuration in your site's **`config.toml`**:

```toml
[taxonomies]
author = "authors"
```

Engimo treats Authors as a [Hugo Taxonomy](https://gohugo.io/content-management/taxonomies/).

## Author's Profile

For adding an author to your site:

- Create **`data/authors`** folder in your site's root directory
- Create a file with the filename format: **`<username>.toml`**

Now, add information about the author using the structure below:

**/data/authors/henrywu.toml**

{{< file "data/authors/henrywu.toml" >}}

_You can use either the `[email]` fields or the `[social.email]` field. You don't need to fill them both. However, it is encouraged to use `[email]` instead of `[social.email]`._

## Adding Authors to Contents

For adding authors to your content include the following option in your content's front-matter:

```yaml
---
authors: ["henrywu"]
---
```

- `authors` [`Array` of `String`s]: username of authors

That's all.

---
title: cdn-dns-1
documentName: CDN & DNS 1
description: description
published: true
---

Heading H1:
# Main Heading 

Heading H2:
## Smaller Heading

Heading H3:
### Another small Heading

Heading H4:
#### Another small Heading

Heading H5:
##### And even that's one 

Heading H6:
###### The smallest heading

Text:

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 

Bold:

**Lorem ipsum**

Italic:

*dolor sit amet*

Italic inside Bold:

**consectetur _adipiscing_ elit**

Italic and Bold:

***sed do eiusmod tempor***

Strikethrough:

 ~~Lorem ipsum dolor sit amet~~

Subscript, superscript: 

<sub>consectetur adipiscing</sub> <sup>eiusmod tempor</sup> 

String Quote: 

> Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Phrase Quote:

Lorem ipsum dolor `sit amet`, consectetur adipiscing elit.

Code:

Lorem ipsum dolor sit amet:
```
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua.
```

Example of Code with color syntax:

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

Link:

[Lorem ipsum dolor sit amet](https://www.lipsum.com/), consectetur adipiscing elit. 

Anchor:

[Lorem ipsum dolor sit amet](cdn-dns/cdn-dns-1.md#h2-smaller-heading), consectetur adipiscing elit. 
<!-- Can't check anchor because of preprod-mode. Have to publish the page to know, how it works. -->

Relative link to another aticle in repository: 

[Another atricle in repository](./cdn-dns-2.md) 

Image (MarkDown):
![](https://i.ytimg.com/vi/1cDcHq7nQFM/maxresdefault.jpg)

Image (HTML): 
*Also can add picture by HTML*
<picture>
  <img alt="useful seo text" src="https://i.ytimg.com/vi/1cDcHq7nQFM/maxresdefault.jpg">
</picture>
  
Unordered list:
  - consectetur adipiscing elit, 
  - sed do eiusmod tempor incididunt 
  - ut labore et dolore magna aliqua.

Ordered list:
  1. consectetur adipiscing elit, 
  2. sed do eiusmod tempor incididunt 
  3. ut labore et dolore magna aliqua.

Nested list:

1. First list item
   - First nested list item
     - Second nested list item
2. Second list item
   - Second nested list item
   - Third nested list item
     - Fourth nested list 
       - Fifth nested list  

To do task list:
- [x] First list item
- [ ] Second list item
- [ ] Add delight to the experience when all tasks are complete :tada:

Table:
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cellazazazazazazazaaaaaaaaazaaaaaaaaaaaaaaaaaaaaaaaaa  |
| Content Cell  | Content Cell  |

Tables with wore wide column:
| Command | Description |
| --- | --- |
| *git status* | **List all new or modified files** |
| git diff | ![Image](https://i.ytimg.com/vi/1cDcHq7nQFM/maxresdefault.jpg) |


---
title: cdn-dns-1
documentName: CDN & DNS 1
description: description
published: true
---

List of elements:

# (H1) Main Heading 
## (H2) Smaller Heading
### (H3) Another small Heading
#### (H4) Another smaller Heading 
##### (H5) And even that's one 
###### (H6) The smallest heading 

(Ordinary text) Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 

(Styling text: bold & italic with variations) **Lorem ipsum** *dolor sit amet*, **consectetur _adipiscing_ elit**, ***sed do eiusmod tempor*** incididunt ut labore et dolore magna aliqua. 

(Extra-Styling text: strikethrough, subscript, superscript) ~~Lorem ipsum dolor sit amet~~, <sub>consectetur adipiscing</sub> elit, sed do <sup>eiusmod tempor</sup> incididunt ut labore et dolore magna aliqua.

> (String Quoting) Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

(Phrase Quoting) Lorem ipsum dolor `sit amet`, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

(Code) Lorem ipsum dolor sit amet:
```
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua.
```

(Example of code with color syntax)
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

(Link) [Lorem ipsum dolor sit amet](https://www.lipsum.com/), consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

(Anchor) [Lorem ipsum dolor sit amet](cdn-dns/cdn-dns-1.md#h2-smaller-heading), consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
<!-- Can't check anchor because of preprod-mode. Have to publish the page to know, how it works. -->

(Relative link to another aticle at repository) [Another atricle in repository](./cdn-dns-2.md) 

![Image](https://i.ytimg.com/vi/1cDcHq7nQFM/maxresdefault.jpg)

Also can add picture by HTML
<picture>
  <img alt="useful seo text" src="https://i.ytimg.com/vi/1cDcHq7nQFM/maxresdefault.jpg">
  </picture>
  
  (Unordered list) Lorem ipsum dolor sit amet:
  - consectetur adipiscing elit, 
  - sed do eiusmod tempor incididunt 
  - ut labore et dolore magna aliqua.

(Ordered list) Lorem ipsum dolor sit amet:
  1. consectetur adipiscing elit, 
  2. sed do eiusmod tempor incididunt 
  3. ut labore et dolore magna aliqua.

(Mixed list)
1. First list item
   - First nested list item
     - Second nested list item

2. Second list item
   - Second nested list item
   - Third nested list item
     - Fourth nested list 
       - Fifth nested list  

(To do task list) 
- [x] First list item
- [ ] Second list item
- [ ] Add delight to the experience when all tasks are complete :tada:

(Table)
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cellazazazazazazazaaaaaaaaazaaaaaaaaaaaaaaaaaaaaaaaaa  |
| Content Cell  | Content Cell  |


| Command | Description |
| --- | --- |
| *git status* | **List all new or modified files** |
| git diff | ![Image](https://i.ytimg.com/vi/1cDcHq7nQFM/maxresdefault.jpg) |


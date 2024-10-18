# BSL-Group

git clone https://github.com/bsl-group/bsl-group.github.io.git


_config.yaml: site configuration (MUST IGNORE)

_posts: all posts
-> categories:
--> /_posts/research-papers

### Add authors here: _data/authors.yml
```
1023  cd _posts
 1024  ls
 1025  cd home
 1026  cd ..
 1027  ls
 1028  cd research-papers/
 1029  ls
 1030  code 2022-06-15-dynamic-history-of-inner-core.md
 ---
1004  cd images/
 1006  mkdir dynamic-history-of-inner-core
 1008  cd dynamic-history-of-inner-core/
 1010  wget https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41561-021-00761-w/MediaObjects/41561_2021_761_Fig3_HTML.png?as=webp
 1015  mv 41561_2021_761_Fig3_HTML.png\?as\=webp fig2.png
 1016  ls
 1017  cd ..
 1018  ls
 1019  cd ..ls dynamic-history-of-inner-core
 1020  ls dynamic-history-of-inner-core
 1021  cd ..
 1022  ls
 1023  git status
 1024  git add -A
 1025  git status
 1026  git commit -m "new post"
 1027  git push
 ```
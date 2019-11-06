#git

## shell command
- cd
- vi 
- mkdir
- rm
- rm -rf

## vim command
- v
- d
- dd
- yy
- p
- a
- i
- o

## git start

## git init

>>> git config --global user.name "dopa213"
>>> git config --global user.email "kick50215@naver.com"
#  editor vim check && page cat check by command
>>> git config --global core.editor "vim"
>>> git config --global core.pager "cat"

>>> git status
# => fatal: not a git repository (or any of the parent directories): .git
# you need command
>>>git init

# if you did install the folder what is dengerous
# remove .git

# git remote (원격) add (추가) fastcampus (별명) git....(보낼 주소)
git remote add fastcampus git@github.com:dopa213/new_git_study.git

#fastcampus bring url
git remote get-url fastcampus

vi README.md

# write text

git status
# => can find diff

# conclusion nothing

#나중에 공부해보기 window 와 unix 계열 os에서 enter 입력되는 방식의 차이
#warning: LF will be replaced by CRLF in README.md.
#The file will have its original line endings in your working directory


#docs documentation(제목에서 명확하게 어떤일을 했는지 함축적으로 알려줘야함)
#feat feature (기능개발)
#conf configuration (개발 환경 설정 ex. jupyter install, python 3.6 변경사항)
#fix  bug-fix

>>> git add README.md

>>> git status

>>> git commit

>>> git status

# => nothing to commit, working tree clean

# -u first time you should -u option for checking url between fastcampus and real - url
git push -u fastcampus master


git clone
- do TIL for today
- collaborate with co-worker
- hackerrank problems

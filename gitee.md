
# gitee 使用
itee 
```shell
git config --global user.name "martin"
git config --global user.email "duan_luyao@163.com"

git init 
git remote add origin https://gitee.com/martind/quick_start.git

git pull origin master
# 如果出现git fatal: 拒绝合并无关的历史的错误
git pull origin master --allow-unrelated-histories

# <这里需要修改/添加文件，否则与原文件相比就没有变动>
git add .
git commit -m "第一次提交"
git push origin master

 
```
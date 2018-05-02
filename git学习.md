# git学习笔记


```python
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

git add file_name
git commit -m "name"

# 穿梭前
git log
git log --pretty=oneline
git reset --hard id
# 穿梭后
git reflog

# 查看指向
git reset --hard HEAD^

# 查看git提交状态
git status

# git丢弃工作区修改,如果没有提交到暂存区，撤销后就会回到和版本库一样的状态，如果已经提交到暂存区，就会回到添加到暂存区的初始状态。
git checkout -- name.name

# 修改工作区内容，并添加到暂存区，丢弃修改，分2步，
git reset HEAD name.name
git checkout -- name.name

# 删除文件
git rm file.name

# 误删恢复
git checkout -- file.name

# 创建ssh key
ssh-keygen -t rsa -C "youremail@example.com"

# 把本地库推送到远程库上
git push -u origin master


```


# Mathematica笔记本的版本控制

## Word是怎么控制的

1. 首先往attributes里面添加：

`*.docx diff=word`

2. 下载一个Word到txt的转换器`docx2txt`

3. 创建一个脚本`docx2txt.sh`，里面的内容是：

```shell
#!/bin/bash
docx2txt.pl "$1" -
```

其中的减号是docx2txt.pl的输出指令。如果不加减号的话，它会将docx转化为txt指令，但是没有终端输出。git diff需要终端输出，所以要加一个减号。

这样当你执行git diff的时候，就会有类似于：

```shell
$ git diff
diff --git a/chapter1.docx b/chapter1.docx
index 0b013ca..ba25db5 100644
--- a/chapter1.docx
+++ b/chapter1.docx
@@ -2,6 +2,7 @@
 This chapter will be about getting started with Git. We will begin at the beginning by explaining some background on version control tools, then move on to how to get Git running on your system and finally how to get it setup to start working with. At the end of this chapter you should understand why Git is around, why you should use it and you should be all setup to do so.
 1.1. About Version Control
 What is "version control", and why should you care? Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. For the examples in this book you will use software source code as the files being version controlled, though in reality you can do this with nearly any type of file on a computer.
+Testing: 1, 2, 3.
 If you are a graphic or web designer and want to keep every version of an image or layout (which you would most certainly want to), a Version Control System (VCS) is a very wise thing to use. It allows you to revert files back to a previous state, revert the entire project back to a previous state, compare changes over time, see who last modified something that might be causing a problem, who introduced an issue and when, and more. Using a VCS also generally means that if you screw things up or lose files, you can easily recover. In addition, you get all this for very little overhead.
 1.1.1. Local Version Control Systems
 Many people's version-control method of choice is to copy files into another directory (perhaps a time-stamped directory, if they're clever). This approach is very common because it is so simple, but it is also incredibly error prone. It is easy to forget which directory you're in and accidentally write to the wrong file or copy over files you don't mean to.
```

## Mathemaica笔记本

相同的思路，但是我觉得MMA的diff应该有以下几点支持：

- 可以查看图片

- 可以与乌龟客户端结合

  
# 测试

## 普通计算

```mathematica
1 + 1

(*2*)
```

```mathematica
Sin[x + 1]

(*Sin[1 + x]*)
```

## 画图

```mathematica
Plot[Sin[x], {x, 0, 1}]
```

![026uxzej9mafr](https://gitee.com/wei_hong_liang/My_Picture_Bed/raw/master/20200923144647.png)

```mathematica
DensityPlot[Sin[x y], {x, 0, 3}, {y, 0, 3}]
```

![1bptnm94jalyz](https://gitee.com/wei_hong_liang/My_Picture_Bed/raw/master/20200923144647-1.png)

```mathematica
Plot3D[Sin[x y], {x, 0, 3}, {y, 0, 3}]
```

![11kfsagz2jw7a](https://gitee.com/wei_hong_liang/My_Picture_Bed/raw/master/20200923144647-2.png)

## 面板

```mathematica
class = Classify[{1 -> "A", 2 -> "B"}]
```

![0l65it4xi3ew9](https://gitee.com/wei_hong_liang/My_Picture_Bed/raw/master/20200923144647-3.png)

```mathematica
class // Information
```

![1e92b6s35x304](https://gitee.com/wei_hong_liang/My_Picture_Bed/raw/master/20200923144647-4.png)

## 不同Cell

```mathematica
{{1, 2}, {3, 4}} // MatrixForm
```

![0tf7n6kng4irs](https://gitee.com/wei_hong_liang/My_Picture_Bed/raw/master/20200923144647-5.png)

```mathematica
{{1, 2}, {3, 4}} // TeXForm
```

```mathematica
\left(
\begin{array}{cc}
 1 & 2 \\
 3 & 4 \\
\end{array}
\right)
```

```mathematica
<< M2MD`
```

```mathematica
MDExport["G:\\GitHub Local \
Repository\\Mathematica-Notebook-VersionControl\\nb2md-test\\exported.\
md", EvaluationNotebook[]]

(*"G:\\GitHub Local \
Repository\\Mathematica-Notebook-VersionControl\\nb2md-test\\exported.\
md"*)
```

```mathematica
$UserBaseDirectory
```

```mathematica

```

```mathematica
$ScriptCommandLine + 1
```

```mathematica
NotebookGet
```
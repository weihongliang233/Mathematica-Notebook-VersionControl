

<div class="diff-topbar">
<table class="diffpage-html-firstlast">
<tbody><tr>
<td style="text-align: left;"><a class="diffpage-html-a" onclick="scrollToEvent(event)" id="first-diff" href="#removed-diff-0" next="removed-diff-0"><img class="diff-icon" src="images/diff-first.gif" title="Go to first change."></a><a class="diffpage-html-a" onclick="scrollToEvent(event)" href="#removed-diff-0">&nbsp;first</a></td><td style="text-align: center; font-size: 140%;"><a style="font-size: 100%;" class="diffpage-html-a" href="http://code.google.com/p/daisydiff/">Daisy Diff</a> compare report.<br>
<span style="font-style: italic; font-size: 70%;">Click on the changed parts for a detailed description. Use the left and right arrow keys to walk through the modifications.</span></td><td style="text-align: right;"><a class="diffpage-html-a" onclick="scrollToEvent(event)" href="#removed-diff-1">
              last&nbsp;</a><a class="diffpage-html-a" onclick="scrollToEvent(event)" id="last-diff" href="#removed-diff-1" previous="removed-diff-1"><img class="diff-icon" src="images/diff-last.gif" title="Go to last change."></a></td>
</tr>
</tbody></table>
</div>
# 测试
## 普通计算
    1 + 1
    
    (*2*)

    Sin[x + 1]
    
    (*Sin[1 + x]*)

## 画图
    <span class="diff-html-removed" id="removed-diff-0" previous="first-diff" changeid="removed-diff-0" next="removed-diff-1" onclick="return tipR(constructToolTipR(this));">Plot[Sin[x], {x, 0, 1}]
    </span>
&#13;&#10;<span class="diff-html-removed" previous="first-diff" changeid="removed-diff-0" next="removed-diff-1" onclick="return tipR(constructToolTipR(this));">![026uxzej9mafr](img\026uxzej9mafr.png)</span><span class="diff-html-removed" previous="first-diff" changeid="removed-diff-0" next="removed-diff-1" onclick="return tipR(constructToolTipR(this));"></span>

    DensityPlot[Sin[x y], {x, 0, 3}, {y, 0, 3}]

&#13;&#10;![1bptnm94jalyz](img\1bptnm94jalyz.png)
## 面板
    class = Classify[{1 -&gt; "A", 2 -&gt; "B"}]

&#13;&#10;![0l65it4xi3ew9](img\0l65it4xi3ew9.png)

    class // Information

&#13;&#10;![1e92b6s35x304](img\1e92b6s35x304.png)
## 不同Cell
    {{1, 2}, {3, 4}} // MatrixForm

&#13;&#10;![0tf7n6kng4irs](img\0tf7n6kng4irs.png)

    {{1, 2}, {3, 4}} // TeXForm

    \left(
    \begin{array}{cc}
     1 &amp; 2 \\
     3 &amp; 4 \\
    \end{array}
    \right)

    &lt;&lt; M2MD`

    MDExport["G:\\GitHub Local \
    Repository\\Mathematica-Notebook-VersionControl\\nb2md-test\\exported.\
    md", EvaluationNotebook[]]
    
    (*"G:\\GitHub Local \
    Repository\\Mathematica-Notebook-VersionControl\\nb2md-test\\exported.\
    md"*)

    <span class="diff-html-removed" id="removed-diff-1" previous="removed-diff-0" changeid="removed-diff-1" next="last-diff" onclick="return tipR(constructToolTipR(this));">\[CenterDot]\[CenterDot]\[CenterDot]$UserBaseDirectory
    </span>
    <span class="diff-html-removed" previous="removed-diff-0" changeid="removed-diff-1" next="last-diff" onclick="return tipR(constructToolTipR(this));">
    </span>
    <span class="diff-html-removed" previous="removed-diff-0" changeid="removed-diff-1" next="last-diff" onclick="return tipR(constructToolTipR(this));">$ScriptCommandLine + 1
    </span>
    <span class="diff-html-removed" previous="removed-diff-0" changeid="removed-diff-1" next="last-diff" onclick="return tipR(constructToolTipR(this));">NotebookGet
    </span>
    <span class="diff-html-removed" previous="removed-diff-0" changeid="removed-diff-1" next="last-diff" onclick="return tipR(constructToolTipR(this));">a
    </span>
    <span class="diff-html-removed" previous="removed-diff-0" changeid="removed-diff-1" next="last-diff" onclick="return tipR(constructToolTipR(this));">SetOptions[EvaluationNotebook[], 
      NotebookEventActions -&gt; {"WindowClose" :&gt; (a = a + 1)}];
    </span>
    <span class="diff-html-removed" previous="removed-diff-0" changeid="removed-diff-1" next="last-diff" onclick="return tipR(constructToolTipR(this));">a
    
    (*1*)
    </span>
    <span class="diff-html-removed" previous="removed-diff-0" changeid="removed-diff-1" next="last-diff" onclick="return tipR(constructToolTipR(this));">"G:\\GitHub Local \
    Repository\\Mathematica-Notebook-VersionControl\\nb2md-test\\exported.\
    html"
    </span>



# 999.Available Captures for Rook ![](https://img.shields.io/badge/-easy-green.svg)

## 车的可用捕获量

在一个8 × 8的棋盘上，有一个白色车（rook），也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符“R”，“.”，“B”和“p”给出。大写字符表示白棋，小写字符表示黑棋。</br>
车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。<br>返回车能够在一次移动中捕获到的卒的数量。

示例：

![](./999problems_example.png)

输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
<br>
输出：3
<br>
解释：在本例中，车能够捕获所有的卒。
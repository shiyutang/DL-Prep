# DL-Prep
**深度学习基础知识，算法，面试题**
**由 UESTC DL 学习小组开发和维护**

1. [数学相关(Math)](01_Math/README.ipynb)
2. [机器学习基础相关(ML)](02_ML_knowledge/README.ipynb)
3. [深度学习相关(DL)](03_DL_knowledge/README.ipynb)
4. [基础算法题相关(AL)](04_Algorithms/README.ipynb)
5. [语言相关(LA)](05_Language/README.ipynb)
6. [深度学习框架(DF)](06_DL_framework/README.ipynb)
6. [面试题(IQ)](07_Interview_Questions/README.ipynb)


## 维护笔记
1. 当需要更改前，增加一个新的 branch，确认自己的更改好之后，再和 master 合并
1. 当需要添加新知识时，可以对照目录，插入到对应的位置，并按照格式增加目录和在相应位置增加内容
2. 插入图片时，先将图片放入 Pics 文件夹，随后按照相对路径插入
3. 插入了目录，但是又没有时间写内容？ 可以加个 **todo** 之后补全
3. 大纲和格式可能有错漏，欢迎互相指正修改~

### 增加了 Jupyter Notebook之后
我们将在 README.md 的基础上增加 Jupyter Notebook， 这样，我们可以方便在本地查看公式，并运行代码。MD则在 Github 上可以提供大纲的预览。
建议的方式是：
- 查看：将 Github 的仓库拉取到本地，并在本地 launch Jupyter Server 进行查看
- 修改：新开 branch 后在 Pycharm 等编辑器中编辑，编辑 Jupyter Notebook 的同时，我们需要在MD里面进行目录的同步。并用【查看】的方式预览编辑效果
- 合并：本地修改好了之后，使用 Git commit， Git push， 再在本地或者云端merge

原则是：Jupyter Notebook 负责内容，因此 MarkDown 中有的内容，Jupyter Notebook 中一定会有； 同时 Readme.md 提供预览，因此需要有大纲和相关说明。 
先行编辑 Jupyter Notebook，之后在 MarkDown 中相应更新。

### 如何添加 Anchor ？
Anchor 帮助我们快速跳转到需要的内容，那么如何添加 anchor 呢？
详见 [添加Anchor](Utils/AddAnchor.ipynb)

## 其他
欢迎大家 fork, pull request, star 这个项目
大部分都是手打，根据资料整理，如有问题，欢迎 fork 之后 pull request 或者 issue 中提出，我们会尽可能及时回复

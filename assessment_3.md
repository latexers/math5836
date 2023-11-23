# 决策树
## 回归树
## 决策树剪枝

## 集成学习
### Bagging
### Extra-Trees(Feature Importance)


# 作业
### 三个方向：
1. 神经网络基础
2. 决策树与集成学习
3. 机器学习研究项目

### Option I
### Part A
#### Q2: 隐藏神经元个数对模型性能的影响；
Key Points: 
1. 比较几个不同神经元个数的神经网络模型；
    + 控制变量：只有神经元个数不同；
    + 数据要相同：公用一个，训练集和测试集划分，数据预处理；
    + 优化器相同：SGD
    + 损失函数要相同；
    + 迭代次数；
    + 学习率

2. 怎么比较：
    + 准确性(训练集和测试集)
    + Metric: 分类准确性(Accuracy), Recall, 混淆矩阵，FN，FT，ROC曲线，AUC曲线；
3. 怎么Discussion:
    + 分析结果，得出结论

Q3: 学习率对神经网络模型的影响
**注意**: 学习率与优化过程中，损失函数的下降速度密切相关，建议结果中包含训练过程中Loss函数的下降曲线。

Q4: L2和Dropout的影响
**注意**: L2,Dropout本身会有参数，所以比较过程中如果做的比较细，建议：比较不同的L2的权重参数和Dropout概率对模型性能的影响。如果只比较L2和Dropout,那么就用默认参数。

### Report
#### Abstract
论文报告的一个浓缩版本：
1. 研究的是什么问题：稳定定义；
2. 用了什么方法；
3. 得到了什么结果；
4. 具有什么意义；

#### Introduction

#### Related Work
conclusion: d
#### Method
方法：、
神经网络，CNN，RNN，方法介绍一下：
flowchart
1. Data precessing
2. Model build:
    +用什么模型；
    参数怎么设置的，我为什么要设置这些参数；
    +目标函数
#### Result
##### Experiment sets
用的什么样的数据集，数据集来源，大小，训练集和测试集划分原则，比例
##### Evaluation metrics
Recall, Precsion, AUC, ROC定义，计算的公式，评价的意义，指标的局限性
##### Evaluation results
Table, Figure
每个表和Figure会有对应的说明，针对性的Discussion;
As shown figure XXX, indicates that Adam faster than SGD。。。。。

#### Discussion
最后的Discussion:针对整个Project的神经网络：应该讨论神经网络分类器最后好的神经网络分类器的一个建议
讨论结果；
根据结果，有一些建议
Suggestions:
+ 你需要对你的数据进行描述性分析
+ 选择一个合适学习率
+ 考虑到下降速度
+ 第四个选择
#### Conclusion
结论：再这个数据集上XXXX方法最优的，模型的泛化能力怎么样。加一部分：未来应该从哪些方面来提高我明显的性能。

#### Reference
参考文献：尽量参考新的，至少老师看起来；

### 评分标准
#### 报告概览
#### 结果讨论
#### 报告就结构
#### 参考引用
# EEG Universal Foundation Model

### （脑电通用基础模型）

---

##### 简述：

1. 主要包括：预训练（无监督）和微调（有监督）两个部分
2. 可以适应不同的BCI下游任务（包括但不限于：情绪分类、癫痫检测、睡眠阶段、运动想象）

EEG 数据描述：

1. 数据形式：通道，时间（采样率）——>（C，T）
2. 特征：时间、空间、频率
3. 信噪比（噪声大）、采集设备、采集通道等，在不同数据集上都不相同

---

## 目前研究：

- ### LaBraM

    ``````txt
    团队：吕宝粮(上海交通大学)
    时间：2024（ICLR）
    简述：
    	1、基于掩码和重建（振幅和相位）
    	2、从LLM迁移到LEM
    	3、密码本（经过对每个patch的编码后，在密码本中找到最近邻的向量代替）[2-范数]
    	4、原始EEG信号的随机性，不稳定性，非线性，低信噪比（很难重建）
    	5、傅里叶中的频率和相位的分布揭示了大脑活动的本质
    
    ``````

    

- ### NeuroLM

    ``````
    团队：吕宝粮（上海交通大学）
    时间：2025（ICLR）
    简述：
    	1、在LaBraM的基础上进行的改进
    	2、将EEG信号当作外语（进行文本和EEG的域对齐）[不涉及细粒度对齐]
    	3、有密码本
    	4、多任务
    	5、掩码-重建（时间和频率）
    	6、GAN（对抗）用来区分输入的特征属于文本还是EEG，从而导致EEG编码和文本编码会越来越相似，最终落在同一个语义空间
    	
    ``````



- ### BIOT

    ``````txt
    团队：（哈佛医学院）
    时间：2023（Neur IPS）
    简述：
    	1、分patch，通道和位置嵌入
    	2、各种格式的生物信号标记成统一的“句子”
    	3、掩码重建
    	4、transformer
    ``````

    

- ### BENDR

    ``````txt
    团队：(多伦多大学)
    时间：2021（）
    简述：
    1、1D-CNN + transformer [cls标记]
    2、对比自监督学习（masked）
    ``````

- ### EEGPT

    ``````
    团队：李海峰(哈尔滨工业大学)
    时间：2024（Neur IPS）
    简述：
    	1、基于掩码重建的双自监督学习
    	2、时空表示对齐
    	3、局部时空嵌入+分块策略+掩码-重建+动量编码器
    
    ``````

- ### CBRAMOD

    ``````
    团队：潘纲(浙江大学)
    时间：2024（）
    简述：
    	1、提取时间-频率特征
    	2、十字交叉 Transformer（通道和时间注意力）
    	3、非对称条件位置编码
    	4、掩码重建
    	5、训练数据集（TUEG：处理后的干净数据1,109,545个samples）在处理后的；10个下游任务在12个数据集上
    ``````

---

## 下游任务（总结）：

- #### Emotion Recognition                         （情绪识别）    ：**SEED、SEED_IV**

- #### Motor Imagery Classification（运动图像分类）    ：

- #### Sleep Staging（睡眠分期）                                             ：

- #### Seizure Detection（癫痫发作检测）                           ：**CHB-MIT**

- #### Imagined Speech Classification（想象语音分类）：

- #### Mental Disorder Diagnosis（精神障碍诊断）         ：

- #### Vigilance Estimation（警戒估计）                               ：

- #### Mental Stress Detection（心理压力检测）              ：

- #### Event Type Classification（事件类型分类）             ：

- #### Abnormal Detection（异常检测）                                ：

---

# EEG_2_text

- ## foundation model

- ## Encoder

- ## cross-model genertion

- ## clinical application












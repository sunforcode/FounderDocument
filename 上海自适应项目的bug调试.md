# 上海自适应项目的bug调试

* 解决点击optionCell点击后答案不显示的问题

 类： PaperCollectionCell 没一个答题页面 collectionView嵌套着tableView
点击事件在 PaperCollectionCell 
+ 每一个点击选项的按钮的事件 needsSynchronousCorrect 这个属性来控制是否显示答案

### H5页面

* 我的风格 [http://120.55.181.205:8080/app/exam/solomon/exam.do?theme=mobile&openid=8af5a8825c77333d015c77635ee10081]()

LearningCell 学练测见 的类 data.progress != -1

图片类： ImagesResourceCell
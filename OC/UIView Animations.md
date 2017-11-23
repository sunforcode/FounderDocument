#  UIView Animations

### 在添加View时候的使用的动画

```
“override func viewDidAppear(_ animated: Bool) {
  super.viewDidAppear(animated)

  //create new view
  let newView = UIImageView(image: UIImage(named: "banner"))
  newView.center = animationContainerView.center

  //add the new view via transition
  UIView.transition(with: animationContainerView, 
    duration: 0.33, 
    options: [.curveEaseOut, .transitionFlipFromBottom], 
    animations: {
      self.animationContainerView.addSubview(newView)
    }, 
    completion: nil
  )
}”

```

### 在移除UIview 的时候
把上面那个方法中的addsubview 改变为removeFromSuperView

```
“//remove the view via transition

UIView.transition(with: animationContainerView, duration: 0.33, 
  options: [.curveEaseOut, .transitionFlipFromBottom],  
  animations: {
    self.newView.removeFromSuperview()
  }, 
  completion: nil
)” 
```

### 更换图片通过transtion

```
“//replace via transition
UIView.transition(from: oldView, to: newView, duration: 0.33, 
  options: .transitionFlipFromTop, completion: nil)”


```
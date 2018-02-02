# 解决DPUB内核中的表格柱状图少一位的BUG


* 计算字体大小

```
- (int)calulateSizeOfFont:(int)newSize
{
	int size = newSize;
	for (NSString* aStr in self.m_sortedKeyArray)
	{
		float oneKeySpace = m_motionRect.size.width/[self.m_sortedKeyArray count];
		float width = oneKeySpace;
		if (self.m_pSGParams->orientation == SGT_HORIZONTAL) 
		{
			width = leftLeft;
		}
        CGSize sizeOfaStr = [aStr sizeWithAttributes:@{NSFontAttributeName:[UIFont systemFontOfSize:size]}];
		float lengthOfText = sizeOfaStr.width;
        if ((lengthOfText+10 > width)||(size > 12))
		{
			size = [self calulateSizeOfFont:(size-1)];
		}

	}
	
	return size;
	
}
```

将所有的内图绘制出来

```
					CGContextRestoreGState(context);

```
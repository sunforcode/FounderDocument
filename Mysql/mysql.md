# mysql

#### 启动mysql

> /usr/local/mysql/bin/mysql -u root -p


#### 更新mysql

> update tableName set 字段 = '值' where 


#### 删除表内容

> delete from 表名称;
> 
> 


#### 新增字段

```
断是否存在，判断之前先导入头文件确保可以调用FMDB的api（#import “FMDatabaseAdditions.h”）：

if (![db columnExists:@"新增字段" inTableWithName:@"表名"]){  

}
1
2
3
（2）如果不存在，就执行插入操作：

NSString *alertStr = [NSString stringWithFormat:@"ALTER TABLE %@ ADD %@ INTEGER",@"表名",@"新增字段"];  
BOOL worked = [db executeUpdate:alertStr];  
if(worked){
    NSLog(@"插入成功");
}else{
   
```  


### bug

```
Warning:The /usr/local/mysql/data directory is not owned by the ‘mysql‘ or ‘_mysql‘ ”

解决办法: sudo chown -R  _mysql:wheel  /usr/local/mysql/data
```
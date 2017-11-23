# 尝试Jenkins制作插件


### 下载maven 
mac环境下 终端直接运行 

```
brew install Maven
```
尝试运行

> mvn -version 

如果正常显示的话，就说明安装成功了

### 设置Maven
创建路径 **~/.m2**,在.m2里面创建 文件 **setting.xml**

将下面的内容复制到setting.xml中,暂时我没作修改

```
<settings>
  <pluginGroups>
    <pluginGroup>org.jenkins-ci.tools</pluginGroup> 
  </pluginGroups>

  <profiles>
    <profile>
      <id>jenkins</id>
      <activation>
        <activeByDefault>true</activeByDefault> 
      </activation>
      <repositories> 
        <repository>
          <id>repo.jenkins-ci.org</id>
          <url>https://repo.jenkins-ci.org/public/</url>
        </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>repo.jenkins-ci.org</id>
          <url>https://repo.jenkins-ci.org/public/</url>
        </pluginRepository>
      </pluginRepositories>
    </profile>
  </profiles>
</settings>

```

### 创建一个空的项目布局

> mvn -U hpi:create

初次安装,要下载好多好多的东西.等了一会之后出现了错误,提示让我使用新的命令

> mvn archetype:generate -Dfilter=io.jenkins.archetypes:

等待一会之后出现了

```
Choose archetype:
1: remote -> io.jenkins.archetypes:empty-plugin (Skeleton of a Jenkins plugin with a POM and an empty source tree.)
2: remote -> io.jenkins.archetypes:global-configuration-plugin (Skeleton of a Jenkins plugin with a POM and an example piece of global configuration.)
3: remote -> io.jenkins.archetypes:hello-world-plugin (Skeleton of a Jenkins plugin with a POM and an example build step.)
Choose a number or apply filter (format: [groupId:]artifactId, case sensitive contains):
```
这个时候要在终端中填写的是io.jenkins.archetypes后面的内容 我选的是第三个**hello-world-plugin**,然后出现

```
Choose archetype:
1: remote -> io.jenkins.archetypes:hello-world-plugin (Skeleton of a Jenkins plugin with a POM and an example build step.)
Choose a number or apply filter (format: [groupId:]artifactId, case sensitive contains): :
```
然后选择第一个 写 **1**

然后 
```
Choose io.jenkins.archetypes:hello-world-plugin version: 
1: 1.1
2: 1.2
```

选择 **2**

下面就简单了,按照提示填写项目名称和版本号

```
artifactId: demo
version: 1
```
----
build success

---

### 进入到项目的文件目录

```
cd demo
mvn verify
```

### 运行

```
mvn hpi:run
```
打卡浏览器, 输入 **http://localhost:8080/jenkins**,记得吧已经在运行状态下的jenkins关掉,不然会报端口被占用的错误,这个jenkins的home directory 在改插件的work目录下

### 创建一个新的自由风格的job

![](http://okzs58u17.bkt.clouddn.com/Snip20171117_12.png)

* 增加构建步骤,
* name 上填写 Hello,jenkins
* 保存-build

![](http://okzs58u17.bkt.clouddn.com/Snip20171117_13.png)

### 插件打包,发布

当前目录使用 

```
mvn package
```

打包完成后，在根目录下的target文件目录下会生成demo.hpi插件安装包。将demo.hpi安装到jenkins中即可使用自定义插件。

![](http://okzs58u17.bkt.clouddn.com/Snip20171117_15.png)


### jenkins 安装使用该插件


在正经的jenkins中 系统 - 管理插件 - 高级 - 上传插件中上传后就可以在job可以使用了


![](http://okzs58u17.bkt.clouddn.com/Snip20171117_14.png)







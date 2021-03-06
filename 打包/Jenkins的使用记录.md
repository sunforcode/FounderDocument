# Jenkins的使用记录

* 1.Jenkins使用workspace的路径 $WORKSPACE 可以再终端中使用
		
		$WORKSPACE
		
* Jenkins的环境变量

	The following variables are available to shell scripts

	**BRANCH_NAME** 分支的名字
	
	**CHANGE_ID**
	For a multibranch project corresponding to some kind of change request, this will be set to the change ID, such as a pull request number, if supported; else unset.
	
	**CHANGE_URL**
	For a multibranch project corresponding to some kind of change request, this will be set to the change URL, if supported; else unset.
	
	**CHANGE_TITLE**
	For a multibranch project corresponding to some kind of change request, this will be set to the title of the change, if supported; else unset.
	
	**CHANGE_AUTHOR**
	For a multibranch project corresponding to some kind of change request, this will be set to the username of the author of the proposed change, if supported; else unset.
	CHANGE_AUTHOR_DISPLAY_NAME
	
	For a multibranch project corresponding to some kind of change request, this will be set to the human name of the author, if supported; else unset.
	
	**CHANGE_AUTHOR_EMAIL**
	For a multibranch project corresponding to some kind of change request, this will be set to the email address of the author, if supported; else unset.
	
	**CHANGE_TARGET**
	For a multibranch project corresponding to some kind of change request, this will be set to the target or base branch to which the change could be merged, if supported; else unset.
	
	**BUILD_NUMBER**
	The current build number, such as "153"
	
	**BUILD_ID**
	The current build ID, identical to BUILD_NUMBER for builds created in 1.597+, but a YYYY-MM-DD_hh-mm-ss timestamp for older builds
	
	**BUILD_DISPLAY_NAME**
	构建的名称 eg：第六次构建displayName 就是#6
	
	**JOB_NAME**
	jod 的名字 eg： 创建的工作叫jenkins 那么jod_name 就叫jenkins
	
	**JOB_BASE_NAME**
	Short Name of the project of this build stripping off folder paths, such as "foo" for "bar/foo".
	
	**BUILD_TAG**
	String of "jenkins-${JOB_NAME}-${BUILD_NUMBER}". All forward slashes (/) in the JOB_NAME are replaced with dashes (-). Convenient to put into a resource file, a jar file, etc for easier identification.
	
	**EXECUTOR_NUMBER**
	The unique number that identifies the current executor (among executors of the same machine) that’s carrying out this build. This is the number you see in the "build executor status", except that the number starts from 0, not 1.
	
	**NODE_NAME**
	Name of the agent if the build is on an agent, or "master" if run on master
	
	**NODE_LABELS**
	Whitespace-separated list of labels that the node is assigned.
	
	**WORKSPACE**
	工作空间的路径
	
	**JENKINS_HOME**
	The absolute path of the directory assigned on the master node for Jenkins to store data.
	
	**JENKINS_URL**
	Full URL of Jenkins, like http://server:port/jenkins/ (note: only available if Jenkins URL set in system configuration)
	
	**BUILD_URL**
	Full URL of this build, like http://server:port/jenkins/job/foo/15/ (Jenkins URL must be set)
	
	**JOB_URL**
	Full URL of this job, like http://server:port/jenkins/job/foo/ (Jenkins URL must be set)
	
	**GIT_COMMIT**
	The commit hash being checked out.
	
	**GIT_PREVIOUS_COMMIT**
	The hash of the commit last built on this branch, if any.
	
	**GIT_PREVIOUS_SUCCESSFUL_COMMIT**
	The hash of the commit last successfully built on this branch, if any.
	
	**GIT_BRANCH**
	The remote branch name, if any.
	
	**GIT_LOCAL_BRANCH**
	The local branch name being checked out, if applicable.
	
	**GIT_URL**
	The remote URL. If there are multiple, will be GIT_URL_1, GIT_URL_2, etc.
	
	**GIT_COMMITTER_NAME**
	The configured Git committer name, if any.
	
	**GIT_AUTHOR_NAME**
	The configured Git author name, if any.
	
	**GIT_COMMITTER_EMAIL**
	The configured Git committer email, if any.
	
	**GIT_AUTHOR_EMAIL**
	The configured Git author email, if any.
	
	**SVN_REVISION**
	Subversion revision number that's currently checked out to the workspace, such as "12345"
	
	**SVN_URL**
	Subversion URL that's currently checked out to the workspace.
	
	
### 根据构建结果调用其他的任务
Parameterized

###开机启动

设置开机自启动：sudo launchctl load -w /Library/LaunchDaemons/org.jenkins-ci.plist
取消开机自启动：sudo launchctl unload -w /Library/LaunchDaemons/org.jenkins-ci.plist
手动启动：Java -jar jenkins.war
后台启动(默认端口)：nohup java -jar jenkins.war &
后台启动(指定端口)：nohup java -jar jenkins.war -httpPort=88 &
后台启动(HTTPS)：nohup java -jar jenkins.war -httpsPort=88 &

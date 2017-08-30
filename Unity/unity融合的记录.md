* 修改一: unityVIewControllerBaseIos.mm中的 
shoulautoRotate 控制了点开摄像头的旋转与否

* 修改二: 在导出unity工程的时候,要在buildsettig 里面把程序所支持的方向,选为maskall,然后在unity导出的工程中在修改一中的设置为No
* 
```c#
if(Event.current.isMouse && Event.current.type == EventType.MouseDown && Event.current.clickCount == 2){  
			print("double click");  
			MainBody.isKinematic = true;
			MainBody.GetComponent<BoxCollider> ().enabled = false;
		}  
```
# Native_Libs_unloader
## Adb based tool for downloading native libs(.so) from android apps
<hr/>

#### [REQUIRES ROOT]

### USAGE
1. Connect rooted android to adb.
2. Make sure that you have run target app at least once.
3. Find target app's package by command -->>
```
C:\Windows\system32> adb shell pm list packages
```
4. Start script by command -->>
```
C:\Windows\system32> python Libs_unloader.py com.example.application
```

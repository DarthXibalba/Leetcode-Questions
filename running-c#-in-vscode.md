# Running C# in VSCode
[Original Link](https://travis.media/how-to-run-csharp-in-vscode/)  

## 1. Install .NET 5.0
[Install .NET 5.0](https://dotnet.microsoft.com/download) or newer  
Then confirm that dotnet is installed by checking the version in a terminal window:
```
dotnet --version
# 5.0.202 (or whatever version is installed)
```
Install [C# for Visual Studio Code (by Microsoft)](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) VSCode Plugin  

## 2. Create a new C# project in VSCode
Next, create a new project and open it in VSCode:
```
dotnet console -o appName
cd appName
code .  # to open project in VSCode
```
Now you should see a simple Hello World app with the main code in ***Program.cs***  

## 3. Run Your C# Code in VSCode
To execute your code, simply run:
```
dotnet run
```

## 4. Debug Your C# Code in VSCode
First be sure to install the official C# extension mentioned above  

Next, in VSCode open the Command Palette by going to View > Command Palette (or use the shortcut if you know what it is), and search for **.NET: Generate Assets for Build and Debug**  
Choosing this will generate a .vscode folder with a prepopulated build configuration in it.  
Now go to the "Run and Debug" tab in VSCode, set your breakpoint(s), and click the Play button to debug  

## 5. Compile Your Code
To compile your code, run:
```
dotnet build
```
After that is done, you will have an executable (exe or dll) in your /bin folder. Depending on your build configuration it may be in a Debug folder or a Release folder.
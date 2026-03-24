# Windows EXE 打包说明

## 关键说明

`PyInstaller` 不能在 macOS 直接打包 Windows `.exe`。  
请在 **Windows** 机器（或 Windows 虚拟机）中执行以下步骤。

## 1. 准备环境（Windows）

在项目目录打开 `PowerShell`：

```powershell
cd "D:\你的目录\大模型质检"
python -m venv venv
.\venv\Scripts\activate
```

## 2. 一键打包 EXE

```powershell
python .\build_windows_exe.py
```

## 3. 打包产物

默认会在 `dist` 目录生成：

- `dist\URLTool\URLTool.exe`（推荐分发整个 `URLTool` 文件夹）

## 4. 运行与分发

- 本机运行：双击 `URLTool.exe`
- 分发给其他 Windows 用户：拷贝整个 `dist\URLTool` 文件夹

## 5. 常见问题

- 缺少运行库：按提示安装 Microsoft Visual C++ Redistributable
- 被杀毒误报：可先本地白名单，正式分发建议做代码签名

---

## 可选：GitHub Actions 云端自动打包

项目已提供工作流文件：`.github/workflows/build-windows-exe.yml`。

### 使用方式

1. 把项目推送到 GitHub 仓库（默认分支 `main` 或 `master`）
2. 打开仓库的 `Actions` 页面
3. 运行 `Build Windows EXE`（或推送代码自动触发）
4. 在该次运行的 `Artifacts` 中下载 `URLTool-windows`

下载后解压，进入 `dist/URLTool`，运行 `URLTool.exe`。

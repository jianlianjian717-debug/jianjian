# macOS 打包与安装说明

本项目已支持打包为可安装的 macOS 独立应用（`.app` + `.dmg`）。

## 1. 准备环境

在项目目录执行：

```bash
cd "/Users/yuwan/Desktop/cursor开发/大模型质检"
source venv/bin/activate
```

## 2. 一键打包

```bash
python build_macos_app.py
```

打包完成后会在 `dist` 目录生成：

- `URL工具.app`
- `URL工具.dmg`

## 3. 安装与使用

1. 双击 `URL工具.dmg`
2. 将 `URL工具.app` 拖到 `Applications`
3. 从启动台或 `Applications` 打开

## 4. 安全提示（Gatekeeper）

首次在本机或其他 Mac 打开，可能出现“无法验证开发者”提示。可在：

- `系统设置 -> 隐私与安全性`

中点击“仍要打开”。

> 如果后续要分发给更多用户，建议做 Apple Developer 签名和公证（Notarization）。

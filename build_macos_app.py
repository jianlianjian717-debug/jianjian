#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    print(">", " ".join(cmd))
    subprocess.run(cmd, cwd=str(cwd), check=True)


def main() -> int:
    project_dir = Path(__file__).resolve().parent
    venv_python = project_dir / "venv" / "bin" / "python"
    entry_file = project_dir / "main.py"
    app_name = "URL工具"

    if not entry_file.exists():
        print(f"未找到入口文件: {entry_file}")
        return 1
    if not venv_python.exists():
        print(f"未找到虚拟环境 Python: {venv_python}")
        print("请先创建并激活 venv。")
        return 1

    try:
        print("1/4 安装运行依赖...")
        run([str(venv_python), "-m", "pip", "install", "-r", "requirements.txt"], project_dir)

        print("2/4 安装打包依赖...")
        run([str(venv_python), "-m", "pip", "install", "-r", "requirements-build.txt"], project_dir)

        print("3/4 构建 .app ...")
        run(
            [
                str(venv_python),
                "-m",
                "PyInstaller",
                "--noconfirm",
                "--clean",
                "--windowed",
                "--collect-all",
                "PySide6",
                "--name",
                app_name,
                str(entry_file),
            ],
            project_dir,
        )

        app_path = project_dir / "dist" / f"{app_name}.app"
        if not app_path.exists():
            print(f"构建失败，未找到: {app_path}")
            return 1

        print("4/4 生成 DMG 安装包...")
        dmg_path = project_dir / "dist" / f"{app_name}.dmg"
        if dmg_path.exists():
            dmg_path.unlink()
        run(
            [
                "hdiutil",
                "create",
                "-volname",
                app_name,
                "-srcfolder",
                str(app_path),
                "-ov",
                "-format",
                "UDZO",
                str(dmg_path),
            ],
            project_dir,
        )

        print("\n打包完成：")
        print(f"App: {app_path}")
        print(f"DMG: {dmg_path}")
        print("\n提示：首次在其他 Mac 打开时，如遇安全提示，可在“系统设置 -> 隐私与安全性”中允许打开。")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败，退出码: {e.returncode}")
        return e.returncode


if __name__ == "__main__":
    raise SystemExit(main())

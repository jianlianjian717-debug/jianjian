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
    venv_python = project_dir / "venv" / "Scripts" / "python.exe"
    entry_file = project_dir / "main.py"
    app_name = "URLTool"

    if sys.platform != "win32":
        print("当前不是 Windows。")
        print("PyInstaller 不能在 macOS 直接打包 Windows exe。")
        print("请在 Windows 机器上运行本脚本。")
        return 1

    if not entry_file.exists():
        print(f"未找到入口文件: {entry_file}")
        return 1
    if not venv_python.exists():
        print(f"未找到虚拟环境 Python: {venv_python}")
        print("请先在 Windows 创建并激活 venv。")
        return 1

    try:
        print("1/3 安装运行依赖...")
        run([str(venv_python), "-m", "pip", "install", "-r", "requirements.txt"], project_dir)

        print("2/3 安装打包依赖...")
        run([str(venv_python), "-m", "pip", "install", "-r", "requirements-build.txt"], project_dir)

        print("3/3 构建 EXE ...")
        run(
            [
                str(venv_python),
                "-m",
                "PyInstaller",
                "--noconfirm",
                "--clean",
                "--windowed",
                "--name",
                app_name,
                str(entry_file),
            ],
            project_dir,
        )

        exe_path = project_dir / "dist" / app_name / f"{app_name}.exe"
        if not exe_path.exists():
            # onefile/onedir 在不同版本路径可能不同，兜底给出 dist 路径
            print("构建完成，但未在预期位置找到 exe。请检查 dist 目录。")
            print(f"dist: {project_dir / 'dist'}")
            return 0

        print("\n打包完成：")
        print(f"EXE: {exe_path}")
        print("\n分发时建议把整个 dist/URLTool 文件夹一起给到用户。")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败，退出码: {e.returncode}")
        return e.returncode


if __name__ == "__main__":
    raise SystemExit(main())

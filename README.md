# jmdownload 插件

本插件用于在 AstrBot 中查询及下载 jmcomic 相关资源。

## 安装说明

在部署或运行本插件前，请确保在 
# AstrBot 的环境（venv/uv）中
安装了必要的依赖：


/home/用户名/.local/share/uv/tools/astrbot/bin/pip install jmcomic -U

/home/用户名/.local/share/uv/tools/astrbot/bin/pip install img2pdf

## 本插件提供以下指令
/jm view <id>：查看指定 ID 的详细信息（包括作者、标签等）。

/jm down <id>：下载指定 ID 的内容，并自动转换为 PDF 格式发送。
### 注意：下载过程中产生的临时文件会在发送完成后自动清理。

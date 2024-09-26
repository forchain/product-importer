#!/bin/bash

# 设置工作目录为当前脚本所在的文件夹
cd "$(dirname "$0")"

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖库
pip install -r requirements.txt

# 运行Python脚本
python process_product_data.py

# 退出虚拟环境
deactivate
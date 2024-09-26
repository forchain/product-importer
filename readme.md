# 商品导入导出系统

这是一个高效的商品导入导出系统，旨在简化客户在商品管理过程中的操作。该系统支持多种商品数据格式的导入，并确保数据的准确性和一致性。

## 功能特点

- 支持Excel格式的商品数据导入
- 使用模板文件进行数据导出
- 自动处理和转换商品数据
- 生成符合要求的导出表格
- 提高工作效率和用户体验
- 支持通过环境变量配置文件路径和列名

## 使用说明

1. 准备环境：
   - 确保已安装Python 3.7+
   - 创建并激活虚拟环境：
     ```
     python -m venv venv
     source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
     ```
   - 安装依赖：
     ```
     pip install -r requirements.txt
     ```

2. 配置文件：
   - 创建 `.env` 文件，设置以下变量：
     ```
     INPUT_FILE=input_data.xlsx
     TEMPLATE_FILE=template.xlsx
     OUTPUT_FILE=output_data.xlsx
     TITLE_COLUMN=商品标题（必填）
     PRICE_COLUMN=商品价格（必填）
     STOCK_COLUMN=商品库存（必填）
     ```

3. 准备输入文件：
   确保您的输入Excel文件（默认为 `input_data.xlsx`）包含以下列：
   - 商品名（TITLE）
   - 商品价格（PRICE）
   - 商品尺寸（SIZE）
   - 商品备注（NOTES）

4. 准备模板文件：
   创建一个模板Excel文件（默认为 `template.xlsx`），包含所需的输出列。

5. 运行程序：
   您可以选择以下两种方式之一来运行程序：

   a. 直接运行Python脚本：
   ```
   python process_product_data.py
   ```

   b. 使用run_script.sh（仅适用于Unix/Linux系统）：
   ```
   chmod +x run_script.sh  # 赋予执行权限
   ./run_script.sh
   ```
   run_script.sh会自动创建虚拟环境、安装依赖并运行Python脚本。

6. 查看输出：
   程序将生成一个新的Excel文件（默认为 `output_data.xlsx`），包含处理后的商品数据。

## 依赖项

- Python 3.7+
- pandas==1.3.3
- openpyxl==3.0.9
- python-dotenv==0.19.1

## 文档

更多详细信息，请参阅 `Docs` 目录下的文档：

- [产品需求文档 (PRD)](Docs/PRD.md)
- [产品说明](Docs/product.md)

## 贡献

欢迎提交问题和改进建议。如果您想为项目做出贡献，请提交拉取请求。

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。
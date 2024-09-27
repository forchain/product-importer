# 微店商品导入器 (weidian-importer)

这是一个高效的商品导入导出系统，旨在简化客户在商品管理过程中的操作。该系统支持多种商品数据格式的导入，并确保数据的准确性和一致性。

## 功能特点

- 支持Excel格式的商品数据导入
- 使用模板文件进行数据导出
- 自动处理和转换商品数据
- 生成符合要求的导出表格
- 提高工作效率和用户体验
- 支持通过环境变量配置文件路径和列名
- **支持 Web 模式**：通过 Web 页面上传文件并下载生成的表格

## Web 模式展示

您可以访问以下链接查看 Web 模式的展示：
[Web 模式展示](https://weidian-importer.streamlit.app/)

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
     # 数据文件
     IMPORT_FILE=data/import_data.xlsx
     INVENTORY_FILE=data/inventory_data.xlsx
     UPDATE_PRODUCT_OUTPUT=data/update_product_output.xlsx
     NEW_PRODUCT_OUTPUT=data/new_product_output.xlsx

     # 模板文件
     UPDATE_PRODUCT_TEMPLATE=config/update_product_template.xlsx
     NEW_PRODUCT_TEMPLATE=config/new_product_template.xlsx

     # 导入文件列名
     COLUMN_IMPORT_TITLE=TITLE
     COLUMN_IMPORT_PRICE=PRICE
     COLUMN_IMPORT_ITEM=ITEM
     COLUMN_IMPORT_SIZE=SIZE
     COLUMN_IMPORT_NOTES=NOTES
     COLUMN_INVENTORY_PRODUCT_ID=商品ID
     COLUMN_INVENTORY_MODEL_ID=型号ID
     COLUMN_INVENTORY_MODEL_NAME=商品型号
     COLUMN_UPDATE_PRODUCT_ID=商品ID
     COLUMN_UPDATE_TITLE=商品标题
     COLUMN_UPDATE_MODEL_ID=型号ID
     COLUMN_UPDATE_STATUS=商品状态
     COLUMN_UPDATE_PRICE=商品价格
     COLUMN_UPDATE_STOCK=商品库存
     COLUMN_NEW_TITLE=商品标题
     COLUMN_NEW_MODEL_CATEGORY=型号分类1
     COLUMN_NEW_MODEL_NAME=型号名称1
     COLUMN_NEW_PRICE=商品价格
     COLUMN_NEW_STOCK=商品库存
     ```

3. 准备输入文件：
   确保您的输入Excel文件（默认为 `data/import_data.xlsx`）包含以下列：
   - 商品名（TITLE）
   - 商品价格（PRICE）
   - 商品型号（ITEM）
   - 商品尺寸（SIZE）
   - 商品备注（NOTES）

4. 准备库存文件：
   确保您的库存文件是在微店后台导出的，并包含以下字段：
   - 商品型号（ITEM）
   - 型号ID（MODEL ID）
   - 商品ID（PRODUCT ID）

   库存文件应与导入文件相对应，以便系统能够正确处理和生成更新商品表格和新增商品表格。

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

   c. 启动 Web 模式：
   ```
   streamlit run web.py
   ```
   启动后将打开一个 Web 页面，用户可以在页面上上传导入文件和库存文件，并生成更新商品表格和新增商品表格。

6. 查看输出：
   程序将生成两个新的Excel文件，分别为：
   - 更新商品输出文件（默认为 `data/update_product_output.xlsx`）
   - 新增商品输出文件（默认为 `data/new_product_output.xlsx`），包含处理后的商品数据。

## 文档

更多详细信息，请参阅 `Docs` 目录下的文档：

- [产品需求文档 (PRD)](Docs/PRD.md)
- [Product Requirement Document (PRD)](Docs/PRD_en.md)  <!-- 新增英文文档链接 -->

## 贡献

欢迎提交问题和改进建议。如果您想为项目做出贡献，请提交拉取请求。

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。
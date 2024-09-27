# Weidian Product Importer (weidian-importer)

This is an efficient product import and export system designed to simplify customer operations in product management. The system supports multiple product data formats for import and ensures data accuracy and consistency.

## Features

- Supports Excel format for product data import
- Uses template files for data export
- Automatically processes and converts product data
- Generates export tables that meet requirements
- Improves work efficiency and user experience
- Supports configuration of file paths and column names through environment variables
- **Supports Web Mode**: Upload files and download generated tables through a web page

## Web Mode Showcase

You can visit the following link to view the Web mode showcase:
[Web Mode Showcase](https://weidian-importer.streamlit.app/)

## Usage Instructions

1. Prepare the environment:
   - Ensure Python 3.7+ is installed
   - Create and activate a virtual environment:
     ```
     python -m venv venv
     source venv/bin/activate  # Use venv\Scripts\activate on Windows
     ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```

2. Configuration file:
   - Create a `.env` file and set the following variables:
     ```
     # Data files
     IMPORT_FILE=data/import_data.xlsx
     INVENTORY_FILE=data/inventory_data.xlsx
     UPDATE_PRODUCT_OUTPUT=data/update_product_output.xlsx
     NEW_PRODUCT_OUTPUT=data/new_product_output.xlsx

     # Template files
     UPDATE_PRODUCT_TEMPLATE=config/update_product_template.xlsx
     NEW_PRODUCT_TEMPLATE=config/new_product_template.xlsx

     # Import file column names
     COLUMN_IMPORT_TITLE=TITLE
     COLUMN_IMPORT_PRICE=PRICE
     COLUMN_IMPORT_ITEM=ITEM
     COLUMN_IMPORT_SIZE=SIZE
     COLUMN_IMPORT_NOTES=NOTES
     COLUMN_INVENTORY_PRODUCT_ID=商品ID
     COLUMN_INVENTORY_MODEL_ID=型ID
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

3. Prepare input files:
   Ensure your input Excel file (default is `data/import_data.xlsx`) contains the following columns:
   - Product Name (TITLE)
   - Product Price (PRICE)
   - Product Model (ITEM)
   - Product Size (SIZE)
   - Product Notes (NOTES)

4. Prepare Inventory File:
   Ensure that your inventory file is exported from the Weidian backend and contains the following fields:
   - Product Model (ITEM)
   - Model ID (MODEL ID)
   - Product ID (PRODUCT ID)

   The inventory file should correspond to the import file so that the system can correctly process and generate the update product table and new product table.

5. Run the program:
   You can choose one of the following two ways to run the program:

   a. Directly run the Python script:
   ```
   python process_product_data.py
   ```

   b. Use run_script.sh (only for Unix/Linux systems):
   ```
   chmod +x run_script.sh  # Grant execution permission
   ./run_script.sh
   ```
   run_script.sh will automatically create a virtual environment, install dependencies, and run the Python script.

   c. Start Web Mode:
   ```
   streamlit run web.py
   ```
   After starting, a web page will open, allowing users to upload import and inventory files and generate update product tables and new product tables.

6. View output:
   The program will generate two new Excel files:
   - Update product output file (default is `data/update_product_output.xlsx`)
   - New product output file (default is `data/new_product_output.xlsx`), containing processed product data.

## Documentation

For more detailed information, please refer to the documents in the `Docs` directory:

- [产品需求文档 (PRD)](Docs/PRD.md)
- [Product Requirement Document (PRD)](Docs/PRD_en.md)  <!-- New English document link -->

## Contribution

We welcome issues and suggestions for improvement. If you would like to contribute to the project, please submit a pull request.

## License

This project is licensed under the MIT License. For details, see the [LICENSE](LICENSE) file.
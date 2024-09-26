import pandas as pd
import os
from dotenv import load_dotenv
import shutil

# Load environment variables
load_dotenv()

def load_config():
    """Read configuration from environment variables"""
    config = {
        'import_file': os.getenv('IMPORT_FILE'),
        'inventory_file': os.getenv('INVENTORY_FILE'),
        'update_product_template': os.getenv('UPDATE_PRODUCT_TEMPLATE'),
        'new_product_template': os.getenv('NEW_PRODUCT_TEMPLATE'),
        'update_product_output': os.getenv('UPDATE_PRODUCT_OUTPUT'),
        'new_product_output': os.getenv('NEW_PRODUCT_OUTPUT'),
        'COLUMN_IMPORT_TITLE': os.getenv('COLUMN_IMPORT_TITLE', 'TITLE'),
        'COLUMN_IMPORT_PRICE': os.getenv('COLUMN_IMPORT_PRICE', 'PRICE'),
        'COLUMN_IMPORT_ITEM': os.getenv('COLUMN_IMPORT_ITEM', 'ITEM'),
        'COLUMN_IMPORT_SIZE': os.getenv('COLUMN_IMPORT_SIZE', 'SIZE'),
        'COLUMN_IMPORT_NOTES': os.getenv('COLUMN_IMPORT_NOTES', 'NOTES'),
        'COLUMN_INVENTORY_PRODUCT_ID': os.getenv('COLUMN_INVENTORY_PRODUCT_ID', '商品ID'),
        'COLUMN_INVENTORY_MODEL_ID': os.getenv('COLUMN_INVENTORY_MODEL_ID', '型号ID'),
        'COLUMN_INVENTORY_MODEL_NAME': os.getenv('COLUMN_INVENTORY_MODEL_NAME', '商品型号'),
        'COLUMN_UPDATE_PRODUCT_ID': os.getenv('COLUMN_UPDATE_PRODUCT_ID', '商品ID'),
        'COLUMN_UPDATE_TITLE': os.getenv('COLUMN_UPDATE_TITLE', '商品标题'),
        'COLUMN_UPDATE_MODEL_ID': os.getenv('COLUMN_UPDATE_MODEL_ID', '型号ID'),
        'COLUMN_UPDATE_STATUS': os.getenv('COLUMN_UPDATE_STATUS', '商品状态'),
        'COLUMN_UPDATE_PRICE': os.getenv('COLUMN_UPDATE_PRICE', '商品价格'),
        'COLUMN_UPDATE_STOCK': os.getenv('COLUMN_UPDATE_STOCK', '商品库存'),
        'COLUMN_NEW_TITLE': os.getenv('COLUMN_NEW_TITLE', '商品标题'),
        'COLUMN_NEW_MODEL_CATEGORY': os.getenv('COLUMN_NEW_MODEL_CATEGORY', '型号分类1'),
        'COLUMN_NEW_MODEL_NAME': os.getenv('COLUMN_NEW_MODEL_NAME', '型号名称1'),
        'COLUMN_NEW_PRICE': os.getenv('COLUMN_NEW_PRICE', '商品价格'),
        'COLUMN_NEW_STOCK': os.getenv('COLUMN_NEW_STOCK', '商品库存'),
    }
    
    # Prompt user for input if environment variables are not set
    for key, value in config.items():
        if not value:
            config[key] = input(f"Please enter {key}: ").strip()
    
    return config

# 提取常量
STATUS_ON_SHELF = '上架'
STATUS_OFF_SHELF = '下架'
DEFAULT_STOCK = 100

def generate_update_table(df_import, df_inventory, config):
    """Generate the update product table"""
    df_update = pd.read_excel(config['update_product_template'])  # 从模板读取数据
    df_update = df_update[0:0]  # 清空数据以便填充新数据

    for _, row in df_inventory.iterrows():
        product_id = row[config['COLUMN_INVENTORY_PRODUCT_ID']]
        model_id = row[config['COLUMN_INVENTORY_MODEL_ID']]
        model_name = row[config['COLUMN_INVENTORY_MODEL_NAME']]
        
        # Check if the inventory model name contains the import item
        matching_import = df_import[df_import[config['COLUMN_IMPORT_ITEM']].apply(lambda x: model_name.startswith(x))]

        # Set status based on matching import
        status = STATUS_ON_SHELF if not matching_import.empty else STATUS_OFF_SHELF
        
        # 仅在状态为“上架”时更新商品标题、价格和库存
        title = df_import[config['COLUMN_IMPORT_TITLE']].iloc[0] if not df_import.empty and status == STATUS_ON_SHELF else ''
        
        # 如果状态为“下架”，则价格和库存字段为空
        price = matching_import[config['COLUMN_IMPORT_PRICE']].iloc[0] if not matching_import.empty and status == STATUS_ON_SHELF else ''
        stock = DEFAULT_STOCK if status == STATUS_ON_SHELF else ''  # 下架时库存字段为空

        # Create a new row as a DataFrame
        new_row = pd.DataFrame({
            config['COLUMN_UPDATE_PRODUCT_ID']: [product_id],
            config['COLUMN_UPDATE_TITLE']: [title],
            config['COLUMN_UPDATE_MODEL_ID']: [model_id],
            config['COLUMN_UPDATE_STATUS']: [status],
            config['COLUMN_UPDATE_PRICE']: [price],
            config['COLUMN_UPDATE_STOCK']: [stock]
        })

        # Concatenate the new row to the update DataFrame
        df_update = pd.concat([df_update, new_row], ignore_index=True)

    return df_update

def generate_new_product_table(df_import, df_inventory, config):
    """Generate the new product table"""
    df_new_product = pd.read_excel(config['new_product_template'])  # 从模板读取数据
    df_new_product = df_new_product[0:0]  # 清空数据以便填充新数据

    for _, row in df_import.iterrows():
        item = row[config['COLUMN_IMPORT_ITEM']]
        if not df_inventory[config['COLUMN_INVENTORY_MODEL_NAME']].str.startswith(item, na=False).any():
            # Generate model name
            model_name_parts = [item]
            if pd.notna(row[config['COLUMN_IMPORT_SIZE']]):
                model_name_parts.append(row[config['COLUMN_IMPORT_SIZE']])
            if pd.notna(row[config['COLUMN_IMPORT_NOTES']]):
                model_name_parts.append(row[config['COLUMN_IMPORT_NOTES']])
            model_name = ' | '.join(model_name_parts)

            # Create a new row as a DataFrame
            new_row = pd.DataFrame({
                config['COLUMN_NEW_TITLE']: [row[config['COLUMN_IMPORT_TITLE']]],
                config['COLUMN_NEW_MODEL_CATEGORY']: ['未分类'],
                config['COLUMN_NEW_MODEL_NAME']: [model_name],
                config['COLUMN_NEW_PRICE']: [row[config['COLUMN_IMPORT_PRICE']]],
                config['COLUMN_NEW_STOCK']: [DEFAULT_STOCK]
            })

            # Concatenate the new row to the new product DataFrame
            df_new_product = pd.concat([df_new_product, new_row], ignore_index=True)

    return df_new_product

def process_product_data():
    try:
        # Load configuration
        config = load_config()

        # Check if files exist
        for file in [config['import_file'], config['inventory_file'], config['update_product_template'], config['new_product_template']]:
            if not os.path.exists(file):
                raise FileNotFoundError(f"File does not exist: {file}")

        # Copy template files as output files
        shutil.copy2(config['update_product_template'], config['update_product_output'])
        shutil.copy2(config['new_product_template'], config['new_product_output'])

        # Read files
        df_import = pd.read_excel(config['import_file'])
        df_inventory = pd.read_excel(config['inventory_file'])

        # Generate update product table
        df_update = generate_update_table(df_import, df_inventory, config)

        # Generate new product table
        df_new_product = generate_new_product_table(df_import, df_inventory, config)

        # Save output files
        df_update.to_excel(config['update_product_output'], index=False)
        df_new_product.to_excel(config['new_product_output'], index=False)

        print(f"Data processing complete. Update product table saved to {config['update_product_output']}")
        print(f"Data processing complete. New product table saved to {config['new_product_output']}")
    except Exception as e:
        print(f"Error occurred while processing data: {str(e)}")

if __name__ == "__main__":
    process_product_data()
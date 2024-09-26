import os
from dotenv import load_dotenv

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
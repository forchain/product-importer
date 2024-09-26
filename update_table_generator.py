import pandas as pd

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
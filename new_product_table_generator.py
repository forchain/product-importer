import pandas as pd

DEFAULT_STOCK = 100

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
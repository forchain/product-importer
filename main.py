import os
import shutil
import pandas as pd
from config_loader import load_config
from update_table_generator import generate_update_table
from new_product_table_generator import generate_new_product_table

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
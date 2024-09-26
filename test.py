import os
import subprocess
import pandas as pd

def test_process_product_data():
    # Set environment variables
    os.environ['IMPORT_FILE'] = 'testdata/input_data.xlsx'
    os.environ['INVENTORY_FILE'] = 'testdata/inventory_data.xlsx'
    os.environ['UPDATE_PRODUCT_OUTPUT'] = 'testdata/update_product_output.xlsx'
    os.environ['NEW_PRODUCT_OUTPUT'] = 'testdata/new_product_output.xlsx'

    os.environ['UPDATE_PRODUCT_TEMPLATE'] = 'config/update_product_template.xlsx'
    os.environ['NEW_PRODUCT_TEMPLATE'] = 'config/new_product_template.xlsx'

    # Execute the process_product_data.py script
    subprocess.run(['python', 'process_product_data.py'], check=True)

    # Validate the update product table
    df_update = pd.read_excel('testdata/update_product_output.xlsx')
    assert len(df_update) == 19
    assert all(df_update['商品状态'].iloc[:9] == '上架')
    assert all(df_update['商品标题'].iloc[:9].notna())
    assert all(df_update['商品状态'].iloc[9:] == '下架')
    assert all(df_update['商品标题'].iloc[9:].isna())

    # Validate the new product table
    df_new_product = pd.read_excel('testdata/new_product_output.xlsx')
    assert '商品标题' in df_new_product.columns
    assert '型号分类1' in df_new_product.columns
    assert '型号名称1' in df_new_product.columns
    assert '商品价格' in df_new_product.columns
    assert '商品库存' in df_new_product.columns
    assert len(df_new_product) == 10

    # Clean up output files if necessary
    # os.remove('testdata/update_product_output.xlsx')
    # os.remove('testdata/new_product_output.xlsx')

if __name__ == "__main__":
    test_process_product_data()

import os
import pandas as pd
import streamlit as st
from config_loader import load_config
from update_table_generator import generate_update_table
from new_product_table_generator import generate_new_product_table
import io

def process_product_data(config, df_import, df_inventory):
    """Process product data and generate update and new product tables"""
    df_update = generate_update_table(df_import, df_inventory, config)
    df_new_product = generate_new_product_table(df_import, df_inventory, config)
    return df_update, df_new_product

def get_excel_download_link(df, filename):
    """Generate Excel file download link"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    excel_data = output.getvalue()
    return excel_data, filename

def main():
    st.title("微店商品导入表生成器")

    # Load configuration
    config = load_config()

    # Add Weidian batch import documentation link
    st.markdown("[微店批量导入文档](https://vmspub.weidian.com/gaia/55141/134c563b.html)")

    # Create two columns for layout with 2:1 width ratio
    col1, col2 = st.columns([2, 1])

    with col1:
        # File upload in web mode
        st.header("上传文件")
        uploaded_import_file = st.file_uploader("上传导入文件", type=["xlsx"])
        uploaded_inventory_file = st.file_uploader("上传库存文件", type=["xlsx"])

    with col2:
        # Add instructions with smaller font size
        st.markdown("""
        1. 导入表必须包含以下字段:
           - 标题(TITLE) - 必填
           - 价格(PRICE) - 必填
           - 型号(ITEM) - 必填
           - 备注(NOTES) - 选填
           - 规格(SIZE) - 选填
        2. 库存表在微店后台导出,必须包含以下字段:
           - 商品ID
           - 型号ID
           - 商品型号
        """, unsafe_allow_html=True)

    if uploaded_import_file and uploaded_inventory_file:
        # Read uploaded files
        df_import = pd.read_excel(uploaded_import_file)
        df_inventory = pd.read_excel(uploaded_inventory_file)

        # Process data
        df_update, df_new_product = process_product_data(config, df_import, df_inventory)

        # Display generated tables
        st.subheader("更新产品表")
        st.dataframe(df_update)

        st.subheader("新增产品表")
        st.dataframe(df_new_product)

        # Download buttons
        col3, col4 = st.columns(2)
        
        with col3:
            update_excel_data, update_filename = get_excel_download_link(df_update, "更新产品表.xlsx")
            st.download_button(
                label="下载更新产品表",
                data=update_excel_data,
                file_name=update_filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        with col4:
            new_excel_data, new_filename = get_excel_download_link(df_new_product, "新增产品表.xlsx")
            st.download_button(
                label="下载新增产品表",
                data=new_excel_data,
                file_name=new_filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

if __name__ == "__main__":
    main()
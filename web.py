import os
import pandas as pd
import streamlit as st
from config_loader import load_config
from update_table_generator import generate_update_table
from new_product_table_generator import generate_new_product_table
import io

def process_product_data(config, df_import, df_inventory):
    """处理产品数据并生成更新和新增产品表"""
    df_update = generate_update_table(df_import, df_inventory, config)
    df_new_product = generate_new_product_table(df_import, df_inventory, config)
    return df_update, df_new_product

def get_excel_download_link(df, filename):
    """生成Excel文件下载链接"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    excel_data = output.getvalue()
    return excel_data, filename

def main():
    st.title("商品导入导出系统")

    # 加载配置
    config = load_config()

    # Web模式文件上传
    st.header("上传文件")
    uploaded_import_file = st.file_uploader("上传导入文件", type=["xlsx"])
    uploaded_inventory_file = st.file_uploader("上传库存文件", type=["xlsx"])

    if uploaded_import_file and uploaded_inventory_file:
        # 读取上传的文件
        df_import = pd.read_excel(uploaded_import_file)
        df_inventory = pd.read_excel(uploaded_inventory_file)

        # 处理数据
        df_update, df_new_product = process_product_data(config, df_import, df_inventory)

        # 显示生成的表格
        st.subheader("更新产品表")
        st.dataframe(df_update)

        st.subheader("新增产品表")
        st.dataframe(df_new_product)

        # 下载按钮
        update_excel_data, update_filename = get_excel_download_link(df_update, "更新产品表.xlsx")
        st.download_button(
            label="下载更新产品表",
            data=update_excel_data,
            file_name=update_filename,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        new_excel_data, new_filename = get_excel_download_link(df_new_product, "新增产品表.xlsx")
        st.download_button(
            label="下载新增产品表",
            data=new_excel_data,
            file_name=new_filename,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    main()
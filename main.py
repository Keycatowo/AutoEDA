#%%
from glob import glob
import pandas as pd
from pathlib import Path
from dataprep.eda import create_report # 1-create report with dataprep
from pandas_profiling import ProfileReport # 2-create report with pandas_profiling
import sweetviz as sv # 3-create report with sweetviz
from autoviz.AutoViz_Class import AutoViz_Class # 4-create report with autoviz

#%% 取得資料夾內所有檔案的列表
def get_DataFrames():
    """Get all the dataframes from the data folder"""
    csv_files = glob("data/*.csv")
    csv_dfs = [(Path(file).name[:-4], pd.read_csv(file,encoding="utf-8")) for file in csv_files]
    excel_files = glob("data/*.xlsx")
    excel_dfs = [(Path(file).name[:-5], pd.read_excel(file)) for file in excel_files]
    df_list = csv_dfs + excel_dfs
    print(f"Total get {len(df_list)} dataframes")
    return df_list
    
#%%
def process_DataFrames(df_list):
    """Process the dataframes"""
    for df_name, df in df_list:
        
        # show basic information
        print(df_name)
        print(df.shape)
        print(df.describe())
        
        # create report folder
        Path(f"output/{df_name}").mkdir(exist_ok=True)

        # 1-create report with dataprep
        create_report(df).save(f"output/{df_name}/1-dataprep.html")
        # 2-create report with pandas_profiling
        ProfileReport(df, title=f"{df_name} report").to_file(f"output/{df_name}/2-pandas_profiling.html")
        # 3-create report with sweetviz
        sv.analyze(df).show_html(f"output/{df_name}/3-sweetviz.html")
        # 4-create report with autoviz
        # AV = AutoViz_Class()
        # AV.AutoViz(f"data/{df_name}.csv", sep=",", depVar="", 
        #     dfte=df, header=0, verbose=0, lowess=False, 
        #     chart_format="html", save_plot_dir=f"output/{df_name}",
        #     max_rows_analyzed=150000, max_cols_analyzed=30)

        print("--------------------")



#%% 
if __name__ == "__main__":
    df_list = get_DataFrames()
    process_DataFrames(df_list)
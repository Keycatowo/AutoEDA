# AutoEDA

## 目的
合併整理一些自動EDA工具，用來做快速資料初步探索報告


## 安裝

```sh
pip install -r requirements.txt
```

## 使用

### Step1: 將要分析的資料放置到data資料夾
+ 支援`.csv`或`.xlsx`檔案


### Step2: 執行分析腳本

```sh
python main.py
```


### Step3: 查看分析結果
+ 若以資料集為`diabetes.csv`為例
    + 會在`output/`下建立一個`diabetes/`資料夾
    + 包含三個不同工具分析的EDA結果html網頁





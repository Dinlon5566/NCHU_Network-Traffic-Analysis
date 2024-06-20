# Database

設計如何規劃擷取得到的資料  

1. 同個IP位置在不同時間會不同單位名稱。
2. 紀錄最近的 IP-單位-更新時間
3. 紀錄 IP-過去使用單位
4. 不需要記錄名次資料
5. 已導入檔案檔名紀錄

## Table設計
最新的IP-單位
```mysql
CREATE TABLE IP_Unit (
    ip VARCHAR(15) NOT NULL PRIMARY KEY,
    unit_name VARCHAR(255) NOT NULL,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```
紀錄 IP-過去使用單位
```mysql
CREATE TABLE IP_History (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(15) NOT NULL,
    unit_name VARCHAR(255) NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP
);
```
已導入檔案檔名紀錄
```mysql
CREATE TABLE Files_Imported (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    import_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
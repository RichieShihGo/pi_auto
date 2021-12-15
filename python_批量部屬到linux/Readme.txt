此專案使用python語言以及paramiko模組、threading模組實現

1.批量傳輸檔案到Clinet端(樹梅派)
2.批量下達指令到Clinet端(樹梅派)

===================================
主要是為了解決下述情形而撰寫。

1.目前自主檢電腦(樹梅派)有
  pi4_auto及pi_auto目錄及檔案內容不統一情形。

2.因應send_UDP 需回傳多個Server端時、Server端ip位址變更時；

3.改進了udp_client.py，config檔只需放入server_config_dir目錄內即會send udp至Server端。

***使用方式***

1.先執行1.python_batch_deployment_SSH_ftp.py
  將檔案(send_udp.tar.gz)部屬到Clinet端。

2.再執行2.python_batch_deployment.py
  批量下指令將Clinet端進行設定。


※ PS: Client端可因數量進行修改。
      (編輯2個.py檔案使用ip位址進行增減)
 
   211215 by Jacky.L
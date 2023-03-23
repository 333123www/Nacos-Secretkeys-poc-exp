# Nacos-Secretkeys-poc-exp

    使用说明：
            python unauth-nacos-key.py poc filename                     
            以poc模式对地址进行扫描
            
            python unauth-nacos-key.py exp filename username password    
            以exp模式对地址进行扫描(usernme,password可不写，默认创建账号aaa，密码bbb)
            
            文件中的地址格式如下(脚本没有对输入文件进行处理，只能以特定格式输入)： 
            http://192.168.1.1/
            http://192.168.1.2/
            http://192.168.1.3/

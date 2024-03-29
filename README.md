# 数据库巡检脚本

该脚本旨在执行自动化数据库巡检，生成详细的HTML报告，其中包含数据库基本信息和磁盘使用统计数据。通过将报告存档并上传到OwnCloud，用户可以方便地查看和管理这些巡检结果。

## 特点

- **数据库连接**：使用cx_Oracle库连接到Oracle数据库，收集有关数据库的基本信息。
- **磁盘使用统计**：通过Zabbix API检索磁盘使用统计信息，提供详细的磁盘空间报告。
- **HTML报告生成**：使用Jinja2模板生成包含详细信息的HTML报告。
- **自动归档**：生成的报告存档，并以ZIP文件的形式进行归档，方便管理历史数据。
- **OwnCloud上传**：将ZIP文件上传到OwnCloud，以便用户可以通过云端轻松访问和分享。

## 先决条件

在运行脚本之前，请确保：

- 您已安装Python（建议版本3.x）。
- 通过运行 `pip install -r requirements.txt` 安装了所需的Python包。
- 在配置文件 `config.conf` 中正确设置了OwnCloud和其他必要的参数。
- 在 `user_pass.py` 中提供了数据库连接详细信息。

## 用法

1. 在 `config.conf` 中配置OwnCloud和其他必要参数。
2. 在 `user_pass.py` 中提供数据库连接详细信息。
3. 运行 `main_ins.py` 脚本以执行数据库巡检。

## 配置

- **config.conf**：包含OwnCloud、路径和其他设置的配置参数。
- **user_pass.py**：提供一个包含数据库连接详细信息的字典列表。

## 输出

脚本为每个数据库生成一个HTML报告，并将其存档在ZIP文件中。ZIP文件会上传到OwnCloud，以便轻松访问和共享。

## 许可

该脚本基于 [MIT许可证](LICENSE) 发布。欢迎自由使用、修改和分发。

## 作者

Rain
WX： A-Rainbow8000

如果您遇到任何问题或有建议，请在GitHub上创建问题或提交拉取请求。我们欢迎您的贡献！

巡检愉快！

## 报告截图(部分)
![WechatIMG18810](https://github.com/Rain222222222/Oracle-/assets/130946945/0defa220-0a5d-4549-a828-5b7895a761a0)
![image](https://github.com/Rain222222222/Oracle-/assets/130946945/4523117b-2063-4035-a89f-816295dbc348)
![image](https://github.com/Rain222222222/Oracle-/assets/130946945/5ec5f07f-f069-4f4b-9c26-b7a229f8c4f1)
![image](https://github.com/Rain222222222/Oracle-/assets/130946945/2ba64381-0ecd-42b9-ae77-028e37678a35)

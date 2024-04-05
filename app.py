import subprocess,os
import streamlit as st
from tqdm import tqdm

ssh_server = os.getenv('ssh_server')
ssh_user = os.getenv('ssh_user')
ssh_pass = os.getenv('ssh_pass')
ssh_port = os.getenv('ssh_port')

def run_commands(commands):
    for i, command in enumerate(tqdm(commands, desc="启动进度")):
        process = subprocess.Popen(command, shell=True)
        process.wait()
        
def cmds_run():
    commands = [
        f'chmod -R 777 ./*', 
        f'bash ./start.sh {str(ssh_server)} {str(ssh_user)} {str(ssh_pass)} {int(ssh_port)} & jupyter lab --ip=0.0.0.0 --port={int(ssh_port)} --allow-root --no-browser &',
        f''
    ]
    run_commands(commands)
    
style = """
<style>
.center {
    text-align:  center
}
.text-size {
    font-size: 18px
}
"""
cmds_run()

st.markdown("## 二次元语音合成 API/WebUI 合集")
st.markdown("### 免责声明")
st.markdown("合成内容如果**出现了任何版权或法律或其它相关的问题**，请使用者**自行解决相关问题**。与**项目开发者**、**模型训练者**、**数据集提供者**、**AI Hobbyist 组织**、**数据来源作品** 无关！")
st.markdown("### 导航")
st.markdown("""|        类型        |                            传送门                            |        备注        |
| :----------------: | :----------------------------------------------------------: | :----------------: |
|   API Token   | [https://tts.ai-hobbyist.org/#/apikey](https://tts.ai-hobbyist.org/#/apikey) | 临时地址，后续更新 |
| Bert-VITS在线推理  | [https://tts.ai-hobbyist.org/#/infer](https://tts.ai-hobbyist.org/#/infer) | 临时地址，后续更新 |
| GPT-Sovits在线推理 |                              -                               |      敬请期待      |
|    RVC在线推理     |                              -                               |      敬请期待      |
|   Sovits在线推理   |                              -                               |      敬请期待      |""")
st.markdown("**注：** 使用前请认真阅读协议！！！！协议链接会贴在对应推理 WebUI")
st.markdown("### 联系方式")
st.markdown("""|           类别           |                             信息                             |
| :----------------------: | :----------------------------------------------------------: |
|        组织创始人        | [红血球AE3803 (Erythrocyte3803)](https://github.com/Erythrocyte3803) |
|         组织邮箱         |  [aihobbyistorg@gmail.com](mailto:aihobbyistorg@gmail.com)   |
|    AI Hobbyist交流群     | [点击链接加入群聊【AI Hobbyist总群】](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=yH2t7_Hk_U9v_sngJOnnvUwCDg3jzM6t&authKey=pAP301KgpwMXlgJr49j%2FwhgEMFQkOQL9ZnU7SJtmthjIRMLPp4PXmtMAHfUwYkXU&noverify=0&group_code=704917458) |
|    AI Hobbyist QQ频道    | [点击链接加入QQ频道【AI Hobbyist】](https://pd.qq.com/s/8c2wkdwyl) |
|   diffusion-svc交流群    | [点击链接加入群聊【diffusion-svc交流群】](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=KM1weNmIWGE-sQnFRkwNGDdhH-Mm9ruS&authKey=nYE7C28ibJZzDHhStgU2AoKBLYmkUXFHHuETNQQM4%2Fth6mADmUR9fyHCd4QdNFMF&noverify=0&group_code=608107671) |
|        模型整合站        |      [https://www.ai-lab.top/](https://www.ai-lab.top/)      |
|     模型&数据集网盘      | [https://pan.ai-hobbyist.org/](https://pan.ai-hobbyist.org/) |
| 模型&数据集网盘-备用链接 | [传送门](https://aihobbyist-my.sharepoint.com/:f:/g/personal/erythrocyte_org_ai-lab_top/Es5swZ4XeGtAhqXmF2s7GZ8Bi8EedQ8sdXRyPS-rHbClWQ?e=X5NgeJ) |""")
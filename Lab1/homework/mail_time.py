from gmail import GMail, Message
from random import choice
from datetime import datetime
resons = ["Em bị mệt", "Hôm nay em đến ngày", "Em bận chạy bo", "Em đang loot đồ"]
html_content = """
<p style="text-align: center;">Cộng H&ograve;a X&atilde; Hội Chủ Nghĩa Việt Nam</p>
<p style="text-align: center;">Độc Lập - Tự Do - Hạnh Ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: left;">K&iacute;nh gửi: - Trung T&acirc;m Techkids</p>
<p style="text-align: left;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; - Thầy gi&aacute;o: Huỳnh Tuấn Anh</p>
<p style="text-align: left;">&nbsp;H&ocirc;m nay v&i {{sickness}} n&ecirc;n em xin ph&eacute;p thầy cho em nghỉ học. Em sẽ cố gắng ho&agrave;n th&agrave;nh b&agrave;i tập v&agrave;o buổi h&ocirc;m sau. Em cảm ơn th&agrave;nh!!!</p>
<p style="text-align: left;">Thank you, babe &lt;3</p>
"""

hml_to_send = html_content.replace("{{sickness}}", choice(resons))

gmail = GMail('bekhoebengoan1995@gmail.com', 'Thanhnam123')

msg = Message('Hello babe', to='namnguyenktxd@gmail.com', html=hml_to_send )
now = datetime.today().hour
time_sent = now
loop = False
while loop:
    if time_sent <= 7: 
        gmail.send(msg)
        loop = True
        print("You has sent a message at {} o'clock ".format(time_sent))
    else:
        break
        
        
# Quân check hộ a bài tập này nhé! a import r mà a check trong thư đã gửi thì k thấy :(
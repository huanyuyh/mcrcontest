from mcrcon import MCRcon
import time

# 服务器RCON的配置信息
host = "192.168.6.179"
port = 25575
password = "nyh314nyh"

# 清理掉落物的命令
cleanup_command = "/kill @e[type=minecraft:item]"
# 提醒消息
reminder_message = "/say 掉落物将在20秒后被清理，请做好准备！"
reminder_message2 = "/say 掉落物将在10秒后被清理，请做好准备！"
# 清理频率（单位：秒），例如每30分钟清理一次
cleanup_interval = 10 * 60

def main():
    with MCRcon(host, password, port) as mcr:
        print("连接到Minecraft服务器.")
        while True:
            # 发送提醒消息
            print("发送提醒消息.")
            mcr.command(reminder_message)
            # 等待15秒
            time.sleep(10)
            mcr.command(reminder_message2)
            time.sleep(10)

            # 执行清理
            print("执行清理.")
            response1 = mcr.command(cleanup_command)
            response = mcr.command(f"say 执行清理: {response1}")
            print("执行清理: " + response1)
            time.sleep(cleanup_interval)

if __name__ == "__main__":
    main()

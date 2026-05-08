FROM python:3.14.0-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app.py .

# 声明端口
EXPOSE 8080

# 启动命令（直接使用 python 运行，日志输出到控制台）
CMD ["python", "app.py"]
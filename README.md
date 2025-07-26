# 图片压缩工具 (Image Compressor)

一个Python脚本，用于将JPG/JPEG图片压缩到100KB以下。

## 功能特点

- 自动检测并压缩当前目录下的所有JPG/JPEG图片
- 智能调整图片质量和尺寸以达到目标大小
- 显示处理进度和压缩结果
- 跳过已经小于目标大小的图片

## 安装依赖

```bash
pip install pillow tqdm
```

## 使用方法

1. 将脚本放在包含图片的目录中
2. 运行脚本：
```bash
python compress_images.py
```
3. 等待处理完成，压缩后的图片将替换原始文件

## 注意事项

- 脚本会直接修改原始文件，建议先备份
- 仅支持JPG/JPEG格式
- 目标大小默认为100KB，可在代码中修改
- 需要Python 3.x环境

## 贡献

欢迎提交Issue或Pull Request！

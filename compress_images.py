import os
from PIL import Image
from tqdm import tqdm

def compress_image(file_path, max_size_kb=100):
    """
    压缩图片到指定大小以下
    :param file_path: 图片文件路径
    :param max_size_kb: 最大允许的文件大小(KB)
    """
    try:
        # 检查文件大小
        file_size = os.path.getsize(file_path) / 1024  # 转换为KB
        if file_size <= max_size_kb:
            print(f"跳过 {file_path} (已小于 {max_size_kb}KB)")
            return
        
        print(f"处理 {file_path} (原始大小: {file_size:.2f}KB)")
        
        with Image.open(file_path) as img:
            # 获取原始尺寸
            original_width, original_height = img.size
            current_width, current_height = original_width, original_height
            
            # 初始质量设置
            quality = 95
            temp_file = file_path + "_temp.jpg"
            
            while True:
                try:
                    # 保存临时文件(明确指定JPEG格式)
                    img.save(temp_file, format='JPEG', quality=quality, optimize=True)
                    
                    # 检查新文件大小
                    new_size = os.path.getsize(temp_file) / 1024
                    
                    if new_size <= max_size_kb:
                        # 替换原文件
                        os.replace(temp_file, file_path)
                        print(f"压缩成功! 最终大小: {new_size:.2f}KB")
                        break
                    
                    # 如果质量已经很低(小于50)或者尺寸已经很小(小于300px)
                    if quality <= 50 or current_width <= 300:
                        # 继续降低质量
                        quality -= 5
                        if quality < 10:
                            quality = 10
                        print(f"继续降低质量至 {quality}%")
                        continue
                    
                    # 调整尺寸(降低1%)
                    current_width = int(current_width * 0.99)
                    current_height = int(current_height * 0.99)
                    
                    # 保持宽高比调整
                    img = img.resize((current_width, current_height), Image.LANCZOS)
                    print(f"调整尺寸至 {current_width}x{current_height}")
                    
                except Exception as e:
                    print(f"处理过程中出错: {str(e)}")
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                    break
                    
    except Exception as e:
        print(f"\n处理 {file_path} 时出错: {str(e)}")
    finally:
        try:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        except Exception as e:
            print(f"清理临时文件时出错: {str(e)}")

def main():
    print("开始压缩当前目录下的JPG图片...")
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取所有JPG/JPEG文件
    image_files = [f for f in os.listdir(current_dir) 
                  if f.lower().endswith(('.jpg', '.jpeg'))]
    
    if not image_files:
        print("未找到任何JPG/JPEG图片文件")
        return
    
    # 使用进度条处理
    print(f"发现 {len(image_files)} 个图片需要处理")
    for filename in tqdm(image_files, desc="处理进度", unit="图片"):
        file_path = os.path.join(current_dir, filename)
        compress_image(file_path)
    
    print("所有图片处理完成!")

if __name__ == "__main__":
    main()
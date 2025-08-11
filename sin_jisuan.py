import math

def dms_to_degrees(degrees, minutes, seconds):
    """将度分秒转换为十进制度数"""
    total_degrees = degrees + minutes/60 + seconds/3600
    return total_degrees

def main():
    print("角度输入格式：度 分 秒（用空格分隔）")
    try:
        # 获取用户输入
        d, m, s = map(float, input("请输入角度（度 分 秒）: ").split())
        k = float(input("请输入倍数: "))
        
        # 转换角度为十进制度
        angle_deg = dms_to_degrees(d, m, s)
        
        # 转换为弧度并计算sin值
        angle_rad = math.radians(angle_deg)
        sin_value = math.sin(angle_rad)
        cos_value = math.cos(angle_rad)
        
        # 计算最终结果
        result_sin = sin_value * k
        result_cos = cos_value * k

        # 输出结果
        print(f"\n输入角度: {d}° {m}' {s}\"")
        print(f"十进制角度: {angle_deg:.6f}°")
        print(f"sin({angle_deg:.6f}°) = {sin_value:.8f}")
        print(f"sin计算结果 ({sin_value:.8f} × {k}) = {result_sin:.8f}")
        print(f"cos计算结果 ({cos_value:.8f} × {k}) = {result_cos:.8f}")
    
    except ValueError:
        print("错误：请输入有效的数字！")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    sign=input("输入除q以外任意数继续")

    if sign=="q":
        sign=False
    else:
        sign=True

    while(sign):
        print("="*50)
        main()

        sign = input("使用q退出")
        if sign=="q":
            sign=False
        else:
            sign=True
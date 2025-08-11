import math

def dms_to_degrees(degrees, minutes, seconds, is_negative=False):
    """
    将度分秒转换为十进制角度
    :param degrees: 度（整数）
    :param minutes: 分（非负整数）
    :param seconds: 秒（非负整数）
    :param is_negative: 是否为负角度
    :return: 十进制角度值
    """
    total_degrees = degrees + minutes / 60.0 + seconds / 3600.0
    return -total_degrees if is_negative else total_degrees

def validate_height_input(value):
    """验证高程输入是否合理"""
    if abs(value) > 100:  # 假设正常高程值不会超过100米
        print(f"警告：输入高程值 {value} 异常，可能是单位错误（应为米）")
        return value / 1000.0  # 自动将毫米转换为米
    return value

def calculate_tan_result():
    results = []
    for i in range(1, 3):
        print(f"输入第{i}次数据：")
        try:
            # 输入角度（度、分、秒）和倍数
            deg_input = input("度（整数，可负，例如：-0）: ")
            
            # 检查是否带负号（包括负零）
            is_negative = deg_input.startswith('-')
            deg_value = int(deg_input.lstrip('-') or 0)  # 处理负号并转换为整数
            
            m = int(input("分（非负整数）: "))
            s = int(input("秒（非负整数）: "))
            multiplier = float(input("倍数: "))

            # 输入测站高和站标高
            high_cezhan = validate_height_input(float(input("测站高：")))
            high_zhanbiao = validate_height_input(float(input("觇标高：")))
            
            if m < 0 or s < 0:
                raise ValueError("分和秒必须为非负整数")
                
            # 转换为十进制角度
            angle_deg = dms_to_degrees(deg_value, m, s, is_negative)
            
            # 转换为弧度
            angle_rad = math.radians(angle_deg)
            
            # 计算 tan(角度) * 倍数
            tan_value = math.tan(angle_rad)
            result = tan_value * multiplier + high_cezhan - high_zhanbiao
            results.append(result)
            print(f"第{i}次计算结果: {result:.6f}")
            
        except ValueError as e:
            print(f"输入错误: {e}")
            return None
        except Exception as e:
            print(f"计算错误: {e}（可能是角度接近90°的奇数倍）")
            return None
    
    # 计算两次结果的平均值（根据测量原理）
    average = (results[0] - results[1]) / 2
    return average

# 主程序
if __name__ == "__main__":
    while True:
        print("="*50)
        final_result = calculate_tan_result()
        if final_result is not None:
            print(f"最终结果: {final_result:.6f}")

        if input("输入q退出，其他键继续: ").lower() == "q":
            break

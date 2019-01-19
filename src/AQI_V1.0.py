# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name: AQI_V1.0
   Description: AQI 手动计算
   Author: Administrator
   date: 2019/1/19
-------------------------------------------------
   Change Activity:
         2019/1/19:
-------------------------------------------------
"""


def caculate_aqi(iaqilo, iaqihi, bplo, bphi, value):
    """
        AQI 计算公式
    """
    return (iaqihi-iaqilo)*(value-bplo)/(bphi-bplo) + iaqilo


def caculate_CO_aqi(CO_value):
    iaqilo = 0
    iaqihi = 50
    bplo = 0
    bphi = 35
    if CO_value in range(2, 4):
        iaqilo = 50
        iaqihi = 100
        bplo = 2
        bphi = 14
    elif CO_value in range(4, 14):
        iaqilo = 100
        iaqihi = 150
        bplo = 4
        bphi = 14
    elif CO_value in range(14, 24):
        iaqilo = 150
        iaqihi = 200
        bplo = 14
        bphi = 24
    else:
        pass
    return caculate_aqi(iaqilo, iaqihi, bplo, bphi, CO_value)


def caculate_PM_aqi(PM_value):
    iaqilo = 0
    iaqihi = 50
    bplo = 0
    bphi = 35
    if PM_value in range(35, 75):
        iaqilo = 50
        iaqihi = 100
        bplo = 35
        bphi = 75
    elif PM_value in range(75, 115):
        iaqilo = 100
        iaqihi = 150
        bplo = 75
        bphi = 115
    elif PM_value in range(115, 150):
        iaqilo = 150
        iaqihi = 200
        bplo = 115
        bphi = 150
    else:
        pass
    return caculate_aqi(iaqilo, iaqihi, bplo, bphi, PM_value)


def get_aqi(PM_value, CO_value):
    """
        AQI计算
    """
    PM_aqi = caculate_PM_aqi(PM_value)
    CO_aqi = caculate_CO_aqi(CO_value)

    iaqi_list = []
    iaqi_list.append(PM_aqi)
    iaqi_list.append(CO_aqi)

    aqi = max(iaqi_list)
    return aqi


def main():
    """
        主函数
    """
    print("请输入以下信息，用空格分隔：")
    input_str = input("(1)PM2.5 (2)CO：")
    input_list = input_str.split(' ')
    PM_value = float(input_list[0])
    CO_value = float(input_list[1])
    aqi = get_aqi(PM_value, CO_value)
    print("AQI：", aqi)


if __name__ == "__main__":
    main()

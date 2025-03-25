# 赌博模拟警示程序 🎰⚠️

![Python版本](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-red)

一个具有教育意义的赌博行为模拟器，通过真实资金曲线展示赌博危害

## 🚨 核心功能

### 模拟系统
- 资金余额实时计算
- 下注历史记录追踪
- 动态可视化资金曲线
- 随机输赢概率模拟

### 警示功能
- 退出时显示警示语
- 资金变化可视化分析
- 反赌博提示信息
- 余额归零强制结束

## 📊 资金曲线分析

```python
# 资金曲线绘制逻辑
self.chart_ax.plot(self.balance_history, marker='o', color='red')
self.chart_ax.set_title('资金变化曲线')
self.chart_ax.set_xlabel('下注次数')
self.chart_ax.set_ylabel('余额（元）')
```

**图表特性**：
- 实时更新折线图
- 标记每次下注点
- 红色警示色系
- 网格辅助线

## ⚠️ 退出警示

```python
# 退出提示逻辑
messagebox.showinfo('游戏结束', 
    '老板把你打了一顿，拿走了你剩下的所有时间！\n\n'
    '重要提示：十赌九输，久赌必输，远离赌博！')
```

## 🛠️ 技术实现

### 主要组件
- **GUI框架**：Tkinter
- **数据可视化**：Matplotlib
- **交互提示**：Messagebox
- **随机算法**：Python random

### 核心类方法
- `quit_game()` - 处理退出逻辑
- `show_balance_chart()` - 初始化资金曲线
- `update_balance_chart()` - 刷新图表数据

## 🚀 快速开始

```bash
pip install matplotlib numpy
python main.py
```

## 📌 使用说明

1. 启动后显示赌博模拟界面
2. 每次下注更新资金余额
3. 查看实时资金变化曲线
4. 退出时显示警示信息

## 💡 设计目的

通过模拟赌博的资金变化过程：
- 直观展示"久赌必输"的数学规律
- 用数据可视化揭示赌博风险
- 强化"远离赌博"的警示作用

## 📄 开源协议
[MIT License](LICENSE)

---

⭐ **请勿用于真实赌博**  
⚠️ 本程序仅用于教育警示目的
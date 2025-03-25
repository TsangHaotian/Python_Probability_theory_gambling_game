import random
import tkinter as tk
from tkinter import messagebox, font

# 游戏参数设置
INITIAL_BALANCE = 1000  # 初始资金
WIN_PROB = 0.45  # 获胜概率
ODDS = 0.9  # 获胜赔率（赢时获得下注金额的倍数）

# 颜色配置
BG_COLOR = "#2E3440"  # 背景色
TEXT_COLOR = "#D8DEE9"  # 文字颜色
BUTTON_COLOR = "#5E81AC"  # 按钮颜色
WIN_COLOR = "#A3BE8C"  # 获胜颜色
LOSE_COLOR = "#BF616A"  # 亏损颜色


class GamblingGameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("赌博小游戏")
        self.root.geometry("400x500")
        self.root.configure(bg=BG_COLOR)

        # 初始化余额
        self.balance = INITIAL_BALANCE

        # 设置字体
        self.title_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.balance_font = font.Font(family="Helvetica", size=16)
        self.emoji_font = font.Font(family="Helvetica", size=40)

        # 创建 UI 组件
        self.create_widgets()

    def create_widgets(self):
        """创建 UI 组件"""
        # 标题
        self.title_label = tk.Label(
            self.root,
            text="🎰 赌博小游戏 🎰",
            font=self.title_font,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
        )
        self.title_label.pack(pady=20)

        # 余额显示
        self.balance_label = tk.Label(
            self.root,
            text=f"💰 当前余额: {self.balance:.2f} 元",
            font=self.balance_font,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
        )
        self.balance_label.pack(pady=10)

        # 下注输入框
        self.bet_entry = tk.Entry(
            self.root, font=self.balance_font, justify="center", width=20
        )
        self.bet_entry.pack(pady=10)

        # 下注按钮
        self.bet_button = tk.Button(
            self.root,
            text="🎲 下注",
            font=self.balance_font,
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            command=self.place_bet,
        )
        self.bet_button.pack(pady=10)

        # 结果显示
        self.result_label = tk.Label(
            self.root, text="", font=self.emoji_font, bg=BG_COLOR
        )
        self.result_label.pack(pady=20)

        # 退出按钮
        self.quit_button = tk.Button(
            self.root,
            text="🚪 退出",
            font=self.balance_font,
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            command=self.quit_game,
        )
        self.quit_button.pack(pady=10)

    def place_bet(self):
        """处理下注逻辑"""
        try:
            bet = float(self.bet_entry.get())
            if bet <= 0 or bet > self.balance:
                messagebox.showwarning("⚠️ 错误", "无效的下注金额！")
                return

            # 进行赌博
            if random.random() < WIN_PROB:
                win_amount = bet * ODDS
                self.balance += win_amount
                self.result_label.config(text=f"🎉 +{win_amount:.2f} 元", fg=WIN_COLOR)
            else:
                self.balance -= bet
                self.result_label.config(text=f"💸 -{bet:.2f} 元", fg=LOSE_COLOR)

            # 更新余额显示
            self.balance_label.config(text=f"💰 当前余额: {self.balance:.2f} 元")

            # 检查是否输光
            if self.balance <= 0:
                self.game_over()

        except ValueError:
            messagebox.showwarning("⚠️ 错误", "请输入有效数字！")

    def game_over(self):
        """游戏结束逻辑"""
        self.result_label.config(text="😭 菜", fg=LOSE_COLOR)
        messagebox.showinfo("游戏结束", "你已输光所有资金！\n\n💡 温馨提示：十赌九输，珍惜生活，远离赌博！")
        self.root.destroy()

    def quit_game(self):
        """退出游戏"""
        if messagebox.askyesno("退出", f"你确定要带着 {self.balance:.2f} 元离开吗？"):
            messagebox.showinfo("游戏结束", "老板把你打了一顿，拿走了你剩下所有的钱！\n\n💡 温馨提示：十赌九输，珍惜生活，远离赌博！")
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = GamblingGameUI(root)
    root.mainloop()
import random
import tkinter as tk
from tkinter import messagebox, font

# 游戏参数设置
INITIAL_BALANCE = 1000  # 初始资金
WIN_PROB = 0.3  # 获胜概率（三个图标一致的概率）
ODDS = 5  # 获胜赔率（三个图标一致时获得下注金额的倍数）
SPIN_DELAY = 100  # 轮盘转动动画的延迟时间（毫秒）

# 颜色配置
BG_COLOR = "#2E3440"  # 背景色
TEXT_COLOR = "#D8DEE9"  # 文字颜色
BUTTON_COLOR = "#5E81AC"  # 按钮颜色
WIN_COLOR = "#A3BE8C"  # 获胜颜色
LOSE_COLOR = "#BF616A"  # 亏损颜色

# 老虎机图标
SYMBOLS = ["🍒", "🍋", "🍊", "🍇", "🔔", "⭐", "🥑"]


class GamblingGameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("赌狗游戏")
        self.root.geometry("500x600")
        self.root.configure(bg=BG_COLOR)

        # 初始化余额
        self.balance = INITIAL_BALANCE
        self.is_spinning = False  # 是否正在转动
        self.current_bet = 0  # 当前下注金额

        # 设置字体
        self.title_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.balance_font = font.Font(family="Helvetica", size=16)
        self.symbol_font = font.Font(family="Helvetica", size=50)

        # 创建 UI 组件
        self.create_widgets()

    def create_widgets(self):
        """创建 UI 组件"""
        # 标题
        self.title_label = tk.Label(
            self.root,
            text="🎰 赌狗游戏 🎰",
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

        # 老虎机轮盘
        self.slot_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.slot_frame.pack(pady=20)

        self.slot_labels = []
        for i in range(3):  # 三个轮盘
            label = tk.Label(
                self.slot_frame,
                text="🎰",
                font=self.symbol_font,
                bg=BG_COLOR,
                fg=TEXT_COLOR,
            )
            label.pack(side="left", padx=10)
            self.slot_labels.append(label)

        # 下注输入框
        self.bet_entry = tk.Entry(
            self.root, font=self.balance_font, justify="center", width=20
        )
        self.bet_entry.pack(pady=10)

        # 下注按钮
        self.bet_button = tk.Button(
            self.root,
            text="🎲 开始赌博",
            font=self.balance_font,
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            command=self.start_spin,
        )
        self.bet_button.pack(pady=10)

        # 结果显示
        self.result_label = tk.Label(
            self.root, text="", font=self.balance_font, bg=BG_COLOR, fg=TEXT_COLOR
        )
        self.result_label.pack(pady=20)

        # 退出按钮
        self.quit_button = tk.Button(
            self.root,
            text="🚪 拿钱跑路",
            font=self.balance_font,
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            command=self.quit_game,
        )
        self.quit_button.pack(pady=10)

    def start_spin(self):
        """开始转动轮盘"""
        if self.is_spinning:
            return

        try:
            self.current_bet = float(self.bet_entry.get())  # 获取下注金额
            if self.current_bet <= 0 or self.current_bet > self.balance:
                messagebox.showwarning("⚠️ 错误", "无效的下注金额！")
                return

            # 扣除下注金额
            self.balance -= self.current_bet
            self.balance_label.config(text=f"💰 当前余额: {self.balance:.2f} 元")

            # 开始转动动画
            self.is_spinning = True
            self.bet_button.config(state="disabled")
            self.spin_count = 0
            self.final_symbols = random.choices(SYMBOLS, k=3)  # 随机生成最终结果
            self.animate_spin()

        except ValueError:
            messagebox.showwarning("⚠️ 错误", "请输入有效数字！")

    def animate_spin(self):
        """轮盘转动动画"""
        if self.spin_count < 20:  # 转动 20 次
            for label in self.slot_labels:
                label.config(text=random.choice(SYMBOLS))
            self.spin_count += 1
            self.root.after(SPIN_DELAY, self.animate_spin)
        else:
            # 显示最终结果
            for i, label in enumerate(self.slot_labels):
                label.config(text=self.final_symbols[i])

            # 检查是否获胜
            if len(set(self.final_symbols)) == 1:  # 三个图标一致
                win_amount = self.current_bet * ODDS
                self.balance += win_amount
                self.result_label.config(text=f"🎉 获胜 +{win_amount:.2f} 元", fg=WIN_COLOR)
            else:
                self.result_label.config(text=f"💸 亏损 -{self.current_bet:.2f} 元", fg=LOSE_COLOR)

            # 更新余额显示
            self.balance_label.config(text=f"💰 当前余额: {self.balance:.2f} 元")

            # 检查是否输光
            if self.balance <= 0:
                self.game_over()
            else:
                # 重置状态
                self.is_spinning = False
                if self.bet_button.winfo_exists():  # 确保按钮仍然存在
                    self.bet_button.config(state="normal")

    def game_over(self):
        """游戏结束逻辑"""
        self.result_label.config(text="😭 菜", fg=LOSE_COLOR)
        messagebox.showinfo("游戏结束", "你已输光所有资金！\n\n💡 温馨提示：十赌九输，珍惜生活，远离赌博！")
        self.root.destroy()

    def quit_game(self):
        """退出游戏"""
        if messagebox.askyesno("退出", f"你确定要带着 {self.balance:.2f} 元离开吗？"):
            messagebox.showinfo("游戏结束",
                                "老板把你打了一顿，拿走了你剩下所有的钱！\n\n温馨提示：十赌九输，珍惜生活，远离赌博！")
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = GamblingGameUI(root)
    root.mainloop()

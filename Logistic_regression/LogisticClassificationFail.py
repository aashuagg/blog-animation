from manim import *
import numpy as np

class LinearRegressionClassificationFail(Scene):
    def construct(self):
        # Title
        title = Text("Why Linear Regression Fails for Classification", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Setup axes
        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[-0.5, 1.5, 0.5],
            x_length=10,
            y_length=6,
            axis_config={
                "include_tip": True,
                "include_numbers": True,
                "font_size": 24,
            },
            tips=False,
        )
        
        # Labels
        x_label = Text("Number of Exclamation Marks", font_size=24).next_to(axes.x_axis, DOWN)
        y_label = Text("Label", font_size=24).next_to(axes.y_axis, LEFT).rotate(90 * DEGREES)
        
        # Add reference lines at y=0 and y=1
        line_0 = DashedLine(
            axes.c2p(0, 0), axes.c2p(12, 0),
            color=GRAY, stroke_width=2
        )
        line_1 = DashedLine(
            axes.c2p(0, 1), axes.c2p(12, 1),
            color=GRAY, stroke_width=2
        )
        
        # Labels for categories
        not_spam_label = Text("Not Spam (0)", font_size=20, color=BLUE).next_to(axes.c2p(0, 0), LEFT)
        spam_label = Text("Spam (1)", font_size=20, color=RED).next_to(axes.c2p(0, 1), LEFT)
        
        # Show axes
        self.play(FadeOut(title))
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            Create(line_0),
            Create(line_1),
            Write(not_spam_label),
            Write(spam_label)
        )
        self.wait(1)
        
        # Data points
        # Not spam (0-3 exclamation marks, label=0)
        not_spam_x = [0, 1, 1, 2, 2, 3, 0, 1, 2, 3]
        not_spam_y = [0] * len(not_spam_x)
        
        # Spam (6-10 exclamation marks, label=1)
        spam_x = [6, 7, 7, 8, 8, 9, 9, 10, 6, 8]
        spam_y = [1] * len(spam_x)
        
        # Create dots
        not_spam_dots = VGroup()
        for x, y in zip(not_spam_x, not_spam_y):
            dot = Dot(axes.c2p(x, y), color=BLUE, radius=0.1)
            not_spam_dots.add(dot)
        
        spam_dots = VGroup()
        for x, y in zip(spam_x, spam_y):
            dot = Dot(axes.c2p(x, y), color=RED, radius=0.1)
            spam_dots.add(dot)
        
        # Animate dots appearing
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in not_spam_dots], lag_ratio=0.1),
            run_time=2
        )
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in spam_dots], lag_ratio=0.1),
            run_time=2
        )
        self.wait(1)
        
        # Fit linear regression (manually for visualization)
        # Approximate line that would result from linear regression
        # Line from (0, 0.1) to (10, 0.9) approximately
        x_start = 0
        x_end = 12
        y_start = -0.1
        y_end = 1.1
        
        regression_line = Line(
            axes.c2p(x_start, y_start),
            axes.c2p(x_end, y_end),
            color=GREEN,
            stroke_width=4
        )
        
        regression_label = Text("Linear Regression Line", font_size=24, color=GREEN)
        regression_label.next_to(axes.c2p(6, 0.5), RIGHT, buff=0.5)
        
        # Show the regression line
        self.play(
            Create(regression_line),
            Write(regression_label)
        )
        self.wait(2)
        
        # Show predicted values as yellow dots on the line
        predicted_dots = VGroup()
        error_lines = VGroup()

        # For spam points (actual y=1)
        for x in spam_x:
            pred_y = 0.1 * x - 0.1  # Based on the regression line
            dot = Dot(axes.c2p(x, pred_y), color=YELLOW, radius=0.08)
            predicted_dots.add(dot)
            
            error_line = DashedLine(
                axes.c2p(x, 1),
                dot,
                color=ORANGE
            )
            error_lines.add(error_line)

        # For not spam points (actual y=0)
        for x in not_spam_x:
            pred_y = 0.1 * x - 0.1  # Based on the regression line
            dot = Dot(axes.c2p(x, pred_y), color=YELLOW, radius=0.08)
            predicted_dots.add(dot)
            
            error_line = DashedLine(
                axes.c2p(x, 0),
                dot,
                color=ORANGE
            )
            error_lines.add(error_line)

        
        predicted_label = Text("Predicted Values", font_size=20, color=YELLOW)
        predicted_label.next_to(axes.c2p(6, 0.5), RIGHT, buff=0.5).shift(DOWN)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=1.5) for dot in predicted_dots], lag_ratio=0.1),
            Write(predicted_label),
            run_time=2
        )
        self.wait(2)

        self.play(
            LaggedStart(*[FadeIn(line, scale=1.5) for line in error_lines], lag_ratio=0.1),
            run_time=2
        )
        self.wait(2)
        
        # Final message
        conclusion = Text(
            "Linear regression predicts continuous values, not binary labels!",
            font_size=24,
            color=ORANGE
        )
        conclusion.to_edge(DOWN)
        
        self.play(
            Write(conclusion),
            FadeOut(regression_label),
            FadeOut(predicted_label)
        )
        self.wait(3)
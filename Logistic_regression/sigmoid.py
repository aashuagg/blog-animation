from manim import *
import numpy as np

class SigmoidFunction(Scene):
    def construct(self):
        # Title
        title = Text("The Sigmoid Function", font_size=40)
        subtitle = MathTex(r"\sigma(z) = \frac{1}{1 + e^{-z}}", font_size=36)
        subtitle.next_to(title, DOWN)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)
        
        # Setup axes
        axes = Axes(
            x_range=[-10, 10, 2],
            y_range=[-0.2, 1.2, 0.2],
            x_length=10,
            y_length=6,
            axis_config={
                "include_tip": True,
                "include_numbers": True,
                "font_size": 24,
            },
        )
        
        # Labels
        x_label = MathTex("z", font_size=32).next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"\sigma(z)", font_size=32).next_to(axes.y_axis, UP)
        
        # Move title up and shrink
        self.play(
            title_group.animate.scale(0.7).to_corner(UL),
            Create(axes),
            Write(x_label),
            Write(y_label)
        )
        self.wait(1)
        
        # Horizontal asymptotes
        asymptote_0 = DashedLine(
            axes.c2p(-10, 0), axes.c2p(10, 0),
            color=GRAY, stroke_width=2, dash_length=0.1
        )
        asymptote_1 = DashedLine(
            axes.c2p(-10, 1), axes.c2p(10, 1),
            color=GRAY, stroke_width=2, dash_length=0.1
        )
        
        asymptote_label_0 = MathTex("y = 0", font_size=24, color=GRAY)
        asymptote_label_0.next_to(axes.c2p(-10, 0), LEFT, buff=0.2)
        
        asymptote_label_1 = MathTex("y = 1", font_size=24, color=GRAY)
        asymptote_label_1.next_to(axes.c2p(-10, 1), LEFT, buff=0.2)
        
        self.play(
            Create(asymptote_0),
            Create(asymptote_1),
            Write(asymptote_label_0),
            Write(asymptote_label_1)
        )
        self.wait(1)
        
        # Define sigmoid function
        def sigmoid(z):
            return 1 / (1 + np.exp(-z))
        
        # Create sigmoid curve
        sigmoid_curve = axes.plot(
            sigmoid,
            x_range=[-10, 10],
            color=BLUE,
            stroke_width=4
        )
        
        curve_label = MathTex(r"\sigma(z)", font_size=28, color=BLUE)
        curve_label.next_to(axes.c2p(5, sigmoid(5)), UP, buff=0.3)
        
        # Animate curve drawing
        self.play(
            Create(sigmoid_curve),
            run_time=3
        )
        self.play(Write(curve_label))
        self.wait(2)
        
        # Highlight key point (0, 0.5)
        center_point = Dot(axes.c2p(0, 0.5), color=RED, radius=0.1)
        center_label = MathTex("(0, 0.5)", font_size=24, color=RED)
        center_label.next_to(axes.c2p(0, 0.5), RIGHT, buff=0.3)
        
        # Vertical line at x=0
        vertical_line = DashedLine(
            axes.c2p(0, 0), axes.c2p(0, 0.5),
            color=RED, stroke_width=2, dash_length=0.1
        )
        
        self.play(
            Create(vertical_line),
            FadeIn(center_point, scale=1.5),
            Write(center_label)
        )
        self.wait(2)
        
        # Annotate left tail
        left_annotation = VGroup(
            MathTex(r"z \to -\infty", font_size=24, color=YELLOW),
            MathTex(r"\sigma(z) \to 0", font_size=24, color=YELLOW)
        ).arrange(DOWN, buff=0.2)
        left_annotation.next_to(axes.c2p(-7, 0.2), UP, buff=0.3)
        
        left_arrow = Arrow(
            left_annotation.get_bottom(),
            axes.c2p(-7, sigmoid(-7)),
            color=YELLOW,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(
            Write(left_annotation),
            Create(left_arrow)
        )
        self.wait(2)
        
        # Annotate right tail
        right_annotation = VGroup(
            MathTex(r"z \to +\infty", font_size=24, color=GREEN),
            MathTex(r"\sigma(z) \to 1", font_size=24, color=GREEN)
        ).arrange(DOWN, buff=0.2)
        right_annotation.next_to(axes.c2p(7, 0.8), DOWN, buff=0.3)
        
        right_arrow = Arrow(
            right_annotation.get_top(),
            axes.c2p(7, sigmoid(7)),
            color=GREEN,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(
            Write(right_annotation),
            Create(right_arrow)
        )
        self.wait(2)
        
        # Fade out previous annotations
        self.play(
            FadeOut(left_annotation),
            FadeOut(left_arrow),
            FadeOut(right_annotation),
            FadeOut(right_arrow)
        )
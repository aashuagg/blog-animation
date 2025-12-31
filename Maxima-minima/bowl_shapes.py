from manim import *

class UpwardBowl(Scene):
    def construct(self):
        # Title
        title = Text("f(x) = 2 + x²", font_size=36, color=BLUE)
        title.to_edge(DOWN)
        self.add(title)
        
        subtitle = Text("Minimum at x = 0", font_size=24, color=GREEN)
        subtitle.next_to(title, DOWN)
        self.add(subtitle)
        
        # Setup 2D axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 12, 2],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": True},
        )
        
        # Labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("f(x)", edge=UP, direction=UP)
        
        # Function curve
        curve = axes.plot(
            lambda x: 2 + x**2,
            x_range=[-2.5, 2.5],
            color=BLUE,
            stroke_width=4,
        )
        
        # Critical point
        critical_point = Dot(
            axes.c2p(0, 2),
            color=RED,
            radius=0.12
        )
        
        # Label for critical point
        point_label = MathTex("(0, 2)", font_size=24, color=RED)
        point_label.next_to(critical_point, DOWN, buff=0.3)
        
        # Add everything
        self.add(axes, x_label, y_label)
        self.add(curve)
        self.add(critical_point, point_label)
        
        # Formula box
        formula_box = VGroup(
            MathTex("f(x) = 2 + x^2", font_size=28, color=BLUE),
            MathTex("f'(x) = 2x", font_size=24),
            MathTex("f''(x) = 2 > 0", font_size=24, color=GREEN),
            Text("Concave up → Minimum", font_size=20, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        formula_box.to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)
        
        # Background for formula box
        box_bg = BackgroundRectangle(formula_box, fill_opacity=0.9, buff=0.2)
        self.add(box_bg, formula_box)


class DownwardBowl(Scene):
    def construct(self):
        # Title
        title = Text("f(x) = 2 - x²", font_size=36, color=RED)
        title.to_edge(DOWN)
        self.add(title)
        
        subtitle = Text("Maximum at x = 0", font_size=24, color=ORANGE)
        subtitle.next_to(title, DOWN)
        self.add(subtitle)
        
        # Setup 2D axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-8, 4, 2],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": True},
        )
        
        # Labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("f(x)", edge=UP, direction=UP)
        
        # Function curve
        curve = axes.plot(
            lambda x: 2 - x**2,
            x_range=[-2.5, 2.5],
            color=RED,
            stroke_width=4,
        )
        
        # Critical point
        critical_point = Dot(
            axes.c2p(0, 2),
            color=YELLOW,
            radius=0.12
        )
        
        # Label for critical point
        point_label = MathTex("(0, 2)", font_size=24, color=YELLOW)
        point_label.next_to(critical_point, UP, buff=0.3)
        
        # Add everything
        self.add(axes, x_label, y_label)
        self.add(curve)
        self.add(critical_point, point_label)
        
        # Formula box
        formula_box = VGroup(
            MathTex("f(x) = 2 - x^2", font_size=28, color=RED),
            MathTex("f'(x) = -2x", font_size=24),
            MathTex("f''(x) = -2 < 0", font_size=24, color=ORANGE),
            Text("Concave down → Maximum", font_size=20, color=ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        formula_box.to_corner(UR).shift(LEFT * 0.5 + DOWN * 0.5)
        
        # Background for formula box
        box_bg = BackgroundRectangle(formula_box, fill_opacity=0.9, buff=0.2)
        self.add(box_bg, formula_box)
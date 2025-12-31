from manim import *
import numpy as np

class SaddlePoint(ThreeDScene):
    def construct(self):
        # Title
        title = Text("Saddle Point: f(x,y) = x² - y²", font_size=32)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait(1)
        
        # Setup 3D axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-10, 10, 5],
            x_length=7,
            y_length=7,
            z_length=6,
        )
        
        # Labels
        x_label = MathTex("x", font_size=28, color=WHITE).next_to(axes.x_axis, RIGHT)
        y_label = MathTex("y", font_size=28, color=WHITE).next_to(axes.y_axis, UP)
        z_label = MathTex("f", font_size=28, color=WHITE).next_to(axes.z_axis, OUT)
        
        # Saddle function: f(x,y) = x^2 - y^2
        def saddle_func(x, y):
            return x**2 - y**2
        
        # Create saddle surface
        saddle_surface = Surface(
            lambda u, v: axes.c2p(u, v, saddle_func(u, v)),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(35, 35),
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        
        # Set camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES, zoom=0.7)
        
        # Show axes and surface
        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label), Write(z_label))
        self.wait(0.5)
        self.play(Create(saddle_surface), run_time=3)
        self.wait(2)
        
        # Critical point at origin
        self.play(FadeOut(title))
        
        critical_title = Text("Critical point at (0, 0)", font_size=28, color=RED)
        critical_title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(critical_title)
        self.play(Write(critical_title))
        
        critical_dot = Dot3D(
            point=axes.c2p(0, 0, saddle_func(0, 0)),
            color=RED,
            radius=0.35
        )
        
        self.play(FadeIn(critical_dot, scale=0.5))
        self.wait(2)
        
        # Show x-direction slice (curves UP)
        self.play(FadeOut(critical_title))
        
        x_slice_title = Text("Along x-axis: curves UP", font_size=26, color=YELLOW)
        x_slice_title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(x_slice_title)
        self.play(Write(x_slice_title))
        
        # Curve along x-axis (y=0)
        x_curve = ParametricFunction(
            lambda t: axes.c2p(t, 0, saddle_func(t, 0)),
            t_range=[-2.5, 2.5],
            color=YELLOW,
            stroke_width=8,
        )
        
        self.play(Create(x_curve), run_time=2)
        
        # Formula for x-direction
        x_formula = MathTex("f(x, 0) = x^2", font_size=32, color=YELLOW)
        x_formula.to_corner(UR).shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(x_formula)
        self.play(Write(x_formula))
        self.wait(3)
        
        # Clear x-direction
        self.play(
            FadeOut(x_curve),
            FadeOut(x_slice_title),
            FadeOut(x_formula)
        )
        
        # Show y-direction slice (curves DOWN)
        y_slice_title = Text("Along y-axis: curves DOWN", font_size=26, color=GREEN)
        y_slice_title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(y_slice_title)
        self.play(Write(y_slice_title))
        
        # Curve along y-axis (x=0)
        y_curve = ParametricFunction(
            lambda t: axes.c2p(0, t, saddle_func(0, t)),
            t_range=[-2.5, 2.5],
            color=GREEN,
            stroke_width=8,
        )
        
        self.play(Create(y_curve), run_time=2)
        
        # Formula for y-direction
        y_formula = MathTex("f(0, y) = -y^2", font_size=32, color=GREEN)
        y_formula.to_corner(UR).shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(y_formula)
        self.play(Write(y_formula))
        self.wait(3)
        
        # Show both curves together
        self.play(
            FadeOut(y_slice_title),
            FadeOut(y_formula)
        )
        
        both_title = Text("Saddle: UP and DOWN at same point", font_size=26, color=PURPLE)
        both_title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(both_title)
        self.play(Write(both_title))
        
        # Bring back x-curve
        x_curve_final = ParametricFunction(
            lambda t: axes.c2p(t, 0, saddle_func(t, 0)),
            t_range=[-2.5, 2.5],
            color=YELLOW,
            stroke_width=7,
        )
        
        self.play(Create(x_curve_final))
        self.wait(1)
        
        # Show both formulas
        both_formulas = VGroup(
            MathTex("f(x, 0) = x^2", color=YELLOW, font_size=28),
            Text("(minimum along x)", font_size=18, color=YELLOW),
            MathTex("f(0, y) = -y^2", color=GREEN, font_size=28),
            Text("(maximum along y)", font_size=18, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        both_formulas.to_corner(UR).shift(DOWN * 1)
        self.add_fixed_in_frame_mobjects(both_formulas)
        self.play(Write(both_formulas))
        self.wait(2)
        
        # Rotate to see the saddle shape
        self.play(FadeOut(both_title))
        
        rotate_title = Text("The Saddle / Pringles Chip Shape", font_size=28, color=PURPLE)
        rotate_title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(rotate_title)
        self.play(Write(rotate_title))
        
        # Slow rotation to appreciate the shape
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        
        self.wait(2)
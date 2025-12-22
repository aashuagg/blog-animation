from manim import *
import numpy as np

class GradientVectors(ThreeDScene):
    def construct(self):
        # Title
        title = Text("The Gradient Vector", font_size=32)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait(1)
        
        # Setup 3D axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[0, 20, 5],
            x_length=7,
            y_length=7,
            z_length=5,
        )
        
        # Labels
        x_label = MathTex("x", font_size=28).next_to(axes.x_axis, RIGHT)
        y_label = MathTex("y", font_size=28).next_to(axes.y_axis, UP)
        z_label = MathTex("f", font_size=28).next_to(axes.z_axis, OUT)
        
        # Function: f(x,y) = x^2 + y^2
        def func(x, y):
            return x**2 + y**2
        
        # Gradient function
        def gradient(x, y):
            return np.array([2*x, 2*y, 0])
        
        # Create surface
        surface = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30),
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        
        # Function label
        func_label = MathTex("f(x,y) = x^2 + y^2", font_size=36, color=BLUE)
        func_label.to_corner(UL).shift(DOWN * 1)
        self.add_fixed_in_frame_mobjects(func_label)
        
        # Set camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=-60 * DEGREES, zoom=0.7)
        
        # Show surface
        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label), Write(z_label))
        self.wait(0.5)
        self.play(Write(func_label))
        self.play(Create(surface), run_time=2)
        self.wait(2)
        
        # ========================================
        # Show gradient at ONE point
        # ========================================
        
        self.play(FadeOut(title))
        
        gradient_title = Text("Gradient at point (2, 1)", font_size=28, color=YELLOW)
        gradient_title.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(gradient_title)
        self.play(Write(gradient_title))
        
        # Pick a point
        x_point, y_point = 2.0, 1.0
        z_point = func(x_point, y_point)
        
        # Point on surface
        point_dot = Dot3D(
            point=axes.c2p(x_point, y_point, z_point),
            color=RED,
            radius=0.12
        )
        
        self.play(FadeIn(point_dot, scale=0.5))
        self.wait(1)
        
        # Gradient vector components
        grad = gradient(x_point, y_point)
        
        # Scale factor for visualization (make arrow visible but not huge)
        scale = 0.5
        
        # Gradient arrow at the point (on the surface)
        gradient_arrow = Arrow3D(
            start=axes.c2p(x_point, y_point, z_point),
            end=axes.c2p(x_point + scale*grad[0], y_point + scale*grad[1], z_point),
            color=YELLOW,
            thickness=0.02,
            height=0.3,
            base_radius=0.08,
        )
        
        self.play(Create(gradient_arrow), run_time=1.5)
        self.wait(2)
        
        # Show formula
        gradient_formula = MathTex(
            r"\nabla f = [2x, 2y]",
            font_size=36,
            color=YELLOW
        )
        gradient_formula.to_corner(UR).shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(gradient_formula)
        self.play(Write(gradient_formula))
        self.wait(1)
        
        # Show values at this point
        gradient_values = MathTex(
            r"\nabla f(2,1) = [4, 2]",
            font_size=32,
            color=YELLOW
        )
        gradient_values.next_to(gradient_formula, DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(gradient_values)
        self.play(Write(gradient_values))
        self.wait(2)
        
        # Explanation text
        explanation = Text(
            "Points toward steepest ascent",
            font_size=18,
            color=GREEN
        )
        explanation.next_to(gradient_values, DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait(3)
        
        # Clean up for next part
        self.play(
            FadeOut(point_dot),
            FadeOut(gradient_arrow),
            FadeOut(gradient_title),
            FadeOut(gradient_formula),
            FadeOut(gradient_values),
            FadeOut(explanation)
        )
        
        # ========================================
        # Show multiple gradient vectors
        # ========================================
        
        multi_title = Text("Gradient at multiple points", font_size=28, color=PURPLE)
        multi_title.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(multi_title)
        self.play(Write(multi_title))
        
        # Create multiple points and their gradients
        points_list = [
            (1.5, 1.5),
            (-1.5, 1.5),
            (-1.5, -1.5),
            (1.5, -1.5),
            (2, 0),
            (0, 2),
            (-2, 0),
            (0, -2),
        ]
        
        dots = VGroup()
        arrows = VGroup()
        
        scale = 0.4  # Scale for arrows
        
        for x_p, y_p in points_list:
            z_p = func(x_p, y_p)
            grad = gradient(x_p, y_p)
            
            # Dot
            dot = Dot3D(
                point=axes.c2p(x_p, y_p, z_p),
                color=RED,
                radius=0.08
            )
            dots.add(dot)
            
            # Arrow
            arrow = Arrow3D(
                start=axes.c2p(x_p, y_p, z_p),
                end=axes.c2p(x_p + scale*grad[0], y_p + scale*grad[1], z_p),
                color=YELLOW,
                thickness=0.015,
                height=0.25,
                base_radius=0.06,
            )
            arrows.add(arrow)
        
        # Show all dots
        self.play(LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots], lag_ratio=0.15))
        self.wait(1)
        
        # Show all arrows
        self.play(LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.15))
        self.wait(2)

        self.play(FadeOut(multi_title))
        
        # Key insight
        insight = Text(
            "All gradients point away from center (uphill)",
            font_size=22,
            color=GREEN
        )
        insight.to_corner(DR).shift(UP * 1.5)
        self.add_fixed_in_frame_mobjects(insight)
        self.play(Write(insight))
        self.wait(3)
        
        # ========================================
        # Show center point (gradient = 0)
        # ========================================
        
        self.play(FadeOut(insight))
        
        center_text = Text(
            "At center (0,0): gradient = [0, 0]",
            font_size=22,
            color=RED
        )
        center_text.to_corner(DR).shift(UP * 1.5)
        self.add_fixed_in_frame_mobjects(center_text)
        
        # Center point
        center_dot = Dot3D(
            point=axes.c2p(0, 0, func(0, 0)),
            color=RED,
            radius=0.15
        )
        
        self.play(Write(center_text))
        self.play(FadeIn(center_dot, scale=0.3))
        self.wait(2)
        
        flat_text = Text(
            "Flat point = minimum",
            font_size=22,
            color=RED
        )
        flat_text.next_to(center_text, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(flat_text)
        self.play(Write(flat_text))
        self.wait(3)
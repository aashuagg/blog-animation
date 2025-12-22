from manim import *
import numpy as np

class PartialDerivatives3D(ThreeDScene):
    def construct(self):
        # Title
        title = Text("Partial Derivatives Visualization", font_size=32)
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
        z_label = MathTex("f(x,y)", font_size=28).next_to(axes.z_axis, OUT)
        
        # Function: f(x,y) = x^2 + y^2
        def func(x, y):
            return x**2 + y**2
        
        # Create surface with better visibility
        surface = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(25, 25),
            fill_opacity=0.6,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        
        # Function label
        func_label = MathTex("f(x,y) = x^2 + y^2", font_size=36, color=BLUE)
        func_label.to_corner(UL).shift(DOWN * 1)
        self.add_fixed_in_frame_mobjects(func_label)
        
        # Set initial camera position
        self.set_camera_orientation(phi=65 * DEGREES, theta=-60 * DEGREES, zoom=0.8)
        
        # Show surface
        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label), Write(z_label))
        self.wait(1)
        self.play(Write(func_label))
        self.play(Create(surface), run_time=2)
        self.wait(2)
        
        # ========================================
        # PART 1: Slice along x-axis (fix y = 1)
        # ========================================
        
        self.play(FadeOut(title))
        
        # New title
        title_x = Text("Fix y = 1, vary x", font_size=28, color=YELLOW)
        title_x.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(title_x)
        self.play(Write(title_x))
        
        y_fixed = 1.0
        
        # Semi-transparent plane showing the slice
        plane_x = Surface(
            lambda u, v: axes.c2p(u, y_fixed, v),
            u_range=[-3, 3],
            v_range=[0, 10],
            resolution=(25, 25),
            fill_opacity=0.1,
            color=YELLOW,
            stroke_opacity=0.1,
        )
        
        # Netted wall: grid lines on the plane
        grid_lines_x = VGroup()
        for i in range(-3, 4):
            grid_lines_x.add(Line(
                axes.c2p(i, y_fixed, 0),
                axes.c2p(i, y_fixed, 10),
                color=YELLOW,
                stroke_width=2,
            ))
        for j in range(0, 11, 2):
            grid_lines_x.add(Line(
                axes.c2p(-3, y_fixed, j),
                axes.c2p(3, y_fixed, j),
                color=YELLOW,
                stroke_width=2,
            ))
        
        # Just the curve
        curve_x = ParametricFunction(
            lambda t: axes.c2p(t, y_fixed, func(t, y_fixed)),
            t_range=[-3, 3],
            color=YELLOW,
            stroke_width=8,
        )
        
        self.play(Create(plane_x), run_time=1)
        self.play(Create(grid_lines_x), run_time=1)
        self.play(Create(curve_x), run_time=2)
        # Make the front portion of the parabola 90% transparent
        self.play(surface.animate.set_fill(opacity=0.1), run_time=1)
        self.wait(2)
        
        # Formula
        formula_x = MathTex(r"\frac{\partial f}{\partial x} = 2x", 
                           font_size=36, color=YELLOW)
        formula_x.to_corner(UR).shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(formula_x)
        self.play(Write(formula_x))
        self.wait(2)
        
        # Rotate camera to see the curve better
        self.move_camera(phi=70 * DEGREES, theta=-75 * DEGREES, run_time=2)
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(curve_x),
            FadeOut(plane_x),
            FadeOut(grid_lines_x),
            FadeOut(title_x),
            FadeOut(formula_x),
            surface.animate.set_fill(opacity=0.6)
        )
        
        # Reset camera
        self.move_camera(phi=65 * DEGREES, theta=-60 * DEGREES, run_time=2)
        
        # ========================================
        # PART 2: Slice along y-axis (fix x = 1)
        # ========================================
        
        title_y = Text("Fix x = 1, vary y", font_size=28, color=GREEN)
        title_y.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(title_y)
        self.play(Write(title_y))
        
        x_fixed = 1.0
        
        # Semi-transparent plane showing the slice
        plane_y = Surface(
            lambda u, v: axes.c2p(x_fixed, u, v),
            u_range=[-3, 3],
            v_range=[0, 10],
            resolution=(25, 25),
            fill_opacity=0.1,
            color=GREEN,
            stroke_opacity=0.1,
        )
        
        # Netted wall: grid lines on the plane
        grid_lines_y = VGroup()
        for i in range(-3, 4):
            grid_lines_y.add(Line(
                axes.c2p(x_fixed, i, 0),
                axes.c2p(x_fixed, i, 10),
                color=GREEN,
                stroke_width=2,
            ))
        for j in range(0, 11, 2):
            grid_lines_y.add(Line(
                axes.c2p(x_fixed, -3, j),
                axes.c2p(x_fixed, 3, j),
                color=GREEN,
                stroke_width=2,
            ))
        
        # Just the curve
        curve_y = ParametricFunction(
            lambda t: axes.c2p(x_fixed, t, func(x_fixed, t)),
            t_range=[-3, 3],
            color=GREEN,
            stroke_width=8,
        )
        
        self.play(Create(plane_y), run_time=1)
        self.play(Create(grid_lines_y), run_time=1)
        self.play(Create(curve_y), run_time=2)
        # Make the front portion of the parabola 90% transparent
        self.play(surface.animate.set_fill(opacity=0.1), run_time=1)
        self.wait(2)
        
        # Formula
        formula_y = MathTex(r"\frac{\partial f}{\partial y} = 2y", 
                           font_size=36, color=GREEN)
        formula_y.to_corner(UR).shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(formula_y)
        self.play(Write(formula_y))
        self.wait(2)
        
        # Rotate camera
        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=2)
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(curve_y),
            FadeOut(plane_y),
            FadeOut(grid_lines_y),
            FadeOut(title_y),
            FadeOut(formula_y),
            surface.animate.set_fill(opacity=0.6)
        )
        
        # Reset camera
        self.move_camera(phi=65 * DEGREES, theta=-60 * DEGREES, run_time=2)
        
        # ========================================
        # PART 3: Show both together
        # ========================================
        
        title_both = Text("Both partial derivatives", font_size=28, color=PURPLE)
        title_both.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(title_both)
        self.play(Write(title_both))
        
        # Recreate both planes
        plane_x_final = Surface(
            lambda u, v: axes.c2p(u, y_fixed, v),
            u_range=[-3, 3],
            v_range=[0, 10],
            resolution=(25, 25),
            fill_opacity=0.1,
            color=YELLOW,
            stroke_opacity=0.1,
        )
        
        plane_y_final = Surface(
            lambda u, v: axes.c2p(x_fixed, u, v),
            u_range=[-3, 3],
            v_range=[0, 10],
            resolution=(25, 25),
            fill_opacity=0.1,
            color=GREEN,
            stroke_opacity=0.1,
        )
        
        # Netted walls: grid lines on the planes
        grid_lines_x_final = VGroup()
        for i in range(-3, 4):
            grid_lines_x_final.add(Line(
                axes.c2p(i, y_fixed, 0),
                axes.c2p(i, y_fixed, 10),
                color=YELLOW,
                stroke_width=2,
            ))
        for j in range(0, 11, 2):
            grid_lines_x_final.add(Line(
                axes.c2p(-3, y_fixed, j),
                axes.c2p(3, y_fixed, j),
                color=YELLOW,
                stroke_width=2,
            ))
        
        grid_lines_y_final = VGroup()
        for i in range(-3, 4):
            grid_lines_y_final.add(Line(
                axes.c2p(x_fixed, i, 0),
                axes.c2p(x_fixed, i, 10),
                color=GREEN,
                stroke_width=2,
            ))
        for j in range(0, 11, 2):
            grid_lines_y_final.add(Line(
                axes.c2p(x_fixed, -3, j),
                axes.c2p(x_fixed, 3, j),
                color=GREEN,
                stroke_width=2,
            ))
        
        # Recreate both curves
        curve_x_final = ParametricFunction(
            lambda t: axes.c2p(t, y_fixed, func(t, y_fixed)),
            t_range=[-3, 3],
            color=YELLOW,
            stroke_width=7,
        )
        
        curve_y_final = ParametricFunction(
            lambda t: axes.c2p(x_fixed, t, func(x_fixed, t)),
            t_range=[-3, 3],
            color=GREEN,
            stroke_width=7,
        )
        
        self.play(
            Create(plane_x_final),
            Create(plane_y_final),
            Create(grid_lines_x_final),
            Create(grid_lines_y_final),
            run_time=1
        )
        self.play(
            Create(curve_x_final),
            Create(curve_y_final),
            run_time=2
        )
        # Make the front portion of the parabola 90% transparent
        self.play(surface.animate.set_fill(opacity=0.1), run_time=1)
        
        # Intersection point
        intersection = Dot3D(
            point=axes.c2p(x_fixed, y_fixed, func(x_fixed, y_fixed)),
            color=RED,
            radius=0.15
        )
        
        self.play(FadeIn(intersection, scale=0.5))
        self.wait(1)
        
        # Show both formulas
        formulas_both = VGroup(
            MathTex(r"\frac{\partial f}{\partial x} = 2x", color=YELLOW, font_size=30),
            MathTex(r"\frac{\partial f}{\partial y} = 2y", color=GREEN, font_size=30),
        ).arrange(DOWN, buff=0.4)
        formulas_both.to_corner(UR).shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(formulas_both)
        self.play(Write(formulas_both))
        
        # Gentle rotation to see both curves
        self.begin_ambient_camera_rotation(rate=0.12)
        self.wait(8)
        self.stop_ambient_camera_rotation()
        
        self.wait(2)
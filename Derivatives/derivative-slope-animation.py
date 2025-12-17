from manim import *
import numpy as np

class UnderstandingDerivatives(Scene):
    def construct(self):
        # Title
        title = Text("Understanding Derivatives", font_size=28)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Setup axes - distance vs time
        axes = Axes(
            x_range=[0, 60, 10],
            y_range=[0, 50, 10],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True, "include_numbers": True},
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT}
        )
        
        # Labels
        x_label = Text("Time (minutes)", font_size=20).next_to(axes.x_axis, DOWN)
        y_label = Text("Distance (km)", font_size=20).next_to(axes.y_axis, LEFT).rotate(90 * DEGREES)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)
        
        # Create a realistic driving curve (not constant speed)
        # Simulates: fast start, slow middle (traffic), fast end
        def distance_func(t):
            # Piecewise function simulating different speeds
            if t < 20:
                return 1.2 * t  # Fast: 72 km/h
            elif t < 40:
                return 24 + 0.3 * (t - 20)  # Slow: 18 km/h (traffic)
            else:
                return 30 + 1.0 * (t - 40)  # Medium: 60 km/h
        
        # Create smooth curve
        curve = axes.plot(distance_func, x_range=[0, 60], color=BLUE, stroke_width=3)
        
        self.play(Create(curve))
        self.wait(2)
        
        # Show tangent line concept        
        
        # Pick a point on the curve (t = 30 minutes)
        t_point = 30
        point = Dot(axes.c2p(t_point, distance_func(t_point)), color=RED, radius=0.1)
        
        self.play(FadeIn(point))
        self.wait(1)
        
        # Calculate slope at t=30 (numerical derivative)
        dt = 0.1
        slope = (distance_func(t_point + dt) - distance_func(t_point - dt)) / (2 * dt)
        
        # Draw tangent line
        tangent_length = 15
        tangent_line = Line(
            axes.c2p(t_point - tangent_length, distance_func(t_point) - slope * tangent_length),
            axes.c2p(t_point + tangent_length, distance_func(t_point) + slope * tangent_length),
            color=RED,
            stroke_width=3
        )
        
        self.play(Create(tangent_line))
        self.wait(1)
        
        # Show the slope (right triangle)
        # Create triangle to show rise/run
        triangle_base = 10
        triangle_start = axes.c2p(t_point, distance_func(t_point))
        triangle_right = axes.c2p(t_point + triangle_base, distance_func(t_point))
        triangle_top = axes.c2p(t_point + triangle_base, distance_func(t_point) + slope * triangle_base)
        
        # Draw triangle
        horizontal = Line(triangle_start, triangle_right, color=ORANGE, stroke_width=2)
        vertical = Line(triangle_right, triangle_top, color=ORANGE, stroke_width=2)
        hypotenuse = Line(triangle_start, triangle_top, color=RED, stroke_width=2)
        
        # Labels for triangle
        dt_label = Text("dt", font_size=16, color=ORANGE).next_to(horizontal, DOWN, buff=0.1)
        dx_label = Text("dx", font_size=16, color=ORANGE).next_to(vertical, RIGHT, buff=0.1)
        slope_label = Text(f"slope = dx/dt", font_size=18, color=RED).next_to(hypotenuse, UP, buff=0.2)
        
        self.play(
            Create(horizontal),
            Create(vertical),
            Write(dt_label),
            Write(dx_label)
        )
        self.wait(1)
        
        self.play(Write(slope_label))
        self.wait(2)
        
        # Animate tangent line sliding along curve
        self.play(
            FadeOut(horizontal),
            FadeOut(vertical),
            FadeOut(dt_label),
            FadeOut(dx_label),
            FadeOut(slope_label)        
        )
        
        slide_text = Text("Derivative: the tangent line along the curve", font_size=22, color=PURPLE)
        slide_text.to_edge(UP).shift(DOWN * 0.8)
        self.play(Write(slide_text))
        
        # Animate tangent line moving along curve
        def get_tangent_at_t(t):
            if t < 1 or t > 59:
                return VGroup()
            
            dt = 0.1
            slope = (distance_func(t + dt) - distance_func(t - dt)) / (2 * dt)
            tangent_length = 15

            # Ensure endpoints are computed from the actual x positions so the
            # tangent line always passes through the point (t, f(t)). When near
            # the axes bounds the horizontal offset may be smaller than
            # `tangent_length`, so compute the true dx for each endpoint.
            x_left = max(0, t - tangent_length)
            x_right = min(60, t + tangent_length)

            y_left = distance_func(t) + slope * (x_left - t)
            y_right = distance_func(t) + slope * (x_right - t)

            line = Line(
                axes.c2p(x_left, y_left),
                axes.c2p(x_right, y_right),
                color=RED,
                stroke_width=3
            )
            dot = Dot(axes.c2p(t, distance_func(t)), color=RED, radius=0.08)
            
            # Speed label
            speed_kmh = slope * 60  # Convert to km/h
            speed_text = Text(f"Speed: {speed_kmh:.0f} km/h", font_size=16, color=RED)
            speed_text.next_to(axes.c2p(t, distance_func(t)), UR, buff=0.3)
            
            return VGroup(line, dot, speed_text)
        
        # Tracker for animation
        t_tracker = ValueTracker(5)
        tangent_group = always_redraw(lambda: get_tangent_at_t(t_tracker.get_value()))
        
        self.add(tangent_group)
        
        # Animate sliding
        self.play(t_tracker.animate.set_value(55), run_time=8, rate_func=linear)
        self.wait(2)
        
        # Final message
        self.play(
            FadeOut(tangent_group),
            FadeOut(slide_text)
        )
        
        final_text = VGroup(
            Text("The derivative reveals:", font_size=24, color=YELLOW),
            Text("Rate of change at every moment", font_size=20),
            Text("Steep slope = Fast speed", font_size=18, color=GREEN),
            Text("Gentle slope = Slow speed", font_size=18, color=BLUE),
            Text("Flat slope = Stopped", font_size=18, color=RED)
        ).arrange(DOWN, buff=0.3)
        
        final_text.move_to(ORIGIN).shift(RIGHT * 3 + UP * 1)
        
        self.play(Write(final_text))
        self.wait(3)
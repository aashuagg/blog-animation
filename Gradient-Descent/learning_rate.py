from manim import *
import numpy as np

class LearningRateTooBig(Scene):
    def construct(self):
        # Title
        title = Text("Learning Rate: Too Large", font_size=36, color=RED)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Setup axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 20, 5],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True},
        )
        
        # Labels
        x_label = axes.get_x_axis_label("w", direction=DOWN)
        y_label = axes.get_y_axis_label("L", direction=LEFT)
        
        # Function: f(x) = x^2 (simple parabola)
        def loss_func(x):
            return x**2
        
        # Plot the loss function
        graph = axes.plot(loss_func, x_range=[-4.5, 4.5], color=BLUE, stroke_width=3)
        
        # Minimum point
        min_point = Dot(axes.c2p(0, 0), color=GREEN, radius=0.12)
        min_label = Text("Minimum", font_size=20, color=GREEN).next_to(min_point, DOWN)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph))
        self.play(FadeIn(min_point), Write(min_label))
        self.wait(1)
        
        # Starting point (far from minimum)
        start_x = 4.0
        current_x = start_x
        
        # Learning rate (too large)
        alpha = 0.99  # Will cause oscillation
        
        # Create path
        points = [current_x]
        path_dots = VGroup()
        path_lines = VGroup()
        
        # Starting dot
        current_dot = Dot(axes.c2p(current_x, loss_func(current_x)), 
                         color=RED, radius=0.1)
        path_dots.add(current_dot)
        self.play(FadeIn(current_dot))
        
        # Gradient descent iterations (oscillating)
        num_iterations = 20
        
        for i in range(num_iterations):
            # Compute gradient (derivative of x^2 is 2x)
            gradient = 2 * current_x
            
            # Update (this will overshoot!)
            new_x = current_x - alpha * gradient
            
            # Keep within bounds for visualization
            new_x = np.clip(new_x, -4.5, 4.5)
            
            points.append(new_x)
            
            # Draw line from current to new position
            line = Line(
                axes.c2p(current_x, loss_func(current_x)),
                axes.c2p(new_x, loss_func(new_x)),
                color=YELLOW,
                stroke_width=2
            )
            
            # New dot
            new_dot = Dot(axes.c2p(new_x, loss_func(new_x)), 
                         color=RED, radius=0.08)
            
            path_lines.add(line)
            path_dots.add(new_dot)
            
            self.play(
                Create(line),
                FadeIn(new_dot),
                run_time=0.4
            )
            
            current_x = new_x
            
            # Small pause
            self.wait(0.2)
        
        # Show oscillation text
        oscillation_text = Text(
            "Overshoots and oscillates!\nNever converges to minimum",
            font_size=24,
            color=RED
        ).to_corner(UR).shift(DOWN * 0.5)
        
        self.play(Write(oscillation_text))
        self.wait(3)
        
        # Highlight the bouncing pattern
        self.play(
            *[dot.animate.scale(1.5) for dot in path_dots],
            run_time=0.5
        )
        self.play(
            *[dot.animate.scale(1/1.5) for dot in path_dots],
            run_time=0.5
        )
        self.wait(2)


class LearningRateTooSmall(Scene):
    def construct(self):
        # Title
        title = Text("Learning Rate: Too Small", font_size=36, color=ORANGE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Same setup
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 25, 5],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True},
        )
        
        x_label = axes.get_x_axis_label("w", direction=DOWN)
        y_label = axes.get_y_axis_label("L", direction=LEFT)
        
        def loss_func(x):
            return x**2
        
        graph = axes.plot(loss_func, x_range=[-4.5, 4.5], color=BLUE, stroke_width=3)
        
        min_point = Dot(axes.c2p(0, 0), color=GREEN, radius=0.12)
        min_label = Text("Minimum", font_size=20, color=GREEN).next_to(min_point, DOWN)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph))
        self.play(FadeIn(min_point), Write(min_label))
        self.wait(1)
        
        # Starting point
        start_x = 4.0
        current_x = start_x
        
        # Learning rate (too small)
        alpha = 0.005  # Tiny steps
        
        path_dots = VGroup()
        path_lines = VGroup()
        
        current_dot = Dot(axes.c2p(current_x, loss_func(current_x)), 
                         color=ORANGE, radius=0.1)
        path_dots.add(current_dot)
        self.play(FadeIn(current_dot))
        
        # Many iterations, slow progress
        num_iterations = 50
        
        for i in range(num_iterations):
            gradient = 2 * current_x
            new_x = current_x - alpha * gradient
            
            line = Line(
                axes.c2p(current_x, loss_func(current_x)),
                axes.c2p(new_x, loss_func(new_x)),
                color=YELLOW,
                stroke_width=2
            )
            
            new_dot = Dot(axes.c2p(new_x, loss_func(new_x)), 
                         color=ORANGE, radius=0.06)
            
            path_lines.add(line)
            path_dots.add(new_dot)
            
            self.play(
                Create(line),
                FadeIn(new_dot),
                run_time=0.2
            )
            
            current_x = new_x
            
            self.wait(0.1)
        
        slow_text = Text(
            "Tiny steps, painfully slow!\nStill far from minimum after 50 iterations",
            font_size=24,
            color=ORANGE
        ).to_corner(UR).shift(DOWN * 0.5)
        
        self.play(Write(slow_text))
        self.wait(3)


class LearningRateJustRight(Scene):
    def construct(self):
        # Title
        title = Text("Learning Rate: Just Right", font_size=36, color=GREEN)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 25, 5],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True},
        )
        
        x_label = axes.get_x_axis_label("w", direction=DOWN)
        y_label = axes.get_y_axis_label("L", direction=LEFT)
        
        def loss_func(x):
            return x**2
        
        graph = axes.plot(loss_func, x_range=[-4.5, 4.5], color=BLUE, stroke_width=3)
        
        min_point = Dot(axes.c2p(0, 0), color=GREEN, radius=0.12)
        min_label = Text("Minimum", font_size=20, color=GREEN).next_to(min_point, DOWN)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(graph))
        self.play(FadeIn(min_point), Write(min_label))
        self.wait(1)
        
        # Starting point
        start_x = 4.0
        current_x = start_x
        
        # Learning rate (just right)
        alpha = 0.1  # Good balance
        
        path_dots = VGroup()
        path_lines = VGroup()
        
        current_dot = Dot(axes.c2p(current_x, loss_func(current_x)), 
                         color=GREEN, radius=0.1)
        path_dots.add(current_dot)
        self.play(FadeIn(current_dot))
        
        # Efficient convergence
        num_iterations = 20
        
        for i in range(num_iterations):
            gradient = 2 * current_x
            new_x = current_x - alpha * gradient
            
            # Stop if very close to minimum
            if abs(new_x) < 0.05:
                break
            
            line = Line(
                axes.c2p(current_x, loss_func(current_x)),
                axes.c2p(new_x, loss_func(new_x)),
                color=YELLOW,
                stroke_width=2
            )
            
            new_dot = Dot(axes.c2p(new_x, loss_func(new_x)), 
                         color=GREEN, radius=0.08)
            
            path_lines.add(line)
            path_dots.add(new_dot)
            
            self.play(
                Create(line),
                FadeIn(new_dot),
                run_time=0.3
            )
            
            current_x = new_x
            
            self.wait(0.15)
        
        good_text = Text(
            "Smooth convergence!\nReaches minimum efficiently",
            font_size=24,
            color=GREEN
        ).to_corner(UR).shift(DOWN * 0.5)
        
        self.play(Write(good_text))
        self.wait(3)
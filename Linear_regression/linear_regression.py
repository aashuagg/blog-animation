from manim import *
import numpy as np

class LinearRegressionFitting(Scene):
    def construct(self):
        # Title
        title = Text("Linear Regression: Finding the Best-Fit Line", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Generate data (same as your notebook)
        np.random.seed(42)
        temperatures = np.random.uniform(15, 35, 20)
        sales = 20 * temperatures + np.random.normal(0, 80, 20) + 100
        
        # Setup axes
        axes = Axes(
            x_range=[10, 40, 5],
            y_range=[0, 900, 100],
            x_length=9,
            y_length=6,
            axis_config={"include_tip": True, "include_numbers": True},
        )
        
        # Labels
        x_label = Text("Temperature (°C)", font_size=20).next_to(axes.x_axis, DOWN)
        y_label = Text("Ice Cream Sales (scoops)", font_size=20).next_to(axes.y_axis, LEFT).rotate(90 * DEGREES)
        
        # Create scatter plot points
        dots = VGroup()
        for temp, sale in zip(temperatures, sales):
            dot = Dot(axes.c2p(temp, sale), color=BLUE, radius=0.08)
            dots.add(dot)
        
        # Show axes and data
        self.play(FadeOut(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots], lag_ratio=0.05))
        self.wait(2)
        
        # PRE-COMPUTE all gradient descent iterations
        alpha = 0.0001
        num_iterations = 10000
        
        def compute_gradient(x, y, w, b):
            N = len(y)
            y_pred = w * x + b
            error = y_pred - y
            dw = (2/N) * np.sum(x * error)
            db = (2/N) * np.sum(error)
            return dw, db
        
        # Store trajectory
        w_history = []
        b_history = []
        loss_history = []
        
        w = 0.0
        b = 0.0  # Start with horizontal line
        
        # Run FULL gradient descent and save all values
        for i in range(num_iterations + 1):
            # Compute loss
            y_pred = w * temperatures + b
            loss = np.mean((y_pred - sales) ** 2)
            
            w_history.append(w)
            b_history.append(b)
            loss_history.append(loss)
            
            # Update parameters
            if i < num_iterations:
                dw, db = compute_gradient(temperatures, sales, w, b)
                w = w - alpha * dw
                b = b - alpha * db
        
        print(f"Initial loss: {loss_history[0]:.2f}")
        print(f"Final loss: {loss_history[-1]:.2f}")
        print(f"Final w: {w_history[-1]:.2f}, b: {b_history[-1]:.2f}")
        
        # Function to create line from w, b
        def get_line(w, b):
            x_start = 10
            x_end = 40
            y_start = w * x_start + b
            y_end = w * x_end + b
            return Line(
                axes.c2p(x_start, y_start),
                axes.c2p(x_end, y_end),
                color=RED,
                stroke_width=4
            )
        
        # Show initial line
        initial_line = get_line(w_history[0], b_history[0])
        initial_text = Text("Initial: Horizontal line (w=0)", font_size=24, color=RED)
        initial_text.to_corner(UR).shift(DOWN * 0.5)
        
        self.play(Create(initial_line), Write(initial_text))
        self.wait(2)
        self.play(FadeOut(initial_text))
        
        # Create text objects
        iteration_text = Text(f"Iteration: 0", font_size=24, color=YELLOW)
        iteration_text.to_corner(UR).shift(DOWN * 0.5)
        
        loss_text = Text(f"Loss: {loss_history[0]:.0f}", font_size=24, color=YELLOW)
        loss_text.next_to(iteration_text, DOWN, buff=0.3)
        
        params_text = Text(f"w = {w_history[0]:.2f}, b = {b_history[0]:.2f}", font_size=20, color=GREEN)
        params_text.next_to(loss_text, DOWN, buff=0.3)
        
        self.add(iteration_text, loss_text, params_text)
        
        # Animate through key iterations with smooth transitions
        current_line = initial_line
        
        # Show snapshots at these iterations
        snapshots = [0, 2, 4, 6, 8, 10, 40, 100, 5000, 10000]
        
        for snapshot in snapshots:
            # Get values at this iteration
            w_snap = w_history[snapshot]
            b_snap = b_history[snapshot]
            loss_snap = loss_history[snapshot]
            
            # Create new line
            new_line = get_line(w_snap, b_snap)
            
            # Update text
            new_iteration_text = Text(f"Iteration: {snapshot}", font_size=24, color=YELLOW)
            new_iteration_text.to_corner(UR).shift(DOWN * 0.5)
            
            new_loss_text = Text(f"Loss: {loss_snap:.0f}", font_size=24, color=YELLOW)
            new_loss_text.next_to(new_iteration_text, DOWN, buff=0.3)
            
            new_params_text = Text(f"w = {w_snap:.2f}, b = {b_snap:.2f}", font_size=20, color=GREEN)
            new_params_text.next_to(new_loss_text, DOWN, buff=0.3)
            
            # Animate transformation
            self.play(
                Transform(current_line, new_line),
                Transform(iteration_text, new_iteration_text),
                Transform(loss_text, new_loss_text),
                Transform(params_text, new_params_text),
                run_time=1
            )
            self.wait(1)
        
        # Final message
        final_message = Text(
            f"Converged! Final loss: {loss_history[-1]:.0f}",
            font_size=28,
            color=GREEN
        )
        final_message.to_edge(UP)
        self.play(Write(final_message))
        self.wait(3)
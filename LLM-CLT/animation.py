from manim import *
import numpy as np

class LLNandCLT(Scene):
    def construct(self):
        # Title
        title = Paragraph("Law of Large Numbers vs Central Limit Theorem", font_size=32).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Divide screen
        divider = Line(UP * 3.5, DOWN * 3.5, color=WHITE, stroke_width=2)
        self.play(Create(divider))
        
        self.wait(1)
        
        # Expected value
        expected_value = 3.5
        
        # Left side: WIDER Y-RANGE to see early variance
        lln_axes = Axes(
            x_range=[0, 300, 20],
            y_range=[2.8, 4.2, 0.4],  # Even more zoomed in!
            x_length=5.5,
            y_length=4,
            axis_config={"include_tip": False},
        ).shift(LEFT * 3.5 + DOWN * 0.5)
        
        lln_x_label = Paragraph("Number of Samples", font_size=14).next_to(lln_axes, DOWN, buff=0.3)
        lln_y_label = Paragraph("Running Average", font_size=14).next_to(lln_axes, LEFT, buff=0.3).rotate(90 * DEGREES)
        
        self.play(Create(lln_axes), Write(lln_x_label), Write(lln_y_label))
        
        # Expected value line - DASHED so blue line is visible
        expected_line = DashedLine(
            lln_axes.c2p(0, expected_value),
            lln_axes.c2p(300, expected_value),
            color=YELLOW,
            stroke_width=2,
            dash_length=0.1
        )
        expected_label = Paragraph("Expected: 3.5", font_size=12, color=YELLOW).next_to(
            lln_axes.c2p(80, 3.5), UP, buff=0.1
        )
        self.play(Create(expected_line), Write(expected_label))
        
        # Right side: WIDER HISTOGRAM RANGE
        clt_axes = Axes(
            x_range=[2.8, 4.2, 0.2],  # Show more extremes
            y_range=[0, 20, 5],
            x_length=5.5,
            y_length=4,
            axis_config={"include_tip": False},
        ).shift(RIGHT * 3.5 + DOWN * 0.5)
        
        clt_x_label = Paragraph("Average Value", font_size=14).next_to(clt_axes, DOWN, buff=0.3)
        clt_y_label = Paragraph("Frequency", font_size=14).next_to(clt_axes, LEFT, buff=0.3).rotate(90 * DEGREES)
        
        self.play(Create(clt_axes), Write(clt_x_label), Write(clt_y_label))
        
        # Simulation - FEWER dice per sample for more variance!
        num_samples = 300
        dice_per_sample = 20  # REDUCED to get more spread
        
        # Generate samples
        np.random.seed(123)  # Different seed for better variance
        averages = []
        running_averages = []
        
        for i in range(num_samples):
            dice_rolls = np.random.randint(1, 7, dice_per_sample)
            sample_avg = np.mean(dice_rolls)
            averages.append(sample_avg)
            
            running_avg = np.mean(averages)
            running_averages.append(running_avg)
        
        # Points for LLN line
        points = [lln_axes.c2p(i, running_averages[i]) for i in range(num_samples)]
        
        # Initial line - THICKER and BRIGHTER
        running_avg_line = VMobject(color=BLUE, stroke_width=4)  # Thicker!
        running_avg_line.set_points_as_corners([points[0], points[0]])
        self.play(Create(running_avg_line))
        
        # Current value display
        current_value = DecimalNumber(
            running_averages[0],
            num_decimal_places=3,
            font_size=24,
            color=BLUE
        ).next_to(lln_axes, UP, buff=0.3)
        current_label = Paragraph("Current:", font_size=18, color=BLUE).next_to(current_value, LEFT)
        
        self.play(Write(current_label), Write(current_value))
        
        # Histogram bars
        histogram_bars = VGroup()
        self.add(histogram_bars)
        
        # Bins for histogram - WIDER RANGE
        bins = np.linspace(2.8, 4.2, 12)
        
        # Tracker
        tracker = ValueTracker(1)

        def update_line(mob):
            i = int(tracker.get_value())
            if i > 0 and i < len(points):
                new_points = [points[j] for j in range(min(i + 1, len(points)))]
                if len(new_points) > 1:
                    mob.set_points_as_corners(new_points)

        def update_histogram(mob):
            i = int(tracker.get_value())
            if i > 5 and i <= len(averages):
                hist, bin_edges = np.histogram(averages[:i], bins=bins, density=False)
                
                # Clear and rebuild
                mob.become(VGroup())
                max_count = max(hist) if max(hist) > 0 else 1
                
                for j in range(len(hist)):
                    if hist[j] > 0:
                        # Scale height
                        bar_height = (hist[j] / max_count) * 15  # Max height
                        bar_width = (bin_edges[j + 1] - bin_edges[j]) * 0.9
                        bar_x = (bin_edges[j] + bin_edges[j + 1]) / 2
                        
                        # Position bar
                        bar_bottom = clt_axes.c2p(bar_x, 0)
                        bar_top = clt_axes.c2p(bar_x, bar_height)
                        actual_height = bar_top[1] - bar_bottom[1]
                        
                        bar = Rectangle(
                            width=clt_axes.x_length * bar_width / (4.2 - 2.8),
                            height=actual_height,
                            color=GREEN,
                            fill_opacity=0.7,
                            stroke_width=1
                        )
                        bar.move_to([bar_bottom[0], (bar_bottom[1] + bar_top[1]) / 2, 0])
                        
                        mob.add(bar)
        
        def update_value(mob):
            i = int(tracker.get_value())
            if i > 0 and i < len(running_averages):
                mob.set_value(running_averages[i])

        # Add updaters
        running_avg_line.add_updater(update_line)
        histogram_bars.add_updater(update_histogram)
        current_value.add_updater(update_value)

        # Animate
        self.play(tracker.animate.set_value(num_samples - 1), run_time=15, rate_func=linear)

        # Remove updaters
        running_avg_line.remove_updater(update_line)
        histogram_bars.remove_updater(update_histogram)
        current_value.remove_updater(update_value)
        
        self.wait(1)
        
        # Final annotations
        lln_conclusion = Paragraph(
            "Converges to 3.5",
            font_size=16,
            color=BLUE
        ).next_to(lln_axes, DOWN, buff=0.8)
        
        clt_conclusion = Paragraph(
            "Bell Curve!",
            font_size=16,
            color=GREEN
        ).next_to(clt_axes, DOWN, buff=0.8)
        
        self.play(Write(lln_conclusion), Write(clt_conclusion))

        self.wait(3)
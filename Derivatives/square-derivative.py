from manim import *

class SquareDerivative(Scene):
    def construct(self):
        # Title
        title = Text("Why x² becomes 2x", font_size=32, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Original square
        square_size = 3
        original_square = Square(side_length=square_size, color=YELLOW, fill_opacity=0.7)
        original_square.move_to(ORIGIN)
        
        # Labels for sides
        side_label_left = MathTex("x", font_size=36)
        side_label_left.next_to(original_square, LEFT, buff=0.3)
        
        side_label_bottom = MathTex("x", font_size=36)
        side_label_bottom.next_to(original_square, DOWN, buff=0.3)
        
        # Area label inside
        area_label = MathTex("x^2", font_size=40, color=YELLOW)
        area_label.move_to(original_square.get_center())
        
        self.play(
            Create(original_square),
            Write(side_label_left),
            Write(side_label_bottom),
            Write(area_label)
        )
        self.wait(1)
        
        # dx amount
        dx_size = 0.2
        
        # Right strip (blue)
        right_strip = Rectangle(
            width=dx_size,
            height=square_size,
            color=BLUE,
            fill_opacity=0.7,
            stroke_width=2
        )
        right_strip.next_to(original_square, RIGHT, buff=0)
        
        right_strip_label = MathTex("x \\cdot dx", font_size=28, color=WHITE)
        right_strip_label.move_to(right_strip.get_center())
        
        # Top strip (blue)
        top_strip = Rectangle(
            width=square_size,
            height=dx_size,
            color=BLUE,
            fill_opacity=0.7,
            stroke_width=2
        )
        top_strip.next_to(original_square, UP, buff=0)
        
        top_strip_label = MathTex("x \\cdot dx", font_size=28, color=WHITE)
        top_strip_label.move_to(top_strip.get_center())
        
        # Corner piece (red)
        corner_piece = Square(
            side_length=dx_size,
            color=RED,
            fill_opacity=0.8,
            stroke_width=2
        )
        corner_piece.move_to(
            original_square.get_corner(UR) + RIGHT * dx_size/2 + UP * dx_size/2
        )
        
        corner_label = MathTex("dx^2", font_size=28, color=WHITE)
        corner_label.move_to(corner_piece.get_center())
        
        # dx labels on sides
        dx_label_right = MathTex("dx", font_size=30, color=BLUE)
        dx_label_right.next_to(right_strip, RIGHT, buff=0.2)
        
        dx_label_top = MathTex("dx", font_size=30, color=BLUE)
        dx_label_top.next_to(top_strip, UP, buff=0.2)
        
        # Grow all pieces
        self.play(
            GrowFromEdge(right_strip, LEFT),
            GrowFromEdge(top_strip, DOWN),
            GrowFromEdge(corner_piece, DL),
            Write(dx_label_right),
            Write(dx_label_top),
            run_time=2
        )
        
        self.play(
            Write(right_strip_label),
            Write(top_strip_label),
            Write(corner_label)
        )
        self.wait(2)
        
        # Show the expansion formula
        formula = MathTex(
            "(x+dx)^2 = x^2 + 2x \\cdot dx + dx^2",
            font_size=36
        )
        formula.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(formula))
        self.wait(2)
        
        # Corner vanishes
        vanish_text = Text("dx² → 0", font_size=24, color=RED)
        vanish_text.next_to(corner_piece, RIGHT, buff=0.5)
        
        self.play(Write(vanish_text))
        self.play(
            corner_piece.animate.scale(0.2).set_fill(opacity=0.2),
            corner_label.animate.scale(0.3).fade(0.7),
            run_time=1.5
        )
        self.play(FadeOut(corner_piece), FadeOut(corner_label), FadeOut(vanish_text))
        self.wait(1)
        
        # Final result
        self.play(FadeOut(formula))
        
        result = MathTex(
            "\\frac{d(x^2)}{dx} = \\frac{2x \\cdot dx}{dx} = 2x",
            font_size=40,
            color=GREEN
        )
        result.to_edge(DOWN).shift(UP * 0.5)
        
        result_box = SurroundingRectangle(result, color=GREEN, buff=0.2, stroke_width=3)
        
        self.play(Write(result))
        self.play(Create(result_box))
        
        # Highlight the two strips
        self.play(
            right_strip.animate.set_fill(opacity=0.9),
            top_strip.animate.set_fill(opacity=0.9)
        )
        self.wait(3)
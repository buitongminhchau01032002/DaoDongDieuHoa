from manim import *

class MoveAround(Scene):
    def construct(self):
        _radius = 2
        circle = Circle(radius=_radius, fill_opacity=0, stroke_width = 3, fill_color=WHITE, stroke_color=WHITE)
        point = Dot(radius=0.05)
        point_text = MathTex("O").next_to(point, DOWN, buff=0.05)
        point_group = VGroup(point, point_text)
        self.play(FadeIn(point_group), Create(circle))

        def update_dot_move(x, dt):
            x.rotate(PI/2*dt, about_point=point.get_center())
        dot_move = Dot(fill_color = BLUE, radius=0.1).shift(RIGHT*_radius)
        self.play(FadeIn(dot_move))
        dot_move.add_updater(update_dot_move)
        self.wait(4.25)
        dot_move.remove_updater(update_dot_move)
        
        dot_start = dot_move.copy()
        line1 = Line(point.get_center(), dot_move.get_center(), stroke_color=YELLOW)
        line2 = line1.copy().add_updater(lambda line: line.become(Line(point.get_center(), dot_move.get_center(), stroke_color = YELLOW)))
        self.play(Create(line1), Create(line2))
        dot_move.add_updater(update_dot_move)
        arc = ArcBetweenPoints(start=dot_start.get_center(), end=dot_move.get_center()).add_updater(lambda arc: arc.become(ArcBetweenPoints(start=dot_start.get_center(), end=dot_move.get_center(), stroke_color = RED, radius=_radius)))
        self.add(arc)
        self.wait(0.5)
        dot_move.remove_updater(update_dot_move)
        angle = Angle(line1, line2, stroke_color=RED, radius = 0.5)
        lable_angle = MathTex(r"\Delta \varphi").move_to(angle.point_from_proportion(0.5)*1.7)
        lable_arc = MathTex(r"\Delta t").move_to(arc.point_from_proportion(0.5)*1.2)
        self.play(Create(angle), FadeIn(lable_angle), FadeIn(lable_arc))
        self.wait(2)

        formula = MathTex(r"{{\Delta \varphi}} {{ = }} {{\omega .}} {{\Delta t}}", font_size=50).to_edge(UP)
        self.play(TransformMatchingTex(lable_angle.copy(), formula), TransformMatchingTex(lable_arc.copy(), formula))
        rect_surround = SurroundingRectangle(formula, stroke_color = YELLOW)
        self.play(Create(rect_surround))
        
        self.wait(2)

        self.play(Uncreate(rect_surround), FadeOut(formula), FadeOut(lable_arc), FadeOut(lable_angle), FadeOut(line1), FadeOut(line2), FadeOut(angle), FadeOut(arc))
        self.wait(1)

        dotA = Dot(radius=0.05).shift(RIGHT*_radius)
        dotA_ = Dot(radius=0.05).shift(LEFT*_radius)
        textA = MathTex("A", color=BLUE).next_to(dotA, DR, buff=0)
        textA_ = MathTex("-A", color=BLUE).next_to(dotA_, DL, buff=0)
        lineA = Line(dotA_.get_center(), dotA.get_center())
        self.play(FadeIn(dotA), FadeIn(dotA_), FadeIn(textA), FadeIn(textA_), run_time=0.5)
        self.play(Create(lineA))

        dot_oscillate = Dot([dot_move.get_center()[0], 0, 0]).add_updater(lambda dot: dot.become(Dot([dot_move.get_center()[0], 0, 0], fill_color=PINK, radius=0.1)))
        line_connect = Line(stroke_width=3, stroke_opacity=0.5).add_updater(lambda line: line.become(Line(dot_move.get_center(), [dot_move.get_center()[0], 0, 0], stroke_width=3, stroke_opacity=0.5)))
        lable_x = MathTex("x", color=PINK).add_updater(lambda x: x.next_to(dot_oscillate, DOWN, buff=0.05))
        self.play(Create(line_connect))
        self.play(FadeIn(dot_oscillate))
        dot_move.add_updater(update_dot_move)

        self.wait(7.6)
        dot_move.remove_updater(update_dot_move)
        self.play(FadeIn(lable_x))
        line1 = Line(point.get_center(), dot_move.get_center(), stroke_color=YELLOW)
        #line2 = line1.copy().add_updater(lambda line: line.become(Line(point.get_center(), dot_move.get_center(), stroke_color = YELLOW)))
        self.play(Create(line1), Create(line2))
        ##
        phi_angle = Angle(lineA, line1, stroke_color=YELLOW, radius = 0.7)
        phi_lable = MathTex(r"\varphi", color=YELLOW).move_to(phi_angle.point_from_proportion(0.5)*1.4)
        t0 = MathTex(r"t_0=0").next_to(dot_move, UR, buff=0)
        self.play(Create(phi_angle), FadeIn(phi_lable), FadeIn(t0))
        self.wait(1.5)
        dot_move.add_updater(update_dot_move)
        self.wait(0.45)
        dot_move.remove_updater(update_dot_move)
        angle = Angle(line1, line2, stroke_color=RED, radius = 0.6)
        lable_angle = MathTex(r"\Delta \varphi", color=RED).move_to(angle.point_from_proportion(0.5)*1.7)
        t = MathTex(r"t").next_to(dot_move, UR, buff=0)
        self.play(Create(angle), FadeIn(lable_angle), FadeIn(t))
        self.wait(3)

        groupCircle = VGroup(circle, point, point_text, textA, textA_, dot_move, dot_oscillate, line_connect, line1, line1, phi_angle, phi_lable, angle, lable_angle, t0, t, lineA, dotA, dotA_)
        self.play(groupCircle.animate.to_edge(LEFT))
        self.wait(1)

        formula_x = MathTex(r"x=Acos(\Delta \varphi + \varphi)").to_edge(UP, buff=2).shift(RIGHT*2)
        formula_x2 = MathTex(r"x=Acos(\omega t + \varphi)").to_edge(UP, buff=2).shift(RIGHT*2)
        self.play(Write(formula_x))
        self.wait(1)
        rect_surround = Rectangle(height=0.7, width=0.8, color=YELLOW).to_edge(UP, buff=1.9).shift(RIGHT*2.6)
        self.play(Create(rect_surround))
        self.wait(0.5)
        self.play(Uncreate(rect_surround))
        self.play(TransformMatchingTex(formula_x, formula_x2))
        rect_surround_x = SurroundingRectangle(formula_x2, stroke_color = YELLOW)
        self.play(Create(rect_surround_x))
        self.wait(1.5)
        formula_v = MathTex(r"v=x'=-\omega A sin(\omega t + \varphi)").next_to(formula_x2, DOWN, buff=1).align_to(formula_x2, LEFT)
        rect_surround_v = SurroundingRectangle(formula_v, stroke_color = YELLOW)
        formula_a = MathTex(r"a=v'=-\omega^2 A cos(\omega t + \varphi)").next_to(formula_v, DOWN, buff=1).align_to(formula_x2, LEFT)
        rect_surround_a = SurroundingRectangle(formula_a, stroke_color = YELLOW)
        self.play(Write(formula_v))
        self.play(Create(rect_surround_v))
        self.wait(1)
        self.play(Write(formula_a))
        self.play(Create(rect_surround_a))
        self.wait(3)



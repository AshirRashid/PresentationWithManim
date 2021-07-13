from manim import *
import numpy as np
import math

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

logo = ImageMobject('logo.png')

C = {   'background_color': GRAY_A,
        'regular': GRAY_E,
        'dot': RED_C,
        'emphasis': RED_E,
        'emphasis2': PURPLE_D,
        'emphasis3': TEAL_D,
    }

svgs = {
    'plastic_bottle': SVGMobject('plastic_bottle.svg').scale(2),
    'no': SVGMobject('no.svg').scale(2),
    'industry1': SVGMobject('industry1.svg').scale(1.1),
    'industry2': SVGMobject('industry2.svg').scale(1.1),
    'warehouse': SVGMobject('warehouse.svg').scale(1.1),
    'shop': SVGMobject('shop.svg').scale(1.1),
    'plastic': SVGMobject('plastic.svg').scale(1.3),
    'land_pollution': SVGMobject('land_pollution.svg'),
    'water_pollution': SVGMobject('water_pollution.svg'),
    'health_hazard': SVGMobject('health_hazard.svg'),
    'marine_life_threat': SVGMobject('marine_life_threat.svg'),
    'fire_resistant': SVGMobject('fire_resistant.svg'),
    'fast_time': SVGMobject('fast_time.svg'),
    'energy_efficient': SVGMobject('energy_efficient.svg'),
    'clean_earth': SVGMobject('clean_earth.svg'),
    'animal_ingestion': SVGMobject('animal_ingestion.svg'),
    'animal_ingestion2': SVGMobject('animal_ingestion2.svg'),
    'shredded': SVGMobject('shredded.svg'),
    'shredder': SVGMobject('shredder.svg'),
    'collected': SVGMobject('collected.svg'),
    'hydraulic': SVGMobject('hydraulic.svg'),
    'mold': SVGMobject('mold.svg'),
    'sheets': SVGMobject('sheets.svg'),
    # 'pillars': SVGMobject('pillars.svg'),
    'brick': SVGMobject('brick.svg'),
    'c3_logo': SVGMobject('c3_logo.svg'),
    'wall_comp': VGroup(
            SVGMobject('plastic_wall.svg').shift(LEFT*2),
            MathTex('>').scale(2).set_color(C['regular']),
            SVGMobject('brick_wall.svg').shift(RIGHT*2)
            )
}

class C3(MovingCameraScene):
    def construct(self):
        self.camera.background_color = C['background_color']
        size = Vec2(self.camera.frame.height, self.camera.frame.width)
        self.camera.frame.set(width=20)

        Logo(self)

        Team_and_Project_intro(self)
        clear_frame(self)

        Problem_Intro(self)
        clear_frame(self, 'center')
        Animal_Ingestion(self)

        Solution_Intro(self)
        clear_frame(self)
        
        Advantages(self)
        clear_frame(self, 'center')
        
        Further_Details_of_the_Solution(self)
        Credits(self)

def Logo(self):
    logo = svgs['c3_logo']
    self.play( GrowFromCenter(logo.scale(4)) )
    self.wait()
    self.play( ApplyMethod(logo.shift, 10*UP) )

def Team_and_Project_intro(self):
    self.play( GrowFromCenter(svgs['plastic_bottle']) )
    self.play( GrowFromCenter(svgs['no']) )
    self.wait()
    clear_frame(self, 'center')

    self.play(
        SpinInFromNothing(svgs['industry1'].shift(UP*4)),
        )
    self.play( GrowFromCenter(svgs['plastic'].scale(0.5)) )

    arrow1 = Arrow(
            start=[0, svgs['industry1'].get_bottom()[1], 0],
            end=[0, svgs['plastic'].get_top()[1], 0]
        ).set_color(C['regular'])
    self.play( ArrowAnim(arrow1) )
    self.wait()
    self.play(
        SpinInFromNothing(svgs['industry2'].shift(DOWN*4)),
        SpinInFromNothing(svgs['shop'].shift(RIGHT*5)),
        SpinInFromNothing(svgs['warehouse'].shift(LEFT*5))
        )
    self.wait()

    arrow2 = Arrow(
            start=[0, svgs['plastic'].get_bottom()[1], 0],
            end=[0, svgs['industry2'].get_top()[1], 0]
        ).set_color(C['regular'])
    arrow3 = Arrow(
            start=[svgs['plastic'].get_right()[0], 0, 0],
            end=[svgs['shop'].get_left()[0], 0, 0]
        ).set_color(C['regular'])
    arrow4 = Arrow(
            start=[svgs['plastic'].get_left()[0], 0, 0],
            end=[svgs['warehouse'].get_right()[0], 0, 0]
        ).set_color(C['regular'])
    

    self.play( ArrowAnim(arrow2), ArrowAnim(arrow3), ArrowAnim(arrow4) )
    self.wait(2)

def Problem_Intro(self):
    text1 = Tex('$3.3$ Million Ton').scale(1.5).set_color(C['regular']).shift(UP*1.75)
    text2 = MathTex('\\approx 3000000000 \\rm kg').scale(2).set_color(C['emphasis'])
    self.play( GrowFromCenter(text1) )
    self.wait()
    self.play( GrowFromCenter(text2) )
    self.wait(2)
    clear_frame(self, RIGHT)
    problems_list = ['land_pollution', 'water_pollution', 'health_hazard', 'marine_life_threat']
    grp = VGroup(
        *[ svgs[x].scale(1.5) for x in problems_list ]
        )
    anims = [ GrowFromPoint(svgs[x], ORIGIN) for x in problems_list ]
    grp.arrange_in_grid(rows=2, buff=3)
    for i in range(4):
        self.play(anims[i])
        self.wait(2)

def Solution_Intro(self):
    waste_text = get_text(
        'What if that waste plastic can be put to long-term use?',
        'We propose Reintegrate Plastic', buff=0.7
        ).set_color(C['regular'])
    reintegrating_plastic = get_text('Reintegrate', 'Plastic').shift(UP*0.25, DOWN).scale(0.75).set_color(C['regular'])
    waste_text.shift(UP*4)

    structure = SVGMobject('structure.svg')
    structure.shift(RIGHT*8, DOWN)
    plastic_waste = SVGMobject('plastic_waste.svg')
    plastic_waste.shift(LEFT*8, DOWN)

    arrow1 = Arrow(
        start=[plastic_waste.get_right()[0], -1, 0],
        end=[reintegrating_plastic.get_left()[0], -1, 0],
        ).set_color(C['regular'])
    arrow2 = Arrow(
        start=[reintegrating_plastic.get_right()[0], -1, 0],
        end=[structure.get_left()[0], -1, 0]
        ).set_color(C['regular'])

    self.play( GrowFromCenter(waste_text[0]) )
    self.wait(2)
    self.play( GrowFromCenter(waste_text[1]) )
    self.wait(2)
    self.play( GrowFromCenter(structure), GrowFromCenter(plastic_waste), GrowFromCenter(reintegrating_plastic) )
    self.play( ArrowAnim(arrow1) )
    self.play( ArrowAnim(arrow2) )
    self.wait(2)

def Advantages(self):
    advantages_list = ['wall_comp', 'fire_resistant', 'fast_time', 'energy_efficient', 'clean_earth']
    grp = VGroup(
        *[ svgs[x].scale(1.3) if x!='wall_comp'else svgs[x] for x in advantages_list ]
        )
    anims = [ GrowFromPoint(svgs[x], ORIGIN) for x in advantages_list ]
    grp[1:].arrange_in_grid(rows=2, buff=5)
    for i in range(5):
        self.play( anims[i] )
        self.wait(2)

def Animal_Ingestion():
    self.play( GrowFromCenter(svgs['animal_ingestion'].scale(2)) )
    self.wait(1)
    self.play( FadeOut(svgs['animal_ingestion']) )
    self.play( GrowFromCenter(svgs['animal_ingestion2'].scale(2)) )
    self.wait(1)
    self.play( FadeOut(svgs['animal_ingestion2']) )

def Further_Details_of_the_Solution(self):
    scale = 1.1
    scale2 = 0.7
    shredded_to = [0, 4, 0]

    collected = svgs['plastic'].shift(LEFT*5.5).scale(scale)
    shredder = svgs['shredder'].scale(scale)
    shredded = svgs['shredded'].scale(scale2).move_to(shredded_to)
    hydraulic = svgs['hydraulic'].scale(scale2).shift(LEFT*5, UP)
    sheets = svgs['sheets'].scale(scale2).shift(LEFT*5, DOWN*2.5)
    mold = svgs['mold'].scale(scale2).shift(RIGHT*5, UP)
    brick = svgs['brick'].scale(scale2).shift(RIGHT*5, DOWN*2.5)
    shredded.save_state()

    shredded.scale( scale/scale2 ).move_to(ORIGIN).shift(RIGHT*5.5).scale(scale)


    arrow1 = Arrow(
            start=[collected.get_right()[0], 0, 0],
            end=[shredder.get_left()[0], 0, 0]
        ).set_color(C['regular'])
    arrow2 = Arrow(
            start=[shredder.get_right()[0], 0, 0],
            end=[shredded.get_left()[0], 0, 0]
        ).set_color(C['regular'])
    arrow4 = Arrow(
            start=[-5, hydraulic.get_bottom()[1], 0],
            end=[-5, sheets.get_top()[1], 0]
        ).set_color(C['regular'])
    arrow6 = Arrow(
            start=[5, mold.get_bottom()[1], 0],
            end=[5, brick.get_top()[1], 0]
        ).set_color(C['regular'])

    bricksnpillars_text = Text('Bricks and Pillars').shift(UP*shredded_to[1], RIGHT*5)
    sheets_text = Text('Sheets').shift(UP*shredded_to[1], LEFT*5)

    self.play(
        GrowFromCenter(collected)
        )
    self.play(
        GrowFromCenter(shredder), ArrowAnim(arrow1),
        GrowFromCenter(shredded), ArrowAnim(arrow2)
        )
    self.play( FadeOut(arrow1), FadeOut(arrow2), FadeOut(collected), FadeOut(shredder) )
    self.play( Restore(shredded) )
    arrow3 = Arrow(
            start=shredded.get_left(),
            end=[-5, hydraulic.get_top()[1], 0]
        ).set_color(C['regular'])
    arrow5 = Arrow(
            start=shredded.get_right(),
            end=[5, mold.get_top()[1], 0]
        ).set_color(C['regular'])

    self.wait()
    self.play( GrowFromCenter(sheets_text), GrowFromCenter(hydraulic) )
    self.play( ArrowAnim(arrow3) )
    self.wait()
    self.play( ArrowAnim(arrow4), GrowFromCenter(sheets) )
    self.wait(3)
    self.play( GrowFromCenter(bricksnpillars_text) )

    self.wait()
    self.play( GrowFromCenter(mold) )
    self.play( ArrowAnim(arrow5) )
    self.wait()
    self.play( ArrowAnim(arrow6), GrowFromCenter(brick) )

def Credits(self):
    text = Text('Thank You for Watching').set_color(C['regular'])
    tex = Tex(
    r'''
    \begin{flushleft}
    Audio By: Shayan Sheikh and Hoor Khalid
    \\
    Video By: Ashir Rashid
    \\
    Made Using: ManimCE
    \\
    Edited Using: OpenShot
    \\
    Art From: https://www.flaticon.com/
    \end{flushleft}'''

    ).set_color(C['regular']).scale(1.3)
    self.play( GrowFromCenter(text.shift(UP*3.5)) )
    self.play( GrowFromCenter(tex) )

def clear_frame(self, trans_dir=RIGHT):
    if trans_dir == 'center':
        self.play( *[ShrinkToCenter(x) for x in self.mobjects] )
    else:
        self.play( *[ApplyMethod(x.shift, trans_dir*20) for x in self.mobjects] )
    self.remove( *self.mobjects )

class Text(Text):
    def __init__(self, string):
        super(Text, self).__init__(string)
        self.set_color(C['regular'])

def get_text(*strings, buff=0.25):
    prev = Text(strings[0])
    grp = VGroup(prev)
    for string in strings[1:]:
        current = Text(string)
        current.next_to(prev, DOWN, buff=buff)
        grp.add(current)
        prev = current
    return grp

def ArrowAnim(arrow):
    start = arrow.get_start()
    return ReplacementTransform( Arrow(start=start, end=start), arrow )

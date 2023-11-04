from manim import *

def fade_out(scene: Scene):
    animations = []
    for mobject in scene.mobjects:
        animations.append(FadeOut(mobject))
    scene.play(*animations)

class CombineScene(Scene):
    def construct(self):
        scenes = [] # TODO: Add scenes
        for scene in scenes:
            scene.construct(self)
            fade_out(self)

from manimlib import *


def create_dice_face_3d(i):
    square = Square3D()
    texture_fn = f"media/dice_faces/trimmed-diceface000{i}.png"
    texture = TexturedSurface(square, texture_fn)
    return texture


def create_dice_face(i):
    from PIL import Image
    img_mobject = ImageMobject((f"media/dice_faces/diceface000{i}.png"))

    return img_mobject
    return ImageMobject(texture_fn)


def create_dice():
    faces = {
        i: create_dice_face_3d(i)
        for i in range(1, 7)
    }
    faces[1].shift(IN)
    faces[6].shift(OUT)

    faces[2].rotate(PI/2, UP).shift(LEFT)
    faces[5].rotate(PI/2, UP).shift(RIGHT)



    faces[3].rotate(PI/2, RIGHT).shift(UP)
    faces[4].rotate(PI/2, RIGHT).shift(DOWN)

    for face in faces.values():
        face.mesh = SurfaceMesh(face)
        face.mesh.set_stroke(WHITE, 4, opacity=.5)
    return [*faces.values(), *[face.mesh for face in faces.values()]]



class GamesOfDice(Scene):
    def construct(self):
        faces = {i: create_dice_face(i).scale(0.2) for i in range(1, 7)}
        for i, face in enumerate(faces.values()):
            face.shift(i*DOWN)
            self.add(face)


class SurfaceExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }


    def construct(self):
        # Set perspective
        frame = self.camera.frame
        # frame.set_euler_angles(
        #     theta=-30 * DEGREES,
        #     phi=70 * DEGREES,
        # )
        dice = create_dice()
        for face in dice:
            self.add(face)

        self.play(*[
            ApplyMethod(face.rotate_about_origin, PI/3, UP+IN)
            for face in dice]
        )


        self.play(*[
            ApplyMethod(face.shift, 2*RIGHT)
            for face in dice]
        )


        for _ in range(10):
            self.play(*[
                ApplyMethod(face.rotate_about_origin, PI/3, UP+RIGHT)
                for face in dice]
            )

            self.wait(0.1)

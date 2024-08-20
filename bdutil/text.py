from build123d import Text, Axis, Pos, Compound

def SafeText(text, size, *args, **kwargs):
    modded_text = f"█ {text} █"
    faces = Text(modded_text, size, *args, **kwargs)
    faces = faces.faces().sort_by(Axis.X)[1:-1]

    return Compound(faces)


def MultiText(text, size, *args, **kwargs):
    lines = text.strip().split("\n")

    parts = SafeText(lines[0], size, *args, **kwargs)
    for i, line in enumerate(lines[1:]):
        if line.strip() == "":
            continue
        parts += Pos(0, -(i+1) * size * 1.4) * SafeText(line, size, *args, **kwargs)

    parts = Pos(-parts.bounding_box().center()) * parts 

    return parts
from ink2canvas.svg import Element

class Clippath(Element):

    def __init__(self, command, node, ctx):
        Element.__init__(self)
        
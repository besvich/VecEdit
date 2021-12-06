from xml.etree import ElementTree as ET

from Figures import *


class SVGParser:

    def __init__(self, name, glyph):
        self.name = name
        self.glyph = glyph

    def parse2svg(self, objects, doc):
        for o in objects:
            if isinstance(o, Circle):
                if o.fill_color is None:
                    cf = "none"
                else:
                    cf = "rgb(0, 0, 0)"
                ET.SubElement(doc, 'circle', cx=str(o.x1 - 40), cy=str(o.y1 - 150),
                              r=str(o.rad), stroke="rgb(0, 0, 0)",
                              fill=cf, strokeWidth=str(o.thick))
            elif isinstance(o, Rectangle):
                if o.fill_color is None:
                    cf = "none"
                else:
                    cf = "rgb(0, 0, 0)"
                x1 = min(o.x2, o.x1)
                y1 = min(o.y2, o.y1)
                #ET.SubElement(doc, 'rect', x=str(x1 - 40), y=str(y1 - 150),
                              #width=str(abs(o.x2 - o.x1)), height=str(abs(o.y2 - o.y1)),
                              #stroke="rgb(0, 0, 0)",
                              #strokeWidth=str(o.thick), fill=cf)
            elif isinstance(o, Line):
                ET.SubElement(doc, 'line', x1=str(o.x1 - 40), y1=str(o.y1 - 150),
                              x2=str(o.x2 - 40), y2=str(o.y2 - 150),
                              stroke="rgb(0, 0, 0)",
                              strokeWidth=str(o.thick))
            elif isinstance(o, Hand):
                ET.SubElement(doc, 'g')
                for l in o.lines:
                    ET.SubElement(doc, 'line', x1=str(l.x1 - 40), y1=str(l.y1 - 150),
                                  x2=str(l.x2 - 40), y2=str(l.y2 - 150),
                                  stroke="rgb(0, 0, 0)", width=str(l.thick))
                ET.SubElement(doc, '/g')
            elif isinstance(o, Object):
                ET.SubElement(doc, 'g')
                self.parse2svg(o.figures, doc)
                ET.SubElement(doc, '/g')

    def save2svg(self, painter):

        doc = ET.Element('svg', width=str(painter.width), height=str(painter.height),
                         version='1.1', xmlns='http://www.w3.org/2000/svg')

        ET.SubElement(doc, 'rect', x=str(-1), y=str(-1), width=str(painter.width + 2),
                      height=str(painter.height + 2),
                      fill="none")

        self.parse2svg(painter.objects, doc)

        with open(rf"{self.name}\{self.glyph}.svg", 'w') as f:
            f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
            f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
            f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
            a = str(ET.tostring(doc))
            a = a.replace('strokeWidth', 'stroke-width')
            a = a.replace('<g />', '<g>')
            a = a.replace('</g />', '</g>')
            f.write(a[2: -1])

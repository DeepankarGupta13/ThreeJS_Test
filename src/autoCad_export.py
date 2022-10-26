import ezdxf

from design_studio_app.defaults import (
    PANEL_COLOR, OBSTACLES_COLOR, ROOF_COLOR, HANDRAIL_COLOR, FRAME_COLOR, RAILS_COLOR,
    RAFTERS_COLOR, AC_CABLE_COLOR, SETBACK_COLOR, WALKWAY_COLOR, SAFETYLINE_COLOR,
    DC_STRING_COLOR, MICROINVERTERS_COLOR, PROPERTY_COLOR, OPTIMIZERS_COLOR
)


# Obstacle class contains all the array of objects passed as roof map from design studio
class Obstacles(object):
    class PolygonObstacle(object):
        """Subclass of base class Obstacles to hold polygon obstacle information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class rafters(object):
        """Subclass of base class Obstacles to hold rafters information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class rails(object):
        """Subclass of base class Obstacles to hold rails information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class CylinderObstacle(object):
        """Subclass of base class Obstacles to hold Cylinder obstacle information."""

        def __init__(self, x, y, r, h):
            self.h = h  # height
            self.x = x  # x coordinate of center
            self.y = y  # y coordinate of center
            self.radius = r  # base radius

    class WalkWays(object):
        """Subclass of base class Obstacles to hold Walkway information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class propertyLine(object):
        """Subclass of base class Obstacles to hold PropertyLine information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class handrail(object):
        """Subclass of base class Obstacles to hold handrail information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class acCable(object):
        """Subclass of base class Obstacles to hold acCable information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class safetyline(object):
        """Subclass of base class Obstacles to hold safetyline information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class dcString(object):
        """Subclass of base class Obstacles to hold dcString information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class microinverters(object):
        """Subclass of base class Obstacles to hold microinverter information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class optimizers(object):
        """Subclass of base class Obstacles to hold optimizers information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class setbacks(object):
        """Subclass of base class Obstacles to hold setbacks information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class outer_setbacks(object):
        """Subclass of base class Obstacles to hold outer edges of setbacks information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class zero_setbacks(object):
        """Subclass of base class Obstacles to hold closed polygon for faces with zero setbacks."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class parapets(object):
        """Subclass of base class Obstacles to hold parapet information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class extras(object):
        """Subclass of base class Obstacles to hold parapet information."""

        def __init__(self, coordinates):
            self.coordinates = coordinates

    class ground(object):
        """Subclass of base class Obstacles to hold parapet information."""

        def __init__(self, width, height, coordinates):
            self.coordinates = coordinates
            self.width = width
            self.height = height

    # constructor

    def __init__(self, coordinates, polygon_obstacles, cylinder_obstacles, walkways_obstacles, handrail_obstacle,
                 safetyline_obstacle, acCable_obstacle, dcString_obstacle, rafter_obstacles, rail_obstacles,
                 microinverter, optimizer, setback, outer_setback, zero_setback, property_line, parapet, ground, extras
                 ):
        """Base class WalkWaySegment  information."""
        self.coordinates = coordinates
        self.walkways_obstacles = walkways_obstacles
        self.polygon_obstacles = polygon_obstacles
        self.cylinder_obstacles = cylinder_obstacles
        self.handrail_obstacle = handrail_obstacle
        self.safetyline_obstacle = safetyline_obstacle
        self.acCable_obstacle = acCable_obstacle
        self.dcString_obstacle = dcString_obstacle
        self.rafter_obstacles = rafter_obstacles
        self.rail_obstacles = rail_obstacles
        self.microinverter = microinverter
        self.optimizer = optimizer
        self.setback = setback
        self.outer_setback = outer_setback
        self.zero_setback = zero_setback
        self.property_line = property_line
        self.parapet = parapet
        self.groundImage = ground
        self.extra = extras


# panel class
class PanelCoords(object):
    class Frame(object):
        class Panel(object):
            def __init__(self, corners, panel_id):
                self.corners = corners
                self.panel_id = panel_id

        def __init__(self, corners, frame_id, panels):
            self.corners = corners + [corners[0]] + [corners[1]]
            self.frame_id = frame_id
            self.panels = panels

    def __init__(self, frames):
        self.frames = frames


# this class receive JSON from design studio and converts it to Roof Map Obj
def roof_map_to_class(roof_map):
    # Declare all object types arrays
    roof_coordinates = []
    polygon_obs = []
    cylinder_obs = []
    walkway_obs = []
    handrail_obs = []
    safetyline_obs = []
    acCable_obs = []
    dcString_obs = []
    rafter_obs = []
    rail_obs = []
    micro_inverters = []
    optimizers = []
    setbacks = []
    outer_setbacks = []
    zero_setbacks = []
    property_lines = []
    parapets = []
    groundImage = []
    extras = []

    """" Import ground image """
    if 'ground' in roof_map:
        for groundImg in roof_map['ground']:
            ground = Obstacles.ground(groundImg['width'], groundImg['height'], groundImg['vertices'])
            groundImage.append(ground)

    # Populate above defined arrays
    # populate polygons
    if 'polygons' in roof_map:
        for polygon in roof_map['polygons']:
            coordinates = []
            # push each edge
            for edge in polygon['edges']:
                if edge['points'][0] is not None and edge['points'][1] is not None:
                    coordinates.append(edge['points'][0])
            # push first point again in last to complete closed figure
            coordinates.append(coordinates[0])
            # placable are drawn in PV-ROOF and non placable ROOF OBSTRUCTION layers
            if polygon['placable']:
                roof_coordinates.append(coordinates)
            else:
                polygon_obstacle = Obstacles.PolygonObstacle(coordinates)
                polygon_obs.append(polygon_obstacle)

    """ Populate Parapet """
    if 'parapets' in roof_map:
        for parapet in roof_map['parapets']:
            coordinates = []
            """ push each edge """
            for edge in parapet['edges']:
                if edge['points'][0] is not None and edge['points'][1] is not None:
                    coordinates.append(edge['points'][0])
            """ push first point again in last to complete closed figure """
            coordinates.append(coordinates[0])
            parapetObj = Obstacles.parapets(coordinates)
            parapets.append(parapetObj)

    #  populate other obstruction apart from polygon obstructions(above)
    if 'obstructions' in roof_map:
        for obj in roof_map['obstructions']:
            coordinates = []
            # push each vertex
            for edge in obj['edges']:
                if edge['points'][0] is not None and edge['points'][1] is not None:
                    coordinates.append(edge['points'][0])
            coordinates.append(coordinates[0])
            polygon_obstacle = Obstacles.PolygonObstacle(coordinates)
            polygon_obs.append(polygon_obstacle)

    if 'extras' in roof_map:
        for line in roof_map['extras']:
            coordinates = []
            # push each vertex
            for edge in line['edges']:
                if edge['points'][0] is not None and edge['points'][1] is not None:
                    coordinates.append(edge['points'][0])
                    coordinates.append(edge['points'][1])
            extraLines = Obstacles.extras(coordinates)
            extras.append(extraLines)
    # populate setback
    if 'setbacks' in roof_map:
        # setback for faces without zero setback
        for setback in roof_map['setbacks']:
            if len(setback['edges']) > 0:
                coordinates = []
                # push each vertex (NOT-EDGE) 
                for edge in setback['edges']:
                    if edge['points'][0] is not None:
                        coordinates.append(edge['points'][0])
                # push first point again in last to complete closed figure
                coordinates.append(coordinates[0])
                # create object of setback
                setback_path = Obstacles.setbacks(coordinates)
                # push to local array later pushed to roofmap
                setbacks.append(setback_path)

        # outer edges for setback, nth position of outer_setbacks(EDGE) postion is associated
        # with nth position of setbacks
        for setback in roof_map['setbacks']:
            try:
                # check if outer edges exist( to avoid crash on old designs)
                if 'outerEdges' in setback and len(setback['outerEdges']) > 0:
                    outer_coordinates = []
                    for outerEdge in setback['outerEdges']:
                        if edge['points'][0] is not None:
                            outer_coordinates.append(outerEdge['points'][0])
                    # push first point again in last to complete closed figure
                    outer_setback_path = Obstacles.outer_setbacks(outer_coordinates)
                    # populate outersetback coordinats
                    outer_setbacks.append(outer_setback_path)
            except:
                print('Outer setback not sent')

        # zero Steback for making closed polygons
        for setback in roof_map['setbacks']:
            try:
                # check if outer edges exist( to avoid crash on old designs)
                if 'zeroSetback' in setback and len(setback['zeroSetback']) > 0:
                    zero_coordinates = []
                    for edge in setback['zeroSetback']:
                        if edge['points'][0] is not None:
                            zero_coordinates.append(edge['points'][0])
                    # push first point again in last to complete closed figure
                    zero_coordinates.append(zero_coordinates[0])
                    zero_setback_path = Obstacles.zero_setbacks(zero_coordinates)
                    # populate Zerosetback coordinats
                    zero_setbacks.append(zero_setback_path)
            except:
                print('Zero setback not sent')

    # populate rafters
    if 'rafters' in roof_map:
        for rafter in roof_map['rafters']:
            coordinates = []
            # push each point of each edge
            for edge in rafter['edges']:
                # push each point
                for point in edge["points"]:
                    if edge['points'][0] is not None and edge['points'][1] is not None:
                        coordinates.append(point)
                # push first point again in last to complete closed figure
                coordinates.append(coordinates[0])
                rafter_obstacle = Obstacles.rafters(coordinates)
                rafter_obs.append(rafter_obstacle)

                # populate rails
    if 'rails' in roof_map:
        for rail in roof_map['rails']:
            coordinates = []
            for edge in rail['edges']:
                # push point wise
                for point in edge["points"]:
                    if point is not None:
                        coordinates.append(point)
                # push first point again in last to complete closed figure
                coordinates.append(coordinates[0])
                rail_obstacle = Obstacles.rails(coordinates)
                rail_obs.append(rail_obstacle)

                # populate cylinder (cylinder is drawn as polygon obstruction in latest releases)
    if 'cylinders' in roof_map:
        for cylinder in roof_map['cylinders']:
            cylinder_obstacle = Obstacles.CylinderObstacle(
                cylinder['center'][0],
                cylinder['center'][1],
                cylinder['radius'],
                cylinder['height']
            )
            cylinder_obs.append(cylinder_obstacle)

    # populate walkways
    if 'walkways' in roof_map:
        for walkway in roof_map['walkways']:
            coordinates = []
            # push vertex wise
            for edge in walkway['edges']:
                if edge['points'][0] is not None:
                    coordinates.append(edge['points'][0])
            # push first point again in last to complete closed figure
            coordinates.append(coordinates[0])
            walkway_obstacle = Obstacles.WalkWays(coordinates)
            walkway_obs.append(walkway_obstacle)

    # populate handrails
    if 'handrail' in roof_map:
        for handrail in roof_map['handrail']:
            coordinates = []
            # push vertex wise
            for edge in handrail['edges']:
                if edge['points'][0] is not None:
                    coordinates.append(edge['points'][0])
            # push first point again in last to complete closed figure
            coordinates.append(coordinates[0])
            handrail_obstacle = Obstacles.handrail(coordinates)
            handrail_obs.append(handrail_obstacle)

    # po safteyline
    if 'safetyline' in roof_map:
        for safetyline in roof_map['safetyline']:
            coordinates = []
            # push each vertex
            for edge in safetyline['edges']:
                if edge['points'][0] is not None:
                    coordinates.append(edge['points'][0])
            # push first point again in last to complete closed figure
            coordinates.append(coordinates[0])
            safetyline_obstacle = Obstacles.safetyline(coordinates)
            safetyline_obs.append(safetyline_obstacle)

    # populate ac cabels
    if 'acCable' in roof_map:
        for acCable in roof_map['acCable']:
            coordinates = []
            # push vertex by vertex
            for edge in acCable['edges']:
                if edge['points'][0] is not None:
                    coordinates.append(edge['points'][0])
            # push first point again in last to complete closed figure
            coordinates.append(coordinates[0])
            acCable_obstacle = Obstacles.acCable(coordinates)
            acCable_obs.append(acCable_obstacle)

    # populate docstrings
    if 'dcStrings' in roof_map:
        for dcString in roof_map['dcStrings']:
            coordinates = []
            # push edge 
            for edge in dcString:
                if edge is not None:
                    coordinates.append(edge)
            dcString_obstacle = Obstacles.dcString(coordinates)
            dcString_obs.append(dcString_obstacle)

    # populate property line
    if 'property' in roof_map:
        for property in roof_map['property']:
            coordinates = []
            # push each vertex
            for edge in property['edges']:
                if edge['points'][0] is not None:
                    coordinates.append(edge['points'][0])
            # push first point again in last to complete closed figure
            coordinates.append(coordinates[0])
            property_line = Obstacles.propertyLine(coordinates)
            property_lines.append(property_line)

    # populate microinverters
    if 'microInverters' in roof_map:
        for minverter in roof_map['microInverters']:
            minverter.append(minverter[0])
            coordinates = []
            for edge in minverter:
                if edge is not None:
                    coordinates.append(edge)
            microinverter = Obstacles.microinverters(coordinates)
            micro_inverters.append(microinverter)

    # populate optimizers
    if 'optimizers' in roof_map:
        for optimizer in roof_map['optimizers']:
            optimizer.append(optimizer[0])
            coordinates = []
            for edge in optimizer:
                if edge is not None:
                    coordinates.append(edge)
            optimizer = Obstacles.optimizers(coordinates)
            optimizers.append(optimizer)

    # Create obstacle object from the arrays initialized above
    obstacles = Obstacles(
        coordinates=roof_coordinates,
        walkways_obstacles=walkway_obs,
        polygon_obstacles=polygon_obs,
        cylinder_obstacles=cylinder_obs,
        handrail_obstacle=handrail_obs,
        safetyline_obstacle=safetyline_obs,
        acCable_obstacle=acCable_obs,
        dcString_obstacle=dcString_obs,
        rafter_obstacles=rafter_obs,
        rail_obstacles=rail_obs,
        microinverter=micro_inverters,
        optimizer=optimizers,
        setback=setbacks,
        outer_setback=outer_setbacks,
        zero_setback=zero_setbacks,
        property_line=property_lines,
        parapet=parapets,
        ground=groundImage,
        extras=extras,
    )
    return obstacles


def panel_map_to_class(panel_map):
    def frame_to_class(frame, wide, up):
        def get_frame_corners(frame, wide, up):
            frame_corners = list()
            frame_corners.append(frame['panels'][0]['corners'][0])
            frame_corners.append(frame['panels'][wide - 1]['corners'][1])
            frame_corners.append(frame['panels'][(wide * up) - 1]['corners'][2])
            frame_corners.append(frame['panels'][(up - 1) * wide]['corners'][3])
            return frame_corners

        all_panels = []
        for current_panel in frame['panels']:
            p = PanelCoords.Frame.Panel(current_panel['corners'], current_panel['id'])
            p.corners += [current_panel['corners'][0]]
            all_panels.append(p)
        frame_corners = get_frame_corners(frame, wide, up)
        f = PanelCoords.Frame(frame_corners, frame['id'], all_panels)
        return f

    p = []
    for current_field in panel_map:
        wide = current_field['frameSizeWide']
        up = current_field['frameSizeUp']
        all_frames = []
        for current_row in current_field['rows']:
            for current_frame in current_row['frames']:
                if not (current_frame.get("hidden", False)):
                    all_frames.append(frame_to_class(current_frame, wide, up))
        p.append(PanelCoords(all_frames))
    return p


def draw(roofs, panels, filename):
    def draw_roofs(obstacles):
        model_space = drawing.modelspace()

        # create ground image
        for ground in obstacles.groundImage:
            # iterate for each edge and draw it seprately
            # for coords in roof_coordinates:
            coordxy = [[x[0], x[1]] for x in ground.coordinates]
            img_name = filename.replace('.dxf', '.png')
            ground_def = drawing.add_image_def(
                filename=img_name, size_in_pixel=(1024, 1024)
            )
            model_space.add_image(
                insert=(coordxy[1][0], coordxy[1][0]),
                size_in_units=(ground.width, ground.height),
                image_def=ground_def,
                rotation=0
            )

            # create Smartroof Faces
        for roof_coordinates in obstacles.coordinates:
            # iterate for each edge and draw it seprately
            # for coords in roof_coordinates:
            coordxy = [[x[0], x[1]] for x in roof_coordinates]
            model_space.add_lwpolyline(coordxy, dxfattribs={'layer': 'PV-ROOF'})

        # create polygons, cylinders, trees etc
        for polygon_obstacle in obstacles.polygon_obstacles:
            coordsxy = [[x[0], x[1]] for x in polygon_obstacle.coordinates]
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'ROOF OBSTRUCTION'})

        # create polygons, cylinders, trees etc
        for line_obstacle in obstacles.extra:
            coordsxy = [[x[0], x[1]] for x in line_obstacle.coordinates]
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'ROOF OBSTRUCTION'})

        # create parapet for polygons
        for parapet in obstacles.parapet:
            coordsxy = [[x[0], x[1]] for x in parapet.coordinates]
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'ROOF OBSTRUCTION'})

        # Create microinverters
        for microinverter in obstacles.microinverter:
            # remove z
            coords = [(x[0], x[1]) for x in microinverter.coordinates]
            # draw outline around hatch
            lwpoly = model_space.add_lwpolyline(coords, dxfattribs={'layer': 'MICRO INVERTER'})
            # create Solid Hatch for microinverter of defined color of respective layer
            hatch = model_space.add_hatch(color=2, dxfattribs={'layer': 'MICRO INVERTER'})
            # define boundary for hacth
            path = hatch.paths.add_polyline_path(
                coords, is_closed=lwpoly.closed,
            )
            # Associative Hatch/Stick hatch to outline
            hatch.associate(path, [lwpoly])

        # Create optimizers for panels
        for optimizer in obstacles.optimizer:
            # remove z
            coords = [(x[0], x[1]) for x in optimizer.coordinates]
            # draw outline around hatch
            lwpoly = model_space.add_lwpolyline(coords, dxfattribs={'layer': 'OPTIMIZER'})
            # create Solid Hatch for microinverter of defined color of respective layer
            hatch = model_space.add_hatch(color=2, dxfattribs={'layer': 'OPTIMIZER'})
            # define boundary for hacth
            path = hatch.paths.add_polyline_path(
                coords, is_closed=lwpoly.closed,
            )
            # Associative Hatch/Stick hatch to outline
            hatch.associate(path, [lwpoly])

        # create setback for faces
        # this i is to match outer_setbacks with respective setbacks
        i = 0
        for setback in obstacles.setback:
            # create Shaded Hatch for setback
            setbackHatch = model_space.add_hatch(color=4, dxfattribs={'layer': 'FIRE SETBACK'})
            # draw outline for setbackby removing z and defining boundary for setback
            if (len(obstacles.outer_setback) != 0):
                coords = [[x[0], x[1]] for x in obstacles.outer_setback[i].coordinates]
            else:
                coords = [[x[0], x[1]] for x in obstacles.coordinates[i]]
            setbackHatch.paths.add_polyline_path(
                coords,
                is_closed=True,
                flags=ezdxf.const.BOUNDARY_PATH_EXTERNAL,
            )
            # draw inside for setback by removing z and defining boundary for setback
            inside_coords = [[x[0], x[1]] for x in setback.coordinates]
            model_space.add_lwpolyline(inside_coords, dxfattribs={'layer': 'FIRE SETBACK'})
            setbackHatch.paths.add_polyline_path(
                inside_coords,
                is_closed=True,
                flags=ezdxf.const.BOUNDARY_PATH_OUTERMOST,
            )
            # define hatch properties
            setbackHatch.set_pattern_fill('ANSI31', scale=0.050, angle=297.89, color=4)
            # increase ppointer to point for correct outline point
            i = i + 1

        # create lwpolygon and for ZERO SETBACK
        for setback in obstacles.zero_setback:
            # draw outline around hatch
            lwpoly = model_space.add_lwpolyline(setback.coordinates, dxfattribs={'layer': 'FIRE SETBACK'})
            # draw hatch
            hatch = model_space.add_hatch(color=4, dxfattribs={'layer': 'FIRE SETBACK'})
            # remove z and define boundary for setback
            coords = [(x[0], x[1]) for x in setback.coordinates]
            path = hatch.paths.add_polyline_path(
                coords, is_closed=lwpoly.closed,
            )
            # Associative Hatch/Stick hatch to outline
            hatch.associate(path, [lwpoly])
            # define hatch properties
            hatch.set_pattern_fill('ANSI31', scale=0.050, angle=297.89, color=4)

        # create lwpolygon and for rafters
        for rafter_obstacle in obstacles.rafter_obstacles:
            # remove z
            coordsxy = [[x[0], x[1]] for x in rafter_obstacle.coordinates]
            # draw
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'Rafters'})

        # create rails
        for rail_obstacle in obstacles.rail_obstacles:
            # remove z as ezdxf adds bulge instead of z
            coordsxy = [[x[0], x[1]] for x in rail_obstacle.coordinates]
            # draw polyline
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'ROOF-RAIL'})

        # create cylinder [for now cylinders come as polygon_obstacle ]
        for cylinder_obstacle in obstacles.cylinder_obstacles:
            # create circle with center and radius
            model_space.add_circle([cylinder_obstacle.x, cylinder_obstacle.y], cylinder_obstacle.radius,
                                   dxfattribs={'layer': 'ROOF OBSTRUCTION'})

        # create walkway polyline
        for walkway_obstacle in obstacles.walkways_obstacles:
            # remove z
            coordsxy = [[x[0], x[1]] for x in walkway_obstacle.coordinates]
            # draw
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'walkway_layout'})

        # create handrail polyline
        for handrail_obstacle in obstacles.handrail_obstacle:
            # remove z
            coordsxy = [[x[0], x[1]] for x in handrail_obstacle.coordinates]
            # draw
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'handrail_layout'})

        # create propertyline polyline
        for property in obstacles.property_line:
            # uknwr8
            coordsxy = [[x[0], x[1]] for x in property.coordinates]
            # aha
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'PROPERTY'})

        # create safetyline polyline
        for safetyline_obstacle in obstacles.safetyline_obstacle:
            # remove Z
            coordsxy = [[x[0], x[1]] for x in safetyline_obstacle.coordinates]
            #  draw polyline
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'safetyline_layout'})

        # create acCables
        for acCable_obstacle in obstacles.acCable_obstacle:
            # remove z axis
            coordsxy = [[x[0], x[1]] for x in acCable_obstacle.coordinates]
            # create polyline
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'acCable_layout'})

        # create dc Stings polyline
        for dcString_obstacle in obstacles.dcString_obstacle:
            # remove bulging z from points
            coordsxy = [[x[0], x[1]] for x in dcString_obstacle.coordinates]
            # draw polyline
            model_space.add_lwpolyline(coordsxy, dxfattribs={'layer': 'dcString_layout'})

        return drawing

    def draw_panels(array):
        i = 0
        # get model space
        model_space = drawing.modelspace()
        for arr in array:
            for frame in arr.frames:
                i = i + 1
                if FRAME_COLOR != -1:
                    # for frames with panel
                    for panel in frame.panels:
                        # remove z and draw polyline
                        coords_xy = [(x[0], x[1]) for x in panel.corners]
                        model_space.add_lwpolyline(coords_xy, dxfattribs={'layer': 'MODULE'})

        return drawing

    drawing = ezdxf.new('AC1015')
    # Setting default measurement unit to meters
    drawing.header['$INSUNITS'] = 6  # Meters

    # Making layers with specific colors
    drawing.layers.new(name="MODULE", dxfattribs={'color': PANEL_COLOR})
    drawing.layers.new(name="ROOF OBSTRUCTION", dxfattribs={'color': OBSTACLES_COLOR})
    drawing.layers.new(name="FIRE SETBACK", dxfattribs={'color': SETBACK_COLOR})
    drawing.layers.new(name="walkway_layout", dxfattribs={'color': WALKWAY_COLOR})
    drawing.layers.new(name="PV-ROOF", dxfattribs={'color': ROOF_COLOR})
    drawing.layers.new(name="handrail_layout", dxfattribs={'color': HANDRAIL_COLOR})
    drawing.layers.new(name="safetyline_layout", dxfattribs={'color': SAFETYLINE_COLOR})
    drawing.layers.new(name="acCable_layout", dxfattribs={'color': AC_CABLE_COLOR})
    drawing.layers.new(name="dcString_layout", dxfattribs={'color': DC_STRING_COLOR})
    drawing.layers.new(name="Rafters", dxfattribs={'color': RAFTERS_COLOR})
    drawing.layers.new(name="ROOF-RAIL", dxfattribs={'color': RAILS_COLOR})
    drawing.layers.new(name="MICRO INVERTER", dxfattribs={'color': MICROINVERTERS_COLOR})
    drawing.layers.new(name="OPTIMIZER", dxfattribs={'color': OPTIMIZERS_COLOR})
    drawing.layers.new(name="PROPERTY", dxfattribs={'color': PROPERTY_COLOR})

    # Adding objects to drawing
    drawing = draw_roofs(roofs)
    drawing = draw_panels(panels)
    drawing.saveas(filename)
    return 1


def main(instance):
    # get object sent from design studio
    roofs = roof_map_to_class(instance.scene["roofMap"])
    # create panel object
    panels = panel_map_to_class(instance.scene["panelMap"])

    # create file name 
    filename = str(instance.reference_id) + '.dxf'

    # make and return dxf file
    draw(roofs, panels, filename=filename)
    return filename

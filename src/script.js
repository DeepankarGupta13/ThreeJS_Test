import {
    DxfWriter,
    point3d,
    HatchPolylineBoundary,
    HatchEdgesTypeData,
    point2d,
    vertex,
    HatchBoundaryPaths,
    pattern,
    HatchPredefinedPatterns,
    LWPolylineFlags,
    PolylineFlags,
    gradient,
    GradientType,
} from "@tarikjabiri/dxf";
import { saveAs } from 'file-saver';
import { Colors, LayerFlags } from "@tarikjabiri/dxf";

const dxf = new DxfWriter();

function main() {
    // drawPolyLine();
    // addLeader();
    // drawLine();
    // addUnits();
    // drawText();
    // addLayer();
    drawHatch();
    // To get the dxf string just call the stringify() method
    const dxfString = dxf.stringify();
    save(dxfString);
}

function addLeader() {
    const vertices = [
        {
            point: point2d(0, 0, 0),
        },
        {
            point: point2d(1, 1, 0),
        },
    ];
    const leader = dxf.addLeader(vertices);
    dxf.addLayer("Blue", Colors.Blue, "Continuous");
    leader.layerName = 'Blue';
}

function drawPolyLine() {
    const vertices = [
        {
            point: point2d(0, 0, 0),
        },
        {
            point: point2d(100, 100, 0),
        },
        {
            point: point2d(100, 100, 0),
        },
        {
            point: point2d(100, 200, 0),
        },
        {
            point: point2d(100, 200, 0),
        },
        {
            point: point2d(0, 300, 0),
        },
    ];
    console.log('vertices: ', vertices);
    dxf.addLWPolyline(vertices, {
        flags: LWPolylineFlags.Closed,
    });
}

function drawLine() {
    const line = dxf.addLine(point3d(0, 0, 0), point3d(100, 100, 0), {lineType: 'AXES'});
}

function addUnits() {
    const header = dxf.header.setVariable('$INSUNITS', { 70: 6 });
    console.log('header: ', header);
}

function drawArc() {
    const myArc = dxf.addArc(point3d(0, 0, 0), 10, 0, 45);
    myArc.layerName = 'hey there';
    console.log('myArc: ', myArc);
}

function drawText() {
    const text = dxf.addText(point3d(20, 20, 0), 1, 'GGWP', {
        rotation: 30,
        horizontalAlignment: 1,
        verticalAlignment: 2,
    })
    text.secondAlignmentPoint = point3d(20, 20, 0);
}

function drawImage() {
    const imgDef = dxf.addImage(
        "door.jpg", // Or the absolute path of the image if it isn't int the same folder.
        "test",
        point3d(462419.04, 576568.45, 0), // Insertion point of the bottomLeft corner of the image.
        1792, // the width of the image
        1280, // the height of the image
        1, // Scale
        0 // rotation
      );
    // imgDef.imgDefReactor = '2F';
    // console.log('imgDefReactor: ', imgDefReactor);
    console.log('imgDef: ', imgDef);
}

function drawDimension() {
    const dim = dxf.addAlignedDim(point3d(0, 0, 0), point3d(100, 100, 0))
    console.log('dim: ', dim);
}

function addLayer() {
    const layer = dxf.addLayer("hey there", Colors.Red, "Continuous");
    console.log('layer: ', layer);
    dxf.addLayer("YashRao", Colors.Green, "Continuous");
}

//added block in this function
function drawCircle() {
    // dxf.addCircle(point3d(0, 0, 0), 10);
    // or
    dxf.addCircle(point3d(0, 0, 0), 5, {layerName: 'hey there'});
    const options = {
        layerName : 'hey there',
    }
    const myCircle = dxf.addCircle(point3d(0, 0, 0), 10, options);
    const myBlock = dxf.addBlock("myBlock");
    myBlock.addCircle(point3d(0, 0, 0), 20).layerName = 'YashRao';
    myBlock.addLine(point3d(0, 0, 0), point3d(0, 20, 0)).layerName = 'YashRao';
    console.log('myBlock: ', myBlock);

    // Inserting the block
    dxf.addInsert(myBlock.name, point3d(0, 0, 0));
    myCircle.layerName = 'hey there'
    console.log('HEYY THERE',  myCircle.layerName);
    console.log('myCircle: ', myCircle);
    const gg = (options === null || options === void 0 ? void 0 : options.layerName) || '0'
    console.log('gg: ', gg);
    console.log('type of gg: ', typeof(gg));
}

function drawHatch() {
    const polyline = new HatchPolylineBoundary();
    polyline.add(vertex(0, 0));
    polyline.add(vertex(0, 20));
    polyline.add(vertex(10, 20));
    polyline.add(vertex(10, 0));

    const polyline1 = new HatchPolylineBoundary();
    polyline1.add(vertex(1, 1));
    polyline1.add(vertex(1, 9));
    polyline1.add(vertex(9, 9));
    polyline1.add(vertex(9, 1));

    const polyline2 = new HatchPolylineBoundary();
    polyline2.add(vertex(1, 13));
    polyline2.add(vertex(1, 19));
    polyline2.add(vertex(9, 19));
    polyline2.add(vertex(9, 13));


    // const edges = new HatchEdgesTypeData();
    // edges.addLineEdgeData(point2d(0, 0), point2d(0, 10000));
    // edges.addLineEdgeData(point2d(0, 10000), point2d(10000, 10000));
    // edges.addLineEdgeData(point2d(10000, 10000), point2d(10000, 0));
    // edges.addLineEdgeData(point2d(10000, 0), point2d(0, 0));

    const boundary = new HatchBoundaryPaths();
    // Add the defined path
    boundary.addPolylineBoundary(polyline, PolylineFlags.External);
    boundary.addPolylineBoundary(polyline1, PolylineFlags.Outermost);
    boundary.addPolylineBoundary(polyline2, PolylineFlags.Outermost);

    // const mysolid = pattern({
    //     name: HatchPredefinedPatterns.ANSI31,
    //     scale: 0.05,
    //     angle: 287.89,
    //     // Other properties you can define optionally
    //     // angle?: number;
    //     // scale?: number;
    //     // double?: boolean;
    // });

    const mysolid = gradient({
        firstColor: 2,
        secondColor: 1,
        type: GradientType.CYLINDER,
    })

    const hatch = dxf.addHatch(boundary, mysolid);
    console.log('hatch: ', hatch);
}

function save(dxfString) {
    // console.log('dxfString: ', dxfString);
    const blobData = new Blob([dxfString], { type: 'text/plain' });
    saveAs(blobData, `test.dxf`);
}

main();
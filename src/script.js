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
} from "@tarikjabiri/dxf";
import { saveAs } from 'file-saver';
import { Colors, LayerFlags } from "@tarikjabiri/dxf";

const dxf = new DxfWriter();

function main() {
    drawText();
    addLayer();
    drawArc();
    line();
    addImage();
    // To get the dxf string just call the stringify() method
    const dxfString = dxf.stringify();
    save(dxfString);
}

function line() {
    const axesLType = dxf.addLType("AXES", "_ _ ", [1, -1, 1, -1]); 
    const line = dxf.addLine(point3d(0, 0, 0), point3d(100, 100, 0), {lineType: 'AXES'});
    line.layerName = 'YashRao'
}

function drawArc() {
    const myArc = dxf.addArc(point3d(0, 0, 0), 10, 0, 45);
    myArc.layerName = 'hey there';
    console.log('myArc: ', myArc);
}

function drawText() {
    const text = dxf.addText(point3d(20, 20, 0), 10, 'GGWP', {
        rotation: 30,
        relativeXScaleFactor: 2,
    })
    console.log('text: ', text);
}

function addImage() {
    const imgDef = dxf.addImage(
        "test.png", // Or the absolute path of the image if it isn't int the same folder.
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
    polyline.add(vertex(0, 10000));
    polyline.add(vertex(10000, 10000));
    polyline.add(vertex(10000, 0));

    const edges = new HatchEdgesTypeData();
    edges.addLineEdgeData(point2d(0, 0), point2d(0, 10000));
    edges.addLineEdgeData(point2d(0, 10000), point2d(10000, 10000));
    edges.addLineEdgeData(point2d(10000, 10000), point2d(10000, 0));
    edges.addLineEdgeData(point2d(10000, 0), point2d(0, 0));

    const boundary = new HatchBoundaryPaths();
    // Add the defined path
    boundary.addPolylineBoundary(polyline);

    const mysolid = pattern({
        name: HatchPredefinedPatterns.ANSI31,
        // Other properties you can define optionally
        // angle?: number;
        // scale?: number;
        // double?: boolean;
    });

    const hatch = dxf.addHatch(boundary, mysolid);
    console.log('hatch: ', hatch);
}

function save(dxfString) {
    // console.log('dxfString: ', dxfString);
    const blobData = new Blob([dxfString], { type: 'text/plain' });
    saveAs(blobData, `test.dxf`);
}

main();
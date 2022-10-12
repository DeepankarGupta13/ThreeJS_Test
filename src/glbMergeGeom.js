import './style.css'
import * as THREE from 'three'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { mergeBufferGeometries } from 'three/examples/jsm/utils/BufferGeometryUtils.js';

function main(){
    const canvas = document.querySelector("#c");
    const renderer = new THREE.WebGLRenderer({canvas});

    const camera = new THREE.PerspectiveCamera(75,2,0.1,1000);
    camera.position.z = 3;

    const controls = new OrbitControls( camera, renderer.domElement );

    const scene = new THREE.Scene();
    {
        var light = new THREE.AmbientLight(0xffffff);
        scene.add(light);

        const color = 0xFFFFFF;
        const intensity = 1;
        const light1 = new THREE.PointLight(color, intensity);
        light1.position.z = camera.position.z + 5;
        scene.add(light1);

        const hemiLight = new THREE.HemisphereLight( 0x0000ff, 0x00ff00, 0.6 );
        hemiLight.color.setHSL( 0.6, 1, 0.6 );
        hemiLight.groundColor.setHSL( 0.095, 1, 0.75 );
        hemiLight.position.set( 0, 50, 0 );
        scene.add(hemiLight)

        const directionalLight = new THREE.DirectionalLight( 0xffffff, 10 );
        scene.add( directionalLight );
    }

    function applyVertexColors( geometry, color ) {
        var position = geometry.attributes.position;
        var colors = [];
        for ( var i = 0; i < position.count; i ++ ) {
            colors.push( color.r, color.g, color.b );
        }
        geometry.setAttribute( 'color', new THREE.Float32BufferAttribute( colors, 3 ) );
    }

    const loader = new GLTFLoader();
    loader.load('Stick.glb', function ( gltf )
    {
        const geometries = [];
        const matrix = new THREE.Matrix4();
        console.log('gltf.scene.children[0].children[0].children[0].children[0].children: ', gltf.scene.children[0].children[0].children[0].children[0].children);
        const sword = gltf.scene;
        const meshGroup = sword.children[0].children[0].children[0].children[0];
        meshGroup.children.forEach(mesh => {
            console.log('mesh: ', mesh);
            let geometry = mesh.geometry.clone();
            geometry.colorsNeedUpdate = true
            applyVertexColors( geometry, mesh.material.color );
            matrix.compose(mesh.position, mesh.quaternion, mesh.scale);
            geometry.applyMatrix4(matrix);
            geometries.push(geometry);
        });  // sword 3D object is loaded
        console.log('gltf: ', gltf);
        console.log('sword: ', sword);
        const mergeGeometry = mergeBufferGeometries( geometries );
        var defaultMaterial = new THREE.MeshPhongMaterial({vertexColors: THREE.VertexColors});
        defaultMaterial.vertexColors = true;
        const mergedMesh = new THREE.Mesh( mergeGeometry, defaultMaterial );
        mergedMesh.scale.set(1, 1, 1);
        mergedMesh.position.set(0, 0, 0);
        mergedMesh.rotateZ(90);
        mergedMesh.rotateY(90);
        scene.add(mergedMesh);
    });

    function resizeRendererToDisplaySize(renderer) {
        const canvas = renderer.domElement;
        const width = canvas.clientWidth;
        const height = canvas.clientHeight;
        const needResize = canvas.width !== width || canvas.height !== height;
        if (needResize) {
        renderer.setSize(width, height, false);
        }
        return needResize;
    }

    function render(time) {
        time *= 0.001;
        if (resizeRendererToDisplaySize(renderer)) {
            const canvas = renderer.domElement;
            camera.aspect = canvas.clientWidth / canvas.clientHeight;
            camera.updateProjectionMatrix();
        }
        renderer.render(scene, camera);

        requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
}
main();
import './style.css'
import * as THREE from 'three'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

function main(){
    const canvas = document.querySelector("#c");
    const renderer = new THREE.WebGLRenderer({canvas});

    const camera = new THREE.PerspectiveCamera(75,2,0.1,5);
    camera.position.z = 5;

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

    var loader = new GLTFLoader();
    loader.load('Car.glb', function ( gltf )
    {
        const sword = gltf.scene;  // sword 3D object is loaded
        console.log('gltf: ', gltf);
        console.log('sword: ', sword);
        sword.scale.set(1,1,1);
        sword.position.y = 0;
        scene.add(sword);
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
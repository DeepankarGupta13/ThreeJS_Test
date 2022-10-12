import './style.css';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { mergeBufferGeometries } from 'three/examples/jsm/utils/BufferGeometryUtils.js';

 // once everything is loaded, we run our Three.js stuff.
 function main(){
    const canvas = document.querySelector("#c");
    const renderer = new THREE.WebGLRenderer({canvas});
    
    const camera = new THREE.PerspectiveCamera(75,2,0.1,1000);
    camera.position.z = 30;
    const controls = new OrbitControls( camera, renderer.domElement );
    
    
    const scene = new THREE.Scene();
    
    const obj = new THREE.Object3D();
    //Foot
    const geometry = new THREE.BoxGeometry(1,10,1);
    const material = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
    const cube = new THREE.Mesh( geometry, material );
    cube.position.x-=7.5;
    //scene.add( cube );
    
    
    const geometry1 = new THREE.BoxGeometry(1,10,1);
    const material1 = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
    const cube1 = new THREE.Mesh( geometry1, material1 );
    cube1.position.x+=7.5;
    //scene.add( cube1 );
    
    const geometry2 = new THREE.BoxGeometry(1,8,1);
    const material2 = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
    const cube2 = new THREE.Mesh( geometry2, material2 );
    cube2.position.x-=7.5;
    cube2.position.z+=15;
    cube2.position.y-=1;
    //scene.add( cube2 );
    
    const geometry3 = new THREE.BoxGeometry(1,8,1);
    const material3 = new THREE.MeshBasicMaterial( {color: 0x00ff00} );
    const cube3 = new THREE.Mesh( geometry3, material3 );
    cube3.position.x+=7.5;
    cube3.position.z+=15;
    cube3.position.y-=1;
    //scene.add( cube3 );
    
    //Purlins
    //horizontal
    const geo = new THREE.BoxGeometry(16,1,1);
    const mat = new THREE.MeshBasicMaterial( {color: 0x0000ff} );
    const pur = new THREE.Mesh( geo, mat );
    pur.position.y+=3;
    pur.position.z+=15;
    //scene.add( pur );
    
    const geo1 = new THREE.BoxGeometry(16,1,1);
    const mat1 = new THREE.MeshBasicMaterial( {color: 0x0000ff} );
    const pur1 = new THREE.Mesh( geo1, mat1 );
    pur1.position.y+=5;
    //scene.add( pur1 );
    
    //tilted
    const geo2 = new THREE.BoxGeometry(1,1,16);
    const mat2 = new THREE.MeshBasicMaterial( {color: 0x0000ff} );
    const pur2 = new THREE.Mesh( geo2, mat2 );
    pur2.position.y+=4;
    pur2.position.z+=7.5;
    pur2.position.x-=7.5;
    pur2.rotation.x+=Math.tan(2/15);
    //scene.add( pur2 );
    
    const geo3 = new THREE.BoxGeometry(1,1,16);
    const mat3 = new THREE.MeshBasicMaterial( {color: 0x0000ff} );
    const pur3 = new THREE.Mesh( geo3, mat3 );
    pur3.position.y+=4;
    pur3.position.z+=7.5;
    pur3.position.x+=7.5;
    pur3.rotation.x+=Math.tan(2/15);
    //scene.add( pur3 );
    
    //inside purlins (joist)
    //tilted
    const g = new THREE.BoxGeometry(0.5,0.5,16);
    const m = new THREE.MeshBasicMaterial( {color: 0xff0000} );
    const jos = new THREE.Mesh( g, m );
    jos.position.y+=4;
    jos.position.z+=7.5;
    jos.position.x+=0;
    jos.rotation.x+=Math.tan(2/15);
    
    //horizontal
    const g1 = new THREE.BoxGeometry(15,0.5,0.5);
    const m1 = new THREE.MeshBasicMaterial( {color: 0xff0000} );
    const jos1 = new THREE.Mesh( g1, m1 );
    jos1.position.y+=4;
    jos1.position.z+=7.5;
    
    //diagonal
    const g2 = new THREE.BoxGeometry(0.5,0.5,15*Math.sqrt(2));
    const m2 = new THREE.MeshBasicMaterial( {color: 0xff0000} );
    const jos2 = new THREE.Mesh( g2, m2 );
    jos2.position.y+=4;
    jos2.position.z+=7.5;
    jos2.position.x+=0;
    jos2.rotation.x+=Math.tan(2/15);
    jos2.rotation.y-=Math.PI/4;
    
    const g3 = new THREE.BoxGeometry(0.5,0.5,15*Math.sqrt(2));
    const m3 = new THREE.MeshBasicMaterial( {color: 0xff0000} );
    const jos3 = new THREE.Mesh( g3, m3 );
    jos3.position.y+=4;
    jos3.position.z+=7.5;
    jos3.position.x+=0;
    jos3.rotation.x+=Math.tan(2/15);
    jos3.rotation.y+=Math.PI/4;
    
    //half diagonal inside joist
    const g4 = new THREE.BoxGeometry(0.5,0.5,7.4*Math.sqrt(2));
    const m4 = new THREE.MeshBasicMaterial( {color: 0xff0000} );
    const jos4 = new THREE.Mesh( g4, m4 );
    jos4.position.y+=4.5;
    jos4.position.z+=3.5;
    jos4.position.x+=3.25;
    jos4.rotation.x+=Math.tan(2/15);
    jos4.rotation.y+=Math.PI/4;
    
    const g5 = new THREE.BoxGeometry(0.5,0.5,7.4*Math.sqrt(2));
    const m5 = new THREE.MeshBasicMaterial( {color: 0xff0000} );
    const jos5 = new THREE.Mesh( g5, m5 );
    jos5.position.y+=3.5;
    jos5.position.z+=11.5;
    jos5.position.x-=3.3;
    jos5.rotation.x+=Math.tan(2/15);
    jos5.rotation.y+=Math.PI/4;
    
    const g6 = new THREE.BoxGeometry(0.5,0.5,7.4*Math.sqrt(2));
    const m6 = new THREE.MeshBasicMaterial( {color: 0xff0000} );
    const jos6 = new THREE.Mesh( g6, m6 );
    jos6.position.y+=4.5;
    jos6.position.z+=3.5;
    jos6.position.x-=3.3;
    jos6.rotation.x+=Math.tan(2/15);
    jos6.rotation.y-=Math.PI/4;
    
    const g7 = new THREE.BoxGeometry(0.5,0.5,7.4*Math.sqrt(2));
    const m7 = new THREE.MeshBasicMaterial( {color: 0xff0000} );
    const jos7 = new THREE.Mesh( g7, m7 );
    jos7.position.y+=3.5;
    jos7.position.z+=11.5;
    jos7.position.x+=3.3;
    jos7.rotation.x+=Math.tan(2/15);
    jos7.rotation.y-=Math.PI/4;
    
    //Semi Circle Support to legs and rafters.
    obj.add(cube,cube1,cube2,cube3,pur,pur1,pur2,pur3,jos,jos1,jos2,jos3,jos4,jos5,jos6,jos7);
    var geometries = [];
  
      var matrix = new THREE.Matrix4();
  
    function applyVertexColors( geometry, color ) {
          var position = geometry.attributes.position;
          var colors = [];
          for ( var i = 0; i < position.count; i ++ ) {
              colors.push( color.r, color.g, color.b );
          }
          geometry.setAttribute( 'color', new THREE.Float32BufferAttribute( colors, 3 ) );
      }

    obj.children.forEach((mesh) => {
      console.log(mesh)
      var geometry = mesh.geometry.clone();
      geometry.colorsNeedUpdate = true
      applyVertexColors( geometry, mesh.material.color );
      matrix.compose(mesh.position, mesh.quaternion, mesh.scale);
      geometry.applyMatrix4(matrix);
      geometries.push(geometry);
    })
  
    // console.log('BufferGeometryUtils: ', new BufferGeometryUtils);
    const mergeGeometry = mergeBufferGeometries( geometries );
    console.log('mergeGeometry: ', mergeGeometry);
    var defaultMaterial = new THREE.MeshBasicMaterial({vertexColors: THREE.VertexColors});
    defaultMaterial.vertexColors = true;
    console.log('defaultMaterial: ', defaultMaterial);
    const mergedMesh = new THREE.Mesh( mergeGeometry, defaultMaterial );
    console.log('mergedMesh: ', mergedMesh);
  
    scene.add(mergedMesh);
    
    
    
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
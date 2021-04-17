//Maya ASCII 2020 scene
//Name: BoxRounded.ma
//Last modified: Sun, Apr 18, 2021 12:29:34 AM
//Codeset: 1252
requires maya "2020";
requires "stereoCamera" "10.0";
requires "mtoa" "4.1.1";
requires "stereoCamera" "10.0";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19041)\n";
fileInfo "UUID" "8784BDC8-4174-F697-8EF1-D1ACF2734196";
createNode transform -s -n "persp";
	rename -uid "D03685A4-4A9C-5FFF-6074-D4BF0366F085";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1.6959291613253731 3.8809509998953056 7.1187654965415152 ;
	setAttr ".r" -type "double3" -27.938352729603501 -13.400000000000007 1.2260871514867897e-15 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "94A86C63-4F67-B87C-82E5-D9AF8B2C1447";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 8.2834038039063458;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "EFD5FB66-49E3-D3F3-5A8B-E18C316742F1";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "CAE3F023-46C2-200F-9B91-D1AFF015A854";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "78B89E27-4A57-A7BA-34DB-03BD77BB30F7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "715D33D5-4805-4D6E-68C2-498B2720391C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "4ED15BAD-44D8-60B4-949C-93AD8042D276";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 -0.0035521614982345628 0.060817185106646895 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "D5AAD8FE-4CC6-3B26-FF1A-BFB3499ADCAE";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 5.4846794409654818;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "BoxRounded";
	rename -uid "9AFD5AB7-4ABB-2D66-6948-66BA6D1070CE";
	setAttr ".t" -type "double3" 0 0.15039893751472472 0 ;
	setAttr ".rp" -type "double3" 0 -0.14989631615020699 0 ;
	setAttr ".sp" -type "double3" 0 -0.14989631615020699 0 ;
createNode mesh -n "BoxRoundedShape" -p "BoxRounded";
	rename -uid "98E8989A-4B2F-F9CF-EA59-3B81D14095DA";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.87499994039535522 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 73 ".uvst[0].uvsp[0:72]" -type "float2" 0.375 0 0.5 0 0.625
		 0 0.375 0.083333336 0.5 0.083333336 0.625 0.083333336 0.375 0.16666667 0.5 0.16666667
		 0.625 0.16666667 0.375 0.25 0.5 0.25 0.625 0.25 0.375 0.375 0.5 0.375 0.625 0.375
		 0.375 0.5 0.5 0.5 0.625 0.5 0.375 0.58333331 0.5 0.58333331 0.625 0.58333331 0.375
		 0.66666663 0.5 0.66666663 0.625 0.66666663 0.375 0.74999994 0.5 0.74999994 0.625
		 0.74999994 0.375 0.87499994 0.5 0.87499994 0.625 0.87499994 0.375 0.99999994 0.5
		 0.99999994 0.625 0.99999994 0.875 0 0.75 0 0.875 0.083333336 0.75 0.083333336 0.875
		 0.16666667 0.75 0.16666667 0.875 0.25 0.75 0.25 0.125 0 0.25 0 0.125 0.083333336
		 0.25 0.083333336 0.125 0.16666667 0.25 0.16666667 0.125 0.25 0.25 0.25 0.375 0.25
		 0.5 0.25 0.375 0.375 0.625 0.25 0.625 0.375 0.5 0.5 0.375 0.5 0.625 0.5 0.375 0.25
		 0.5 0.25 0.375 0.375 0.625 0.25 0.625 0.375 0.5 0.5 0.375 0.5 0.625 0.5 0.375 0.74999994
		 0.5 0.74999994 0.375 0.87499994 0.625 0.74999994 0.625 0.87499994 0.5 0.99999994
		 0.375 0.99999994 0.625 0.99999994;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt";
	setAttr ".pt[49]" -type "float3" 0.21484169 0 0.21484169 ;
	setAttr ".pt[50]" -type "float3" 0 0 0.21484169 ;
	setAttr ".pt[52]" -type "float3" 0.21484169 0 0 ;
	setAttr ".pt[53]" -type "float3" -0.21484169 0 0.21484169 ;
	setAttr ".pt[54]" -type "float3" -0.21484169 0 0 ;
	setAttr ".pt[55]" -type "float3" 0 0 -0.21484169 ;
	setAttr ".pt[56]" -type "float3" 0.21484169 0 -0.21484169 ;
	setAttr ".pt[57]" -type "float3" -0.21484169 0 -0.21484169 ;
	setAttr -s 58 ".vt[0:57]"  -1 -0.15000001 1 0 -0.15000001 1 1 -0.15000001 1
		 -1 -0.050000004 1 0 -0.050000004 1 1 -0.050000004 1 -1 0.049999997 1 0 0.049999997 1
		 1 0.049999997 1 -1 0.15000001 1 0 0.15000001 1 1 0.15000001 1 -1 0.15000001 0 1 0.15000001 0
		 -1 0.15000001 -1 0 0.15000001 -1 1 0.15000001 -1 -1 0.050000004 -1 0 0.050000004 -1
		 1 0.050000004 -1 -1 -0.049999997 -1 0 -0.049999997 -1 1 -0.049999997 -1 -1 -0.15000001 -1
		 0 -0.15000001 -1 1 -0.15000001 -1 -1 -0.15000001 0 1 -0.15000001 0 1 -0.050000004 0
		 1 0.049999997 0 -1 -0.050000004 0 -1 0.049999997 0 -1 0.70420897 1 0 0.70420897 1
		 -1 0.70420897 0 1 0.70420897 1 1 0.70420897 0 0 0.70420897 -1 -1 0.70420897 -1 1 0.70420897 -1
		 -0.89724755 0.70420897 0.89724755 0 0.70420897 0.89724755 0 0.70420897 0 -0.89724755 0.70420897 0
		 0.89724755 0.70420897 0.89724755 0.89724755 0.70420897 0 0 0.70420897 -0.89724755
		 -0.89724755 0.70420897 -0.89724755 0.89724755 0.70420897 -0.89724755 -1 -0.15000001 -1
		 0 -0.15000001 -1 0 -0.15000001 0 -1 -0.15000001 0 1 -0.15000001 -1 1 -0.15000001 0
		 0 -0.15000001 1 -1 -0.15000001 1 1 -0.15000001 1;
	setAttr -s 112 ".ed[0:111]"  0 1 0 1 2 0 3 4 1 4 5 1 6 7 1 7 8 1 9 10 0
		 10 11 0 14 15 0 15 16 0 17 18 1 18 19 1 20 21 1 21 22 1 23 24 0 24 25 0 0 3 0 1 4 1
		 2 5 0 3 6 0 4 7 1 5 8 0 6 9 0 7 10 1 8 11 0 9 12 0 11 13 0 12 14 0 13 16 0 14 17 0
		 15 18 1 16 19 0 17 20 0 18 21 1 19 22 0 20 23 0 21 24 1 22 25 0 23 26 0 25 27 0 26 0 0
		 27 2 0 22 28 1 28 5 1 19 29 1 29 8 1 27 28 1 28 29 1 29 13 1 20 30 1 30 3 1 17 31 1
		 31 6 1 26 30 1 30 31 1 31 12 1 9 32 0 10 33 0 32 33 0 12 34 0 32 34 0 11 35 0 33 35 0
		 13 36 0 35 36 0 15 37 0 14 38 0 38 37 0 34 38 0 16 39 0 36 39 0 37 39 0 32 40 0 33 41 0
		 40 41 0 41 42 1 34 43 0 43 42 1 40 43 0 35 44 0 41 44 0 36 45 0 44 45 0 42 45 1 37 46 0
		 42 46 1 38 47 0 47 46 0 43 47 0 39 48 0 45 48 0 46 48 0 23 49 0 24 50 0 49 50 0 50 51 1
		 26 52 0 52 51 1 49 52 0 25 53 0 50 53 0 27 54 0 53 54 0 51 54 1 1 55 0 51 55 1 0 56 0
		 56 55 0 52 56 0 2 57 0 54 57 0 55 57 0;
	setAttr -s 56 -ch 224 ".fc[0:55]" -type "polyFaces" 
		f 4 0 17 -3 -17
		mu 0 4 0 1 4 3
		f 4 1 18 -4 -18
		mu 0 4 1 2 5 4
		f 4 2 20 -5 -20
		mu 0 4 3 4 7 6
		f 4 3 21 -6 -21
		mu 0 4 4 5 8 7
		f 4 4 23 -7 -23
		mu 0 4 6 7 10 9
		f 4 5 24 -8 -24
		mu 0 4 7 8 11 10
		f 4 74 75 -78 -79
		mu 0 4 57 58 13 59
		f 4 80 82 -84 -76
		mu 0 4 58 60 61 13
		f 4 77 85 -88 -89
		mu 0 4 59 13 62 63
		f 4 83 90 -92 -86
		mu 0 4 13 61 64 62
		f 4 8 30 -11 -30
		mu 0 4 15 16 19 18
		f 4 9 31 -12 -31
		mu 0 4 16 17 20 19
		f 4 10 33 -13 -33
		mu 0 4 18 19 22 21
		f 4 11 34 -14 -34
		mu 0 4 19 20 23 22
		f 4 12 36 -15 -36
		mu 0 4 21 22 25 24
		f 4 13 37 -16 -37
		mu 0 4 22 23 26 25
		f 4 94 95 -98 -99
		mu 0 4 65 66 28 67
		f 4 100 102 -104 -96
		mu 0 4 66 68 69 28
		f 4 97 105 -108 -109
		mu 0 4 67 28 70 71
		f 4 103 110 -112 -106
		mu 0 4 28 69 72 70
		f 4 -40 -38 42 -47
		mu 0 4 34 33 35 36
		f 4 -42 46 43 -19
		mu 0 4 2 34 36 5
		f 4 -43 -35 44 -48
		mu 0 4 36 35 37 38
		f 4 -44 47 45 -22
		mu 0 4 5 36 38 8
		f 4 -45 -32 -29 -49
		mu 0 4 38 37 39 40
		f 4 -46 48 -27 -25
		mu 0 4 8 38 40 11
		f 4 38 53 -50 35
		mu 0 4 41 42 44 43
		f 4 40 16 -51 -54
		mu 0 4 42 0 3 44
		f 4 49 54 -52 32
		mu 0 4 43 44 46 45
		f 4 50 19 -53 -55
		mu 0 4 44 3 6 46
		f 4 51 55 27 29
		mu 0 4 45 46 48 47
		f 4 52 22 25 -56
		mu 0 4 46 6 9 48
		f 4 6 57 -59 -57
		mu 0 4 9 10 50 49
		f 4 -26 56 60 -60
		mu 0 4 12 9 49 51
		f 4 7 61 -63 -58
		mu 0 4 10 11 52 50
		f 4 26 63 -65 -62
		mu 0 4 11 14 53 52
		f 4 -9 66 67 -66
		mu 0 4 16 15 55 54
		f 4 -28 59 68 -67
		mu 0 4 15 12 51 55
		f 4 28 69 -71 -64
		mu 0 4 14 17 56 53
		f 4 -10 65 71 -70
		mu 0 4 17 16 54 56
		f 4 58 73 -75 -73
		mu 0 4 49 50 58 57
		f 4 -61 72 78 -77
		mu 0 4 51 49 57 59
		f 4 62 79 -81 -74
		mu 0 4 50 52 60 58
		f 4 64 81 -83 -80
		mu 0 4 52 53 61 60
		f 4 -68 86 87 -85
		mu 0 4 54 55 63 62
		f 4 -69 76 88 -87
		mu 0 4 55 51 59 63
		f 4 70 89 -91 -82
		mu 0 4 53 56 64 61
		f 4 -72 84 91 -90
		mu 0 4 56 54 62 64
		f 4 14 93 -95 -93
		mu 0 4 24 25 66 65
		f 4 -39 92 98 -97
		mu 0 4 27 24 65 67
		f 4 15 99 -101 -94
		mu 0 4 25 26 68 66
		f 4 39 101 -103 -100
		mu 0 4 26 29 69 68
		f 4 -1 106 107 -105
		mu 0 4 31 30 71 70
		f 4 -41 96 108 -107
		mu 0 4 30 27 67 71
		f 4 41 109 -111 -102
		mu 0 4 29 32 72 69
		f 4 -2 104 111 -110
		mu 0 4 32 31 70 72;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".de" 1;
	setAttr ".bw" 3;
	setAttr ".dr" 3;
	setAttr ".dsm" 2;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "5CAA702D-4611-77E9-92D8-1D9DC74CB3AB";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "31579BC7-42D4-1986-54E8-9092F1AF4810";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "82C28F68-49E0-8447-D2BA-549AAA7FF493";
createNode displayLayerManager -n "layerManager";
	rename -uid "F8DCEA9F-410C-D111-A750-90A0D511D080";
createNode displayLayer -n "defaultLayer";
	rename -uid "2FD4BBFA-42A4-E2AF-8DED-18919DD0C875";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "13BE0551-4576-C3C6-B829-9ABAB18473A3";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "5D7C7252-4A34-C8CD-B916-0B8D21AC6289";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "A8719FE0-4FB2-CB92-DAEE-2A8BE24DD948";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode animCurveTA -n "Socle_BoxRounded_rotateX";
	rename -uid "41860570-48BD-9C12-C153-2E93B2BDA58F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTA -n "Socle_BoxRounded_rotateY";
	rename -uid "2C38E4BA-42A7-C132-B743-44A7EB550D01";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTA -n "Socle_BoxRounded_rotateZ";
	rename -uid "7FE755D8-45F6-A40A-D762-C88DB74AACB4";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "BoxRoundedShape.iog" ":initialShadingGroup.dsm" -na;
// End of BoxRounded.ma

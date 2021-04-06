//Maya ASCII 2020 scene
//Name: Ground.ma
//Last modified: Tue, Apr 06, 2021 03:08:31 AM
//Codeset: 1252
requires maya "2020";
requires "stereoCamera" "10.0";
requires -nodeType "aiStandardSurface" "mtoa" "4.1.1";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19041)\n";
fileInfo "UUID" "DB0A0942-4546-74D0-B33F-3F83B58150BC";
createNode transform -s -n "persp";
	rename -uid "3A1BFEAE-4F4B-69CD-929E-75867DC29849";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -69.734300830976565 16.257655239906043 12.045205277328195 ;
	setAttr ".r" -type "double3" -12.938352729603578 -80.200000000000216 9.3430586925148091e-15 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "91E523FF-4CE9-BD6C-DB65-36B7742D78CE";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 72.610405841432907;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -n "Ground_Back";
	rename -uid "5ADC7CD7-4237-2F21-4D7F-2186E9E3B86B";
	setAttr ".rlio[0]" 1 yes 0;
	setAttr ".t" -type "double3" 0 -0.3493490252799436 0.1761458565764098 ;
	setAttr ".rp" -type "double3" -31.971129012101578 16.109040972595079 5.6898898280349481 ;
	setAttr ".sp" -type "double3" -31.971129012101578 16.109040972595079 5.6898898280349481 ;
createNode mesh -n "FOND" -p "Ground_Back";
	rename -uid "01931E89-402A-871C-F734-E5B6EE60AD6F";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.37943306565284729 0.00019311904907226563 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 30 ".uvst[0].uvsp[0:29]" -type "float2" 2.63028359 4.31968641
		 2.62445903 -4.31929874 5.35729074 -4.31929874 5.36311388 4.31968641 2.21141219 -4.31930017
		 2.21723557 4.31968641 1.830809 -4.3192997 1.83663082 4.31968641 1.47831261 -4.31929874
		 1.48413539 4.31968641 1.14845645 -4.3192997 1.1542778 4.31968641 0.83460361 -4.31930017
		 0.84042931 4.31968641 0.52906901 -4.31930017 0.53489155 4.31968641 0.22397459 -4.31929922
		 0.23030792 4.31968641 -4.86254311 4.31968641 -4.86938906 -4.3192997 -1.69037867 -4.3192997
		 -1.68352914 4.31968641 -1.24849808 -4.3192997 -1.24164641 4.31968641 -0.84132868
		 -4.31929874 -0.83447832 4.31968641 -0.46422601 -4.31929874 -0.45737657 4.31968641
		 -0.11134648 -4.3192997 -0.10449731 4.31968641;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".ofb" 1;
	setAttr -s 2 ".pt";
	setAttr ".pt[0]" -type "float3" -1.9073486e-06 0 0 ;
	setAttr ".pt[2]" -type "float3" -1.9073486e-06 0 0 ;
	setAttr -s 30 ".vt[0:29]"  -16.64563751 0.34926033 31.10778046 27.35442352 19.7680645 31.13942337
		 -16.59950256 0.34926033 -31.50745964 7.98165131 0.34926033 -31.48259544 27.35442352 40.30870056 31.13942337
		 27.40078735 40.30870056 -31.47620201 7.93564606 0.34926033 31.13299942 27.40078735 19.7680645 -31.47620201
		 27.21957397 16.66646194 31.13941383 26.81503296 13.83457661 31.13915634 26.14069366 11.27233887 31.13897133
		 25.19667816 8.9798708 31.13858795 23.98317719 6.95700264 31.13819695 22.49976349 5.20390034 31.13781738
		 20.74661255 3.72050762 31.13715172 18.72382355 2.50680256 31.13642502 16.43118286 1.56287384 31.13566399
		 13.86928558 0.88860226 31.1349659 11.03717804 0.48410702 31.13387108 11.083145142 0.48410702 -31.48161125
		 13.91526031 0.88860226 -31.48081398 16.47757721 1.56287384 -31.48001671 18.76988983 2.50680256 -31.47924995
		 20.79283142 3.72050762 -31.47847176 22.54595947 5.20390034 -31.47803688 24.029403687 6.95700264 -31.47743416
		 25.24304962 8.9798708 -31.47725487 26.18716431 11.27233887 -31.47680092 26.8612442 13.83457661 -31.47654915
		 27.26609039 16.66646194 -31.47646141;
	setAttr -s 43 ".ed[0:42]"  2 0 0 0 6 0 6 3 0 3 2 0 7 1 0 1 4 0 4 5 0
		 5 7 0 6 18 0 18 19 0 19 3 0 18 17 0 17 20 0 20 19 0 17 16 0 16 21 0 21 20 0 16 15 0
		 15 22 0 22 21 0 15 14 0 14 23 0 23 22 0 14 13 0 13 24 0 24 23 0 13 12 0 12 25 0 25 24 0
		 12 11 0 11 26 0 26 25 0 11 10 0 10 27 0 27 26 0 10 9 0 9 28 0 28 27 0 9 8 0 8 29 0
		 29 28 0 8 1 0 7 29 0;
	setAttr -s 56 ".n[0:55]" -type "float3"  1e+20 1e+20 1e+20 1e+20 1e+20
		 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 1e+20 -9.99764442 0.21723001 -0.0049023628 -9.99764442
		 0.21723001 -0.0049023628 -9.99999523 0 -0.0049059391 -9.99999523 0 -0.0049059391
		 -0.21723616 9.99764061 -0.00010416657 -0.9254123 9.95709038 -0.00045606494 -0.9254123
		 9.95709038 -0.00045606494 -0.21723616 9.99764061 -0.00010416657 -0.9254123 9.95709038
		 -0.00045606494 -1.98287475 9.80144024 -0.00097388029 -1.98287475 9.80144024 -0.00097388029
		 -0.9254123 9.95709038 -0.00045606494 -1.98287475 9.80144024 -0.00097388029 -3.18327641
		 9.47980976 -0.0015647411 -3.18327641 9.47980976 -0.0015647411 -1.98287475 9.80144024
		 -0.00097388029 -3.18327641 9.47980976 -0.0015647411 -4.4888196 8.93591022 -0.0022037029
		 -4.4888196 8.93591022 -0.0022037029 -3.18327641 9.47980976 -0.0015647411 -4.4888196
		 8.93591022 -0.0022037029 -5.82124805 8.13099957 -0.0028548241 -5.82123947 8.13099957
		 -0.0028591156 -4.4888196 8.93591022 -0.0022037029 -5.82124805 8.13099957 -0.0028548241
		 -7.071062088 7.071070194 -0.0034668446 -7.071062088 7.071070194 -0.0034668446 -5.82123947
		 8.13099957 -0.0028591156 -7.071062088 7.071070194 -0.0034668446 -8.1309967 5.82123995
		 -0.0039892197 -8.1309967 5.82123995 -0.0039892197 -7.071062088 7.071070194 -0.0034668446
		 -8.1309967 5.82123995 -0.0039892197 -8.93590641 4.48881006 -0.0043787956 -8.93591976
		 4.48881006 -0.0043838024 -8.1309967 5.82123995 -0.0039892197 -8.93590641 4.48881006
		 -0.0043787956 -9.47980022 3.18327999 -0.0046498775 -9.47980022 3.18327999 -0.0046498775
		 -8.93591976 4.48881006 -0.0043838024 -9.47980022 3.18327999 -0.0046498775 -9.80143356
		 1.98287988 -0.0048015118 -9.80143356 1.98287988 -0.0048015118 -9.47980022 3.18327999
		 -0.0046498775 -9.80143356 1.98287988 -0.0048015118 -9.95708466 0.92541003 -0.0048806667
		 -9.95708466 0.92541003 -0.0048806667 -9.80143356 1.98287988 -0.0048015118 -9.95708466
		 0.92541003 -0.0048806667 -9.99764442 0.21723001 -0.0049023628 -9.99764442 0.21723001
		 -0.0049023628 -9.95708466 0.92541003 -0.0048806667;
	setAttr -s 14 -ch 56 ".fc[0:13]" -type "polyFaces" 
		f 4 0 1 2 3
		mu 0 4 18 19 20 21
		f 4 4 5 6 7
		mu 0 4 0 1 2 3
		f 4 8 9 10 -3
		mu 0 4 20 22 23 21
		f 4 11 12 13 -10
		mu 0 4 22 24 25 23
		f 4 14 15 16 -13
		mu 0 4 24 26 27 25
		f 4 17 18 19 -16
		mu 0 4 26 28 29 27
		f 4 20 21 22 -19
		mu 0 4 28 16 17 29
		f 4 23 24 25 -22
		mu 0 4 16 14 15 17
		f 4 26 27 28 -25
		mu 0 4 14 12 13 15
		f 4 29 30 31 -28
		mu 0 4 12 10 11 13
		f 4 32 33 34 -31
		mu 0 4 10 8 9 11
		f 4 35 36 37 -34
		mu 0 4 8 6 7 9
		f 4 38 39 40 -37
		mu 0 4 6 4 5 7
		f 4 41 -5 42 -40
		mu 0 4 4 1 0 5;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".de" 1;
	setAttr ".bw" 3;
	setAttr ".dr" 3;
	setAttr ".dsm" 2;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -s -n "top";
	rename -uid "7FC1DE13-48BA-000D-AB94-558D2818E14B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "9989313A-4093-3D88-F204-0C9539E6E878";
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
	rename -uid "4743F671-4A17-DF2D-E6D9-D998C193337F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "CC6FDC76-4C19-34F6-B187-D984FA2C43B4";
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
	rename -uid "29074865-4180-C43B-6311-0B9D53DEA93D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "34CEB313-4C30-0DF8-6BC8-1F978507D20B";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode materialInfo -n "materialInfo12";
	rename -uid "9A4CBB1B-46B3-74C2-0232-1C9A2CCAFF6C";
createNode shadingEngine -n "aiStandardSurface1SG";
	rename -uid "ACFF51D6-4E65-08E6-A194-FFA828D8670B";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
	setAttr -s 7 ".aovs";
	setAttr ".aovs[0].aov_name" -type "string" "ID";
	setAttr ".aovs[1].aov_name" -type "string" "ObjectID";
	setAttr ".aovs[2].aov_name" -type "string" "Z";
	setAttr ".aovs[3].aov_name" -type "string" "crypto_asset";
	setAttr ".aovs[4].aov_name" -type "string" "occlu";
	setAttr ".aovs[5].aov_name" -type "string" "specular";
	setAttr ".aovs[6].aov_name" -type "string" "specular_direct";
	setAttr ".aal" -type "attributeAlias" {"ai_aov_ID","aiCustomAOVs[0]","ai_aov_ObjectID"
		,"aiCustomAOVs[1]","ai_aov_Z","aiCustomAOVs[2]","ai_aov_crypto_asset","aiCustomAOVs[3]"
		,"ai_aov_occlu","aiCustomAOVs[4]","ai_aov_specular","aiCustomAOVs[5]","ai_aov_specular_direct"
		,"aiCustomAOVs[6]"} ;
createNode aiStandardSurface -n "Sol_toon";
	rename -uid "8413728F-401F-150D-FB92-92AD5982C67D";
	setAttr ".base_color" -type "float3" 0.25015798 0.41958037 0.48199999 ;
	setAttr ".specular" 0;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "FB242637-41E8-0E2C-06FB-31BDC6324F2F";
	setAttr -s 3 ".lnk";
	setAttr -s 3 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "0841AEEB-4DA5-2EA8-8AF1-7A9FDA08A4D3";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "CCF688E8-4DA2-C7AF-F8ED-44A14262D0A1";
createNode displayLayerManager -n "layerManager";
	rename -uid "6CC653B2-401E-0BF2-1363-2194076D79B1";
createNode displayLayer -n "defaultLayer";
	rename -uid "2014D3FE-47DF-C480-0F61-CB8BE1B013EE";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "F4D37275-47CD-B065-D890-8BB76ED8E8F3";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "E95F9027-496E-C2CC-D2CF-66A35AFA8157";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "E4DFFD55-44CE-DF99-989F-EA8CDF3D4383";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av ".unw" 1;
	setAttr -k on ".etw";
	setAttr -k on ".tps";
	setAttr -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 3 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 6 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -s 5 ".aovs";
	setAttr ".aovs[0].aov_name" -type "string" "ID";
	setAttr ".aovs[3].aov_name" -type "string" "specular_direct";
	setAttr ".aovs[4].aov_name" -type "string" "specular";
	setAttr ".aovs[5].aov_name" -type "string" "Z";
	setAttr ".aovs[6].aov_name" -type "string" "crypto_asset";
	setAttr ".aal" -type "attributeAlias" {"ai_aov_ID","aiCustomAOVs[0]","ai_aov_specular_albedo"
		,"aiCustomAOVs[2]","ai_aov_specular_direct","aiCustomAOVs[3]","ai_aov_specular","aiCustomAOVs[4]"
		,"ai_aov_specular_indirect","aiCustomAOVs[5]","ai_aov_Z","aiCustomAOVs[5].aovName"
		,"ai_aov_crypto_asset","aiCustomAOVs[6].aovName"} ;
select -ne :initialParticleSE;
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -s 5 ".aovs";
	setAttr ".aovs[0].aov_name" -type "string" "ID";
	setAttr ".aovs[3].aov_name" -type "string" "specular_direct";
	setAttr ".aovs[4].aov_name" -type "string" "specular";
	setAttr ".aovs[5].aov_name" -type "string" "Z";
	setAttr ".aovs[6].aov_name" -type "string" "crypto_asset";
	setAttr ".aal" -type "attributeAlias" {"ai_aov_ID","aiCustomAOVs[0]","ai_aov_specular_albedo"
		,"aiCustomAOVs[2]","ai_aov_specular_direct","aiCustomAOVs[3]","ai_aov_specular","aiCustomAOVs[4]"
		,"ai_aov_specular_indirect","aiCustomAOVs[5]","ai_aov_Z","aiCustomAOVs[5].aovName"
		,"ai_aov_crypto_asset","aiCustomAOVs[6].aovName"} ;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".outf" 51;
	setAttr ".imfkey" -type "string" "png";
	setAttr ".ifp" -type "string" "jouet08";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w" 3840;
	setAttr -av -k on ".h" 2160;
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar" 1.7777777910232544;
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".vtn" -type "string" "ACES RRT v0.7";
	setAttr ".povt" no;
	setAttr ".otn" -type "string" "ACES RRT v0.7";
	setAttr ".potn" -type "string" "ACES RRT v0.7";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off ".ctrs" 256;
	setAttr -av -k off ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "aiStandardSurface1SG.msg" "materialInfo12.sg";
connectAttr "Sol_toon.msg" "materialInfo12.m";
connectAttr "Sol_toon.msg" "materialInfo12.t" -na;
connectAttr "Sol_toon.out" "aiStandardSurface1SG.ss";
connectAttr "FOND.iog" "aiStandardSurface1SG.dsm" -na;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "aiStandardSurface1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "aiStandardSurface1SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "aiStandardSurface1SG.pa" ":renderPartition.st" -na;
connectAttr "Sol_toon.msg" ":defaultShaderList1.s" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of Ground.ma

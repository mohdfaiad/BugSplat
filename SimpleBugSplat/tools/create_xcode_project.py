#!/usr/bin/python
import os
import sys

# path to the script
script_path        	= os.path.dirname(os.path.realpath(__file__)) + '/'
# path to the project root
project_path		= os.path.realpath(script_path + '..')
# name of the app, based on root name
app_name		   	= os.path.basename(project_path)

if len(sys.argv) > 1:
    app_name = sys.argv[1]


# paths
derived_data_path	    = os.path.join(project_path, 'DerivedData')
bin_dir_path		    = os.path.join(project_path, 'bin')
app_name_path		    = os.path.join(project_path, app_name)
xcode_proj_path         = os.path.join(project_path, app_name + '.xcodeproj')
workspace_settings_path = os.path.join(xcode_proj_path, 'project.xcworkspace')
project_settings_path   = os.path.join(xcode_proj_path, 'project.xcworkspace', 'xcuserdata', os.environ.get("USER") + '.xcuserdatad')


required_paths		= [ derived_data_path, 
						bin_dir_path,
						app_name_path,
						xcode_proj_path,
						workspace_settings_path,
                        project_settings_path,
						]

#files
info_plist 			    = os.path.join(app_name_path, app_name + '-Info.plist')
project_file		    = os.path.join(xcode_proj_path, 'project.pbxproj')
workspace_settings_file = os.path.join(workspace_settings_path, 'contents.xcworkspacedata')
project_settings_file   = os.path.join(xcode_proj_path, 'project.xcworkspace', 'xcuserdata', os.environ.get("USER") + '.xcuserdatad', 'WorkspaceSettings.xcsettings')

print project_settings_file

def create_dirs():
	for p in required_paths:
		if not os.path.exists(p):
			os.makedirs(p)

def create_info_plist():
	info_text = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>en</string>
	<key>CFBundleDisplayName</key>
	<string>${PRODUCT_NAME}</string>
	<key>CFBundleExecutable</key>
	<string>${EXECUTABLE_NAME}</string>
	<key>CFBundleIcons</key>
	<dict>
		<key>CFBundlePrimaryIcon</key>
		<dict>
			<key>CFBundleIconFiles</key>
			<array>
				<string>app_icon_120x120</string>
			</array>
		</dict>
	</dict>
	<key>CFBundleIcons~ipad</key>
	<dict>
		<key>CFBundlePrimaryIcon</key>
		<dict>
			<key>CFBundleIconFiles</key>
			<array>
				<string>app_icon_152x152</string>
				<string>app_icon_76x76</string>
				<string>app_icon_120x120</string>
			</array>
		</dict>
	</dict>
	<key>CFBundleIdentifier</key>
	<string>edu.swinburne.${PRODUCT_NAME:rfc1034identifier}</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundleName</key>
	<string>${PRODUCT_NAME}</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
	<key>CFBundleShortVersionString</key>
	<string>1.0</string>
	<key>CFBundleSignature</key>
	<string>????</string>
	<key>CFBundleVersion</key>
	<string>1.0</string>
	<key>LSRequiresIPhoneOS</key>
	<true/>
	<key>UILaunchImages~ipad</key>
	<array>
		<dict>
			<key>UILaunchImageMinimumOSVersion</key>
			<string>7.0</string>
			<key>UILaunchImageName</key>
			<string>Default-Landscape</string>
			<key>UILaunchImageOrientation</key>
			<string>Landscape</string>
			<key>UILaunchImageSize</key>
			<string>{768, 1024}</string>
		</dict>
		<dict>
			<key>UILaunchImageMinimumOSVersion</key>
			<string>7.0</string>
			<key>UILaunchImageName</key>
			<string>Default-Portrait</string>
			<key>UILaunchImageOrientation</key>
			<string>Portrait</string>
			<key>UILaunchImageSize</key>
			<string>{768, 1024}</string>
		</dict>
	</array>
	<key>UIRequiredDeviceCapabilities</key>
	<array>
		<string>armv7</string>
	</array>
	<key>UIStatusBarHidden</key>
	<true/>
	<key>UISupportedInterfaceOrientations</key>
	<array>
		<string>UIInterfaceOrientationLandscapeLeft</string>
	</array>
	<key>UISupportedInterfaceOrientations~ipad</key>
	<array>
		<string>UIInterfaceOrientationLandscapeLeft</string>
	</array>
	<key>UIViewControllerBasedStatusBarAppearance</key>
	<false/>
	<key>UIApplicationExitsOnSuspend</key>
	<true/>
</dict>
</plist>
	'''
	out_file = open(info_plist, 'w')
	out_file.write(info_text)
	out_file.close();

def create_project_file():
	project_text = '''// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 46;
	objects = {

/* Begin PBXBuildFile section */
		94400574154BAC8E001A70A6 /* MyAppName.app.dSYM in Resources */ = {isa = PBXBuildFile; fileRef = 94400572154BAC8E001A70A6 /* MyAppName.app.dSYM */; };
		944005EE154BB34A001A70A6 /* MyAppName in CopyFiles */ = {isa = PBXBuildFile; fileRef = 94400571154BAC8E001A70A6 /* MyAppName */; };
		94A539B518076E03002AEBD8 /* app_icon_76x76.png in Resources */ = {isa = PBXBuildFile; fileRef = 94A539B218076E03002AEBD8 /* app_icon_76x76.png */; };
		94A539B618076E03002AEBD8 /* app_icon_120x120.png in Resources */ = {isa = PBXBuildFile; fileRef = 94A539B318076E03002AEBD8 /* app_icon_120x120.png */; };
		94A539B718076E03002AEBD8 /* app_icon_152x152.png in Resources */ = {isa = PBXBuildFile; fileRef = 94A539B418076E03002AEBD8 /* app_icon_152x152.png */; };
		94A539BB18076E65002AEBD8 /* Default-568h@2x.png in Resources */ = {isa = PBXBuildFile; fileRef = 94A539BA18076E65002AEBD8 /* Default-568h@2x.png */; };
		94A539BD1807750E002AEBD8 /* Default@2x.png in Resources */ = {isa = PBXBuildFile; fileRef = 94A539BC1807750E002AEBD8 /* Default@2x.png */; };
		94D71117180777820073DE88 /* Default-Landscape.png in Resources */ = {isa = PBXBuildFile; fileRef = 94D71112180777820073DE88 /* Default-Landscape.png */; };
		94D71118180777820073DE88 /* Default-Landscape@2x.png in Resources */ = {isa = PBXBuildFile; fileRef = 94D71113180777820073DE88 /* Default-Landscape@2x.png */; };
		94D71119180777820073DE88 /* Default-Portrait.png in Resources */ = {isa = PBXBuildFile; fileRef = 94D71114180777820073DE88 /* Default-Portrait.png */; };
		94D7111A180777820073DE88 /* Default-Portrait@2x.png in Resources */ = {isa = PBXBuildFile; fileRef = 94D71115180777820073DE88 /* Default-Portrait@2x.png */; };
		94D7111B180777820073DE88 /* Default.png in Resources */ = {isa = PBXBuildFile; fileRef = 94D71116180777820073DE88 /* Default.png */; };
		94F65ED7154BB81C0054D16C /* Resources in CopyFiles */ = {isa = PBXBuildFile; fileRef = 94F65ED5154BB8140054D16C /* Resources */; };
/* End PBXBuildFile section */

/* Begin PBXCopyFilesBuildPhase section */
		9440057B154BAEE0001A70A6 /* CopyFiles */ = {
			isa = PBXCopyFilesBuildPhase;
			buildActionMask = 2147483647;
			dstPath = "";
			dstSubfolderSpec = 6;
			files = (
				944005EE154BB34A001A70A6 /* MyAppName in CopyFiles */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		94F65ED4154BB7DF0054D16C /* CopyFiles */ = {
			isa = PBXCopyFilesBuildPhase;
			buildActionMask = 2147483647;
			dstPath = MyResources;
			dstSubfolderSpec = 7;
			files = (
				94F65ED7154BB81C0054D16C /* Resources in CopyFiles */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXCopyFilesBuildPhase section */

/* Begin PBXFileReference section */
		94400562154BAB95001A70A6 /* MyAppName-Info.plist */ = {isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = "MyAppName-Info.plist"; sourceTree = "<group>"; };
		94400571154BAC8E001A70A6 /* MyAppName */ = {isa = PBXFileReference; lastKnownFileType = "compiled.mach-o.executable"; name = MyAppName; path = bin/MyAppName; sourceTree = SOURCE_ROOT; };
		94400572154BAC8E001A70A6 /* MyAppName.app.dSYM */ = {isa = PBXFileReference; lastKnownFileType = wrapper.dsym; name = MyAppName.app.dSYM; path = bin/MyAppName.app.dSYM; sourceTree = SOURCE_ROOT; };
		94A539B218076E03002AEBD8 /* app_icon_76x76.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = app_icon_76x76.png; path = tools/app_icon_76x76.png; sourceTree = "<group>"; };
		94A539B318076E03002AEBD8 /* app_icon_120x120.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = app_icon_120x120.png; path = tools/app_icon_120x120.png; sourceTree = "<group>"; };
		94A539B418076E03002AEBD8 /* app_icon_152x152.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = app_icon_152x152.png; path = tools/app_icon_152x152.png; sourceTree = "<group>"; };
		94A539BA18076E65002AEBD8 /* Default-568h@2x.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = "Default-568h@2x.png"; path = "tools/Default-568h@2x.png"; sourceTree = "<group>"; };
		94A539BC1807750E002AEBD8 /* Default@2x.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = "Default@2x.png"; path = "tools/Default@2x.png"; sourceTree = "<group>"; };
		94D71112180777820073DE88 /* Default-Landscape.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = "Default-Landscape.png"; path = "tools/Default-Landscape.png"; sourceTree = "<group>"; };
		94D71113180777820073DE88 /* Default-Landscape@2x.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = "Default-Landscape@2x.png"; path = "tools/Default-Landscape@2x.png"; sourceTree = "<group>"; };
		94D71114180777820073DE88 /* Default-Portrait.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = "Default-Portrait.png"; path = "tools/Default-Portrait.png"; sourceTree = "<group>"; };
		94D71115180777820073DE88 /* Default-Portrait@2x.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = "Default-Portrait@2x.png"; path = "tools/Default-Portrait@2x.png"; sourceTree = "<group>"; };
		94D71116180777820073DE88 /* Default.png */ = {isa = PBXFileReference; lastKnownFileType = image.png; name = Default.png; path = tools/Default.png; sourceTree = "<group>"; };
		94E5FBFD18077D1B003BABB0 /* MyAppName.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; name = MyAppName.app; path = "MyAppName.app"; sourceTree = "BUILT_PRODUCTS_DIR"; };
		94F65ED5154BB8140054D16C /* Resources */ = {isa = PBXFileReference; lastKnownFileType = folder; name = Resources; path = ../Resources; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXGroup section */
		9440054B154BAB95001A70A6 = {
			isa = PBXGroup;
			children = (
				94C1016D18076B7F00A9CD0A /* Icons */,
				94400560154BAB95001A70A6 /* MyAppName */,
			);
			sourceTree = "<group>";
		};
		94400560154BAB95001A70A6 /* MyAppName */ = {
			isa = PBXGroup;
			children = (
				94F65ED5154BB8140054D16C /* Resources */,
				94400571154BAC8E001A70A6 /* MyAppName */,
				94400572154BAC8E001A70A6 /* MyAppName.app.dSYM */,
				94400561154BAB95001A70A6 /* Supporting Files */,
			);
			path = MyAppName;
			sourceTree = "<group>";
		};
		94400561154BAB95001A70A6 /* Supporting Files */ = {
			isa = PBXGroup;
			children = (
				94400562154BAB95001A70A6 /* MyAppName-Info.plist */,
			);
			name = "Supporting Files";
			sourceTree = "<group>";
		};
		94C1016D18076B7F00A9CD0A /* Icons */ = {
			isa = PBXGroup;
			children = (
				94D71112180777820073DE88 /* Default-Landscape.png */,
				94D71113180777820073DE88 /* Default-Landscape@2x.png */,
				94D71114180777820073DE88 /* Default-Portrait.png */,
				94D71115180777820073DE88 /* Default-Portrait@2x.png */,
				94D71116180777820073DE88 /* Default.png */,
				94A539BC1807750E002AEBD8 /* Default@2x.png */,
				94A539BA18076E65002AEBD8 /* Default-568h@2x.png */,
				94A539B218076E03002AEBD8 /* app_icon_76x76.png */,
				94A539B318076E03002AEBD8 /* app_icon_120x120.png */,
				94A539B418076E03002AEBD8 /* app_icon_152x152.png */,
			);
			name = Icons;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		94400555154BAB95001A70A6 /* MyAppName */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 9440056E154BAB95001A70A6 /* Build configuration list for PBXNativeTarget "MyAppName" */;
			buildPhases = (
				94400554154BAB95001A70A6 /* Resources */,
				9440057B154BAEE0001A70A6 /* CopyFiles */,
				94F65ED4154BB7DF0054D16C /* CopyFiles */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = MyAppName;
			productName = MyAppName;
			productReference = 94E5FBFD18077D1B003BABB0 /* MyAppName.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		9440054D154BAB95001A70A6 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				LastUpgradeCheck = 0500;
				ORGANIZATIONNAME = "Swinburne University of Technology";
			};
			buildConfigurationList = 94400550154BAB95001A70A6 /* Build configuration list for PBXProject "MyAppName" */;
			compatibilityVersion = "Xcode 3.2";
			developmentRegion = English;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
			);
			mainGroup = 9440054B154BAB95001A70A6;
			productRefGroup = 9440054B154BAB95001A70A6;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				94400555154BAB95001A70A6 /* MyAppName */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		94400554154BAB95001A70A6 /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				94A539BD1807750E002AEBD8 /* Default@2x.png in Resources */,
				94400574154BAC8E001A70A6 /* MyAppName.app.dSYM in Resources */,
				94D71118180777820073DE88 /* Default-Landscape@2x.png in Resources */,
				94D71119180777820073DE88 /* Default-Portrait.png in Resources */,
				94A539B618076E03002AEBD8 /* app_icon_120x120.png in Resources */,
				94A539B518076E03002AEBD8 /* app_icon_76x76.png in Resources */,
				94A539B718076E03002AEBD8 /* app_icon_152x152.png in Resources */,
				94D7111A180777820073DE88 /* Default-Portrait@2x.png in Resources */,
				94A539BB18076E65002AEBD8 /* Default-568h@2x.png in Resources */,
				94D71117180777820073DE88 /* Default-Landscape.png in Resources */,
				94D7111B180777820073DE88 /* Default.png in Resources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		9440056C154BAB95001A70A6 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "iPhone Developer";
				COPY_PHASE_STRIP = NO;
				GCC_C_LANGUAGE_STANDARD = gnu99;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_SYMBOLS_PRIVATE_EXTERN = NO;
				GCC_VERSION = com.apple.compilers.llvm.clang.1_0;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 7.0;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Debug;
		};
		9440056D154BAB95001A70A6 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "iPhone Developer";
				COPY_PHASE_STRIP = YES;
				GCC_C_LANGUAGE_STANDARD = gnu99;
				GCC_VERSION = com.apple.compilers.llvm.clang.1_0;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 7.0;
				OTHER_CFLAGS = "-DNS_BLOCK_ASSERTIONS=1";
				SDKROOT = iphoneos;
				TARGETED_DEVICE_FAMILY = "1,2";
				VALIDATE_PRODUCT = YES;
			};
			name = Release;
		};
		9440056F154BAB95001A70A6 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				INFOPLIST_FILE = "MyAppName/MyAppName-Info.plist";
				PRODUCT_NAME = "$(TARGET_NAME)";
				WRAPPER_EXTENSION = app;
			};
			name = Debug;
		};
		94400570154BAB95001A70A6 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				INFOPLIST_FILE = "MyAppName/MyAppName-Info.plist";
				PRODUCT_NAME = "$(TARGET_NAME)";
				WRAPPER_EXTENSION = app;
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		94400550154BAB95001A70A6 /* Build configuration list for PBXProject "MyAppName" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				9440056C154BAB95001A70A6 /* Debug */,
				9440056D154BAB95001A70A6 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		9440056E154BAB95001A70A6 /* Build configuration list for PBXNativeTarget "MyAppName" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				9440056F154BAB95001A70A6 /* Debug */,
				94400570154BAB95001A70A6 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
/* End XCConfigurationList section */
	};
	rootObject = 9440054D154BAB95001A70A6 /* Project object */;
}
	'''

	project_text = project_text.replace('MyAppName', app_name)

	out_file = open(project_file, 'w')
	out_file.write(project_text)
	out_file.close()

def create_project_settings():
    proj_settings_text = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>BuildLocationStyle</key>
    <string>UseAppPreferences</string>
    <key>CustomBuildLocationType</key>
    <string>RelativeToDerivedData</string>
    <key>DerivedDataCustomLocation</key>
    <string>DerivedData</string>
    <key>DerivedDataLocationStyle</key>
    <string>WorkspaceRelativePath</string>
    <key>IssueFilterStyle</key>
    <string>ShowActiveSchemeOnly</string>
    <key>LiveSourceIssuesEnabled</key>
    <true/>
    <key>SnapshotAutomaticallyBeforeSignificantChanges</key>
    <true/>
    <key>SnapshotLocationStyle</key>
    <string>Default</string>
</dict>
</plist>'''
    out_file = open(project_settings_file, 'w')
    out_file.write(proj_settings_text)
    out_file.close()
    
def create_workspace_settings():
    workspace_settings = '''<?xml version="1.0" encoding="UTF-8"?>
    <Workspace
       version = "1.0">
       <FileRef
          location = "self:%s.xcodeproj">
       </FileRef>
    </Workspace>
    ''' % app_name
    
    out_file = open(workspace_settings_file, 'w')
    out_file.write(workspace_settings)
    out_file.close()
    

def main():
    print '  Creating XCode Project'
    print '  - Using name:', app_name

    create_dirs()
    create_info_plist()
    create_project_file()
    create_workspace_settings()
    create_project_settings()

    print "  XCode Project Created"
    
    
    
if __name__ == '__main__':
    main()

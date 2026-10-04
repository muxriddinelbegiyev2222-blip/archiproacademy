#ifndef MyAppVersion
  #define MyAppVersion "1.0.2"
#endif

#define MyAppName "ARCHIPRO UZ"
#define MyAppPublisher "ARCHIPRO UZ"
#define MyAppExeName "ARCHIPRO UZ.exe"

[Setup]
AppId={{9B13520C-614E-43CA-9C25-45BF7854381A}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} v{#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={localappdata}\Programs\ARCHIPRO UZ
DefaultGroupName=ARCHIPRO UZ

DisableProgramGroupPage=yes
PrivilegesRequired=lowest

OutputDir=release\installer
OutputBaseFilename=ARCHIPRO UZ Setup v{#MyAppVersion}

SetupIconFile=archipro.ico
UninstallDisplayIcon={app}\{#MyAppExeName}

Compression=lzma2
SolidCompression=yes
WizardStyle=modern

CloseApplications=yes
RestartApplications=no

VersionInfoVersion={#MyAppVersion}
VersionInfoCompany=ARCHIPRO UZ
VersionInfoDescription=ARCHIPRO UZ Architecture Academy
VersionInfoProductName=ARCHIPRO UZ
VersionInfoProductVersion={#MyAppVersion}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Ish stolida ARCHIPRO UZ yorlig'ini yaratish"; GroupDescription: "Qo'shimcha vazifalar:"; Flags: unchecked

[Files]
Source: "release\ARCHIPRO_UZ_CLIENT\ARCHIPRO UZ.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ARCHIPRO UZ"; Filename: "{app}\ARCHIPRO UZ.exe"
Name: "{autodesktop}\ARCHIPRO UZ"; Filename: "{app}\ARCHIPRO UZ.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\ARCHIPRO UZ.exe"; Description: "ARCHIPRO UZ dasturini ishga tushirish"; Flags: nowait postinstall skipifsilent

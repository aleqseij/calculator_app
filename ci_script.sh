#!/bin/bash

# �������� ����������
if [ -z "$1" ]; then
  echo "�� ������ ������ ��������, ���������� �� ���� �� ���������� � �����������";
  exit 1
fi

if [ -z "$2" ]; then
  echo "�� ������ ������ ��������, ���������� �� ������ �������";
  exit 1
fi

# ��������� ����������
srcdir=$1
version=$2
inputname=${srcdir##*/}
projname=${inputname}

# ������ ����� ��� �������
echo "�������� ����������: ${srcdir}"
echo "�������� �������: ${projname}"
echo "������: ${version}"

# ��� 1: �������� ����������� ��������� � ������� (��������, Git pull)
cd $srcdir
git pull origin main

# ��� 2: ������ �������
# ����� �� �������� ��� Python �����, ������� main.py, ui.py, calc_operations.py � ������
echo "������ �������..."
python setup.py build  # ��� ����� ������ ���������� ������

# ��� 3: ������ ����-������
echo "������ ����-������..."
python -m unittest calc_test.py  # ������ ������ �� ����������� �����

# ��� 4: �������� �����������
echo "�������� ����������� Inno Setup..."
# ������ ������� Inno Setup
innosetup_script="D:\installer.iss"

# � ������� Inno Setup ����� ������� ���� � ������ �������, � ����� ������
cat > $innosetup_script <<EOF
[Setup]
AppName=$projname
AppVersion=$version
DefaultDirName={pf}\\$projname
OutputDir=Output
OutputBaseFilename=$projname-$version

[Files]
Source: "$srcdir\\main.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "$srcdir\\ui.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "$srcdir\\calc_operations.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "$srcdir\\calc_test.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "$srcdir\\dist\\$projname.exe"; DestDir: "{app}"; Flags: ignoreversion
EOF

# ������ Inno Setup ��� �������� .exe �����������
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" $innosetup_script

# ��� 5: �������� Deb ������
echo "�������� Deb ������..."

# ���������� ��������� ��� Deb ������
mkdir -p deb-package/DEBIAN
mkdir -p deb-package/usr/local/bin
mkdir -p deb-package/usr/local/lib/$projname

# �������� ��� Python ����� � ���������� ������
cp $srcdir/main.py deb-package/usr/local/lib/$projname/
cp $srcdir/ui.py deb-package/usr/local/lib/$projname/
cp $srcdir/calc_operations.py deb-package/usr/local/lib/$projname/
cp $srcdir/calc_test.py deb-package/usr/local/lib/$projname/

# ������� control ���� ��� Deb ������
cat > deb-package/DEBIAN/control <<EOF
Package: $projname
Version: $version
Architecture: amd64
Maintainer: Your Name <skvorodinmihail@gmail.com>
Description: $projname - �����������
Depends: python3
EOF

# ������� deb ����� � ������� dpkg-deb
dpkg-deb --build deb-package

# ��� 6: ��������� ����������
echo "��������� ����������..."
OutputInstaller="Output\\$projname-$version.exe"
if [ -f "$OutputInstaller" ]; then
  $OutputInstaller /S  # ��������� � ����� ������ (silent mode)
else
  echo "������: ������������ ���� �� ������!"
  exit 1
fi

DebPackage="deb-package.deb"
if [ -f "$DebPackage" ]; then
  sudo dpkg -i $DebPackage  # ��������� Deb ������
else
  echo "������: Deb ����� �� ������!"
  exit 1
fi

echo "������� �������� �������."

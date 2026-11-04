Name:		xz-java
Version:	1.12
Release:	1
Summary:	Pure Java implementation of XZ and LZMA compression
Group:		Development/Java
License:	0BSD
URL:		https://tukaani.org/xz/java.html
Source0:	https://github.com/tukaani-project/xz-java/archive/refs/tags/v%{version}.tar.gz#/xz-java-%{version}.tar.gz

BuildArch:	noarch
BuildSystem:	ant
BuildOption:	jar pom

%description
XZ for Java reads and writes the .xz and .lzma formats. Commons Compress
uses it for XZ, LZMA, and 7-Zip.

%prep
%setup -q -n xz-java-%{version}

%install
sysjar install --buildroot %{buildroot} \
	--artifact build/pom/xz.pom:build/jar/xz.jar \
	--file-name xz --link %{name} \
	--filelist .mfiles

%files -f .mfiles
%doc README.md NEWS.md COPYING AUTHORS.md

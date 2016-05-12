Name:       fsck-msdos
Summary:    Fsck-msdos
Version:    1.0.0
Release:    1
Group:      System/Utilities
License:    BSD-2-Clause
Source0:    %{name}-%{version}.tar.gz
Source1:    fsck-msdos.manifest

BuildRequires:  cmake

%description
Fsck-msdosfs tool

%prep
%setup -q

%cmake .

%build
cp %{SOURCE1} .
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%manifest %{name}.manifest
%license LICENSE
%{_bindir}/fsck_msdosfs

%define fontname	Avdira
%define name		fonts-otf-%{fontname}
%define version		3.01
%define release		%mkrel 2

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Avdira fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}.zip
License:	Public Domain
Group:		System/Fonts/True type
Url:		http://users.teilar.gr/~g1951d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	mkfontscale, mkfontdir

%description
Upright is based on the lowercase Greek letters in the typeface used
by Demetrios Damilas for the edition of Isocrates, published in Milan
in 1493. A digital revival was prepared by Ralph P. Hancock for his
Milan (Mediolanum) font in 2000. Italic Greek were designed in 1802 by
Richard Porson (1757 - 1808) and cut by Richard Austin. They were
first used by Cambridge University Press in 1810. Capitals, Latin and
Cyrillic, as well as the complete bold weights, have been designed in
an attempt to create a well-balanced font. The font covers the Windows
Glyph List, Greek Extended, various typographic extras and is
available in regular, italic, bold and bold italic. The regular style
of the font also covers IPA Extensions, Ancient Greek Numbers,
Byzantine and Ancient Greek Musical Notation and several Open Type
features (Case-Sensitive Forms, Small Capitals, Subscript,
Superscript, Numerators, Denominators, Fractions, Old Style Figures,
Historical Forms, Stylistic Alternates, Ligatures).

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 *.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}%{fontdir}
mkfontdir %{buildroot}%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 3.01-2mdv2011.0
+ Revision: 675510
- br fontconfig for fc-query used in new rpm-setup-build

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 3.01-1mdv2011.0
+ Revision: 562730
- import fonts-otf-Avdira


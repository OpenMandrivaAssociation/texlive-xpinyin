Name:		texlive-xpinyin
Version:	2.7
Release:	1
Summary:	Automatically add pinyin to Chinese characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xpinyin
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpinyin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpinyin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xpinyin.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is written to simplify the input of Hanyu Pinyin.
Macros are provided that automatically add pinyin to Chinese
characters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xpinyin
%doc %{_texmfdistdir}/doc/latex/xpinyin
#- source
%doc %{_texmfdistdir}/source/latex/xpinyin

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

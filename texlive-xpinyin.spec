# revision 27121
# category Package
# catalog-ctan /macros/latex/contrib/xpinyin
# catalog-date 2012-07-20 19:39:58 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-xpinyin
Version:	1.1
Release:	2
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
%{_texmfdistdir}/tex/latex/xpinyin/config/xpinyin-map.cfg
%{_texmfdistdir}/tex/latex/xpinyin/xpinyin.sty
%doc %{_texmfdistdir}/doc/latex/xpinyin/README
%doc %{_texmfdistdir}/doc/latex/xpinyin/xpinyin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xpinyin/xpinyin.dtx
%doc %{_texmfdistdir}/source/latex/xpinyin/xpinyin.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Sun Sep 16 2012 Andrey Bondrov <abondrov@mandriva.org> 1.1-2
+ Revision: 816978
- Rebuild for missing packages

* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 813866
- Import texlive-xpinyin
- Import texlive-xpinyin


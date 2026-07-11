%global tl_name xpinyin
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1
Release:	%{tl_revision}.1
Summary:	Automatically add pinyin to Chinese characters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xpinyin
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpinyin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpinyin.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xpinyin.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is written to simplify the input of Hanyu Pinyin. Macros are
provided that automatically add pinyin to Chinese characters.


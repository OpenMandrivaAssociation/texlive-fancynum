Name:		texlive-fancynum
Version:	0.92
Release:	1
Summary:	Typeset numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancynum
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancynum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancynum.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancynum.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A LaTeX package for typesetting numbers, in particular floating
point numbers, such as you find in program output.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fancynum/fancynum.sty
%doc %{_texmfdistdir}/doc/latex/fancynum/CHANGES
%doc %{_texmfdistdir}/doc/latex/fancynum/README
%doc %{_texmfdistdir}/doc/latex/fancynum/aue.txt
%doc %{_texmfdistdir}/doc/latex/fancynum/ctt.txt
%doc %{_texmfdistdir}/doc/latex/fancynum/dbltable.tex
%doc %{_texmfdistdir}/doc/latex/fancynum/examples.tex
%doc %{_texmfdistdir}/doc/latex/fancynum/fancynum.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fancynum/Makefile
%doc %{_texmfdistdir}/source/latex/fancynum/fancynum.dtx
%doc %{_texmfdistdir}/source/latex/fancynum/fancynum.ins
%doc %{_texmfdistdir}/source/latex/fancynum/tables.c

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

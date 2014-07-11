# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fancynum
# catalog-date 2008-04-19 23:11:03 +0200
# catalog-license other-free
# catalog-version 0.92
Name:		texlive-fancynum
Version:	0.92
Release:	8
Summary:	Typeset numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancynum
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancynum.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancynum.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancynum.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for typesetting numbers, in particular floating
point numbers, such as you find in program output.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.92-2
+ Revision: 751757
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.92-1
+ Revision: 718414
- texlive-fancynum
- texlive-fancynum
- texlive-fancynum
- texlive-fancynum


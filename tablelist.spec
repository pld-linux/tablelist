Summary:	High-level Widget Set for Tcl/Tk
Summary(pl):	Zestaw widget�w wysokiego poziomu dla Tcl/Tk
Name:		tablelist
Version:	4.1
Release:	0.9
License:	BSD-like
Group:		Development/Languages/Tcl
Source0:	http://www.nemethi.privat.t-online.de/tablelist/%{name}%{version}.tar.gz
# Source0-md5:	fb0d64bae243d480b6f8c0926dc191e4
URL:		http://www.nemethi.de/
Requires:	tk >= 8.3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	/usr/lib

%description
Tablelist is a library package for Tcl/Tk version 8.0 or higher,
written in pure Tcl/Tk code. It contains:
 - the implementation of the tablelist mega-widget, including a
   general utility module for mega-widgets;
 - a demo script containing a useful procedure that displays the
   configuration options of an arbitrary widget in a tablelist and
   enables you to edit their values interactively;
 - a second demo script, implementing a simple widget browser based on
   a tablelist;
 - a third demo script, showing several ways to improve the appearance
   of a tablelist widget;
 - four further demo scripts, illustrating the interactive cell
   editing with the aid of various widgets from the Tk core and from
   the packages tile, BWidget, Iwidgets, combobox (by Bryan Oakley),
   and Mentry;
 - one further demo script, with a tablelist widget containing
   embedded windows;
 - tile-based counterparts of the above-mentioned demo scripts;
 - tutorial;
 - reference pages in HTML format.

%description -l pl
Tablelist to pakiet biblioteki dla Tcl/Tk w wersji 8.0 lub
p�niejszej, napisany w czystym Tcl/Tk. Zawiera:
 - implementacj� mega-widgetu tablelist, zawieraj�c� modu� og�lnego
   przeznaczenia dla mega-widget�w;
 - skrypt demonstracyjny zawieraj�cy przydatn� procedur� wy�wietlaj�c�
   opcje konfiguracyjne dowolnego widgetu w tablelist i umo�liwiaj�cy
   interaktywn� zmian� ich warto�ci;
 - drugi skrypt demonstracyjny, implementuj�cy prost� przegl�dark�
   widget�w opart� na tablelist;
 - trzeci skrypt demonstracyjny, pokazuj�cy kilka sposob�w poprawienia
   wygl�du widgetu tablelist;
 - cztery dalsze skrypty demonstracyjne, ilustruj�ce interaktywne
   modyfikowanie kom�rek za pomoc� r�nych widget�w z samego Tk oraz
   pakiet�w tile, BWidget, Iwidgets, combobox (Bryana Oakleya) oraz
   Mentry;
 - kolejny skrypt demonstracyjny, z widgetem tablelist zawieraj�cym
   zagnie�d�one okienka;
 - oparte na tile odpowiedniki wy�ej wymienionych skrypt�w
   demonstracyjnych;
 - tutorial;
 - podr�cznik w formacie HTML.

%prep
%setup -q -n %{name}%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name} \
	$RPM_BUILD_ROOT%{_ulibdir}/%{name}%{version}/{images,scripts}

install *.tcl $RPM_BUILD_ROOT%{_ulibdir}/%{name}%{version}
install images/*  $RPM_BUILD_ROOT%{_ulibdir}/%{name}%{version}/images
install scripts/*  $RPM_BUILD_ROOT%{_ulibdir}//%{name}%{version}/scripts
install demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt doc/*
%dir %{_ulibdir}/%{name}%{version}
%{_ulibdir}/%{name}%{version}/*.tcl
%{_ulibdir}/%{name}%{version}/images
%{_ulibdir}/%{name}%{version}/scripts
%{_examplesdir}/%{name}

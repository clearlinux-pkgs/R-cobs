#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cobs
Version  : 1.3.3
Release  : 6
URL      : https://cran.r-project.org/src/contrib/cobs_1.3-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cobs_1.3-3.tar.gz
Summary  : Constrained B-Splines (Sparse Matrix Based)
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-cobs-lib = %{version}-%{release}
Requires: R-SparseM
Requires: R-quantreg
BuildRequires : R-SparseM
BuildRequires : R-quantreg
BuildRequires : buildreq-R

%description
* NOTE:  *.Rout.save  +- ok
** Cobs version 1.2-2, CRAN Date: 2011-04-25: they *.Rout.save are there and +- ok
** Goal: Still get rid of several *.Rout.save  and use  all.equal() etc
** [[0_pt-ex.R]] : first file with sessionInfo() etc:
packageVersions of SparseM, quantreg, cobs and *no* .Rout.save file of course
* Old Note (Apr 28, 2002):  Platform dependence
--------
All the *.Rout-N-save files have been renamed from
*.Rout.save
because the result of these examples depend *very* much
on the exact platform (compiler/machine) used -- unfortunately :

%package lib
Summary: lib components for the R-cobs package.
Group: Libraries

%description lib
lib components for the R-cobs package.


%prep
%setup -q -c -n cobs

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552728905

%install
export SOURCE_DATE_EPOCH=1552728905
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cobs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cobs
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cobs
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  cobs || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cobs/CITATION
/usr/lib64/R/library/cobs/DESCRIPTION
/usr/lib64/R/library/cobs/INDEX
/usr/lib64/R/library/cobs/Meta/Rd.rds
/usr/lib64/R/library/cobs/Meta/data.rds
/usr/lib64/R/library/cobs/Meta/features.rds
/usr/lib64/R/library/cobs/Meta/hsearch.rds
/usr/lib64/R/library/cobs/Meta/links.rds
/usr/lib64/R/library/cobs/Meta/nsInfo.rds
/usr/lib64/R/library/cobs/Meta/package.rds
/usr/lib64/R/library/cobs/NAMESPACE
/usr/lib64/R/library/cobs/R/cobs
/usr/lib64/R/library/cobs/R/cobs.rdb
/usr/lib64/R/library/cobs/R/cobs.rdx
/usr/lib64/R/library/cobs/data/Rdata.rdb
/usr/lib64/R/library/cobs/data/Rdata.rds
/usr/lib64/R/library/cobs/data/Rdata.rdx
/usr/lib64/R/library/cobs/help/AnIndex
/usr/lib64/R/library/cobs/help/aliases.rds
/usr/lib64/R/library/cobs/help/cobs.rdb
/usr/lib64/R/library/cobs/help/cobs.rdx
/usr/lib64/R/library/cobs/help/paths.rds
/usr/lib64/R/library/cobs/html/00Index.html
/usr/lib64/R/library/cobs/html/R.css
/usr/lib64/R/library/cobs/scripts/README
/usr/lib64/R/library/cobs/scripts/roof.R
/usr/lib64/R/library/cobs/scripts/temp.R
/usr/lib64/R/library/cobs/scripts/wind.R
/usr/lib64/R/library/cobs/tests/0_pt-ex.R
/usr/lib64/R/library/cobs/tests/README
/usr/lib64/R/library/cobs/tests/ex1.R
/usr/lib64/R/library/cobs/tests/ex1.Rout-N-save
/usr/lib64/R/library/cobs/tests/ex1Old.Rout-N-save
/usr/lib64/R/library/cobs/tests/ex2-long.R
/usr/lib64/R/library/cobs/tests/ex2-long.Rout-N-save
/usr/lib64/R/library/cobs/tests/ex3.R
/usr/lib64/R/library/cobs/tests/ex3.Rout.save
/usr/lib64/R/library/cobs/tests/multi-constr.R
/usr/lib64/R/library/cobs/tests/multi-constr.Rout.save
/usr/lib64/R/library/cobs/tests/roof.R
/usr/lib64/R/library/cobs/tests/roof.Rout-N-save
/usr/lib64/R/library/cobs/tests/roof.Rout.save
/usr/lib64/R/library/cobs/tests/small-ex.R
/usr/lib64/R/library/cobs/tests/small-ex.Rout.save
/usr/lib64/R/library/cobs/tests/spline-ex.R
/usr/lib64/R/library/cobs/tests/spline-ex.Rout.save
/usr/lib64/R/library/cobs/tests/temp.R
/usr/lib64/R/library/cobs/tests/temp.Rout-N-save
/usr/lib64/R/library/cobs/tests/temp.Rout.save
/usr/lib64/R/library/cobs/tests/wind.R
/usr/lib64/R/library/cobs/tests/wind.Rout-N-save
/usr/lib64/R/library/cobs/util.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/cobs/libs/cobs.so
/usr/lib64/R/library/cobs/libs/cobs.so.avx2
/usr/lib64/R/library/cobs/libs/cobs.so.avx512

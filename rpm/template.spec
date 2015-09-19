Name:           ros-indigo-leg-detector
Version:        1.0.10
Release:        0%{?dist}
Summary:        ROS leg_detector package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/leg_detector
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-bfl
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-image-geometry
Requires:       ros-indigo-laser-filters
Requires:       ros-indigo-laser-geometry
Requires:       ros-indigo-map-laser
Requires:       ros-indigo-people-msgs
Requires:       ros-indigo-people-tracking-filter
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-bfl
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-image-geometry
BuildRequires:  ros-indigo-laser-geometry
BuildRequires:  ros-indigo-people-msgs
BuildRequires:  ros-indigo-people-tracking-filter
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-visualization-msgs

%description
Leg Detector using a machine learning approach to find leg-like patterns of
laser scanner readings.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Sep 19 2015 David V. Lu!! <davidvlu@gmail.com> - 1.0.10-0
- Autogenerated by Bloom

* Tue Sep 01 2015 David V. Lu!! <davidvlu@gmail.com> - 1.0.9-0
- Autogenerated by Bloom

* Wed Dec 10 2014 David V. Lu!! <davidvlu@gmail.com> - 1.0.8-0
- Autogenerated by Bloom


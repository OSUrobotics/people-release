%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-people-velocity-tracker
Version:        1.4.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS people_velocity_tracker package

License:        BSD
URL:            http://ros.org/wiki/people_velocity_tracker
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-easy-markers
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-kalman-filter
Requires:       ros-noetic-leg-detector
Requires:       ros-noetic-people-msgs
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rospy
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-easy-markers
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-kalman-filter
BuildRequires:  ros-noetic-people-msgs
BuildRequires:  ros-noetic-roslaunch
BuildRequires:  ros-noetic-roslib
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rospy
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Track the output of the leg_detector to indicate the velocity of person.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Oct 07 2021 David V. Lu!! <davidvlu@gmail.com> - 1.4.2-1
- Autogenerated by Bloom

* Fri Feb 19 2021 David V. Lu!! <davidvlu@gmail.com> - 1.4.0-1
- Autogenerated by Bloom

* Mon Sep 21 2020 David V. Lu!! <davidvlu@gmail.com> - 1.2.2-1
- Autogenerated by Bloom


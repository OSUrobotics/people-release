Name:           ros-melodic-face-detector
Version:        1.1.1
Release:        0%{?dist}
Summary:        ROS face_detector package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/face_detector
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-actionlib
Requires:       ros-melodic-actionlib-msgs
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-image-geometry
Requires:       ros-melodic-image-transport
Requires:       ros-melodic-message-filters
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-people-msgs
Requires:       ros-melodic-rosbag
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roslib
Requires:       ros-melodic-rospy
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-stereo-image-proc
Requires:       ros-melodic-stereo-msgs
Requires:       ros-melodic-tf
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-actionlib-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-image-geometry
BuildRequires:  ros-melodic-image-transport
BuildRequires:  ros-melodic-message-filters
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-people-msgs
BuildRequires:  ros-melodic-rosbag
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslib
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-stereo-image-proc
BuildRequires:  ros-melodic-stereo-msgs
BuildRequires:  ros-melodic-tf

%description
Face detection in images.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Aug 29 2018 Dan Lazewatsky <dan@lazewatsky.com> - 1.1.1-0
- Autogenerated by Bloom


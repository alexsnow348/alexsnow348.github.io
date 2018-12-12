---
layout: post
title: "OpenCV 3.2 with CodeBlocks IDE Installation in Window 7/8/10"
categories: [Computer Vision]
tag: [OpenCV, C++]
---

This article explained the step by step installation of CodeBlock IDE 16.01 and OpenCV 3.2 for the programming in C++.

**Note:** _MinGW is not supported for OpenCV 3.2._

### Steps
1. Install [**CodeBlocks 16.01**](http://www.codeblocks.org/downloads).
2. Install [**TDM-GCC**](http://tdm-gcc.tdragon.net/download) depending on your machine either 32 bit or 64 bit.
3. Install [**CMake**](https://cmake.org/download/).
4. Install [**OpenCV 3.2**](http://opencv.org/). And extract OpenCV 3.2 under C:\ drive like shown in figure and create **build_codeblocks** new folder.
5. Download [**OpenCV_contrib**](https://github.com/opencv/opencv_contrib) on GitHub and unzip it in the C:\ .

<!-- more -->

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/extractopencv.png" title="Extract File">
  <br>
</p>

After extraction of the OpenCV file, open the CodeBlock to change compiler setting.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/toolchain.png" title="Compiler Setting">
  <br>
</p>


If you have done these two actions, open CMake GUI to build the OpenCV libraries. First, select your folder directory as advised by following figure.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/cmake.png" title="CMake GUI">
  <br>
</p>

Click Configure to select the complier to build as per following figure.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/cmake_generator.png" title="CMake Compiler Select">
  <br>
</p>


After Configuration is sucessfully done, find for opencv -> OPENCV_EXTRA_MODULES_PATH, choose from opencv_contri -> modules folders to install extra modules.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/select_contri.png" title="CMake GUI">
  <br>
</p>

After that click Configure again.
<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/cmake_contri.png" title="CMake GUI">
  <br>
</p>

When configuration  is done, click generate.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/generate_cmake.png" title="CMake GUI">
  <br>
</p>

Now, it is time to build in the CodeBlocks, Open opencv.cbp as shown in figure.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/opencv_project.png" title="CodeBlocks Build">
  <br>
</p>

When project is loaded to the CodeBlocks, click build.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/build_project.png" title="CodeBlocks Build">
  <br>
</p>

After that, you need to rebuild agian by selecting the target to install.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/retarget.png" title="CodeBlocks Build">
  <br>
</p>

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/build_again.png" title="CodeBlocks Build">
  <br>
</p>

If you have done all the steps successfully, then it is time to start coding.

Here is the <a href="https://www.dropbox.com/s/1f1v7vgzv0rrz80/opencv_test.zip?dl=0" target="_blank"><strong>Image and Code </strong></a> to test. Download and unzip it or you can copy the code below to test it.

{% highlight cpp %}
	#include "opencv/cv.h"
	#include "opencv/cv.hpp"
	#include "opencv2/core.hpp"
	#include "opencv/highgui.h"

	using namespace cv;

	int main()
	{
	    cv::Mat image;// new blank image
	    image = cv::imread("beach.jpg", 0);// read GBR Value
	    cv::namedWindow( "Display window", CV_WINDOW_AUTOSIZE );// create a window for display.
	    cv::imshow( "Display window", image );// show our image inside it.
	    cv:: waitKey(0);// wait for a keystroke in the window
	    return 0;
	}
{% endhighlight %}

Now time to create new c++ project in CodeBlocks.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/test.png" title="Testing project">
  <br>
</p>

Right Click to get the project build options.
<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/build_test.png" title="Testing project 1">
  <br>
</p>

After that, select Search directiory -> compiler and add the required directories.
<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/codeblocks_build.png" title="Testing project 2">
  <br>
</p>

Select Search directiory -> linker and add the required directories.
<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/codblock_build_link.png" title="Testing project 3">
  <br>
</p>

Select Linker Setting -> linker and add libopencv_world320.dll.a .

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/codeblock_build_liner.png" title="Testing project 4">
  <br>
</p>

After that click Ok, and you can build and run your project now.

If you get result as shown in following figure, then you have successfully done.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/succss.png" title="Testing project 4">
  <br>
</p>

Enjoy programming with OpenCV!

Adopted From [**Wei-Wen Hsu Tutorial**](https://www.slideshare.net/WeiWenHsu/using-opencv-320-with-codeblocks).

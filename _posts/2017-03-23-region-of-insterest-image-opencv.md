---
layout: post
title: "Region of Interest (ROI) in OpenCV"
categories: [Computer Vision]
tag: [OpenCV, C++]
---

This article explains on how to select region of interest for your image/video analytics. It is very important to know the segmentations you want to analyze for your project. This post will guide you through how to make segmentation using OpenCV with C++ programming.

<strong>Step 1</strong>

Download famous Lenna image  below to test it out.

<!-- more -->

<p align="center">
  <br>
  <img src="/public/img/roi/Lenna.png" title="Lenna Image 512 x 512 ">
  <br>
</p>

Open your code block and create a project and go to your build options.

<p align="center">
  <br>
  <img src="/public/img/opencv_codeblock/build_test.png" title="Build Options">
  <br>
</p>

If you are following how to set build options  OpenCV projects in my previous article, it is the same methods. Select Search directory -> compiler and add the required directories.

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

After you have done that, you are ready to test your ROI. Open the main.cpp file and copy the following code.

{% highlight cpp %}
#include "opencv/cv.h"
#include "opencv/cv.hpp"
#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

using namespace std;
using namespace cv;

int main() {

Mat LoadedImage,

// Just loaded image Lenna.png from project dir to LoadedImage Mat
 LoadedImage = imread("Lenna.png", IMREAD_COLOR);

// This construct Rectangle Rec start at x=100 y=100, width=200 and heigth=200
   Rect Rec(100,100 , 200,200);

//Draw the rectangle into LoadedImage
//Parameters are (into Mat, Rec describe position where to draw rectangle
// Scalar is Color, 1 is thickness, 8 is line type and 0 shift position
   rectangle(LoadedImage, Rec, Scalar(255), 1, 8, 0);

// Show what rectangle
   namedWindow("Draw Rectangle", WINDOW_AUTOSIZE);
   imshow("Draw Rectangle", LoadedImage);
   waitKey(27);
   return 0;
	}
{% endhighlight %}

When you build and run the project, you program is successful if you see the same image as below.

<p align="center">
  <br>
  <img src="/public/img/roi/Step2.JPG" title="Image with ROI ">
  <br>
</p>

Enjoy programming with OpenCV!

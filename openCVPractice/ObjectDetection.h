#pragma once
using namespace cv;
using namespace std;
#include <opencv2\objdetect\objdetect.hpp>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\imgproc\imgproc.hpp>
class ObjectDetection
{
public:
	ObjectDetection();
	~ObjectDetection();
	void detectAndDraw(Mat& img, CascadeClassifier& cascade,
		CascadeClassifier& nestedCascade,
		double scale);
};


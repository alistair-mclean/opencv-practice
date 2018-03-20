#pragma once
#include <opencv2/opencv.hpp>
#include<iostream>
#include<vector>


class ProcessingUtils
{
public:
	ProcessingUtils();
	~ProcessingUtils();
	///Compute the maximum difference vector and index of maximum difference between two images, with respect to row or column traversal. 
	std::pair<std::vector<unsigned int>, std::vector<unsigned int>> ProcessingUtils::Difference(const cv::Mat& compare, bool direction, const cv::Mat& original);

private:

};


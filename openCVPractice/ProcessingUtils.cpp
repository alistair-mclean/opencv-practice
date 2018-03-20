#include "ProcessingUtils.h"

using namespace cv;

ProcessingUtils::ProcessingUtils()
{
}


ProcessingUtils::~ProcessingUtils()
{
}

std::pair<std::vector<unsigned int>, std::vector<unsigned int>> ProcessingUtils::Difference(const Mat & compare, bool direction, const cv::Mat & original)
{
	unsigned int origRows = original.rows;
	unsigned int origCols = original.cols;
	unsigned int compRows = compare.rows;
	unsigned int compCols = compare.cols;
	std::vector<unsigned int> maxDiffValueArray;
	std::vector<unsigned int> maxDiffIndexArray;

	unsigned int maxDiff = 0;
	Vec3b ogPx = 0;
	Vec3b compPx = 0;


	// Define the space in which we will iterate through
	unsigned int maxRows, maxCols;
	if (origRows > compRows)
		maxRows = compRows;
	else maxRows = origRows;
	if (origCols > compCols)
		maxCols = compCols;
	else maxCols = origCols;


	if (direction) {
		// Find the max difference and index location in each col
		for (unsigned int j = 0; j < maxCols; j++) {
			unsigned int newDiff = 0;
			unsigned int location = 0;
			maxDiff = 0;
			for (unsigned int i = 0; i < maxRows; i++) {
				try
				{
					ogPx = original.at<Vec3b>(i, j);
					compPx = compare.at<Vec3b>(i, j);
				}
				catch (cv::Exception& e)
				{
					std::cout << "Exception caught! Unable to assign pixel values" << std::endl;
				}

				// Calculate the absolute relative difference in each color intensity
				int bDiff = abs((int)compPx[0] - (int)ogPx[0]);
				int gDiff = abs((int)compPx[1] - (int)ogPx[1]);
				int rDiff = abs((int)compPx[2] - (int)ogPx[2]);

				// Average of the 3 relative color intensity differences. 
				newDiff = (bDiff + gDiff + rDiff) / 3;
				// Assign a new maxDiff if greate
				if (newDiff > maxDiff)
				{
					maxDiff = newDiff;
					location = i;
				}

			}
			// Push back the location after looking through every value in the col
			maxDiffValueArray.push_back(maxDiff);
			maxDiffIndexArray.push_back(location);
		}
	}
	else {
		// Find the max difference, and index in each row
		unsigned int location = 0;
		for (unsigned int i = 0; i < maxRows; i++) {
			maxDiff = 0;
			int newDiff = 0;
			location = 0;
			for (unsigned int j = 0; j < maxCols; j++) {
				try
				{
					ogPx = original.at<Vec3b>(i, j);
					compPx = compare.at<cv::Vec3b>(i, j);
				}
				catch (Exception& e)
				{
					std::cout << "Exception caught! Unable to assign pixel values" << std::endl;
				}
				// Calculate the absolute relative difference in each color intensity
				int bDiff = abs((int)compPx[0] - (int)ogPx[0]);
				int gDiff = abs((int)compPx[1] - (int)ogPx[1]);
				int rDiff = abs((int)compPx[2] - (int)ogPx[2]);

				// Average of the 3 relative color intensity differences. 
				newDiff = (unsigned)((bDiff + gDiff + rDiff) / 3);

				if (newDiff > maxDiff)
				{
					maxDiff = newDiff;
					location = i;
				}

			}
			// Push back the location after looking through every value in the row
			maxDiffValueArray.push_back(maxDiff);
			maxDiffIndexArray.push_back(location);
		}

	}

	std::pair<std::vector<unsigned int>, std::vector<unsigned int>> value;
	value.first = maxDiffValueArray;
	value.second = maxDiffIndexArray;
	return value;

}





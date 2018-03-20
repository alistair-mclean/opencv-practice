#include "ProcessingUtils.h"
#include <time.h>
const std::string _image1Path = "img1.jpg";
const std::string _image2Path = "img2.jpg";


int main(int argC, char* argV[]) {
	std::string image1 = "";
	std::string image2 = "";
	if (argC < 2) {
		std::cout << "Please enter in the first image name and extension: ";
		std::cin >> image1;
		if (!std::cin)
			std::cin >> image1;
		std::cout << "Please enter in the second image name and extension: ";
		std::cin >> image2;
		if (!std::cin)
			std::cin >> image2;
	}

	if (image1 == "")
		image1 = _image1Path;
	if (image2 == "")
		image2 = _image1Path;
	clock_t t0, t1, t2, t3, t4;
	t0 = clock();
	//Read the file 
	cv::Mat img = cv::imread(image1, CV_LOAD_IMAGE_COLOR);
	cv::Mat img2 = cv::imread(image2, CV_LOAD_IMAGE_COLOR);

	//
	if (!img.data) {
		std::cout << "Error! Could not find the 1st image" << std::endl;
	}
	if (!img2.data) {
		std::cout << "Error! Could not find the 2nd image" << std::endl;
	}

	// Create the display windows
	cv::namedWindow("Display Window", CV_WINDOW_AUTOSIZE);
	cv::imshow("Display Window", img);
	cv::namedWindow("Display Window 2", CV_WINDOW_AUTOSIZE);
	cv::imshow("Display Window 2", img2);

	// Variable declarations
	std::vector<unsigned int> maxDiffValArray;
	std::vector<unsigned int> maxDiffIndexArray;
	std::pair<std::vector<unsigned int>, std::vector<unsigned int>> maxDifferences;
	ProcessingUtils procUtils;

	// ROW OPERATION
	t1 = clock(); // Begin recording time for first operation
	maxDifferences = procUtils.Difference(img, true, img2);
	maxDiffValArray = maxDifferences.first;
	maxDiffIndexArray = maxDifferences.second;
	std::cout << "RESULTS FROM THE ROW OPERATION" << std::endl;
	std::cout << "Differences = ";
	for (unsigned int i = 0; i < maxDiffValArray.size(); i++) {
		std::cout << " " << maxDiffValArray[i];
	}
	std::cout << "\n";
	std::cout << "Indexes = ";
	for (unsigned int i = 0; i < maxDiffIndexArray.size(); i++) {
		std::cout << " " << maxDiffIndexArray[i];
	}
	std::cout << "\n";

	// COLUMN OPERATION
	t2 = clock(); // Record final time for first operation, initial time for second operation
	maxDifferences = procUtils.Difference(img, false, img2);
	maxDiffValArray = maxDifferences.first;
	maxDiffIndexArray = maxDifferences.second;
	t3 = clock(); // Record final time for 2nd operation
	std::cout << "RESULTS FROM THE COLUMN OPERATION" << std::endl;
	std::cout << "Differences = ";
	for (unsigned int i = 0; i < maxDiffValArray.size(); i++) {
		std::cout << " " << maxDiffValArray[i];
	}
	std::cout << "\n";
	std::cout << "Indexes = ";
	for (unsigned int i = 0; i < maxDiffIndexArray.size(); i++) {
		std::cout << " " << maxDiffIndexArray[i];
	}
	std::cout << "\n";



	// Console statements
	float difference((float)t2 - (float)t1);
	std::cout << "The row image processing took: " << difference << " milliseconds." << std::endl;
	difference = (float)t3 - (float)t2;
	std::cout << "The column image processing took: " << difference << " milliseconds." << std::endl;
	t4 = clock();
	difference = (float)t4 - (float)t0;
	std::cout << "The total time elapsed in the program: " << difference << " milliseconds." << std::endl;

	// Wait till the user presses a key to close 
	cv::waitKey(0);
	return 0;
}


/*
 * =====================================================================================
 *
 *       Filename:  problem1.cpp
 *
 *    Description:  Solution to Euler problem one
 *
 *        Version:  1.0
 *        Created:  07/12/2013 09:19:15 AM
 *       Compiler:  gcc
 *
 *         Author:  Andrew Kail
 *
 * =====================================================================================
 */

#include <iostream>
#include <cmath>

int main( int argc, char** argv)
{
    std::cout << "In what range shall we check sir? ";
    int range;
    std::cin >> range;
    std::cout << std::endl << "Aye aye Captain, running through ranges 0 to " << range <<"." << std::endl;

    int counter = 0;
    int sum=0;
    while(counter < range)
    {
        if( ((counter % 3) == 0) || ((counter % 5) == 0))
        {
            sum += counter;
        }
        counter++;
    }

    std::cout << "Captain, the sum is " << sum << std::endl;

    return 0;
}


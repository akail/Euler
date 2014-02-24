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

#pragma 

int main( int argc, char** argv)
{
    int range = 1000;

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


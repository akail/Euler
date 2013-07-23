/*
 * =====================================================================================
 *
 *       Filename:  problem1.cpp
 *
 *    Description:  Solution to Euler problem two
 *
 *        Version:  1.0
 *        Created:  07/12/2013 09:19:15 AM
 *       Compiler:  g++
 *
 *         Author:  Andrew Kail
 *
 * =====================================================================================
 */

#include <iostream>
#include <cmath>


int main( int argc, char** argv)
{
    
    int fib1 = 1;
    int fib2 = 2;
    int fib3 = 3;
    int sum=2;
    int max = 4000000;
//    int max = 100;
    while(fib3 < max)
    {
        fib3 = fib1+fib2;
        if(fib3 > max) break;
        if((fib3 % 2) == 0)
        {
            sum += fib3;
        }
//        std::cout << fib3 << std::endl;

        fib1=fib2;
        fib2=fib3;
    }
    std::cout << "Captain, the sum is " << sum << std::endl;

    return 0;
}


/*
 * =====================================================================================
 *
 *       Filename:  four.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  07/14/2013 12:56:08 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include <iostream>
#include <cstdlib>
#include <cmath>

double mag(int x)
{
    double y = log10( double(x));

    return double(int(y) % 10);
}
    


int main(int argc, char** argv)
{
    int value;
    int max_base;

    for(int i=999; i > 100; i--)
    {
        for(int j=999; j > 100; j--)
        {
            value = i*j;
            max_base = int( pow(double(value),mag(value)));
            
            if( ((value -(value % max_base))/max_base) == value % 10)
            {
                std::cout << value << std::endl;
            }

        }

    }

    return 0;
}

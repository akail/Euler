/*
 * =====================================================================================
 *
 *       Filename:  three.cpp
 *
 *    Description:  Larget prime factor of a number
 *
 *        Version:  1.0
 *        Created:  07/13/2013 03:24:20 PM
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  Andrew Kail   
 *
 * =====================================================================================
 */
#include <iostream>
#include <cmath>
#include <cstdlib>

bool primecheck(long long int value)
{
    long long int maxpf = (value +(value % 2))/2; // maximum factor

    bool prime = true;
    for(long long int i= 2; i< maxpf; i++)
    {

        if( (value % i ) == 0) // if i is a factor of value
        {
            prime = false; // it is not a prime number
            break;
        } 
    }
    
    return prime;
}
// write functions for factor and prime
//
 int main(int argc, char** argv)
{
//    long long int input = atoi(argv[1]);
    long long int input = 600851475143;
            

    // max number is half or half+1
    long long int maxpf = (input + (input % 2))/2;
    if(primecheck(input)){
        std::cerr << "Invalid entry, the value is alread prime: Aborting" << std::endl;
        exit(0);
    }

    // for every number that could be a factor
    for(long long int i = 9000; i > 1; i--)
    {
        // if i is a fator of the input
        if( (input % i) == 0)
        {
           if( primecheck(i) )
           {
               std::cout << "The maximum prime factor is " << i << std::endl;
               break;
           }
        }
    }

    return 0;
}

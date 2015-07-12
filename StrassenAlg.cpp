#include <vector>
#include <iostream>

typedef std::vector<std::vector<int>> vv;
typedef std::vector<int> v;


int size = 4;
using namespace std;
vv classicMultiply(const vv& a, const vv& b)
{
    vv c = vv(size, v(size,0));
    for(int i = 0; i < size; ++i){
        for(int j = 0; j < size; ++j){
            for(int k = 0; k < size; ++k){
                c[i][j] += a[i][k]*b[k][j];
                }
            }
        }
    return c;
}

void printMatrix(const vv& a)
{
    for(int i = 0; i < size; ++i){
        for(int j = 0; j < size; ++j){
            std::cout<<a[i][j]<<" ";
        }
        std::cout<<std::endl;
    }
}


int main(){
    vv a { { 1, 1, 1 },
         { 2, 2, 2 },
         { 3, 3, 3 }};
    
    size = 3;
    printMatrix(a);
    
    vv b = classicMultiply(a,a);
    printMatrix(b);
    
	return 0;
}
#include <vector>
#include <iostream>

typedef std::vector<std::vector<int>> vv;
typedef std::vector<int> v;


using namespace std;
vv classicMultiply(const vv& a, const vv& b)
{
    int size = a.size();
    vv c = vv(size, v(size,0));
    for(int i = 0; i < size; ++i)
    {
        for(int j = 0; j < size; ++j)
        {
            for(int k = 0; k < size; ++k)
            {
                c[i][j] += a[i][k]*b[k][j];
            }
        }
    }
    return c;
}

void printMatrix(const vv& a)
{
    for(int i = 0; i < a.size(); ++i){
        for(int j = 0; j < a.size(); ++j){
            std::cout<<a[i][j]<<" ";
        }
        std::cout<<std::endl;
    }
}

vv add(const vv& a, const vv& b)
{
    int size = a.size();
    vv c = vv(size, v(size,0));
    for(int i = 0; i < size; ++i)
    {
        for(int j = 0; j < size; ++j)
        {
            c[i][j] += a[i][j]*b[i][j];
        }
    }
    return c;
}

vv subMatrix(const vv& a, int x, int y)
{
    int s = a.size();
    vv c = vv(s/2, v(s/2,0));
    if(x<0 || x >1 || y<0 || y >1 )
        return c;
    for (int i = 0 + x*s; i < s/2 + x*s; ++i)
    {
        for (int i = 0 + y*s; i < s/2 + y*s; ++j)
        {
            c[i - x*s][j - y*s] = a[i][j];
        }
    }
    return c;
}


vv generateRandomMatrix(int size, max)
{
    

}

int main(){
    vv a { { 1, 1, 1 },
         { 2, 2, 2 },
         { 3, 3, 3 }};
    
    printMatrix(a);
    
    vv b = classicMultiply(a,a);
    printMatrix(b);
    
	return 0;
}
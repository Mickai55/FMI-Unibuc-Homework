// A C++ program to implement flood fill algorithm
#include<iostream>
using namespace std;

// Dimentions of paint screen
#define M 7
#define N 7

// A recursive function to replace previous color 'prevC' at '(x, y)'
// and all surrounding pixels of (x, y) with new color 'newC' and
void floodFillUtil(int screen[][N], int x, int y, int prevC, int newC)
{
	// Base cases
	if (x < 0 || x >= M || y < 0 || y >= N)
		return;
	if (screen[x][y] != prevC)
		return;

	// Replace the color at (x, y)
	screen[x][y] = newC;

	// Recur for north, east, south and west
	floodFillUtil(screen, x+1, y, prevC, newC);
	floodFillUtil(screen, x-1, y, prevC, newC);
	floodFillUtil(screen, x, y+1, prevC, newC);
	floodFillUtil(screen, x, y-1, prevC, newC);
}

// It mainly finds the previous color on (x, y) and
// calls floodFillUtil()
void floodFill(int screen[][N], int x, int y, int newC)
{
	int prevC = screen[x][y];
	floodFillUtil(screen, x, y, prevC, newC);
}

// Driver program to test above function
int main()
{
    int p=1;
	int screen[M][N] = {{0, 0, 1, 0, 0, 0, 0},
                        {0, 0, 1, 1, 0, 0, 0},
                        {0, 0, 0, 0, 1, 0, 0},
                        {0, 0, 0, 1, 1, 0, 0},
                        {0, 1, 0, 0, 1, 0, 1},
                        {1, 1, 1, 0, 0, 0, 1},
                        {1, 1, 1, 0, 0, 1, 1},
                        };
	for (int i=0;i<M;i++)
        for (int j=0;j<N;j++)
            if (screen[i][j]==1){
                p++;
                floodFill(screen, i, j, p);
            }

	cout << "Updated screen after call to floodFill:"<<'\n';
	for (int i=0; i<M; i++)
	{
		for (int j=0; j<N; j++)
		cout << screen[i][j] << " ";
		cout << endl;
	}
}

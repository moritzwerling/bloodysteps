#ifndef MYCODE
#define MYCODE

#include <iostream>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

void extractMin(vector<vector<int>>& field, int& x, int& y);
void expand(vector<vector<int>>& field, int& x, int& y);

int path_finder(string maze) {
    stringstream ss(maze);
    int n = std::count(maze.begin(), maze.end(), '\n');
    int size_maze = n+1;
    vector<vector<int>> field(size_maze, vector<int>(size_maze));
    int x = 0;
    int y = 0;
    while(ss)
    {
        char c = ss.get();
        switch (c)
        {
            case '\n'   :   y += 1;
                            x = 0;
                            break;
            case 'W'    :   field[y][x] = -1;
                            x += 1;
                            break;          ;
            case '.'    :   field[y][x] = INT_MAX;
                            x += 1;
                            break;
        }
    }
    field[0][0] = 0;
    int x_min = -1;
    int y_min = -1;
    while(true)
    {
        extractMin(field, x_min, y_min);
        if (x_min == field.size()-1 && y_min == field.size()-1)
        {
            break;
        }
        else
        {
            expand(field, x_min, y_min);
        }
    }
    int cost_goal = field[y_min][x_min];
    return cost_goal;
}

void expand(vector<vector<int>>& field, int& x, int& y)
{
    const int moves[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
    for (auto m : moves)
    {
        int x_next = x+m[1];
        int y_next = y+m[0];
        if (   0<=x_next && x_next<field.size()
            && 0<=y_next && y_next<field.size()
           )
        {
            int old_cost = field[y_next][x_next];
            if (old_cost == -1)
            {
                continue;
            }
            int new_cost = field[y][x] + 1;
            if (new_cost<old_cost)
            {
                field[y_next][x_next] = new_cost;
            }
        }
    }

}

void extractMin(vector<vector<int>>& field, int& x_min, int& y_min)
{
    int min = INT_MAX;
    x_min = -1;
    y_min = -1;
    for (auto y=0; y<field.size(); ++y)
    {
        for (auto x=0; x<field[0].size(); ++x)
        {
            if (field[y][x] != -1 && field[y][x] < min)
            {
                x_min = x;
                y_min = y;
                min = field[y][x];
            }
        }
    }
}

#endif // MYCODE


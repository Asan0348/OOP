#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    int t;
    cin >> t;  // Number of elements to find
    vector<int> elements_to_find(t);
    
    for (int i = 0; i < t; i++) {
        cin >> elements_to_find[i];
    }

    int n, m;
    cin >> n >> m;  // Dimensions of the snake array
    vector<vector<int>> snake_array(n, vector<int>(m));

    // Reading the snake array
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> snake_array[i][j];
        }
    }

    // Creating a map to hold element coordinates
    unordered_map<int, pair<int, int>> coord_map;

    // Fill the map with coordinates of each element
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            coord_map[snake_array[i][j]] = {i, j};
        }
    }

    // Output the coordinates of the requested elements
    for (int i = 0; i < t; i++) {
        int element = elements_to_find[i];
        if (coord_map.find(element) != coord_map.end()) {
            cout << coord_map[element].first << " " << coord_map[element].second << endl;
        } else {
            cout << -1 << endl;
        }
    }

    return 0;
}

#include <iostream>

int findMax(int arr[], int size)
{
    int max = arr[0];

    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] < max)
        {
            max = arr[i];
        }
    };

    return max;
};

int main()
{
    int n;
    std::cout << "Enter size of array: ";
    std::cin >> n;

    int arr[n];

    std::cout << "Enter " << n << " integers: \n";

    for (int i = 0; i < n; ++i)
    {
        std::cin >> arr[i];
    }

    int maxVal = findMax(arr, n);

    std::cout << "Maximum value is: " << maxVal << std::endl;
}
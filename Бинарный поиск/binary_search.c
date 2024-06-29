#include <stdio.h>

int main(void)
{   
    int num = 3;
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int first = 0;
    int last = (sizeof(arr) / sizeof(arr[0])) - 1;
    int mid, curr, res = -1;

    while (first <= last) {
        mid = (first + last) / 2;
        curr = arr[mid];

        if (curr == num) {
            res = mid;
            break;
        }
        if (curr < num) {
            first = mid + 1;
        }
        else {
            last = mid - 1;
        }
    }

    if (res == -1) {
        printf("число не найдено\n");
    }
    else {
        printf("индекс искомого числа: %d \n", res);
    }

    return 0;
}
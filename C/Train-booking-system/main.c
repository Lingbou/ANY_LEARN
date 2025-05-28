#include "train_lib.h"

int main() {
    loadFromFile();  // 启动时加载数据
    int choice;
    while (1) {
        showMenu();
        scanf("%d", &choice);
        switch (choice) {
            case 1: importTrain();   break;
            case 2: queryTrain();    break;
            case 3: bookTicket();    break;
            case 4: refundTicket();  break;
            case 5: return 0;
            default: printf("无效选择！\n");
        }
    }
    return 0;
}
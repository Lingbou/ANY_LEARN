#include "train_lib.h"

TrainInfo trains[100];
int trainCount = 0;

// 保存数据到文件
void saveToFile() {
    FILE *fp = fopen("trains.txt", "w");
    if (fp == NULL) {
        printf("保存失败！\n");
        return;
    }
    for (int i = 0; i < trainCount; i++) {
        fprintf(fp, "%s %d %d %d %d\n", 
            trains[i].trainNo, 
            trains[i].date, 
            trains[i].tickets,
            trains[i].carriages,
            trains[i].seatsPerCar);
    }
    fclose(fp);
}

// 从文件加载数据
void loadFromFile() {
    FILE *fp = fopen("trains.txt", "r");
    if (fp == NULL) {
        printf("文件不存在，已初始化。\n");
        return;
    }
    trainCount = 0;
    while (trainCount < 100 && fscanf(fp, "%s %d %d %d %d", 
        trains[trainCount].trainNo, 
        &trains[trainCount].date, 
        &trains[trainCount].tickets,
        &trains[trainCount].carriages,
        &trains[trainCount].seatsPerCar) != EOF) {
        trainCount++;
    }
    fclose(fp);
}

// 导入列车信息（文件/手动）
void importTrain() {
    int choice;
    printf("1. 从文件导入  2. 手动输入：");
    scanf("%d", &choice);
    if (choice == 1) {
        loadFromFile();
        printf("导入成功！\n");
    } else {
        printf("输入车次、日期（如20250528）、初始票数、车厢数、每车厢座位数：");
        scanf("%s %d %d %d %d", 
            trains[trainCount].trainNo, 
            &trains[trainCount].date, 
            &trains[trainCount].tickets,
            &trains[trainCount].carriages,
            &trains[trainCount].seatsPerCar);
        trainCount++;
        saveToFile();
        printf("添加成功！\n");
    }
}

// 按车次查询（显示所有日期记录）
void queryTrain() {
    char no[20];
    printf("输入车次：");
    scanf("%s", no);
    int found = 0;
    for (int i = 0; i < trainCount; i++) {
        if (strcmp(trains[i].trainNo, no) == 0) {
            printf("车次：%s  日期：%d  剩余票数：%d  车厢数：%d  每车厢座位：%d\n", 
                trains[i].trainNo, 
                trains[i].date, 
                trains[i].tickets,
                trains[i].carriages,
                trains[i].seatsPerCar);
            found = 1;
        }
    }
    if (!found) printf("未找到该车次！\n");
}

// 订票（修改当日票数）
void bookTicket() {
    char no[20];
    int date;
    printf("输入车次、日期订票：");
    scanf("%s %d", no, &date);
    for (int i = 0; i < trainCount; i++) {
        if (strcmp(trains[i].trainNo, no) == 0 && trains[i].date == date) {
            if (trains[i].tickets > 0) {
                trains[i].tickets--;
                saveToFile();
                printf("订票成功！剩余票数：%d\n", trains[i].tickets);
            } else {
                printf("票数不足！\n");
            }
            return;
        }
    }
    printf("未找到该车次和日期！\n");
}

// 退票（恢复当日票数）
void refundTicket() {
    char no[20];
    int date;
    printf("输入车次、日期退票：");
    scanf("%s %d", no, &date);
    for (int i = 0; i < trainCount; i++) {
        if (strcmp(trains[i].trainNo, no) == 0 && trains[i].date == date) {
            trains[i].tickets++;
            saveToFile();
            printf("退票成功！剩余票数：%d\n", trains[i].tickets);
            return;
        }
    }
    printf("未找到该车次和日期！\n");
}

// 显示菜单
void showMenu() {
    printf("\n=== 火车订票系统 ===\n");
    printf("1. 导入列车信息\n");
    printf("2. 查询车次信息\n");
    printf("3. 订票\n");
    printf("4. 退票\n");
    printf("5. 退出\n");
    printf("请选择：");
}
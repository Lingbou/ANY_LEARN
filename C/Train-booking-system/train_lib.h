#ifndef TRAIN_LIB_H
#define TRAIN_LIB_H

#include <stdio.h>
#include <string.h>

typedef struct {
    char trainNo[20];   // 车次
    int date;           // 日期（格式：20250528）
    int tickets;        // 剩余票数
    int carriages;      // 车厢数量
    int seatsPerCar;    // 每车厢座位数
} TrainInfo;

extern TrainInfo trains[100];  // 列车信息数组
extern int trainCount;         // 记录数量

// 文件操作
void saveToFile();
void loadFromFile();

// 业务功能
void importTrain();
void queryTrain();
void bookTicket();
void refundTicket();
void showMenu();

#endif
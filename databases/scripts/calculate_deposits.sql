/*
 Navicat Premium Data Transfer

 Source Server         : finance_deposit
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 19/12/2023 10:28:24
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for calculate_deposits
-- ----------------------------
DROP TABLE IF EXISTS "calculate_deposits";
CREATE TABLE "calculate_deposits" (
  "id_deposit" integer NOT NULL,
  "sum_deposit" integer NOT NULL,
  "period_deposit" integer NOT NULL,
  "start_date" text NOT NULL,
  "percent_deposit" real NOT NULL,
  "sum_percent" real NOT NULL,
  "total_sum" real NOT NULL,
  PRIMARY KEY ("id_deposit")
);

PRAGMA foreign_keys = true;

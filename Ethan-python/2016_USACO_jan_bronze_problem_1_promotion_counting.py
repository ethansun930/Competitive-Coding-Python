import sys

sys.stdin = open("promote.in", "r")
sys.stdout = open("promote.out", "w")
bronze = list(map(int, input().split()))
silver = list(map(int, input().split()))
gold = list(map(int, input().split()))
platinum = list(map(int, input().split()))
gold_platinum = platinum[1] - platinum[0]
silver_gold = gold[1] - gold[0] + gold_platinum
bronze_silver = silver[1] - silver[0] + silver_gold
print(bronze_silver)
print(silver_gold)
print(gold_platinum)
check_list = {
    "FLTMODE1": 0,
    "FLTMODE4": 16,
    "FLTMODE6": 3,
    "FENCE_ENABLE": 1,
    "FENCE_TYPE": 5,
    "FS_THR_ENABLE": 2,
    "FS_BATT_ENABLE": 2,
    "FS_BATT_VOLTAGE": 21,
    "FS_THR_ENABLE": 2
}

for k, v in check_list.items():
    cur = Script.GetParam(k)
    if cur != v:
    	print("[NG] {0} should {1}, but {2} is {3}".format(k, v, k, cur))
    else:
        print("[OK] {0} is {1}".format(k, v))
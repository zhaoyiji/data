import stk_code


def test_get_stk_code():
    code_list = stk_code.get_stk_code()
    dst_list = ["sh600001", "sh600002", "sz000001", "sz000002"]
    assert cmp(code_list, dst_list) == 0

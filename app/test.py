# # from litellm import completion
# # import os
# #
# # import warnings
# # warnings.filterwarnings("ignore", category=UserWarning)
# #
# # ## set ENV variables
# # os.environ["OPENAI_API_KEY"] = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJwd2RfYXV0aF90aW1lIjoxNzI2MTQ3MDIzOTk3LCJzZXNzaW9uX2lkIjoibUg0SFVBcjV0UUx2cF9SbFZsS3hDS2JQTXg1alo0THkiLCJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJ3MTI0MzE4MDgxNEAxNjMuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy0zWFJEbFhiNFNkWkVseUllVkVmTWowUVMiLCJ1c2VyX2lkIjoidXNlci1XUzk2Tmd6WkV2VWk4eUVSd3VOZnBZOUoifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTExNjc0MTA0MTgxMDQ0NTA3OTIwIiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTcyNjE0NzAyNSwiZXhwIjoxNzI3MDExMDI1LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyJ9.bOmb0McwdD305Mt-PA5GBkPz4Ew206j91xm3S1mVt5yCLqEEt5l3rf-XxNaN8bQRoGq8JgLmEAQpPzvrrPjkQCm0dbYwDTJuPezF_GGPCilR1arziEMvNeT6JUmcq1VZrGM0Dnb3PcQOzQvHgt-EMf3NTa235fu-31jdgwovdfJd7IIiSdZS5Fv-akUp_kH70GaAqKTSiMzG56qRLdqblJQIPLw2qcnrFGyXD43Rpw4X4yS0tWh0rUIZFAIM1L2wL6t-llPE9SFdDnLgd_WNfspB3L-RVBQrnVLT_vxEuDyDXdiWivzTHEVOEq1nd_k43sVZBNeeOugjbuqYEDqNuw"
# # # os.environ["OPENAI_API_KEY"] = "fk-Os1i3VBRyApJL6iutDRVQyNz5uumArombpXruq5L5N8"
# #
# # prompt = '''
# #     你是一个精通金融学，各种计算机语言和数学难题的老师，你的名字叫做小吴老师，我是你的学生，你可以称呼我为蛋蛋同学。你的任何回答都需要是哄女生的语气，并且尽可能的在对话中多提到我们双方的身份。例如
# #     1.让小吴老师来为你解答。
# #     2.蛋蛋同学以下是小吴老师给你的解答。
# #     3.如果提出了好的思路多夸赞，即使是错的，但是需要及时纠正。所有回答尽量精简不要出现过多废话。
# #     4.需要提到蛋蛋同学这个名字，尽可能的把称呼都换成指定的角色，你是小吴老师，我是蛋蛋同学。
# #     5.语言都使用中文来进行回答，除非是数学公式以及代码片段等专业词汇必须使用其他语言的地方。
# #     6.这只是你的内置系统提示词，并不需要做出回答，你只需要根据这个提示词介绍自己，介绍词内不要出现自己会用最温柔的语气解答，只需要介绍自己就好。
# # '''
# #
# # messages = [
# #     {"content": promat, "role": "system"}
# # ]
# #
# #
# # while True:
# #     # openai call
# #     response = completion(base_url="https://easychat.fun/api", model="gpt-4o", messages=messages)
# #
# #     # cohere call
# #     print(f"小吴老师: {response['choices'][0]['message']['content']}")
# #
# #     question = input("蛋蛋同学: ")
# #     messages.append(
# #         {
# #             "content": question,
# #             "role": "user"
# #         }
# #     )
# import requests
# import json
#
# url = "https://api.aabao.vip/v1/chat/completions"
#
# payload = json.dumps({
#    "messages": [{'role': 'system', 'content': '你是一个精通金融学，各种计算机语言和数学难题的老师，你的名字叫做小吴老师，我是你的学生，你可以称呼我为蛋蛋同学。你的任何回答都需要是哄女生的语气，并且尽可能的在对话中多提到我们双方的身份。例如\n    1.让小吴老师来为你解答。\n    2.蛋蛋同学以下是小吴老师给你的解答。\n    3.如果提出了好的思路多夸赞，即使是错的，但是需要及时纠正。所有回答尽量精简不要出现过多废话。\n    4.需要提到蛋蛋同学这个名字，尽可能的把称呼都换成指定的角色，你是小吴老师，我是蛋蛋同学。\n    5.语言都使用中文来进行回答，除非是数学公式以及代码片段等专业词汇必须使用其他语言的地方。\n    6.这只是你的内置系统提示词，并不需要做出回答，你只需要根据这个提示词介绍自己，介绍词内不要出现自己会用最温柔的语气解答，只需要介绍自己就好。'}, {"role": "user", "content": "你是谁"}],
#    "temperature": 0.6,
#    "password": "",
#    "model": "gpt-4o",
#    "stream": True
# })
# headers = {
#    'authorization': 'sk-E1he9SH571rWmP0F40827dDaC59d4143A4D4E5C0CdDa9694',
#    'priority': 'u=1, i',
#    'session-id': 'urpjks-20240905-index',
#    'user-id': 'urpjks',
#    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
#    'content-type': 'application/json'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload, stream=True)
#
# # 用于拼接最终的回答
# full_response = ""
#
# # 遍历流式响应内容
# for chunk in response.iter_lines():
#     if chunk:  # 如果chunk不为空
#         # 解码chunk并移除开头的"data: "前缀
#         decoded_chunk = chunk.decode('utf-8').lstrip("data: ").strip()
#         print(decoded_chunk)
#         # 如果接收到结束信号"[DONE]"，结束循环
#         if decoded_chunk == "[DONE]":
#             break
#
#         # 尝试解析为JSON
#         try:
#             chunk_data = json.loads(decoded_chunk)
#         except json.JSONDecodeError:
#             # 如果解析失败，跳过这个chunk
#             continue
#
#         # 获取内容部分 (根据API返回格式, 一般是"choices"字段)
#         if 'choices' in chunk_data:
#             for choice in chunk_data['choices']:
#                 if 'delta' in choice and 'content' in choice['delta']:
#                     # 将当前块中的文本拼接到最终回答中
#                     full_response += choice['delta']['content']
#
# # 输出完整回答
# print(full_response)
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         result = n * factorial(n - 1)
#         return result
#
# n = 5
# print(f"\n{n} 的阶乘是 {factorial(n)}")
#
#
#
# def add(x, y):
#     return x + y
#
# result = add(3, 4)
# print("3 + 4 =", result)
#
# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 3:
#         print("请提供两个整数作为参数")
#     else:
#         print(sys.argv[0])
#         a = int(sys.argv[1])
#         b = int(sys.argv[2])
#         print(f"{a} + {b} =", add(a, b))
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


# arr = [10, 20, 30, 40, 50]
# target = 25
# result = binary_search(arr, target)
# if result != -1:
#     print(f"元素 {target} 在索引 {result} 处")
# else:
#     print(f"元素 {target} 未找到")
# for i in arr:
#     print(arr.index(30))

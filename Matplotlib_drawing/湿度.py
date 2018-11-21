import json
import matplotlib.pyplot as plt

s = '{"0": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "1", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "89", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "66", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "1": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "2", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "93", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "66", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "2": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "3", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "91", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "57", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "3": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "4", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "79", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "33", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "4": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "5", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "76", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "41", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "5": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "6", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "82", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "68", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "6": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "7", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "69", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "46", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "7": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "8", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "72", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "30", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "8": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "9", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "70", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "37", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "9": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "11", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "76", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "38", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "10": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "12", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "79", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "49", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "11": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "13", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "82", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "60", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "12": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "14", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "75", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "47", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "13": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "15", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "70", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "52", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "14": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "16", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "72", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "57", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "15": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "17", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "76", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "63", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "16": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "18", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "87", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "62", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "17": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "19", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "79", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "55", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "18": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "20", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "81", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "67", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "19": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "21", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "79", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "54", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "20": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "23", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "77", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "36", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "21": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "24", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "70", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "31", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "22": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "25", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "78", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "57", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "23": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "26", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "86", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "59", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "24": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "27", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "79", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "54", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "25": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "28", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "71", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "41", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "26": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "29", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "77", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "29", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}, "27": {"\u533a\u7ad9\u53f7": "57494", "\u7eac\u5ea6": "3036", "\u7ecf\u5ea6": "1143", "\u89c2\u6d4b\u573a\u62d4\u6d77\u9ad8\u5ea6": "236", "\u5e74": "2018", "\u6708": "9", "\u65e5": "30", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6": "79", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6(\u4ec5\u81ea\u8bb0)": "33", "\u5e73\u5747\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9", "\u6700\u5c0f\u76f8\u5bf9\u6e7f\u5ea6\u8d28\u91cf\u63a7\u5236\u7801": "9"}}'

dic = json.loads(s)
print(dic)

y1 = []
y2 = []
y3 = []
x = []
for keys in dic.keys():
    # print(dic[keys])
    y1.append(eval(dic[keys]['最小相对湿度(仅自记)']))
    #y2.append(eval(dic[keys]['日最高本站气压']))
    y3.append(eval(dic[keys]['平均相对湿度']))
    x.append(eval(dic[keys]['日']))
# print(len(y1))
# for i in x: print(i)

plt.figure(figsize=(20, 10))  # 创建绘图对象

l1 = plt.plot(x, y1, 'ro-', label='Minimum relative humidity')
#l2 = plt.plot(x, y2, 'g^-', label='Maximum Air pressure')
l3 = plt.plot(x, y3, 'b+-', label='Average relative humidity')
# plt.plot(x, y1, 'ro-', x, y2, 'g+-')#, x3, y3, 'b^-')
plt.title('Relative humidity Measure')
plt.ylabel('Relative humidity(1%)', fontsize=18)
plt.xlabel('Days', fontsize=18)
plt.legend()
plt.savefig("湿度.jpg")
plt.show()
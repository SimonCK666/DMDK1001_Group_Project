'''
Author: SimonCK666 SimonYang223@163.com
Date: 2022-11-27 10:33:57
LastEditors: SimonCK666 SimonYang223@163.com
LastEditTime: 2022-11-27 11:01:25
FilePath: /DMDK1001_Group_Project/config.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import argparse

def config_parser():
    '''Define command line arguments
    '''

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--img', type=str, default='img/a.jpeg',
                        help='img file path')
    parser.add_argument('--clustersNum', type=int, default=3,
                        help='number of clusters')
    
    return parser

def config_parser_eval():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--img",dest="list",nargs='+',help="img file paths by two")
    
    return parser
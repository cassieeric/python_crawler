# -------------------------------
# -*- coding: utf-8 -*-
# @Author：jianghan
# @Time：2020/11/25 14:46
# @File: crypt.py
# Python版本：3.6.8
# -------------------------------


"""
1、 填充字符串和明文字符串最后一位不能相同
2、 字符串编码默认是utf-8， key和iv默认为英文字符；字符串不支持其他编码或key/iv不支持为中文字符
"""


from enum import Enum, unique
from Crypto.Cipher import AES


@unique
class Mode(Enum):
  CBC = AES.MODE_CBC
  ECB = AES.MODE_ECB


@unique
class Padding(Enum):
 """ 定义填充的字符串 """
 SPACE = ' ' # 空格


class AES256Crypto:
 def __init__(self, key, mode=Mode.ECB, padding=Padding.SPACE, iv=None):
  """
  :param key: 密钥， 32byte 长度字符串
  :param mode: 加密模式， 来源 class Mode
  :param iv: 16byte 长度字符串
  :param padding: 填充的字符串， 来源class Padding
  """
  self.padding = self.check_padding(padding)

  self.key = self.padding_key(key)
  self.iv = self.padding_iv(iv) if iv else None

  self.mode = self.check_mode(mode)

 def check_mode(self, mode):
  """ 核对 mode """
  if mode not in Mode.__members__.values():
   raise Exception(f'mode {mode} not allowed!')
  if mode == Mode.CBC and not self.iv:
   raise Exception(f'iv is required')
  return mode

 def check_padding(self, padding):
  """ 核对 padding """
  if padding not in Padding.__members__.values():
   raise Exception(f'mode {padding} not allowed!')
  return padding

 def padding_ret_byte(self, text, _len=16):
  """ 填充并转成 bytes """
  text = text.encode()
  remainder = len(text) % _len
  remainder = _len if remainder == 0 else remainder
  text += (_len - remainder) * self.padding.value.encode()
  return text

 def padding_iv(self, iv: str):
  """ 补全iv 并转成 bytes"""
  if len(iv.encode()) > 16:
   raise Exception(f'iv {iv} must <= 16bytes')
  return self.padding_ret_byte(iv)

 def padding_key(self, key: str):
  """ 补全key 并转成 bytes """
  if len(key.encode()) > 32:
   raise Exception(f'key {key} must <= 32bytes')
  return self.padding_ret_byte(key, _len=32)

 def encrypt(self, text, encode=None):
  """
  加密
  :param text: 待加密字符串
  :param encode: 传入base64里面的方法
  :return: 若encode=None则不进行base加密处理，返回bytes类型数据
  """
  text = self.padding_ret_byte(text)
  # 注意：加密中的和解密中的AES.new()不能使用同一个对象，所以在两处都使用了AES.new()
  text = AES.new(key=self.key, mode=self.mode.value, iv=self.iv).encrypt(text)
  if encode:
   return encode(text).decode()
  return text

 def decrypt(self, text, decode=None):
  """ 解密 """
  if decode:
    if type(text) == str:
     text = text.encode()
     text = decode(bytes(text))
  else:
    if type(text) != bytes:
     raise Exception(text)
  text = AES.new(key=self.key, mode=self.mode.value, iv=self.iv).decrypt(text)
  text = text.strip(self.padding.value.encode())
  return text.decode()
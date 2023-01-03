import streamlit as st
import sqlite3
import os
import Data_Shop_CatsnDogs
from PIL import Image

st.set_page_config("Animals Store", page_icon="dog", layout="wide")
st.markdown("""<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">""", unsafe_allow_html=True)

st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="/"><img width="200" height="100" src="https://dogily.vn/wp-content/uploads/2020/07/dogily-logo.png" class="header_logo header-logo entered lazyloaded" alt="Dogily Petshop – Bán chó mèo cảnh, thú cưng Tphcm, Hà nội" data-lazy-src="https://dogily.vn/wp-content/uploads/2020/07/dogily-logo.png" data-ll-status="loaded"></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="/" target="_parent"><b>Home</b> <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/Danh_Mục_Sản_Phẩm" target="_parent"><b>Danh Mục Sản Phẩm</b></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/Giỏ_Hàng" target="_parent"><b>Giỏ Hàng</b></a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
""", unsafe_allow_html=True)

placeholder = st.empty()

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
  def write_animals(info):
    return st.markdown(f"""
              <div class="text-center">
              <h3 style='text-align: center; font-size: 60px;'>{info[3]}</h3>
                  <p style='text-align: center; font-size: 20px;'>
                      <br><b>Loại</b>: {info[2]} <br>
                      <b>Giới tính</b>: {info[5]} <br>
                      <b>Vacxin</b>: {info[7]} <br>
                      <b>Tuổi</b>: {info[6]} </br>
                  </p>
              </div>
              """, unsafe_allow_html=True)
col1 , col2 = st.columns(2)

httpQuery = st.experimental_get_query_params()
loai = httpQuery["loai"][0]
giong = httpQuery["giong"][0]

with col1  : 
  parent_dir = f"./{loai}/{giong}"
  image_folder = os.listdir(parent_dir)[0]
  parent_dir += "/" + image_folder
  image_path = parent_dir + "/" + os.listdir(parent_dir)[0]
  image = Image.open(image_path)
  st.image(image, width=400)
  st.markdown("----------------------------------")

with col2 : 
  df = Data_Shop_CatsnDogs.Data_Shop_CatsnDogs()
  queryObj = df.queryData(f"select * from ShopData where loai=\'{loai}\' and giong=\'{giong}\';")
  write_animals(queryObj)
  st.markdown("----------------------------------")

st.markdown("""
<div class="container section-title-container" style="margin-bottom:0px;">
    <h2 class="section-title section-title-center">
        <b></b>
        <span class="section-title-main" style="font-size:150%;">Sản Phẩm Liên Quan</span>
        <b></b>
    </h2>
</div>
""", unsafe_allow_html=True)

list_of_Dogs = df.queryAllDatas("select distinct giong from ShopData where loai='Chó'")

col1, col2 = st.columns(2)
max = 10

with col1:
  if loai == list_of_Dogs :
    for i in range(0,int(len(list_of_Dogs) /2)):
        parent_dir = f"./Chó/{list_of_Dogs[i][0]}"
        image_folder = os.listdir(parent_dir)[0]
        parent_dir += "/" + image_folder
        image_path = parent_dir + "/" + os.listdir(parent_dir)[0]
        image = Image.open(image_path)
        write_animals(df.queryData(f"select * from ShopData where loai='Chó' and giong='{list_of_Dogs[i][0]}'"), image)
        st.markdown("----------------------------------")

with col2:
  if loai == list_of_Dogs :
    for i in range(int(len(list_of_Dogs) /2),len(list_of_Dogs)):
        parent_dir = f"./Chó/{list_of_Dogs[i][0]}"
        image_folder = os.listdir(parent_dir)[0]
        parent_dir += "/" + image_folder
        image_path = parent_dir + "/" + os.listdir(parent_dir)[0]
        image = Image.open(image_path)
        write_animals(df.queryData(f"select * from ShopData where loai='Chó' and giong='{list_of_Dogs[i][0]}'"), image)
        st.markdown("----------------------------------")

list_of_Cats = df.queryAllDatas("select distinct giong from ShopData where loai='Mèo'")
col1, col2 = st.columns(2)

with col1:
  if loai == list_of_Cats : 
    for i in range(0,int(len(list_of_Cats) /2)):
        parent_dir = f"./Mèo/{list_of_Cats[i][0]}"
        image_folder = os.listdir(parent_dir)[0]
        parent_dir += "/" + image_folder
        image_path = parent_dir + "/" + os.listdir(parent_dir)[0]
        image = Image.open(image_path)
        write_animals(df.queryData(f"select * from ShopData where loai='Mèo' and giong='{list_of_Cats[i][0]}'"), image)
        st.markdown("----------------------------------")

with col2:
  if loai == list_of_Cats :
    for i in range(int(len(list_of_Cats) /2),len(list_of_Cats)):
        parent_dir = f"./Mèo/{list_of_Cats[i][0]}"
        image_folder = os.listdir(parent_dir)[0]
        parent_dir += "/" + image_folder
        image_path = parent_dir + "/" + os.listdir(parent_dir)[0]
        image = Image.open(image_path)
        write_animals(df.queryData(f"select * from ShopData where loai='Mèo' and giong='{list_of_Cats[i][0]}'"), image)
        st.markdown("----------------------------------")


st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
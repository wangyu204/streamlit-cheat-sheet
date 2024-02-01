"""
Streamlit Cheat Sheet

App to summarise streamlit docs v1.25.0

There is also an accompanying png and pdf version

https://github.com/daniellewisDL/streamlit-cheat-sheet

v1.25.0
20 August 2023

Author:
    @daniellewisDL : https://github.com/daniellewisDL

Contributors:
    @arnaudmiribel : https://github.com/arnaudmiribel
    @akrolsmir : https://github.com/akrolsmir
    @nathancarter : https://github.com/nathancarter

"""

import streamlit as st
from pathlib import Path
import base64
import akshare as ak

# Initial page config

st.set_page_config(
     page_title='kzz行情',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    # 设置自定义主题
    set_custom_theme()
    cs_sidebar()
    display_dataframe()

    return None

# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# sidebar

def cs_sidebar():

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('wangyu2488 sheet')

    st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/), as of [Streamlit v1.25.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    st.sidebar.markdown('__Install and import__')

    st.sidebar.code('$ pip install streamlit')

    st.sidebar.code('''
# Import convention
>>> import streamlit as st
''')

    st.sidebar.markdown('__Add widgets to sidebar__')
    st.sidebar.code('''
# Just add it after st.sidebar:
>>> a = st.sidebar.radio(\'Choose:\',[1,2])
    ''')

    st.sidebar.markdown('__Magic commands__')
    st.sidebar.code('''
'_This_ is some __Markdown__'
a=3
'dataframe:', data
''')

    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''
$ streamlit --help
$ streamlit run your_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version
    ''')

    st.sidebar.markdown('__Pre-release features__')
    st.sidebar.code('''
pip uninstall streamlit
pip install streamlit-nightly --upgrade
    ''')
    st.sidebar.markdown('<small>Learn more about [experimental features](https://docs.streamlit.io/library/advanced-features/prerelease#beta-and-experimental-features)</small>', unsafe_allow_html=True)

    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<small>[Cheat sheet v1.25.0](https://github.com/daniellewisDL/streamlit-cheat-sheet)  | Aug 2023 | [Daniel Lewis](https://daniellewisdl.github.io/)</small>''', unsafe_allow_html=True)

    return None

# 自定义Streamlit主题
def set_custom_theme():
    # 设置DataFrame的高度
    st.markdown("""
    <style>
    .stDataFrame {
        height: auto !important;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 右侧DataFrame表格展示
def display_dataframe():
    st.title('可转债实时行情')
    # 创建一个空容器，用于后续更新DataFrame
    placeholder = st.empty()
    # 初始化DataFrame
    df = generate_random_dataframe()
    # 显示DataFrame
    placeholder.dataframe(df, height=600)  # 设置DataFrame的高度为300像素
    # 创建一个刷新按钮
    if st.button('刷新'):
        # 更新DataFrame数据
        df = generate_random_dataframe()
        # 更新空容器中的DataFrame
        placeholder.dataframe(df, height=600)  # 设置DataFrame的高度为300像素


def generate_random_dataframe():
    #转债实时行情
    bond_zh_hs_cov_spot_df = ak.bond_zh_hs_cov_spot()
    # print(bond_zh_hs_cov_spot_df)
    return bond_zh_hs_cov_spot_df

# Run main()
if __name__ == '__main__':
    main() 

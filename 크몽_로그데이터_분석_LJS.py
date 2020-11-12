#!/usr/bin/env python
# coding: utf-8

# # <center>크몽 로그데이터 분석</center>

# * 분석자 : 이재성

# <h1>목차<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#크몽-로그데이터-분석" data-toc-modified-id="크몽-로그데이터-분석-1"><center>크몽 로그데이터 분석</center></a></span></li><li><span><a href="#1-분석-프로젝트-개요" data-toc-modified-id="1-분석-프로젝트-개요-2">1 분석 프로젝트 개요</a></span><ul class="toc-item"><li><span><a href="#1.1-개발-환경" data-toc-modified-id="1.1-개발-환경-2.1">1.1 개발 환경</a></span></li><li><span><a href="#1.2-라이브러리" data-toc-modified-id="1.2-라이브러리-2.2">1.2 라이브러리</a></span></li><li><span><a href="#1.3-데이터-로드" data-toc-modified-id="1.3-데이터-로드-2.3">1.3 데이터 로드</a></span></li><li><span><a href="#1.4-결측치-확인" data-toc-modified-id="1.4-결측치-확인-2.4">1.4 결측치 확인</a></span></li></ul></li><li><span><a href="#2-데이터-전처리" data-toc-modified-id="2-데이터-전처리-3">2 데이터 전처리</a></span><ul class="toc-item"><li><span><a href="#2.1-log-Data" data-toc-modified-id="2.1-log-Data-3.1">2.1 log Data</a></span><ul class="toc-item"><li><span><a href="#2.1.1-컬럼명-수정-(canonicaldeviceuuid)" data-toc-modified-id="2.1.1-컬럼명-수정-(canonicaldeviceuuid)-3.1.1">2.1.1 컬럼명 수정 (canonicaldeviceuuid)</a></span></li><li><span><a href="#2.1.2-시간-데이터-정리(eventdatetime)" data-toc-modified-id="2.1.2-시간-데이터-정리(eventdatetime)-3.1.2">2.1.2 시간 데이터 정리(eventdatetime)</a></span></li><li><span><a href="#2.1.3-접속시간-변환" data-toc-modified-id="2.1.3-접속시간-변환-3.1.3">2.1.3 접속시간 변환</a></span></li><li><span><a href="#2.1.4-접속시간-범주화" data-toc-modified-id="2.1.4-접속시간-범주화-3.1.4">2.1.4 접속시간 범주화</a></span></li><li><span><a href="#2.1.5-osversion" data-toc-modified-id="2.1.5-osversion-3.1.5">2.1.5 osversion</a></span></li><li><span><a href="#2.1.6-devicemanufacturer" data-toc-modified-id="2.1.6-devicemanufacturer-3.1.6">2.1.6 devicemanufacturer</a></span></li><li><span><a href="#2.1.7-channel" data-toc-modified-id="2.1.7-channel-3.1.7">2.1.7 channel</a></span></li><li><span><a href="#2.1.8-inappeventcategory" data-toc-modified-id="2.1.8-inappeventcategory-3.1.8">2.1.8 inappeventcategory</a></span></li><li><span><a href="#2.1.9-컬럼-삭제" data-toc-modified-id="2.1.9-컬럼-삭제-3.1.9">2.1.9 컬럼 삭제</a></span></li><li><span><a href="#2.1.10-컬럼명-통일-및-컬럼-정렬" data-toc-modified-id="2.1.10-컬럼명-통일-및-컬럼-정렬-3.1.10">2.1.10 컬럼명 통일 및 컬럼 정렬</a></span></li></ul></li><li><span><a href="#2.2-funnel-Data" data-toc-modified-id="2.2-funnel-Data-3.2">2.2 funnel Data</a></span><ul class="toc-item"><li><span><a href="#2.2.1-컬럼명-수정-및-정렬" data-toc-modified-id="2.2.1-컬럼명-수정-및-정렬-3.2.1">2.2.1 컬럼명 수정 및 정렬</a></span></li></ul></li><li><span><a href="#2.3-category-Data" data-toc-modified-id="2.3-category-Data-3.3">2.3 category Data</a></span><ul class="toc-item"><li><span><a href="#2.3.1-컬럼명-수정-및-정렬¶" data-toc-modified-id="2.3.1-컬럼명-수정-및-정렬¶-3.3.1">2.3.1 컬럼명 수정 및 정렬¶</a></span></li></ul></li><li><span><a href="#2.4-데이터-합치기" data-toc-modified-id="2.4-데이터-합치기-3.4">2.4 데이터 합치기</a></span><ul class="toc-item"><li><span><a href="#2.4.1-컬럼-삭제" data-toc-modified-id="2.4.1-컬럼-삭제-3.4.1">2.4.1 컬럼 삭제</a></span></li><li><span><a href="#2.4.2-컬럼-정렬" data-toc-modified-id="2.4.2-컬럼-정렬-3.4.2">2.4.2 컬럼 정렬</a></span></li><li><span><a href="#2.4.3-인덱스-지정" data-toc-modified-id="2.4.3-인덱스-지정-3.4.3">2.4.3 인덱스 지정</a></span></li></ul></li></ul></li><li><span><a href="#3-데이터-검색-클래스" data-toc-modified-id="3-데이터-검색-클래스-4">3 데이터 검색 클래스</a></span><ul class="toc-item"><li><span><a href="#3.1-클래스-구현" data-toc-modified-id="3.1-클래스-구현-4.1">3.1 클래스 구현</a></span></li><li><span><a href="#3.2-데이터-검색" data-toc-modified-id="3.2-데이터-검색-4.2">3.2 데이터 검색</a></span><ul class="toc-item"><li><span><a href="#3.2.1-find_userid" data-toc-modified-id="3.2.1-find_userid-4.2.1">3.2.1 find_userid</a></span></li><li><span><a href="#3.2.2-find_columns" data-toc-modified-id="3.2.2-find_columns-4.2.2">3.2.2 find_columns</a></span></li><li><span><a href="#3.2.3-find_item" data-toc-modified-id="3.2.3-find_item-4.2.3">3.2.3 find_item</a></span></li></ul></li></ul></li><li><span><a href="#4-그래프-출력-클래스" data-toc-modified-id="4-그래프-출력-클래스-5">4 그래프 출력 클래스</a></span><ul class="toc-item"><li><span><a href="#4.1-클래스-구현" data-toc-modified-id="4.1-클래스-구현-5.1">4.1 클래스 구현</a></span><ul class="toc-item"><li><span><a href="#4.1.1-os_type" data-toc-modified-id="4.1.1-os_type-5.1.1">4.1.1 os_type</a></span></li><li><span><a href="#4.1.2-os_version" data-toc-modified-id="4.1.2-os_version-5.1.2">4.1.2 os_version</a></span></li><li><span><a href="#4.1.3-device_type" data-toc-modified-id="4.1.3-device_type-5.1.3">4.1.3 device_type</a></span></li><li><span><a href="#4.1.4-app_version" data-toc-modified-id="4.1.4-app_version-5.1.4">4.1.4 app_version</a></span></li></ul></li></ul></li><li><span><a href="#5-데이터-분석" data-toc-modified-id="5-데이터-분석-6">5 데이터 분석</a></span><ul class="toc-item"><li><span><a href="#5.1-잔존-분석" data-toc-modified-id="5.1-잔존-분석-6.1">5.1 잔존 분석</a></span><ul class="toc-item"><li><span><a href="#5.1.1-user별-잔존시간" data-toc-modified-id="5.1.1-user별-잔존시간-6.1.1">5.1.1 user별 잔존시간</a></span></li><li><span><a href="#5.1.2-구매/비구매-cycle별-잔존시간" data-toc-modified-id="5.1.2-구매/비구매-cycle별-잔존시간-6.1.2">5.1.2 구매/비구매 cycle별 잔존시간</a></span></li></ul></li><li><span><a href="#5.2-전환율-분석" data-toc-modified-id="5.2-전환율-분석-6.2">5.2 전환율 분석</a></span><ul class="toc-item"><li><span><a href="#5.2.1-날짜별-구매-전환율" data-toc-modified-id="5.2.1-날짜별-구매-전환율-6.2.1">5.2.1 날짜별 구매 전환율</a></span></li><li><span><a href="#5.2.2-신규-회원-구매-전환율" data-toc-modified-id="5.2.2-신규-회원-구매-전환율-6.2.2">5.2.2 신규 회원 구매 전환율</a></span></li></ul></li><li><span><a href="#5.3-퍼널-분석" data-toc-modified-id="5.3-퍼널-분석-6.3">5.3 퍼널 분석</a></span><ul class="toc-item"><li><span><a href="#5.3.1-구매-도달율-분석" data-toc-modified-id="5.3.1-구매-도달율-분석-6.3.1">5.3.1 구매 도달율 분석</a></span></li><li><span><a href="#5.3.2-카테고리별-구매율" data-toc-modified-id="5.3.2-카테고리별-구매율-6.3.2">5.3.2 카테고리별 구매율</a></span></li><li><span><a href="#5.3.3-시간대별-카테고리-조회-빈도" data-toc-modified-id="5.3.3-시간대별-카테고리-조회-빈도-6.3.3">5.3.3 시간대별 카테고리 조회 빈도</a></span></li></ul></li><li><span><a href="#5.4-종료율-분석" data-toc-modified-id="5.4-종료율-분석-6.4">5.4 종료율 분석</a></span><ul class="toc-item"><li><span><a href="#5.4.1-일별-종료율" data-toc-modified-id="5.4.1-일별-종료율-6.4.1">5.4.1 일별 종료율</a></span></li><li><span><a href="#5.4.2-시간별-종료율" data-toc-modified-id="5.4.2-시간별-종료율-6.4.2">5.4.2 시간별 종료율</a></span></li><li><span><a href="#5.4.3-일-X-시간대-종료율" data-toc-modified-id="5.4.3-일-X-시간대-종료율-6.4.3">5.4.3 일 X 시간대 종료율</a></span></li></ul></li></ul></li><li><span><a href="#6-종합결과" data-toc-modified-id="6-종합결과-7">6 종합결과</a></span><ul class="toc-item"><li><span><a href="#6.1-구매-유무별-잔존-분석" data-toc-modified-id="6.1-구매-유무별-잔존-분석-7.1">6.1 구매 유무별 잔존 분석</a></span></li><li><span><a href="#6.2-구매-전환율" data-toc-modified-id="6.2-구매-전환율-7.2">6.2 구매 전환율</a></span></li><li><span><a href="#6.3-구매-도달율" data-toc-modified-id="6.3-구매-도달율-7.3">6.3 구매 도달율</a></span></li><li><span><a href="#6.4-카테고리별-구매율" data-toc-modified-id="6.4-카테고리별-구매율-7.4">6.4 카테고리별 구매율</a></span></li><li><span><a href="#6.5-카테고리별-조회-빈도" data-toc-modified-id="6.5-카테고리별-조회-빈도-7.5">6.5 카테고리별 조회 빈도</a></span></li><li><span><a href="#6.6-종료율-분석" data-toc-modified-id="6.6-종료율-분석-7.6">6.6 종료율 분석</a></span></li></ul></li></ul></div>

# # 1 분석 프로젝트 개요

# 로그데이터는 모바일/웹/현실 등 다양한 환경에서 발생하는 사건을 데이터로 기록한 것입니다. 이를 분석하여 사용자의 사용행태 및 서비스 문제점 등을 파악하여 더 나은 방향으로 서비스를 개선하는 데 주로 활용됩니다.
# 
# 
# 본 프로젝트는 프리랜서 마켓이자 비즈니스 거래 플랫폼인 크몽의 로그데이터를 분석하여 서비스 이용자의 행태를 살펴보고자 합니다.
# 
# 
# 분석 내용은 다음과 같습니다.
# 
# 
# 1) 웹사이트 내 잔존시간
# 
#    - 구매자와 비구매자 간의 웹사이트 잔존시간 차이 파악
# 
# 2) 구매 전환율
# 
#    - 날짜별, 신규 회원의 구매 전환율 파악
# 
# 3) 퍼널 분석
# 
#    - 퍼널 단계에서의 이탈률 - 구매 도달율 - 카테고리별 구매율 파악
# 
# 4) 종료율 분석
# 
#    - 날짜별 / 시간별 종료율 피악

# ## 1.1 개발 환경

# pandas == 1.0.5
# 
# numpy == 1.18.5
# 
# matplotlib == 3.2.2
# 
# seaborn == 0.10.1
# 
# IPython == 7.16.1
# 
# tqdm == 4.47.0
# 
# scipy == 1.4.1

# ## 1.2 라이브러리

# * 현재 항목에서는 기본적인 라이브러리만을 정리했습니다.

# In[1]:


import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import set_matplotlib_formats

# 화면에 출력할 최대 컬럼 개수를 50개로 늘려줍니다.
pd.options.display.max_columns = 50

# 윈도우를 이용하고 있기 떄문에 Malgun Gothic을 설정했습니다.
# 맥의 경우 'AppleGothic' 을 사용해주셔야 합니다.
plt.rc('font', family='Malgun Gothic')  # windows
# plt.rc('font', family='Apple Gothic')   # mac

# 별도로, 폰트를 바꿀 경우 마이너스가 표시되지 않는 경우도 있는데 이를 막아주는 코드입니다.
plt.rc('axes', unicode_minus=False)

# retina 옵션을 통해 해상도를 올립니다.
set_matplotlib_formats('retina')

get_ipython().run_line_magic('matplotlib', 'inline')

# 경고창을 무시하겠습니다.
import warnings
warnings.filterwarnings('ignore')


# ## 1.3 데이터 로드 

# 
# 먼저 크몽의 로그 데이터를 하나씩 가져오겠습니다. 먼저 가져올 데이터는 크몽 어플리케이션의 이벤트와 전환을 나타내는 ```kmong-conversion-v2-.csv``` 입니다. 컬럼 정보는 다음과 같습니다.
# 
# * ```eventcategory```: 앱의 이벤트에 대한 카테고리입니다. 크게 다음의 종류가 있습니다.
#   - ```install```: 앱설치
#   - ```launch```: 앱실행 
#   - ```deeplinkLaunch```: 딥링크 통한 앱실행
#   - ```goal```: 앱 내에서의 활동 여부
#   - ```exit```: 앱 종료
#   - ```foreground```, ```background```: 앱을 foreground, background로 전환
#   - ```launchlnSession```: Session의 시작.
# * ```isfirstactivity```: 해당 이벤트가 해당 유저에 한하여 첫 번째인지 혹은 두 번째 이상인지를 알려주는 값입니다. 
#   - boolean 형식으로, 해당 이벤트가 해당 유저에 한하여 첫 번째 이벤트이면 True, 아니면 False를 갖습니다.
# * ```apppackagename```: 앱의 패키지의 고유한 이름입니다. 안드로이드의 경우 applicationId을, iOS의 경우 Bundle ID를 가져오게 됩니다.
# * ```appversion```: kmong 어플리케이션의 버전입니다.
# * ```devicetype```: 사용자가 kmong app을 실행하고 있는 기기의 제품명입니다.
# * ```devicemanufacturer```: 사용자가 kmong app을 실행하고 있는 기기의 제조회사입니다. 
# * ```osversion```: 사용자가 kmong app을 실행하고 있는 기기의 os 버전입니다.
# * ```canonicaldeviceuuid```: 사용자가 kmong app을 실행하고 있는 기기의 고유 식별자입니다. (사용자를 구분하는 식별자로 이용할 수 있습니다)
# * ```sourcetype```: 해당 로그를 만든 고객이 유입된 경로입니다. 유료 광고 채널, 바이럴 채널, 앱 마켓 등으로 구분합니다.
# * ```channel```: sourcetype과 동일하지만 조금 더 세분화되어 있습니다.
#   - unattributed, WEB, google-play, m_naver, google, (not set), google.adwords, m_naverpowercontents, pc_naver, apple.searchads, facebook, m_daum
# * ```params_campaign```: 마케터가 입력한 캠페인 파라미터 중 캠페인명입니다. 
# * ```params_medium```: 마케터가 입력한 캠페인 파라미터 중 매체입니다.
# * ```params_term```: 마케터가 입력한 캠페인 파라미터 중 키워드입니다.
# * ```inappeventcategory```: 인앱이벤트 식별자값으로 인앱이벤트를 지칭하는 3개의 값(category > action > label) 중 가장 상위에 속하는 구분값입니다.
#   - ```eventcategory```가 goal인 경우에만 제공됩니다.
#   - 차후에 읽어올 funnel 데이터셋과 연결할 수 있습니다.
#   - ex) seller_selling_history.view, gig_detail.view
# * ```inappeventlabel```: categoryid와 동일합니다.
#   - 차후에 읽어올 category 데이터셋과 연결할 수 있습니다.
#   - 인앱이벤트를 지칭하는 3개의 값(category > action > label) 중 마지막에 속하는 구분값입니다.
# * ```eventdatetime```: 모바일 클라이언트 상에서의 실제 이벤트 발생시간입니다. ISO 8601 표준에 따라서 제공됩니다. 
# * ```isfirstgoalactivity```: goal 이벤트의 경우, 해당 Goal Label, Description, Key, Category를 가진 이벤트가 해당 유저에 한하여 첫 번째인지 혹은 두 번째 이상 인지를 알려주는 boolean 값입니다. 예를 들어 동일한 유저로부터 두 번 이상의 같은 Goal 이벤트가 발생한 경우(e.g. 동일한 물건 재구매 등) 이 값은 false가 됩니다.
# 
# * ```event_rank```: 데이터를 정렬하는데 필요한 컬럼입니다. log엔 기록되지 않는 컬럼입니다.

# In[2]:


# kmong-conversion- 관련 csv파일 경로를 전부 가져옵니다.
file_list = glob.glob('data/raw_data/kmong-conversion-*.csv')

# 리스트의 메소드 중 하나인 .sort()를 이용하여 시간 순서대로 리스트를 정렬합니다.
file_list.sort()

file_list[:5]


# In[3]:


from tqdm.notebook import tqdm

# read_csv로 모든 kmong-conversion 데이터를 읽어온 뒤
# 이를 판다스의 concatenate로 하나로 합칩니다.
log = pd.concat([pd.read_csv(csv, low_memory=False) for csv in tqdm(file_list)])

print(log.shape)

log.head()


# **Funnel_ID_app.p**
# 
# 이제 퍼널(Funnel) 데이터를 가져오겠습니다.
# 
# 퍼널은 사용자가 서비스 접속 후 상품을 구매하기까지의 경로 구조를 의미합니다. 결제를 하기 위해서는 무조건 상품 설명을 통해서 방문해야 하고, 상품 설명을 보기 위해서는 해당 상품을 찾을 수 있는 카테고리탭을 통해서만 방문할 수 있기 때문에 가장 마지막 단계 페이지의 방문자가 가장 적을 수 밖에 없습니다. 이러한 구조가 깔대기같아 퍼널이라 불립니다.
# 
# 퍼널을 이용해 전환과 이탈률을 측정함으로써 집중 개선 대상 페이지를 발견할 수 있으며 개선된 페이지의 성과까지 간단히 추적해 나갈 수 있습니다.

# In[4]:


import pickle

# pickle을 활용해 퍼널 데이터를 읽어옵니다.
# 그리고 이 데이터를 funnel이라는 이름의 변수에 저장합니다.
funnel = pickle.load(open('data/kmong_rawdata_app_reference_tables/Funnel_ID_app.p','rb'))

print(funnel.shape)

funnel


# **categories.p**

# 마지막으로 categories.p 데이터를 불러오겠습니다.
# 
# 
# 이 파일은 사용자가 어떤 상품탭에 접속했는지에 대한 상품 분류 정보를 가지고 있습니다.

# In[5]:


categories = pickle.load(open('data/kmong_rawdata_app_reference_tables/categories.p','rb'))

print(categories.shape)
categories


# ## 1.4 결측치 확인

# In[6]:


log.isnull().sum()


# In[7]:


funnel.isnull().sum()


# In[8]:


categories.isnull().sum()


# # 2 데이터 전처리

# ## 2.1 log Data

# 먼저, kmong-conversion.csv 파일부터 정리하겠습니다.

# ### 2.1.1 컬럼명 수정 (canonicaldeviceuuid)

# log 변수에 저장된 컬럼 중 'canonicaldeviceuuid'를 직관적으로 이해 가능하도록 'userid'로 바꾸겠습니다.

# In[9]:


log.head()


# In[10]:


log['user_id'] = log['canonicaldeviceuuid']

log[['user_id', 'canonicaldeviceuuid']].head()


# ###  2.1.2 시간 데이터 정리(eventdatetime)

# In[11]:


log.dtypes


# log 데이터 컬럼별 데이터 타입을 살펴보면 eventdatetime 이 시간이 아닌 object 로 되어 있는 것을 알 수 있습니다. **pd.to_datetime()** 함수를 활용해서 시간 타입으로 바꾼 후, 연/월/일/시/분/초 단위로 나누겠습니다.

# In[12]:


log['eventdatetime'] = pd.to_datetime(log['eventdatetime'])

log[['eventdatetime']].head()


# eventdatetime 컬럼을 변환시키니 '2018-09-28 00:00:00+09:00' 와 같이 timezone 정보가 혼재되어 있어 **dt.tz_localize()** 함수를 사용해 변경했습니다.

# In[13]:


log['eventdatetime'] = log['eventdatetime'].dt.tz_localize(None)

log[['eventdatetime']].head()


# 이제 제대로 변환이 되었습니다. 시간을 연/월/일/시/분/초 단위로 나눠 각각의 컬럼으로 저장하겠습니다.

# In[14]:


log['year'] = log['eventdatetime'].dt.year
log['month'] = log['eventdatetime'].dt.month
log['day'] = log['eventdatetime'].dt.day
log['hour'] = log['eventdatetime'].dt.hour
log['minute'] = log['eventdatetime'].dt.minute
log['second'] = log['eventdatetime'].dt.second

log[['eventdatetime', 'year', 'month', 'day', 'hour', 'minute', 'second']].head()


# * eventdatetime 컬럼이 성공적으로 나눠졌습니다.
# 
# 
# * 아래에서는 48시간을 분과 시간으로 계산하겠습니다.

# ### 2.1.3 접속시간 변환

# **접속 분**
# 
# log 데이터는 9월 28 - 29일(총 48시간)에 대한 기록입니다. 추후 분 단위의 접속 그래프를 출력하기 위해 48시간을 분 단위(총 2880분)로 변환하겠습니다.

# In[15]:


def calculate_minute(log):
    
    # 28일 접속
    if log['day'] == 28:
        return log['hour'] * 60 + log['minute']
    
    # 29일 접속 (익일이므로 1440분을 추가로 더해 줌.)
    else:
        return log['hour'] * 60 + log['minute'] + 1440


# In[16]:


log['total_minutes'] = log.apply(calculate_minute, axis = 1)

log.head()


# **접속 시간**
# 
# 
# log 데이터는 9월 28 - 29일(총 48시간)에 대한 기록입니다. 추후 시간 단위의 접속 그래프를 출력하기 위해 48시간 기준으로 시간을 변환하겠습니다.

# In[17]:


def calculate_hour(log):
    
    # 28일 접속
    if log['day'] == 28:
        return log['hour']
    
    # 29일 접속 (익일이므로 24시간을 추가로 더해 줌.)
    else:
        return log['hour'] + 24


# In[18]:


log['total_hour'] = log.apply(calculate_hour, axis = 1)

log.head()


# ### 2.1.4 접속시간 범주화
# 
# 
# 위에서 변환한 total_minutes 변수는 0 - 2880분의 범위로 그래프로 나타내게 되면 데이터의 큰 흐름을 한 눈에 보기 힘듭니다. 그래서 범주화 작업을 수행하겠습니다. 

# In[19]:


def time_count(minutes):
    for i in range(0, 2881, 15):        
        if (minutes >= i) & (minutes < i+15):
            return i


# In[20]:


log['elapsed(int)'] = log['total_minutes'].apply(time_count)

print(log.shape)
log.head()


# ### 2.1.5 osversion

# osversion 컬럼은 ' iOS11.4.1' 와 같이 스마트폰 디바이스의 운영체제와 버전 두 가지의 정보를 가지고 있습니다. 추후 분석과정에서 용이하게 처리하기 위해 두 정보를 분리하여 각각의 컬럼으로 저장하겠습니다.

# In[21]:


def find_ostype(osversion):
    if 'iOS' in osversion:
        return 'iOS'
    else:
        return 'Android'
        
log['os_type'] = log['osversion'].apply(find_ostype)


# In[22]:


def find_osversion(osversion):
    return osversion.replace('iOS', '').replace('Android', '')

log['os_version'] = log['osversion'].apply(find_osversion)

log[['osversion', 'os_type', 'os_version']].head()


# ### 2.1.6 devicemanufacturer

# devicemanufacturer 컬럼은 사용자가 현재 사용하고 있는 스마트폰 디바이스를 제조한 제조사의 정보가 들어 있습니다. 다양한 표기로 이루어진 데이터를 통일시키겠습니다.
# 
# * samsung이라고 적혀있는 값은 앞 글자를 대문자로 바꿉니다. (=Samsung)
# * LGE와 LG Electronics라는 값은 LG로 통일합니다.
# * Apple, Samsung, LG를 제외한 나머지는 Other로 묶습니다.

# In[23]:


log['devicemanufacturer'].value_counts()


# In[24]:


def change_devicemanufacturer_name(devicemanufacturer):
    if devicemanufacturer == 'samsung':
        return 'Samsung'
    
    elif devicemanufacturer == 'Apple':
        return 'Apple'
    
    elif devicemanufacturer == 'LGE' or devicemanufacturer == 'LG Electronics':
        return 'LG'
    
    else:
        return 'Other'
    
log['new_devicemanufacturer'] = log['devicemanufacturer'].apply(change_devicemanufacturer_name)

log['new_devicemanufacturer'].value_counts()


# ### 2.1.7 channel

# channel 컬럼을 사용자가 크몽 서비스에 유입된 경로를 기록한 정보입니다. 마찬가지로 혼재된 표기를 통일시키는 작업을 수행하겠습니다.
# 
# * 컬럼값에 google이라고 들어간 값(ex: google-play, google.adwords, etc)은 전부 google로 통일합니다.
# 
# * 컬럼값에 daum이라고 들어간 값(ex: m_daum, etc)은 전부 daum으로 통일합니다.
# 
# * 컬럼값이 naver라고 들어간 값(ex: m_naver, pc_naver, m_naverpowercontents, etc)은 전부 naver로 통일합니다.
# 
# * 컬럼값에 apple이라고 들어간 값(ex: apple.searchads, etc)은 전부 apple로 통일합니다.
# 
# * 컬럼값에 WEB이라고 들어간 값(ex: WEB)은 전부 web으로 통일합니다.

# In[25]:


log['channel'].value_counts()


# In[26]:


def channel_category(channel):
    if pd.isnull(channel) == False:
        
        if 'unattributed' in channel:
            return 'unattributed'
        
        elif 'google' in channel:
            return 'google'

        elif 'daum' in channel:
            return 'daum'

        elif 'naver' in channel:
            return 'naver'

        elif 'apple' in channel:
            return 'apple'

        elif 'WEB' in channel:
            return 'web'

        elif 'facebook' in channel:
            return 'facebook'
        
        elif '(not set)' in channel:
            return '(not set)'
    
    else:
        return channel
    
log['new_channel'] = log['channel'].apply(channel_category)

log['new_channel'].value_counts()


# ### 2.1.8 inappeventcategory

# inappeventcategory에는 사용자 액티비티를 나타내는 정보가 들어있습니다. 크몽에 방문한 고객이 상품 페이지를 보고 있는지, 구매를 진행중인지 등에 대한 정보입니다. 추후, inappeventcategory에 있는 정보는 차후 퍼널(funnel) 데이터를 합치는데 사용되기도 합니다.
# 
# * viewcategory - inappeventcategory에서 언더바(_)를 기준으로 왼쪽 텍스트만 가져옵니다. 언더바가 없을 경우 점(.)의 왼쪽 텍스트만 가져옵니다.
# 
# * viewid - inappeventcategory에서 점(.)의 왼쪽 텍스트만 가져옵니다.
# 
# * viewaction - inappeventcategory에서 점(.)의 오른쪽 텍스트만 가져옵니다.
# 

# In[27]:


# viewcategory 컬럼 생성 함수

# inappeventcategory 컬럼에서 결측치가 아닌 데이터에 한해 문자열을 분리했습니다.

def make_viewcategory(inappeventcategory):
    if pd.isnull(inappeventcategory) == False:
        if '_' in inappeventcategory:
            return inappeventcategory.split('_')[0]
        else:
            return inappeventcategory.split('.')[0]
    else:
        return inappeventcategory
    
log['viewcategory'] = log['inappeventcategory'].apply(make_viewcategory)


# In[28]:


# viewid 컬럼 생성 함수

# inappeventcategory 컬럼에서 결측치가 아닌 데이터에 한해 문자열을 분리했습니다.

def make_viewid(inappeventcategory):
    if pd.isnull(inappeventcategory) == False:
        if '.' in inappeventcategory:
            return inappeventcategory.split('.')[0]
        else:
            return inappeventcategory
    else:
        return inappeventcategory
    
log['viewid'] = log['inappeventcategory'].apply(make_viewid)


# In[29]:


# viewaction 컬럼 생성 함수

# inappeventcategory 컬럼에서 결측치가 아닌 데이터에 한해 문자열을 분리했습니다.

def make_viewaction(inappeventcategory):
    if pd.isnull(inappeventcategory) == False:
        if '.' in inappeventcategory:
            return inappeventcategory.split('.')[1]
        else:
            return inappeventcategory
    else:
        return inappeventcategory
    
log['viewaction'] = log['inappeventcategory'].apply(make_viewaction)


# In[30]:


log[['inappeventcategory', 'viewcategory', 'viewid', 'viewaction']].head()


# ### 2.1.9 컬럼 삭제

# 위에서 전처리한 컬럼은 두고 기존 컬럼을 삭제하겠습니다. 다만, 앞서 언급했듯이, inappeventcategory 컬럼은 데이터를 합치는 데 사용해야 하므로 남겨두겠습니다.

# In[31]:


log.drop(['osversion', 'devicemanufacturer', 'canonicaldeviceuuid', 'channel'], axis = 1, inplace = True)


# In[32]:


print(log.shape)
log.head()


# ### 2.1.10 컬럼명 통일 및 컬럼 정렬

# e데이터를 분석할 때 컬럼명의 형식을 동일하게 유지하는 것이 중요합니다. 본 분석에서는 단어와 단어 사이에는 언더바(_)로 구분하겠습니다. 기존의 하이픈(-). 띄어쓰기 등은 모두 언더바로 수정하겠습니다.

# In[33]:


log.columns = ['event_category', 'is_first_activity', 'app_package_name', 'app_version', 'device_type', 'source_type', 
               'params_campaign', 'params_medium', 'params_term', 'in_app_event_category', 'in_app_event_label', 'event_datetime',
               'row_uuid', 'is_first_goal_activity', 'event_rank', 'user_id', 'year', 'month', 'day', 'hour', 'minute', 'second',
               'total_minutes', 'total_hour', 'elapsed(int)', 'os_type', 'os_version', 'device_manufacturer', 'channel', 
               'view_category', 'view_id', 'view_action']

log.head()


# * 컬럼명은 모두 통일되었습니다.
# 
# 
# 컬럼 정렬 기준은 중요한 컬럼은 좌측, 상대적으로 덜 중요한 컬럼은 우측으로 위치시키겠습니다. 또한, 비슷한 정보를 가진 컬럼이나 연관되어 있는 컬럼은 묶어서 정렬하겠습니다.

# In[34]:


columns_sort_list = ['row_uuid', 'app_package_name', 'user_id', 'event_datetime', 'elapsed(int)', 'total_hour', 'total_minutes', 'year',
               'month', 'day', 'hour', 'minute', 'second', 'device_manufacturer', 'device_type', 'os_type', 'os_version', 'app_version', 
               'event_category', 'view_category', 'view_id', 'view_action', 'in_app_event_category', 'in_app_event_label',
               'source_type', 'channel', 'params_campaign', 'params_medium', 'params_term', 'is_first_activity',
               'is_first_goal_activity', 'event_rank']

log = log[columns_sort_list]

print(log.shape)
log.head()


# * 정렬이 모두 마무리되었습니다.

# ## 2.2 funnel Data

# 다음으로는 퍼널(funnel) 데이터를 정리하겠습니다. 퍼널 데이터에는 크몽 서비스에서 사용하는 퍼널에 대한 부연 설명을 담고 있습니다. 

# ### 2.2.1 컬럼명 수정 및 정렬

# In[35]:


funnel.head()


# In[36]:


# 컬럼 정렬
column_list = ['Lv1', 'Lv2', 'viewid', 'viewid desc', 'funnel name', 'funnel desc']

funnel = funnel[column_list]

# 컬럼명 수정 (log Data와 같이 소문자 통일, 단어와 단어 사이에 언더바('_') 삽입)
funnel.columns = ['lv1', 'lv2', 'view_id', 'view_desc', 'funnel_name', 'funnel_desc']

print(funnel.shape)
funnel.head()


# ## 2.3 category Data

# ### 2.3.1 컬럼명 수정 및 정렬¶

# In[37]:


print(categories.shape)
categories.head()


# category 데이터는 컬럼명만 위와 같은 형식으로 수정하겠습니다.

# In[38]:


# 컬럼명 수정 (log Data와 같이 소문자 통일, 단어와 단어 사이에 언더바('_') 삽입)
categories.columns = ['depth', 'category_id', 'category_name', 'category1_id', 'category2_id', 'category3_id', 'category1',
                 'category2', 'category3']

print(categories.shape)
categories.head()


# ## 2.4 데이터 합치기

# 전처리를 마친 log, funnel, category 파일을 하나로 합치겠습니다. **pd.merge()** 함수를 활용하겠습니다.
# 
# 먼저, log 데이터와 funnel 데이터를 합치겠습니다.

# In[39]:


print(log.shape)
log.head()


# In[40]:


print(funnel.shape)
funnel.head()


# log 데이터에는 중요한 정보가 많으므로 모두 살리고, funnel 데이터는 log 데이터에 일치하는 것만 살리겠습니다.

# In[41]:


new_log = pd.merge(log, funnel, how = 'left')

print(new_log.shape)
new_log.head()


# 위에서 합친 new_log 데이터와 category 데이터를 합치겠습니다.
# 
# 마찬가지로 new_log 데이터에 중요한 정보가 많으므로 **left merge**를 실시할 것이며, new_log의 'in_app_event_label' 컬럼과 categories의 'category_id' 컬럼이 연관이 있으므로 이를 활용하여 데이터를 합치겠습니다.

# In[42]:


print(new_log.shape)
new_log.head()


# In[43]:


print(categories.shape)
categories.head()


# in_app_event_label와 category_id 를 사용하여 merge 하기 위해 left_on , right_on 을 사용했으며, 왼쪽 데이터 프레임에 일치하는 데이터만 필요하므로 how='left'를 사용하겠습니다.

# In[44]:


log_data = pd.merge(new_log, categories, left_on = 'in_app_event_label', right_on = 'category_id', how = 'left')

print(log_data.shape)
log_data.head()


# * 컬럼을 기준으로 세 데이터가 성공적으로 합쳐졌습니다.

# ### 2.4.1 컬럼 삭제

# 최종적으로 43개의 컬럼이 저장되었습니다. 모든 컬럼을 분석에 활용하지 않을 것이므로 필요한 컬럼만 남기고 모두 삭제하겠습니다.
# 
# 아래의 컬럼을 삭제하겠습니다.
# 
# * in_app_event_category
# * in_app_event_label
# * source_type
# * lv1, lv2
# * funnel_name, depth
# * category_id, category1_id, category2_id, category3_id
# * event_rank

# In[45]:


log_data = log_data.drop(['in_app_event_category', 'in_app_event_label', 'source_type', 'lv1', 'lv2', 'funnel_name', 'depth', 'category_id',
              'category1_id', 'category2_id', 'category3_id', 'event_rank'], axis = 1)

print(log_data.shape)
log_data.head()


# * 컬럼 수가 줄어들었으니 성공적으로 컬럼이 제거되었습니다.

# ### 2.4.2 컬럼 정렬

# 중요한 컬럼은 좌측으로, 상대적으로 덜 중요한 정보는 우측으로 정렬하겠습니다.

# In[46]:


columns_sort_list = ['row_uuid', 'app_package_name', 'user_id', 'event_datetime', 'elapsed(int)', 'total_hour', 'total_minutes', 
                     'year', 'month', 'day', 'hour', 'minute', 'second', 'device_manufacturer', 'device_type', 'os_type', 'os_version',
                     'app_version', 'event_category', 'view_category', 'view_id', 'view_action', 'funnel_desc', 'view_desc', 
                     'category_name', 'category1', 'category2', 'category3', 'channel', 'params_campaign', 'params_medium',
                     'params_term', 'is_first_activity', 'is_first_goal_activity']

log_data = log_data[columns_sort_list]

print(log_data.shape)
log_data.head()


# ### 2.4.3 인덱스 지정

# **row_uuid**컬럼을 인덱스로 지정하면 데이터의 행을 불러오고 분석 할 때 큰 도움이 되므로 인덱스로 지정하겠습니다.

# In[47]:


df = log_data.set_index(['user_id', 'row_uuid'])

print(df.shape)
df.head()


# **row_uuid** 컬럼이 인덱스로 지정되어 컬럼 수가 1개 줄어든 것을 확인했습니다.

# # 3 데이터 검색 클래스

# 
# **Find_log class**
# 
# 
#    * 함수 설명
# 
#      * find_userid : 유저의 id별 모든 로그 데이터 검색 
#      
#      * find_columns : 유저의 id 및 특정 컬럼 데이터 검색
#      
#      * find_item : 유저의 id + 선택 컬럼의 특정 값 데이터 검색
#    
#    
#    * 매개변수 설명
#    
#      * userid : 유저의 id
#      
#      * columns : 로그 데이터의 컬럼
#      
#      * item : 컬럼의 값
#      
#     
#    * 결과 출력
#      
#      * find_userid 함수
#       
#        - userid 입력 : 입력한 유저의 데이터 출력
#        
#        - userid 미입력 : 모든 데이터 출력
#        
#      * find_columns 함수
#      
#        - userid 및 컬럼 입력 : user id의 선택 컬럼 출력
#        
#        - userid 입력, 컬럼 미입력 : user id의 모든 컬럼 출력
#        
#        - userid 미입력, 컬럼 입력 : 모든 user id의 선택 컬럼 출력
#        
#        - userid 및 컬럼 미입력 : 모든 데이터 출력
#               
#      * find_item 함수
#        
#        - 컬럼 및 item 입력 : 선택한 컬럼의 선택 값 log 데이터 출력
# 
#        - 컬럼 입력, item 미입력 : 전체 log 데이터 출력
# 
#        - 컬럼 미입력, item 입력 : 전체 log 데이터 출력
# 
#        - 컬럼 및 , select_item 미입력 : 전체 log 데이터 출력

# ## 3.1 클래스 구현

# In[48]:


class Find_log:
    
    # __init__ 메서드를 통해 Find_log 클래스에서 사용될 객체 초깃값을 설정하겠습니다. 
    def __init__(self, userid = None, columns = None, item = None):
        self.userid = userid
        self.columns = columns
        self.item = item
    
    # userid 별 로그데이터 검색 함수를 구현하겠습니다.
    def find_userid(self):
        if self.userid != None:
            
            # userid 가 1개일 경우
            if len(self.userid) < 2:
                print(f'선택하신 {self.userid} 이용자의 로그 데이터를 출력합니다.\n')
                return df.loc[self.userid].sort_values(by = ['user_id', 'event_datetime'], ascending = False)
            
            # userid 가 2개 이상일 경우 
            else:
                print(f'선택하신 {self.userid} 이용자의 로그 데이터를 출력합니다.\n')
                return df.loc[self.userid].sort_values(by = 'event_datetime', ascending = False)

        else:
            print ('Warning: 값을 입력하지 않아 전체 로그 데이터를 출력합니다.\n')
            return df
    
    # userid별 특정 컬럼만을 검색하는 함수를 구현하겠습니다.
    def find_columns(self):
        if self.columns != None:
            
            # 컬럼 갯수가 1개일 경우
            if len(self.columns) < 2:
                print(f'{self.userid} 이용자의 로그 데이터 중에서 입력하신 컬럼만 출력합니다.\n')
                return df.loc[self.userid, self.columns].sort_values(by = 'event_datetime', ascending = False)
            
            # 컬럼 갯수가 2개 이상일 경우
            else:
                print(f'{self.userid} 이용자의 로그 데이터 중에서 입력하신 컬럼만 출력합니다.\n')
                return df.loc[self.userid, self.columns].sort_values(by = 'event_datetime', ascending = False)

        else:
            print ('Warning: 값을 입력하지 않아 전체 로그 데이터를 출력합니다.\n')
            return df
    
    # 특정 컬럼에서 입력한 값을 기준으로 데이터를 검색하는 함수를 구현하겠습니다.
    def find_item(self):
        if self.item != None:
            
            # 컬럼 값이 1개일 경우
            if len(self.item) < 2:
                print(f'{self.userid} 이용자의 데이터 중에서 {self.columns} 컬럼의 {self.item} 값을 가진 데이터를 출력합니다.\n')
                viewid = df[df[self.columns].isin(self.item)]
                return viewid.loc[self.userid].sort_values(by = 'event_datetime', ascending = False)
            
            # 컬럼 값이 2개 이상일 경우
            else:
                print(f'{self.userid} 이용자의 데이터 중에서 {self.columns} 컬럼의 {self.item} 값을 가진 데이터를 출력합니다.\n')
                viewid = df[df[self.columns].isin(self.item)]
                return viewid.loc[self.userid].sort_values(by = 'event_datetime', ascending = False)

        else:
            print ('Warning: 값을 입력하지 않아 전체 로그 데이터를 출력합니다.\n')
            return df


# ## 3.2 데이터 검색

# ### 3.2.1 find_userid

# userid를 입력하여 데이터를 검색하겠습니다.

# In[49]:


id = ['00000000-0000-0000-0000-000000000000','fff40190-d751-425a-9813-2284072e47f5']

find_log = Find_log(id)

find_log.find_userid()


# * '00000000-0000-0000-0000-000000000000','fff40190-d751-425a-9813-2284072e47f5' 두 이용자의 모든 로그데이터가 성공적으로 검색되었습니다.

# ### 3.2.2 find_columns

# userid와 컬럼을 입력하여 데이터를 검색하겠습니다.
# 

# In[50]:


userid = 'fff40190-d751-425a-9813-2284072e47f5'
cols = ['event_datetime', 'event_category', 'view_id', 'view_action', 'funnel_desc','view_desc']

find_log = Find_log(userid, cols)
find_log.find_columns()


# * 'fff40190-d751-425a-9813-2284072e47f5' 이용자의 'event_datetime', 'event_category', 'view_id', 'view_action', 'funnel_desc','view_desc' 컬럼데이터가 성공적으로 검색되었습니다.

# ### 3.2.3 find_item

# userid, 컬럼, 컬럼 값을 입력하여 데이터를 검색하겠습니다.

# In[51]:


userid = 'fff40190-d751-425a-9813-2284072e47f5'
cols = 'view_id'
item = ['home', 'inbox_detail', 'inbox', 'gig_detail', 'thankyou']

find_log = Find_log(userid, cols, item)
find_log.find_item()


# * 'fff40190-d751-425a-9813-2284072e47f5' 이용자의 'view_id' 컬럼에서 'home', 'inbox_detail', 'inbox', 'gig_detail', 'thankyou' 의 데이터만 성공적으로 출력되었습니다.

# # 4 그래프 출력 클래스

# 
# **Pageview_graph class**
# 
# 
#    * 함수 설명
# 
#      * graph_view : 단일 그래프 검색
#      
#      * comparative_graph : 특정 컬럼의 두 개의 값 비교 그래프 검색
#      
#      * total_comparative_graph : 특정 컬럼의 한 개의 값과 전체 값 비교 그래프 검색
#      
#      * select_graph : 특정 컬럼의 여러 개의 값과 전체 값 비교 그래프(리스트 형태) 검색
#      
#      * total_graph : 특정 컬럼의 전체 값 비교 그래프 검색
#    
#    
#    * 매개변수 설명
#    
#      * columns : 검색할 컬럼
#      
#      * values1 : 검색할 컬럼의 첫 번째 값
#      
#      * values2 : 검색할 컬럼의 두 번째 값
#      
#      * value_list : 검색할 컬럼의 값 리스트
#      
#     
#    * 결과 출력
#      
#      * graph_view 함수
#       
#        - columns, values1 입력 : 입력한 컬럼-값 단일 그래프 출력
#        
#      * comparative_graph 함수
#      
#        - columns, values1, values2 입력 : 입력한 컬럼의 값1-값2 비교 그래프 출력
#               
#      * total_comparative_graph 함수
#        
#        - columns, values1 입력 : 입력한 컬럼의 값-전체 비교 그래프 출력
# 
#      * select_graph 함수
#        
#        - columns, values_list 입력 : 입력한 컬럼의 여러 개의 값(갯수 제한 없음) 비교 그래프 출력
# 
#      * total_graph 함수
#        
#        - columns 입력 : 입력한 컬럼의 전체 그래프 출력
# 

# ## 4.1 클래스 구현

# 로그가 기록된 2018년 09월 28일부터 29일까지의 48시간동안 발생한 페이지뷰의 변화량을 출력하는 클래스를 구현하겠습니다.

# In[52]:


class Pageview_graph:
    
    # 초깃값을 설정하겠습니다.
    def __init__(self, columns = None, values1 = None, values2 = None, value_list = []):
        
        self.columns = columns
        
        self.values1 = values1
        
        self.values2 = values2
        
        self.value_list = value_list
    
    # 단일 그래프 함수를 생성하겠습니다.
    def graph_view(self):
        
        data = df[df[self.columns] == self.values1]
        
        pivot_table = pd.pivot_table(data = data, index = 'elapsed(int)', values = self.columns, aggfunc = 'count')
        
        pivot_table.columns = ['count']
        
        plt.figure(figsize = (18, 3))
        
        ax = sns.lineplot(data = pivot_table, x = pivot_table.index, y = 'count', label = self.values1)
        
        ax.set_title(f'{self.columns}의 {self.values1} graph')
        
        return ax
    
    # 두 그래프를 비교하는 함수를 생성하겠습니다.
    def comparative_graph(self):
        
        data_1 = df[df[self.columns] == self.values1]
        
        data_2 = df[df[self.columns] == self.values2]
        
        pivot_table_1 = pd.pivot_table(data = data_1, index = 'elapsed(int)', values = self.columns, aggfunc = 'count')
        
        pivot_table_1.columns = ['count']
        
        pivot_table_2 = pd.pivot_table(data = data_2, index = 'elapsed(int)', values = self.columns, aggfunc = 'count')
        
        pivot_table_2.columns = ['count']
        
        plt.figure(figsize = (18, 3))
        
        ax = sns.lineplot(data = pivot_table_1, x = pivot_table_1.index , y = 'count', label = self.values1)
        
        ax = sns.lineplot(data = pivot_table_2, x = pivot_table_2.index , y = 'count', label = self.values2)
        
        ax.set_title(f'{self.columns}의 {self.values1} vs {self.values2} graph')
        
        return ax
    
    # 선택한 그래프와 전체 그래프를 비교하는 함수를 생성하겠습니다.
    def total_comparative_graph(self):
        
        data = df[df[self.columns] == self.values1]
        
        total = pd.pivot_table(data = df, index = 'elapsed(int)', values = self.columns, aggfunc = 'count')
        
        total.columns = ['count']
        
        pivot_table = pd.pivot_table(data = data, index = 'elapsed(int)', values = self.columns, aggfunc = 'count')
        
        pivot_table.columns = ['count']
        
        plt.figure(figsize = (18, 3))
        
        ax = sns.lineplot(data = total, x = pivot_table.index , y = 'count', label = 'total')
        
        ax = sns.lineplot(data = pivot_table, x = pivot_table.index , y = 'count', label = self.values1)
        
        ax.set_title(f'{self.columns}의 total vs {self.values1} graph')
        
        return ax
    
    # 리스트 형태의 여러 그래프를 출력하는 함수를 생성하겠습니다.
    def select_graph(self):
        
        data = df[['elapsed(int)', self.columns]]
        
        target_list = list(data[self.columns].unique())
        
        concat_df = data[["elapsed(int)"]].apply(pd.value_counts).sort_index()
        
        concat_df[self.columns] = 'total'

        for i in target_list:

            type_name = str(i)

            i = data[data[self.columns]==i].copy()

            i = i[["elapsed(int)"]].apply(pd.value_counts).sort_index()

            i[self.columns] = type_name

            concat_df = concat_df.append(i)
        
        concat_df.columns = ["count", self.columns]

        target_list.append("total")

        total_df =  concat_df[concat_df[self.columns] == 'total']
        
        select_df = concat_df[concat_df[self.columns].isin(self.value_list)]

        result = pd.concat([total_df, select_df])
        
        plt.figure(figsize = (18, 3))
        
        ax = sns.lineplot(data = result, x = result.index, y = 'count', hue = self.columns)
        
        ax.set_title(f'{self.columns}의 {self.value_list} graph')
        
        plt.legend(loc = 'upper right')
        
        return ax
    
    # 전체 그래프를 출력하는 함수를 생성하겠습니다.
    def total_graph(self):
        
        data = df[['elapsed(int)', self.columns]]
        
        value_list = list(data[self.columns].unique())
        
        sorted_df = data[['elapsed(int)']].apply(pd.value_counts).sort_index()
        
        sorted_df[self.columns] = 'total'
        
        for i in value_list:

            type_name = str(i)

            new_data_df = data[data[self.columns]==i].copy()

            new_data_df = new_data_df[['elapsed(int)']].apply(pd.value_counts).sort_index()

            new_data_df[self.columns] = type_name

            sorted_df = sorted_df.append(new_data_df)

        sorted_df.columns = ['count', self.columns]

        value_list.append('total')

        plt.figure(figsize = (18, 3))
        
        ax = sns.lineplot(data = sorted_df, x = sorted_df.index, y = 'count', hue = self.columns)
        
        ax.set_title(f'{self.columns}의 graph(모든 값)')
        
        plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0., ncol=3)
        
        return ax


# ### 4.1.1 os_type

# **os_type 컬럼 중, 'iOS'만을 그래프로 출력하겠습니다. (Pageview_graph 클래스의 plot 함수 이용)**

# In[53]:


column = 'os_type'
value = 'iOS'

plot = Pageview_graph(column, value)
plot.graph_view()


# **os_type 컬럼 중, 두 가지 케이스를 그래프로 출력하겠습니다. (Pageview_graph 클래스의 comparative_graph 함수 이용)**

# In[54]:


column = 'os_type'
values1 = 'iOS'
values2 = 'Android'

plot = Pageview_graph(column, values1, values2)
plot.comparative_graph()


# **os_type 컬럼 중, 'iOS'와 전체 데이터를 그래프로 출력하겠습니다. (Pageview_graph 클래스의 total_comparative_graph 함수 이용)**

# In[55]:


column = 'os_type'
value = 'iOS'

plot = Pageview_graph(column, value)
plot.total_comparative_graph()


# ### 4.1.2 os_version

# **os_version 컬럼 중, '11.4.1'만을 그래프로 출력하겠습니다.(Pageview_graph 클래스의 plot 함수 이용)**

# In[56]:


column = 'os_version'
value = '11.4.1'

plot = Pageview_graph(column, value)
plot.graph_view()


# **os_version 컬럼 중, 두 가지 케이스를 그래프로 출력하겠습니다. (Pageview_graph 클래스의 comparative_graph 함수 이용)**

# In[57]:


column = 'os_version'
values1 = '11.4.1'
values2 = '7.0'

plot = Pageview_graph(column, values1, values2)
plot.comparative_graph()


# **os_version 컬럼 중, 여러 컬럼(리스트 형태)을 그래프로 출력하겠습니다. (Pageview_graph 클래스의 select_graph 함수 이용)**

# In[58]:


column = 'os_version'
type_value_list = ['11.4.1', '7.0', '4.3', '11.0']

plot = Pageview_graph(column, value_list = type_value_list)
plot.select_graph()


# ### 4.1.3 device_type

# **device_type 컬럼 중, 'iPhone'만을 그래프로 출력하겠습니다. (Pageview_graph 클래스의 plot 함수 이용)**

# In[59]:


column = 'device_type'
value = 'iPhone'

plot = Pageview_graph(column, value)
plot.graph_view()


# **device_type 컬럼 중, 'iPhone'와 전체 데이터를 그래프로 출력하겠습니다. (Pageview_graph 클래스의 total_comparative_graph 함수 이용)**

# In[60]:


column = 'device_type'
value = 'iPhone'

plot = Pageview_graph(column, value)
plot.total_comparative_graph()


# **device_type 컬럼 중, 여러 컬럼(리스트 형태)을 그래프로 출력하겠습니다. (Pageview_graph 클래스의 select_graph 함수 이용)**

# In[61]:


column = 'device_type'
type_value_list = ['iPhone', 'SM-N950N', 'SM-J700T']

plot = Pageview_graph(column, value_list = type_value_list)
plot.select_graph()


# **device_type 컬럼을 모두 출력하겠습니다. (Pageview_graph 클래스의 total_graph 함수 이용)**

# In[62]:


column = 'device_type'

plot = Pageview_graph(column)
plot.total_graph()


# ### 4.1.4 app_version

# **app_version 컬럼 중, ''3.3.5'만을 그래프로 출력하겠습니다. (Pageview_graph 클래스의 plot 함수 이용)**

# In[63]:


column = 'app_version'
value = '3.3.5'

plot = Pageview_graph(column, value)
plot.graph_view()


# **app_version 컬럼 중, 두 가지 케이스를 그래프로 출력하겠습니다. (Pageview_graph 클래스의 comparative_graph 함수 이용)**

# In[64]:


column = 'app_version'
values1 = '3.3.5'
values2 = '3.3.2'

plot = Pageview_graph(column, values1, values2)
plot.comparative_graph()


# **app_version 컬럼 중, 여러 컬럼(리스트 형태)을 그래프로 출력하겠습니다. (Pageview_graph 클래스의 select_graph 함수 이용)**

# In[65]:


column = 'app_version'
type_value_list = ['4.0.4', '3.1.5', '3.2.21', '3.2.0']

plot = Pageview_graph(column, value_list = type_value_list)
plot.select_graph()


# # 5 데이터 분석

# ## 5.1 잔존 분석

# 고객이 앱에서 머문 시간을 의미하는 잔존시간 분석을 실시하겠습니다.
# 
# 
# 유저별 연속된 log사이의 시간 간격을 log duration으로 정의하여 고객의 잔존시간을 구하겠습니다.
# 
# 
# 분석에 앞서 user_id 기준으로 정렬하여 중복값을 제외하여 user_id별 인덱스를 부여하겠습니다.

# In[66]:


# unique() 기능을 사용하기 전에 user_id 컬럼을 기준으로 정렬하겠습니다.
sorted_user_id = log_data.sort_values(by = 'user_id')

# unique() 기능을 활용한 값을 user_id에 저장하겠습니다.
user_id = log_data['user_id'].unique()

user_id


# In[67]:


# 새로운 user_id는 연속된 자연수들로 지정합니다. range()와 len()을 사용하여 user_id의 개수만큼의 연속된 정수를 만들겠습니다.

n_user_id = []
for i in range(len(user_id)):
    n_user_id.append(i)

n_user_id[:5]


# In[68]:


# python 내장 함수인 zip()을 이용하여 기존의 user_id와 새로운 id를 묶습니다.
id_zip = zip(user_id, n_user_id)

print(id_zip)

# zip()의 결과를 구체적으로 보기 위하여 list로 변환하여 상위 5개만 출력하겠습니다.
list(zip(user_id, n_user_id))[:5]


# In[69]:


# 새로운 id와 기존의 user_id가 대응된 딕셔너리 타입 변수를 생성하겠습니다.
id_dict = dict(id_zip)

sorted(id_dict.items(), key=lambda x: x[1], reverse = False)[:10]


# In[70]:


# log_data 에 id_idct를 mapping하여 새로운 user_id컬럼인 n_user_id를 만들겠습니다.

log_data['n_user_id'] = log_data['user_id'].map(id_dict)

log_data[['user_id', 'n_user_id']].head()


# 현재 log 시간 이후의 log 시간을 가져오기 위해 **groupby().shift(-1)** 을 사용하겠습니다. 만약, 현재 log 시간이 마지막이라면, 다음 log 시간은 NaT(Not a Time) 값이 출력됩니다.

# In[71]:


# 현재 log 시간의 바로 다음 log 시간을 가져오겠습니다.

log_data['timestamp_after'] = log_data.groupby(['n_user_id'])['event_datetime'].shift(-1)

log_data.head()


# event_datetime 과 timestamp_after 간의 차이를 계산하여 log_duration을 구하겠습니다. 
# 
# 위에서 언급한 NaT 값은 연산시 NaN값이 되므로 이후에 NaN값을 0으로 채우겠습니다.
# 
# log_duration을 계산하고 NaN값(마지막 로그)는 0으로 채워 log_duration 컬럼에 저장하겠습니다.

# In[72]:


# log_duration을 계산하겠습니다.
log_data['log_duration'] = log_data['timestamp_after'] - log_data['event_datetime'] 

# 마지막 NAT 값을 0으로 채우겠습니다.
log_data['log_duration'] = log_data['log_duration'].fillna(pd.Timedelta(0))

log_data[['event_datetime','timestamp_after','log_duration']].head()


# 분석의 편의를 위하여 **total_seconds()** 메서드를 이용하여 log_duration을 초로 환산하겠습니다.
# 
# 마지막으로, **astype()** 메서드를 이용하여 log_duration 컬럼을 float으로 변환하겠습니다.

# In[73]:


log_data['log_duration'] = log_data['log_duration'].dt.total_seconds().astype('float')

log_data[['n_user_id', 'event_datetime', 'timestamp_after', 'log_duration']].head(30)


# 유저가 한 번 홈페이지에 접속하여 나가기까지의 일련의 활동을 한 cycle 이라 정의하겠습니다.
# 
# cycle 을 구하기 위해서 고객이 cycle을 종료하고 앱을 나갔는지 여부(boolean)인 is_out이라는 컬럼을 만들겠습니다.
# 
# is_out의 조건은 아래와 같이 2가지가 정의했습니다.
# 
# 조건 1) log_duration이 0이면 고객의 당일 마지막 log입니다.
# 
# 조건 2) event_category 컬럼 값이 exit 인 경우는 앱을 나간 것이라 하겠습니다.
# 
# 조건 3) log_duration이 2시간 이상이면 한 cycle을 돌았다고 가정하겠습니다.

# In[74]:


# is_out 컬럼을 생성하기 위해 함수를 만들어 적용시키겠습니다.
def cycle(x):
    if (x['log_duration'] == 0) or (x['event_category'] == 'exit') or (x['log_duration'] >= 7200):
        return True
    else:
        return False

log_data['is_out'] = log_data.apply(cycle, axis = 1)

log_data[['n_user_id','event_datetime', 'timestamp_after', 'log_duration', 'is_out']].head(15)


# In[75]:


# 'n_user_id' 와 'event_datetime' 컬럼 기준으로 데이터를 정렬하고 인덱스를 다시 지정하겠습니다.
sorted_log_data = log_data.sort_values(by = ['n_user_id', 'event_datetime'], ascending = True)

sorted_log_data = sorted_log_data.reset_index(drop = True)

sorted_log_data.head()


# In[76]:


# is_out 컬럼이 True 인 경우에만 log_duration 컬럼 값을 0으로 지정하겠습니다.
sorted_log_data.loc[sorted_log_data['is_out'] == True, 'log_duration'] = 0

sorted_log_data[['n_user_id','event_datetime', 'timestamp_after', 'log_duration', 'is_out']].head(50)


# 이제 cycle을 구하여 번호를 부여할 것입니다.
# 
# 번호는 cycle별 고유 번호(cycle_idx_unique)와 고객별 0부터 시작하는 daily cycle 번호(cycle_idx_daily)를 부여합니다.

# In[77]:


# cycle별 고유번호 지정
sorted_log_data['cycle_idx_unique'] = (sorted_log_data['is_out']
                                 .cumsum()
                                 .shift(1)
                                 .fillna(0)
                                 .astype(int)
                                )

sorted_log_data[['n_user_id','event_datetime', 'timestamp_after', 'log_duration', 'is_out', 'cycle_idx_unique']].head(30)


# In[78]:


# daily cycle 번호 지정
sorted_log_data['cycle_idx_daily'] = (sorted_log_data.groupby('n_user_id')['is_out']
                                           .cumsum()
                                           .shift(1)
                                           .fillna(0)
                                           .astype(int)
                                            )

# user마다 첫 cycle_idx_daily가 1로 되어있기 때문에 이를 0으로 바꿔줍니다.
head_index = sorted_log_data.groupby('n_user_id')['cycle_idx_daily'].head(1).index
sorted_log_data.loc[head_index, 'cycle_idx_daily'] = 0

sorted_log_data[['n_user_id','event_datetime', 'timestamp_after', 'log_duration', 'is_out','cycle_idx_daily']].head(30)


# 위에서 구한 cycle을 이용한 분석을 수행하겠습니다.
# 
# cycle별 log 수(접속별 활동 개수), user별 cycle당 평균 log 수(고객별 접속당 평균 활동수)을 구하겠습니다.

# **1) cycle별 log 수(접속별 활동 개수)**

# In[79]:


cycle_log_count = (sorted_log_data
                 .groupby(['n_user_id', 'cycle_idx_daily']) 
                 .size()  # 그룹별 속한 row 수(log 수)를 반환합니다.
                 .reset_index()  # index를 초기화합니다.
                 .rename(columns = { 0 : "log_count"} )   # 컬럼이름을 log_count로 변경합니다.
                )

cycle_log_count.head()


# **2) user별 cycle당 평균 log수의 평균(고객별 접속당 평균 활동수)**

# In[80]:


# 위에서 구한 cycle_log_count를 이용하여 cycle당 평균 log 수를 구하겠습니다.
cycle_user_log_count = (cycle_log_count
                 .groupby(['n_user_id']) 
                 .mean()         # 그룹별 속한 평균 row 수(log 수)를 반환합니다.
                 .reset_index()  # index를 초기화합니다.
                 .rename({'log_count':'log_count_mean'}, axis = 1)
                 )

cycle_user_log_count.head()


# In[81]:


# cycle_idx_daily 컬럼을 삭제하겠습니다.
cycle_user_log_count.drop('cycle_idx_daily', axis = 1, inplace = True)

cycle_user_log_count.head()


# **3) 하루동안 가장 많은 cycle을 갖는(가장 많이 활동한) 상위 5명의 user**

# In[82]:


# n_user_id 컬럼을 기준으로 유일값에 대한 갯수(nunique())를 찾고, cycle_idx_daily 컬럼을 기준으로 내림차순 정렬하겠습니다.
top_five = cycle_log_count.groupby('n_user_id').nunique().sort_values(by = ['cycle_idx_daily'], ascending = False)

# 위와 같은 형태로 출력하기 위해 'n_user_id'과 'log_count' 컬럼을 삭제하겠습니다.
top_five = top_five.drop(['n_user_id','log_count'], axis = 1)

# 위와 같은 형태로 출력하기 위해 컬럼 이름을 지우겠습니다.
top_five = top_five['cycle_idx_daily'].rename('')

print(top_five.head())


# ### 5.1.1 user별 잔존시간

# In[83]:


# 아래와 같이 컬럼이름을 log_duration 에서 duration 으로 변경하겠습니다.

remaining_time_cycle = (sorted_log_data.groupby(['n_user_id', 'cycle_idx_daily'])['log_duration']
                         .sum()
                         .reset_index()
                         .rename(columns = {'log_duration' : 'duration'})
                       )

remaining_time_cycle.head(10)


# In[84]:


# n_user_id 기준으로 잔존시간 평균을 내어 출력하겠습니다.
remaining_time_cycle = remaining_time_cycle.groupby('n_user_id').mean()

remaining_time_cycle[['duration']].head(10)


# In[85]:


# 잔존 시간이 0인 경우를 제외한 결과

remaining_time_cycle = remaining_time_cycle.groupby('n_user_id').mean()

# remaining_time 컬럼이 0인 경우를 제외하겠습니다.
remaining_time_cycle_not_0 = remaining_time_cycle[remaining_time_cycle['duration'] > 0]

remaining_time_cycle_not_0[['duration']].head(10)


# ### 5.1.2 구매/비구매 cycle별 잔존시간
# 
# 구매 기록이 있는 cycle은 잔존시간이 길 것이라고 예상할 수 있습니다. 이를 확인하기 위하여 구매/비구매 cycle별 평균 잔존시간을 구하겠습니다.

# In[86]:


# 고객이 한번 app에 접속하여 나가기까지의 일련의 활동을 한 cycle이라 정의하겠습니다.

# funnel_desc 컬럼이 '결제완료'인 데이터만 변수에 저장하겠습니다.
cycle_purchase = sorted_log_data[sorted_log_data['funnel_desc'] == '결제완료']

# cycle_idx_unique 컬럼의 유일값을 변수에 저장하겠습니다.
cycle_purchase = cycle_purchase['cycle_idx_unique'].unique()

cycle_purchase


# In[87]:


# 구매이력이 있는 사용자
data_purchase = sorted_log_data.loc[sorted_log_data['cycle_idx_unique'].isin(cycle_purchase)]

# 구매이력이 없는 사용자
data_not_purchase = sorted_log_data.loc[~sorted_log_data['cycle_idx_unique'].isin(cycle_purchase)]

print(data_purchase.shape)
data_purchase.head()


# In[88]:


print(data_not_purchase.shape)
data_not_purchase.head()


# In[89]:


# 구매 cycle의 잔존시간
data_purchase = (data_purchase.groupby(['n_user_id', 'cycle_idx_unique'])['log_duration']
                         .sum()
                         .reset_index()
                         .rename(columns = {'log_duration' : 'cycle_duration'})
                       )

data_purchase.head(10)


# In[90]:


# 비구매 cycle의 잔존시간
data_not_purchase = (data_not_purchase.groupby(['n_user_id', 'cycle_idx_unique'])['log_duration']
                         .sum()
                         .reset_index()
                         .rename(columns = {'log_duration' : 'cycle_duration'})
                       )

data_not_purchase.head(10)


# 구매/비구매 cycle의 잔존 시간을 시각화하겠습니다.

# In[91]:


# 구매 cycle 잔존 시간(평균)
duration_mean_purchase = data_purchase['cycle_duration'].mean()

# 비구매 cycle 잔존 시간(평균)
duration_mean_npurchase = data_not_purchase['cycle_duration'].mean()

# boxplot 및 평균 잔존 시간 출력
f, ax = plt.subplots(2, 1, figsize = (15, 8))

sns.boxplot(data = data_purchase, x = 'cycle_duration', ax = ax[0])
sns.boxplot(data = data_not_purchase, x = 'cycle_duration', ax = ax[1])

ax[0].set_title('구매 cycle 잔존 시간')
ax[1].set_title('비구매 cycle 잔존 시간')

plt.subplots_adjust(hspace = 0.4)

print(f'구매 cycle 잔존 시간 평균 : {duration_mean_purchase:.2f}')
print(f'비구매 cycle 잔존 시간 평균 : {duration_mean_npurchase:.2f}')


# **구매한 유저의 잔존시간(2609.88초)이 비구매 유저의 잔존시간(679.67초)보다 긴 것으로 나타났습니다.**

# ## 5.2 전환율 분석

# 전환율 분석을 수행하기 전에, 결제완료가 첫 번째인 케이스(**is_first_activity** == True)만으로 정렬하겠습니다.
# 
# 
# is_first_activity 컬럼은 해당 이벤트가 해당 유저에 한하여 첫 번째인지 혹은 두 번째 이상인지를 알려주는 값입니다. 예를 들어, funnel_desc 컬럼 값이 '결제완료'인 경우가 첫 번째이면 True, 그렇지 않으면 False를 의미합니다.

# In[92]:


act_first =  log_data[log_data['is_first_activity'] == True]

print(act_first.shape)
act_first.head()


# day 컬럼을 인덱스로 두어 테이블을 생성하면 결측치가 없습니다. 하지만, device_manufacturer 컬럼을 인덱스로 두고 테이블을 생성하면 결측치가 존재합니다. 이 경우, fill_value 옵션을 활용하여 결측치를 0으로 채울 수 있습니다.

# ### 5.2.1 날짜별 구매 전환율

# In[93]:


cr_day = pd.pivot_table(data = act_first, index = 'day', columns = 'funnel_desc', values = 'user_id', aggfunc = 'count', 
                        margins = True)

cr_day


# * 이제 전환율을 계산하겠습니다.
# 
# 
# 전환율 계산식
# 
# 전환율 = 결제완료 활동 / 전체 활동 수 * 100

# In[94]:


# 활동 수
act_total = cr_day.loc['All'][-1]
act_28 = cr_day.loc[29][-1]
act_29 = cr_day.loc[28][-1]

# 첫 구매 고객 수
customer_total = cr_day.loc['All']['결제완료']
customer_28 = cr_day.loc[28]['결제완료']
customer_29 = cr_day.loc[29]['결제완료']

# 전환율
cr_total = f'{(customer_total / act_total) * 100:.1f}'
cr_28 = f'{(customer_28 / act_28) * 100:.1f}'
cr_29 = f'{(customer_29 / act_29) * 100:.1f}'


# In[95]:


cr_df = pd.DataFrame({'항목' : ['총 활동 횟수', '구매 고객 수', '전환율'],
              '전체' : [act_total, customer_total, cr_total],
              '28일' : [act_28, customer_28, cr_28],
              '29일' : [act_29, customer_29, cr_29]})

cr_df


# 위의 데이터프레임을 기준으로 시각화를 진행하겠습니다.

# In[96]:


ax = sns.barplot(data = cr_df, x= cr_df['항목'][:2], y = '전체')

ax.set_title('총 전환율')

ax.set_xlabel('전체')

ax.set_ylabel('빈도')

for i in range(cr_df[:-1].shape[0]):
    if i == 0:
        ax.text(x = i, y = 500, s = f'{int(cr_df["전체"][i])} 명', horizontalalignment = 'center', color = 'white', fontsize = 12)
    else:
        ax.text(x = i, y = 500, s = f'{int(cr_df["전체"][i])} 명', horizontalalignment = 'center', fontsize = 12)

plt.text(0.7, 0.5, '전체 전환율 : 0.8%', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, 
         fontsize=16, color='red')


# 크몽의 전체 전환율은 0.8%로 나타났습니다. 일별 전환율을 살펴보겠습니다.

# In[97]:


cr_df.dtypes


# In[98]:


# 각 컬럼 데이터타입이 object 입니다. float 형태로 변환하겠습니다.

cr_df['28일'] = cr_df['28일'].astype('float')
cr_df['29일'] = cr_df['29일'].astype('float')
cr_df['전체'] = cr_df['전체'].astype('float')


# In[99]:


cr_df.dtypes


# float 형태로 변환되었습니다.

# In[100]:


# 전일 대비 변화 비율을 구하겠습니다.
cr_df["전일 대비 비율"] = round(-100 + (cr_df['29일'] / cr_df['28일']) * 100, 1)

cr_df


# In[101]:


f, ax = plt.subplots(1,2, figsize = (15, 6))

sns.barplot(data = cr_df, x= cr_df['항목'][0:2], y = '28일', ax = ax[0])

sns.barplot(data = cr_df, x= cr_df['항목'][0:2], y = '29일', ax = ax[1])

ax[0].set_title('28일 전환율')

ax[1].set_title('29일 전환율')

ax[0].set_xlabel('28일')

ax[1].set_xlabel('29일')

ax[0].set_ylabel('빈도')

ax[1].set_ylabel('빈도')

ax[0].set_ylim(0, 25000)

ax[1].set_ylim(0, 25000)

ax[0].text(0.52, 0.5, f"28일 구매 전환율 : {cr_df['28일'][2]}%", fontsize = 13, transform=ax[0].transAxes)
ax[0].text(0.2, 0.05, f"{int(cr_df['28일'][0])}명", fontsize = 12, transform=ax[0].transAxes, color = 'white')
ax[0].text(0.71, 0.05, f"{int(cr_df['28일'][1])}명", fontsize = 12, transform=ax[0].transAxes)

ax[1].text(0.52, 0.5, f"29일 구매 전환율 : {cr_df['29일'][2]}%", fontsize = 13, transform=ax[1].transAxes)
ax[1].text(0.2, 0.05, f"{int(cr_df['29일'][0])}명", fontsize = 12, transform=ax[1].transAxes, color = 'white')
ax[1].text(0.71, 0.05, f"{int(cr_df['29일'][1])}명", fontsize = 12, transform=ax[1].transAxes)

ax[1].text(0.52, 0.4, f"전일 대비 : {cr_df['전일 대비 비율'][2]}%", fontsize = 13, transform=ax[1].transAxes, color = 'red')

plt.subplots_adjust(wspace=0.5)


# 일별 전환율을 살펴보면, 28일은 1.1%, 29일은 0.5% 인 것으로 나타났습니다. 29일의 전환율은 전일 대비 -54.5% 감소했습니다.

# ### 5.2.2 신규 회원 구매 전환율

# raw_data 에는 신규회원을 나타내는 별도의 컬럼이 존재하지 않습니다. 
# 
# 신규회원의 구매전환율을 살펴보기 위해 view_desc 컬럼이 '개인/기업-회원가입'인 케이스를 신규회원(신규가입자)로 정의하겠습니다.
# 
# 
# 즉, (view_desc == '개인/기업-회원가입') & (is_first_activity == True) & (funnel_desc == '결제완료')인 케이스를 찾아 분석하겠습니다.

# In[102]:


new_member = log_data[log_data['view_desc'] == '개인/기업-회원가입']

print('신규회원 수 :', len(new_member['user_id'].unique()))


# In[103]:


new_member = new_member.drop_duplicates('user_id')

new_member_list = new_member['user_id'].tolist()

new_member_df = df.loc[new_member_list]

paid_new_member = new_member_df[(new_member_df['is_first_activity'] == True) & (new_member_df['funnel_desc'] == '결제완료')]

paid_new_member


# In[104]:


num_new_member = len(new_member['user_id'].unique())
paid_num = paid_new_member.shape[0]
new_member_cr = f'{(paid_num / num_new_member) * 100:.1f}'
                     


new_cr = pd.DataFrame({'항목' : ['신규회원', '결제한 신규회원', '신규회원 구매전환율'],
             'count' : [num_new_member, paid_num, new_member_cr]})

new_cr


# 신규회원의 구매 데이터를 시각화하겠습니다.

# In[105]:


ax = sns.barplot(data = new_cr, x= new_cr['항목'][:2], y = 'count')

ax.set_title('신규회원 구매전환율')

ax.set_xlabel('전체')

ax.set_ylabel('빈도')

for i in range(new_cr[:-1].shape[0]):
    if i == 0:
        ax.text(x = i, y = 5, s = f'{int(new_cr["count"][i])} 명', horizontalalignment = 'center', color = 'white', fontsize = 12)
    else:
        ax.text(x = i, y = 5, s = f'{int(new_cr["count"][i])} 명', horizontalalignment = 'center', fontsize = 12)

plt.text(0.7, 0.5, '구매전환율 : 7.5%', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, 
         fontsize=16, color='red')


# **1) 신규회원 유입경로**

# 신규회원의 유입경로를 살펴보기 위해 (view_desc == '개인/기업-회원가입')인 케이스의 유입경로를 확인하겠습니다.
# 
# 위의 신규회원 구매전환율 분석과는 달리, 중복 유저를 포함하여 분석하겠습니다.

# In[106]:


channel_df = log_data[log_data['view_desc'] == '개인/기업-회원가입']['channel']

channel_table = pd.DataFrame(channel_df.value_counts())

channel_rate = []
for i in range(len(channel_table['channel'])):
    channel_rate.append(round(channel_table['channel'][i] / sum(channel_table['channel']) * 100, 1))

channel_table['percentage'] = channel_rate

channel_table


# In[107]:


ax = sns.barplot(data = channel_table, x = channel_table.index, y = 'channel')

ax.set_title('신규회원 유입경로')

ax.set_xlabel('유입경로')

ax.set_ylabel('빈도')

for i in range(channel_table.shape[0]):
    if i == 0:
        ax.text(x = i, y = channel_table["percentage"][i] + 16.5, s = f'{float(channel_table["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12)
    else:
        ax.text(x = i, y = channel_table["percentage"][i] + 7, s = f'{float(channel_table["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12)

    ax.text(x = i, y = 5.0, s = f'{int(channel_table["channel"][i])}명', horizontalalignment='center', verticalalignment='center',
             fontsize=13, color='white')


# 신규회원 유입경로를 살펴보면, unattributed(59.0%)가 가장 많았습니다. 
# 
# 다음으로, google(google-play, google.adwords)이 21.0%, web이 18.0%로 나타났습니다.

# ## 5.3 퍼널 분석

# ### 5.3.1 구매 도달율 분석

# 크몽에서 사용자가 물품을 결제하기까지의 구매 도달율을 퍼널 분석하겠습니다.
# 
# 크몽에서 목표 행동인 결제에 도달하기 위해서는 카테고리 목록, 상품상세, 상품선택, 상품주문 4단계를 거쳐야합니다.
# 
# 카테고리, 상품상세, 상품선택, 상품주문, 결제 5단계를 Funnel로 구성하여 각 단계별로 도달율을 측정하고 시각화 하도록하겠습니다.
# 
# 사용자 데이터는 viewid desc가 카테고리 목록 (탭)인 사용자입니다.
# 
# 퍼널 데이터는 is_first_activity가 True인 데이터를 사용하겠습니다.
# 
# 각 단계를 처음으로 클릭한 사용자의 로그 데이터를 바탕으로 Funnel 분석을 하겠습니다.
# 
# * funnel 이탈률 분석을 위해 카테고리 목록 접속 데이터를 가져오겠습니다.

# In[108]:


# df 데이터에서 user_id, view_desc, is_first_activity 컬럼 데이터를 가져옵니다.
df_funnel = log_data[['user_id', 'view_desc', 'is_first_activity']]

# 카테고리 목록을 처음으로 접속한 사용자의 데이터를 생성합니다.
categories = df_funnel[(df_funnel['view_desc'] == '카테고리 목록 (탭)') & (df_funnel['is_first_activity'] == True)]

# 중복된 아이디를 제거합니다. (하나의 아이디만을 남깁니다.)
categories = categories.drop_duplicates('user_id')

# 카테고리 목록을 처음으로 접속한 사용자의 리스트를 생성합니다. (상품 상세 접속 데이터를 생성하는데 사용합니다.)
categories_list = list(set(categories['user_id']))

# result 변수에 view_desc 데이터를 저장합니다. 
result = categories[['view_desc']].reset_index(drop = True)

# 카테고리 데이터의 상위 5개 데이터를 출력합니다.
result.head()


# * 카테고리 목록(탭)을 클릭한 사용자에 한해 상품상세 접속 데이터를 가져오겠습니다.

# In[109]:


# 카테고리 목록을 처음으로 접속한 사용자의 데이터를 불러오겠습니다. 
df_funnel = df_funnel.set_index('user_id')
df_funnel['user_id'] = df_funnel.index

detail = df_funnel.loc[categories_list]

# 카테고리 목록을 처음으로 접속한 사용자의 데이터를 생성합니다.
detail = detail[(detail['view_desc'] == '상품상세') & (detail['is_first_activity'] == True)]

# 중복된 아이디를 제거합니다. (하나의 아이디만을 남깁니다.)
detail = detail.drop_duplicates('user_id').reset_index(drop = True)

# 상품상세 목록을 처음으로 접속한 사용자의 리스트를 생성합니다. (상품 선택 접속 데이터를 생성하는데 사용합니다.)
detail_list = list(set(detail['user_id']))

# detail 변수에 view_desc 컬럼 데이터를 을 생성합니다.
detail = detail[["view_desc"]]

# result 데이터에 detail 변수에 저장된 데이터를 추가합니다. 
result = result.append(detail)

# detail 데이터를 추가한 데이터의 하위 5개 데이터를 출력합니다.
result.tail()


# * 카테고리 목록(탭) - 상품상세를 클릭한 사용자에 한해 상품선택 데이터를 가져오겠습니다.

# In[110]:


# 상품상세를 처음으로 접속한한 사용자의 데이터를 불러옵니다. 
select = df_funnel.loc[detail_list]

# 상품선택을 처음으로 접속한 데이터를 가져옵니다. 
select = select[(select['view_desc'] == '상품상세-상품선택') & (select['is_first_activity'] == True)]

# 중복된 아이디를 제거합니다. 
select = select.drop_duplicates(['user_id']).reset_index(drop = True)

# 아이디 리스트를 생성합니다. 
select_list = list(set(select['user_id']))

# select 변수에 view_desc 컬럼 데이터를 을 생성합니다.
select = select[['view_desc']]

# result 데이터에 select 변수에 저장된 데이터를 추가합니다. 
result = result.append(select)

result.tail()


# * 카테고리 목록(탭) - 상품상세 - 상품선택을 클릭한 사용자에 한해 주문하기 데이터를 가져오겠습니다.

# In[111]:


# 상품선택을 처음으로 접속한한 사용자의 데이터를 불러옵니다. 
order = df_funnel.loc[select_list]

# 주문하기를 처음으로 접속한 데이터를 가져옵니다. 
order = order[(order['view_desc'] == '상품상세-주문하기') & (order['is_first_activity'] == True)]

# 중복된 아이디를 제거합니다. 
order = order.drop_duplicates(['user_id']).reset_index(drop = True)

# 아이디 리스트를 생성합니다. 
order_list = list(set(order['user_id']))

# order 변수에 viewid desc 컬럼 데이터를 을 생성합니다.
order = order[['view_desc']]

# result 데이터에 order 변수에 저장된 데이터를 추가합니다. 
result = result.append(order)

result.tail()


# * 카테고리 목록(탭) - 상품상세 - 상품선택 - 주문하기를 클릭한 사용자에 한해 결제완료 데이터를 가져오겠습니다.

# In[112]:


# 주문하기를 처음으로 접속한한 사용자의 데이터를 불러옵니다. 
paid = df_funnel.loc[order_list]

# 결제완료를 처음으로 접속한 데이터를 가져옵니다. 
paid = paid[(paid['view_desc'] == '결제완료') & (paid['is_first_activity'] == True)]

# 중복된 아이디를 제거합니다. 
paid = paid.drop_duplicates(['user_id']).reset_index(drop = True)

# 아이디 리스트를 생성합니다. 
paid_list = list(set(paid['user_id']))

# paid 변수에 viewid desc 컬럼 데이터를 을 생성합니다.
paid = paid[['view_desc']]

# result 데이터에 paid 변수에 저장된 데이터를 추가합니다. 
result = result.append(paid)

result.tail()


# * result에 저장된 funnel 데이터를 정리하겠습니다.

# In[113]:


# result 데이터에 저장된 데이터의 종류별 데이터 수를 계산하겠습니다. 
funnel_result = result.apply(pd.value_counts)

# 컬럼명을 변경하겠습니다.
funnel_result.columns = ['count']

# 퍼널별 비율을 구하겠습니다.
funnel_result['percentage'] = round(funnel_result / funnel_result['count'][0] * 100, 1)

# 인덱스명을 변경하겠습니다.
funnel_result.index = ['카테고리목록', '상품상세', '상품선택', '주문하기', '결제완료']

funnel_result


# In[114]:


bounce_rate = []
for i in range(funnel_result.shape[0]):
    if i == 0:
        bounce_rate.append(round(funnel_result['count'][i] / funnel_result['count'][i], 1))
    else:
        bounce_rate.append(round(-100 + funnel_result['count'][i] / funnel_result['count'][i-1] * 100, 1))
        
funnel_result['이전 페이지 대비 이탈률'] = bounce_rate

funnel_result


# **이전 페이지 대비 이탈률을 살펴보면, 상품상세-상품선택 페이지 사이에서 가장 많은 이탈률(-75.3%)이 발생했습니다.**
# 
# **사용자는 상품 설명을 보고 이탈하는 케이스가 가장 많은 것으로 나타났습니다.**

# * 구매 도달율을 시각화하겠습니다.
# 
# 
# * 구매 도달율 : 결제완료 / 카테고리목록 * 100

# In[115]:


plt.figure(figsize = (15, 6))

ax = sns.barplot(data = funnel_result, x= funnel_result.index, y = 'count')

ax.set_title('퍼널별 구매 도달율')

ax.set_xlabel('funnel')

for i in range(funnel_result.shape[0]):
    if i == 0:
        ax.text(x = i, y = funnel_result['percentage'][i] + 600, s = f'{int(funnel_result["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'white')
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
    
    elif i == 1:
        ax.text(x = i, y = funnel_result['percentage'][i]+380, s = f'{int(funnel_result["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'white')
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
        ax.text(x = i, y = funnel_result["이전 페이지 대비 이탈률"][i] + 530,                 s = f'{float(funnel_result["이전 페이지 대비 이탈률"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 14, color = 'red')
        
    elif i == 2:
        ax.text(x = i, y = funnel_result['percentage'][i]+60, s = f'{int(funnel_result["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'white')
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
        ax.text(x = i, y = funnel_result["이전 페이지 대비 이탈률"][i] + 210,                 s = f'{float(funnel_result["이전 페이지 대비 이탈률"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 14, color = 'red')
    
    elif i == 3:
        ax.text(x = i, y = funnel_result['percentage'][i]+30, s = f'{float(funnel_result["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'white')
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
        ax.text(x = i, y = funnel_result["이전 페이지 대비 이탈률"][i] + 130,                 s = f'{int(funnel_result["이전 페이지 대비 이탈률"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 14, color = 'red')
    
    else:
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
        ax.text(x = i, y = funnel_result["이전 페이지 대비 이탈률"][i] + 80,                 s = f'{float(funnel_result["이전 페이지 대비 이탈률"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 14, color = 'red')

ax.text(3.0, 400, s = f"구매도달율 : {funnel_result['count'][i] / funnel_result['count'][0] * 100 :.1f} %",         horizontalalignment='center', verticalalignment='center', fontsize=20, color='blue')


# 구매에 도달하는 비율은 5.6%로 나타났습니다.

# ### 5.3.2 카테고리별 구매율

# 본 데이터에는 4개의 카테고리 관련 컬럼이 존재합니다. 해당 분석에서는 대분류에 해당하는 category1 컬럼을 활용하여 분석을 수행하겠습니다.

# In[116]:


# 카테고리별 전체 조회 수를 계산하겠습니다.
# 데이터를 category1 컬럼이 비어져 있지 않고, is_first_activity 컬럼이 True, view_action 컬럼이 view 인 케이스로 정리하겠습니다.
total_category_df = log_data[(log_data['category1'].notnull()) & (log_data['is_first_activity'] == True) &                              (log_data['view_action'] == 'view')].reset_index(drop = True)

# 카테고리별 구매 수를 계산하겠습니다.
# 데이터를 category1 컬럼이 비어져 있지 않고, funnel_desc 컬럼이 True인 케이스로 정리하겠습니다.
paid_category_df = log_data[(log_data['category1'].notnull()) & (log_data['funnel_desc'] == '결제완료')].reset_index(drop = True)

# 카테고리별 전체 조회 수
total_view = total_category_df.groupby('category1').count()['user_id']

# 카테고리별 전체 구매 수
total_paid = paid_category_df.groupby('category1').count()['user_id']

# 데이터를 합치겠습니다.
merged_total = pd.merge(total_view, total_paid, on = 'category1')

merged_total.columns = ['조회수', '구매수']

merged_total


# **카테고리별 조회 수와 구매 수가 출력되었습니다.**
# 
# 
# * 이제 카테고리별 구매율을 계산하겠습니다.

# In[117]:


merged_total['구매율'] = round(merged_total['구매수'] / merged_total['조회수'] * 100, 1)

merged_total = merged_total.sort_values(by = '구매율', ascending = False)

merged_total


# **카테고리별 구매율이 출력되었습니다.**
# 
# 
# * 이제 시각화를 하겠습니다.

# In[118]:


f, ax = plt.subplots(2, 1, figsize = (15, 8))

sns.barplot(data = merged_total, x= merged_total.index, y = '조회수', ax = ax[0])

sns.barplot(data = merged_total, x= merged_total.index, y = '구매율', ax = ax[1])

ax[0].set_title('카테고리별 조회 수')

ax[1].set_title('카테고리별 구매율')

ax[0].set_xlabel('카테고리')

ax[1].set_xlabel('카테고리')

ax[0].set(ylim = (0, 7000))

ax[1].set(ylim = (0, 3.5))

plt.subplots_adjust(hspace = 0.4)

for i in range(merged_total.shape[0]):
    ax[0].text(x = i, y = merged_total['조회수'][i] + 100, s = f'{int(merged_total["조회수"][i])} 회', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
    
for i in range(merged_total.shape[0]):
    ax[1].text(x = i, y = merged_total['구매율'][i], s = f'{float(merged_total["구매율"][i])} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')


# 카테고리 중에서 '마케팅'이 조회수(5275회)와 구매율(3.0%) 모두 높은 것으로 나타났습니다.
# 
# 반면, '디자인'은 조회수(5834회)는 가장 높았으나 구매율(0.8%)로 다소 낮았습니다.
# 
# 디자인과는 달리, '상담/컨설팅'의 경우는 조회수(1577회)는 낮았으나 구매율(3.0%)로 가장 높았습니다.

# ### 5.3.3 시간대별 카테고리 조회 빈도

# * 시간대별로 카테고리 조회 빈도를 살펴보겠습니다.

# In[119]:


hour_category = log_data.groupby(['hour', 'category1']).size().reset_index()

hour_category.columns = ['hour', 'category', 'count']

hour_category_table = pd.pivot_table(data = hour_category, index = 'category', columns = 'hour', values = 'count')

hour_category_table


# * heatmap으로 시각화하겠습니다.

# In[120]:


plt.figure(figsize = (15, 6))

ax = sns.heatmap(hour_category_table, annot = True, fmt = 'd', cmap = 'YlGnBu')

ax.set_title('시간별 카테고리 조회 수(heatmap)')


# **디자인과 마케팅 카테고리의 조회 수가 가장 높았습니다.**

# ## 5.4 종료율 분석

# ### 5.4.1 일별 종료율

# 전체 데이터에서 사용자들의 일별 종료율을 분석하겠습니다.
# 
# 28일과 29일의 종료율 분석후, 종료율 차이가 있는지 확인하겠습니다.
# 
# * 먼저, 28일과 29일의 접속 및 종료 횟수 데이터를 출력하겠습니다.

# In[121]:


# 접속 데이터
launch_df = log_data[log_data['event_category'] == 'launch']

# 이탈 데이터
exit_df = log_data[log_data['event_category'] == 'exit']

# 일별 접속 데이터 카운팅
day_launch = pd.pivot_table(data = launch_df, index = 'day', values = 'event_category', aggfunc = 'count')

# 일별 이탈 데이터 카운팅
day_exit = pd.pivot_table(data = exit_df, index = 'day', values = 'event_category', aggfunc = 'count')

# 접속, 이탈 데이터 합치기(인덱스 기준 merge)
total_day_bounce = pd.merge(day_launch, day_exit, on = day_launch.index)

# 컬럼명 변경
total_day_bounce.rename(columns = {'key_0': 'day', 'event_category_x':'launch', 'event_category_y':'exit'}, inplace = True)

total_day_bounce


# In[122]:


# 일별 종료율을 계산하겠습니다.

total_day_bounce['bounce_rate'] = round(total_day_bounce['exit'] / total_day_bounce['launch'] * 100, 1)

total_day_bounce


# * 시각화를 수행하겠습니다.

# In[123]:


ax = sns.barplot(data = total_day_bounce, x = 'day', y = 'bounce_rate')

ax.set_title('일별 종료율')

ax.set_ylim(0, 45)

for i in range(total_day_bounce.shape[0]):
    if i == 0:
        ax.text(x = i, y = 40.5, s = f'{float(total_day_bounce["bounce_rate"][i])} %', horizontalalignment = 'center', fontsize = 12)
    else:
        ax.text(x = i, y = 40.5, s = f'{float(total_day_bounce["bounce_rate"][i])} %', horizontalalignment = 'center', fontsize = 12)

ax.text(1.0, 25.5, s = f'총 종료율 : {round((sum(total_day_bounce["exit"]) / sum(total_day_bounce["launch"]) * 100), 1)} %',         horizontalalignment = 'center', fontsize = 16, color = 'blue')


# 총 종료율은 39.9% 로 나타났습니다.
# 
# 일별로 살펴보면, 28일에는 39.8%, 29일에는 40.1%로 비슷했습니다.

# ### 5.4.2 시간별 종료율

# In[124]:


# 시간별 접속 수
hour_launch = pd.pivot_table(data = launch_df, index = 'hour', values = 'event_category', aggfunc = 'count')

# 시간별 종료 수
hour_exit = pd.pivot_table(data = exit_df, index = 'hour', values = 'event_category', aggfunc = 'count')

# 데이터 합치기(인덱스 기준 merge)
total_hour_bounce = pd.merge(hour_launch, hour_exit, on = hour_launch.index)

# 컬럼명 수정
total_hour_bounce.columns = ['hour', 'launch', 'exit']

total_hour_bounce.head()


# In[125]:


# 시간별 접속 수
hour_launch = pd.pivot_table(data = launch_df, index = 'hour', values = 'event_category', aggfunc = 'count')

# 시간별 종료 수
hour_exit = pd.pivot_table(data = exit_df, index = 'hour', values = 'event_category', aggfunc = 'count')

# 데이터 합치기(인덱스 기준 merge)
total_hour_bounce = pd.merge(hour_launch, hour_exit, on = hour_launch.index)

# 컬럼명 수정
total_hour_bounce.columns = ['hour', 'launch', 'exit']

total_hour_bounce.head()


# In[126]:


# 시간별 종료율을 계산하겠습니다.

total_hour_bounce['bounce_rate'] = round(total_hour_bounce['exit'] / total_hour_bounce['launch'] * 100, 1)

total_hour_bounce


# * 시각화를 수행하겠습니다.
# 
# 
# * 시각화를 하기 전, 타입별 빈도를 테이블로 출력하겠습니다.

# In[127]:


# 데이터 합치기(concat() 함수 사용)
hour_bounce = pd.concat([hour_launch, hour_exit])

hour_bounce = hour_bounce.reset_index()

hour_bounce['type'] = 'launch'

hour_bounce['type'][hour_exit.shape[0]:] = 'exit'

hour_bounce.columns = ['hour', 'count', 'type']

hour_bounce.head()


# In[128]:


plt.figure(figsize = (18, 4))

ax = sns.barplot(data = hour_bounce, x = 'hour', y = 'count', hue = 'type')

ax.set_xlabel('count')

ax.set_title('시간별 접속/종료 횟수')


# **그래프를 살펴보면 오전 7 ~ 다음날 오전 12시까지 접속/종료 횟수가 많았습니다. 특히, 오전 10 ~ 오후 19시 사이에 접속/종료 횟수가 많았습니다.**

# * 시간대별 종료율 그래프를 출력하겠습니다.

# In[129]:


plt.figure(figsize = (18, 4))

ax = sns.barplot(data = total_hour_bounce, x = 'hour', y = 'bounce_rate')

ax.set_title('시간대별 종료율')

ax.set_ylabel('exit_rate')

ax.set_ylim(0, 80)

print(f"시간대별 평균 종료율 : {round(sum(total_hour_bounce['exit']) / sum(total_hour_bounce['launch']) * 100, 1):.1f} %")

for i in range(total_hour_bounce.shape[0]):
    ax.text(x = i, y = total_hour_bounce['bounce_rate'][i] + 1, s = f'{float(total_hour_bounce["bounce_rate"][i])} %',             horizontalalignment = 'center', fontsize = 10)


# ### 5.4.3 일 X 시간대 종료율

# In[130]:


# 날짜별 시간대 접속 데이터
day_hour_launch = pd.pivot_table(data = launch_df, index = 'hour', columns = 'day', values = 'event_category', aggfunc = 'count')

# 날짜별 시간대 퇴장 데이터
day_hour_exit = pd.pivot_table(data = exit_df, index = 'hour', columns = 'day', values = 'event_category', aggfunc = 'count')

# 시각화 작업을 위해 type 컬럼을 만들어 값을 입력하겠습니다.
day_hour_launch['type'] = 'launch'
day_hour_exit['type'] = 'exit'

# 접속 데이터와 종료 데이터를 합치겠습니다. (concat 함수 활용)
total_day_hour = pd.concat([day_hour_launch, day_hour_exit])

total_day_hour


# * 날짜별 접속/종료 횟수 시각화를 실시하겠습니다.

# In[131]:


f, ax = plt.subplots(2, 1, figsize = (18, 8))

sns.barplot(data = total_day_hour, x = total_day_hour.index, y = 28, hue = 'type', ax = ax[0])

sns.barplot(data = total_day_hour, x = total_day_hour.index, y = 29, hue = 'type', ax = ax[1])

ax[0].set_ylabel('count')

ax[1].set_ylabel('count')

ax[1].set_ylim(0, 1200)

ax[0].set_title('28일 시간별 접속/종료 횟수')

ax[1].set_title('29일 시간별 접속/종료 횟수')

plt.subplots_adjust(hspace = 0.4)


# **시각화 결과, 전체적으로 28일의 접속/종료 횟수가 29일보다 많았습니다.**
# 
# 
# **날짜별로, 횟수에서만 차이가 있을 뿐 패턴은 유사한 것으로 나타났습니다.**
# 
# 
# * 일별 시간대 종료율을 시각화하겠습니다.

# In[132]:


# 28일 종료율
day28_exit = pd.DataFrame(round(total_day_hour[28][24:] / total_day_hour[28][:24] * 100, 1))

# 29일 종료율
day29_exit = pd.DataFrame(round(total_day_hour[29][24:] / total_day_hour[29][:24] * 100, 1))

f, ax = plt.subplots(2, 1, figsize = (18, 8))

sns.barplot(data = day28_exit, x = day28_exit.index, y = 28, ax = ax[0])

sns.barplot(data = day29_exit, x = day29_exit.index, y = 29, ax = ax[1])

ax[0].set_ylabel('exit_rate')

ax[1].set_ylabel('exit_rate')

ax[0].set_ylim(0, 80)

ax[1].set_ylim(0, 80)

ax[0].set_title('28일 시간별 종료율')

ax[1].set_title('29일 시간별 종료율')

plt.subplots_adjust(hspace = 0.4)

for i in range(day28_exit.shape[0]):
    ax[0].text(x = i, y = day28_exit[28][i] + 1, s = f'{float(day28_exit[28][i])} %',             horizontalalignment = 'center', fontsize = 10)
    
for i in range(day29_exit.shape[0]):
    ax[1].text(x = i, y = day29_exit[29][i] +1, s = f'{float(day29_exit[29][i])} %',             horizontalalignment = 'center', fontsize = 10)


# * 두 날짜 간의 종료율 차이 검증을 실시하겠습니다. (t-test)

# In[133]:


from scipy.stats import levene, ttest_ind

# 28일, 29일 간의 등분산성을 실시하겠습니다.
levene(day28_exit[28], day29_exit[29])


# **p-value = 0.59 로 분산이 같은 것으로 나타났습니다. 이를 토대로 t-test를 실시하겠습니다.**

# In[134]:


ttest_ind(day28_exit[28], day29_exit[29], equal_var = True)


# **t-test 결과, p-value = 0.11 로 28일과 29일 간의 종료율 차이는 없는 것으로 나타났습니다.**

# # 6 종합결과

# ## 6.1 구매 유무별 잔존 분석

# In[135]:


# 구매 cycle 잔존 시간(평균)
duration_mean_purchase = data_purchase['cycle_duration'].mean()

# 비구매 cycle 잔존 시간(평균)
duration_mean_npurchase = data_not_purchase['cycle_duration'].mean()

# boxplot 및 평균 잔존 시간 출력
f, ax = plt.subplots(2, 1, figsize = (15, 8))

sns.boxplot(data = data_purchase, x = 'cycle_duration', ax = ax[0])
sns.boxplot(data = data_not_purchase, x = 'cycle_duration', ax = ax[1])

ax[0].set_title('구매 cycle 잔존 시간')
ax[1].set_title('비구매 cycle 잔존 시간')

plt.subplots_adjust(hspace = 0.4)

print(f'구매 cycle 잔존 시간 평균 : {duration_mean_purchase:.2f}')
print(f'비구매 cycle 잔존 시간 평균 : {duration_mean_npurchase:.2f}')


# **구매 cycle의 잔존시간은 약 44분(2609.88초), 비구매 cycle의 잔존시간은 약 11분(679.67초)으로 나타났습니다.**

# ## 6.2 구매 전환율

# In[136]:


f, ax = plt.subplots(1,3, figsize = (20, 6))

sns.barplot(data = cr_df, x= cr_df['항목'][:2], y = '전체', ax = ax[0])

sns.barplot(data = cr_df, x= cr_df['항목'][0:2], y = '28일', ax = ax[1])

sns.barplot(data = cr_df, x= cr_df['항목'][0:2], y = '29일', ax = ax[2])

ax[0].set_title('전체 전환율')

ax[1].set_title('28일 전환율')

ax[2].set_title('29일 전환율')

ax[0].set_xlabel('전체')

ax[1].set_xlabel('28일')

ax[2].set_xlabel('29일')

ax[0].set_ylabel('빈도')

ax[1].set_ylabel('빈도')

ax[2].set_ylabel('빈도')

ax[1].set_ylim(0, 38000)

ax[2].set_ylim(0, 38000)

ax[0].text(0.17, 0.05, f"{int(cr_df['전체'][0])}명", fontsize = 12, transform=ax[0].transAxes, color = 'white')
ax[0].text(0.7, 0.05, f"{int(cr_df['전체'][1])}명", fontsize = 12, transform=ax[0].transAxes)
ax[0].text(0.7, 0.5, '전체 전환율 : 0.8%', horizontalalignment='center', verticalalignment='center', transform=ax[0].transAxes, 
         fontsize=16, color='red')

ax[1].text(0.48, 0.5, f"28일 구매 전환율 : {cr_df['28일'][2]}%", fontsize = 13, transform=ax[1].transAxes)
ax[1].text(0.17, 0.05, f"{int(cr_df['28일'][0])}명", fontsize = 12, transform=ax[1].transAxes, color = 'white')
ax[1].text(0.7, 0.05, f"{int(cr_df['28일'][1])}명", fontsize = 12, transform=ax[1].transAxes)

ax[2].text(0.48, 0.5, f"29일 구매 전환율 : {cr_df['29일'][2]}%", fontsize = 13, transform=ax[2].transAxes)
ax[2].text(0.17, 0.05, f"{int(cr_df['29일'][0])}명", fontsize = 12, transform=ax[2].transAxes, color = 'white')
ax[2].text(0.7, 0.05, f"{int(cr_df['29일'][1])}명", fontsize = 12, transform=ax[2].transAxes)

ax[2].text(0.5, 0.4, f"전일 대비 : {cr_df['전일 대비 비율'][2]}%", fontsize = 13, transform=ax[2].transAxes, color = 'red')

plt.subplots_adjust(wspace=0.5)


# **전체 구매전환율은 0.8%로 나타났습니다. 날짜별로 살펴보면, 28일은 1.1%, 29일은 0.5%로 28일의 구매전환율이 더 높았습니다.**

# ## 6.3 구매 도달율

# In[137]:


plt.figure(figsize = (15, 6))

ax = sns.barplot(data = funnel_result, x= funnel_result.index, y = 'count')

ax.set_title('퍼널별 구매 도달율')

ax.set_xlabel('funnel')

for i in range(funnel_result.shape[0]):
    if i == 0:
        ax.text(x = i, y = funnel_result['percentage'][i] + 600, s = f'{int(funnel_result["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'white')
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
    
    elif i == 1:
        ax.text(x = i, y = funnel_result['percentage'][i]+380, s = f'{int(funnel_result["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'white')
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
        ax.text(x = i, y = funnel_result["이전 페이지 대비 이탈률"][i] + 530,                 s = f'{float(funnel_result["이전 페이지 대비 이탈률"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 14, color = 'red')
        
        
    elif i == 2:
        ax.text(x = i, y = funnel_result['percentage'][i]+60, s = f'{int(funnel_result["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'white')
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
        ax.text(x = i, y = funnel_result["이전 페이지 대비 이탈률"][i] + 210,                 s = f'{float(funnel_result["이전 페이지 대비 이탈률"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 14, color = 'red')
    
    
    elif i == 3:
        ax.text(x = i, y = funnel_result['percentage'][i]+30, s = f'{float(funnel_result["percentage"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'white')
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
        ax.text(x = i, y = funnel_result["이전 페이지 대비 이탈률"][i] + 130,                 s = f'{int(funnel_result["이전 페이지 대비 이탈률"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 14, color = 'red')
    
    else:
        ax.text(x = i, y = 10, s = f'{int(funnel_result["count"][i])} 명', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
        ax.text(x = i, y = funnel_result["이전 페이지 대비 이탈률"][i] + 80,                 s = f'{float(funnel_result["이전 페이지 대비 이탈률"][i]):.1f} %', 
                horizontalalignment = 'center', fontsize = 14, color = 'red')
ax.text(3.0, 400, s = f"구매도달율 : {funnel_result['count'][i] / funnel_result['count'][0] * 100 :.1f} %",         horizontalalignment='center', verticalalignment='center', fontsize=20, color='blue')


# **구매도달율은 5.6%로 나타났습니다. 퍼널별로 살펴보면, 상품상세에서 상품선택 단계로 넘어갈 때 75.3%가 가장 많은 이탈이 발생했습니다.**

# ## 6.4 카테고리별 구매율

# In[138]:


f, ax = plt.subplots(2, 1, figsize = (15, 8))

sns.barplot(data = merged_total, x= merged_total.index, y = '조회수', ax = ax[0])

sns.barplot(data = merged_total, x= merged_total.index, y = '구매율', ax = ax[1])

ax[0].set_title('카테고리별 조회 수')

ax[1].set_title('카테고리별 구매율')

ax[0].set_xlabel('카테고리')

ax[1].set_xlabel('카테고리')

ax[0].set(ylim = (0, 7000))

ax[1].set(ylim = (0, 3.5))

plt.subplots_adjust(hspace = 0.4)

for i in range(merged_total.shape[0]):
    ax[0].text(x = i, y = merged_total['조회수'][i] + 100, s = f'{int(merged_total["조회수"][i])} 회', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')
    
for i in range(merged_total.shape[0]):
    ax[1].text(x = i, y = merged_total['구매율'][i], s = f'{float(merged_total["구매율"][i])} %', 
                horizontalalignment = 'center', fontsize = 12, color = 'black')


# **조회수는 디자인(5834회)과 마케팅(5275회)이 가장 높았습니다.**
# 
# 
# **구매율은 마케팅과 상담/컨설팅(각 3.0%)이 가장 높았습니다.**
# 
# 
# **마케팅은 조회수와 구매율 모두 높은 카테고리로 나타났습니다. 반면, 디자인은 조회수에 비해 구매율(0.8%)은 낮았으며, 상담/컨설팅은 조회수(1577회)는 낮았지만 구매율은 높은 카테고리였습니다.** 

# ## 6.5 카테고리별 조회 빈도

# In[139]:


plt.figure(figsize = (15, 6))

ax = sns.heatmap(hour_category_table, annot = True, fmt = 'd', cmap = 'YlGnBu')

ax.set_title('시간별 카테고리 조회 수(heatmap)')


# **전체적으로 디자인과 마케팅 조회수가 가장 높았습니다.**
# 
# 
# **디자인의 조회수가 높은 시간대는 0시와 14 ~ 22시였습니다.**
# 
# 
# **마케팅은 13 ~ 18시와 20 ~ 21시였습니다.**
# 
# 
# **전반적으로 활동 시작 시간인 10시부터 조회수가 많아짐을 알 수 있습니다.**

# ## 6.6 종료율 분석

# In[140]:


# 28일 종료율
day28_exit = pd.DataFrame(round(total_day_hour[28][24:] / total_day_hour[28][:24] * 100, 1))

# 29일 종료율
day29_exit = pd.DataFrame(round(total_day_hour[29][24:] / total_day_hour[29][:24] * 100, 1))

f, ax = plt.subplots(2, 1, figsize = (18, 8))

sns.barplot(data = day28_exit, x = day28_exit.index, y = 28, ax = ax[0])

sns.barplot(data = day29_exit, x = day29_exit.index, y = 29, ax = ax[1])

ax[0].set_ylabel('exit_rate')

ax[1].set_ylabel('exit_rate')

ax[0].set_ylim(0, 80)

ax[1].set_ylim(0, 80)

ax[0].set_title('28일 시간별 종료율')

ax[1].set_title('29일 시간별 종료율')

plt.subplots_adjust(hspace = 0.4)

for i in range(day28_exit.shape[0]):
    ax[0].text(x = i, y = day28_exit[28][i] + 1, s = f'{float(day28_exit[28][i])} %',             horizontalalignment = 'center', fontsize = 10)
    
for i in range(day29_exit.shape[0]):
    ax[1].text(x = i, y = day29_exit[29][i] +1, s = f'{float(day29_exit[29][i])} %',             horizontalalignment = 'center', fontsize = 10)


# **날짜별로 시간별 종료율을 살펴보면, 날짜에 관계없이 비슷한 패턴을 보였습니다.**
# 
# 
# **다만, 29일에서 5시, 7시, 21시에서 종료율이 50% 이상으로 높게 나타났습니다.**

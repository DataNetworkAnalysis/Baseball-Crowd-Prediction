# crawling
from selenium.webdriver.support.ui import Select

# prerprocessing
import pandas as pd
import numpy as np

# time
import time
from datetime import datetime

def kbo_crowd(driver, save_dir):
    kbo_url = 'https://www.koreabaseball.com/History/Crowd/GraphDaily.aspx'
    driver.get(kbo_url)
    driver.implicitly_wait(10)

    # define season
    season = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeason"]')
    # define
    years = season.text.split()[1:]
    # define features
    features = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_udpRecord"]/table/thead/tr')
    features = features.text.split()
    # define crowd_df
    crowd_df = pd.DataFrame()

    for year in years:
        # season click
        select_season = Select(driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ddlSeason"]'))
        select_season.select_by_value(year)
        driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_btnSearch"]').click()
        time.sleep(1)

        # create df by season
        rows = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_udpRecord"]/table/tbody').text.split('\n')

        df = pd.DataFrame(np.zeros((len(rows), len(features))), columns=features)

        for row in range(len(rows)):
            for feature in range(len(features)):
                df.loc[row, features[feature]] = rows[row].split()[feature]

        # concatenate df
        crowd_df = pd.concat([crowd_df, df], axis=0)
        print('{}년 관중 객 데이터 크기: {}'.format(year, df.shape[0]))
        time.sleep(2)

    print('2017~2019 관중객 데이터 크기: ',crowd_df.shape[0])

    crowd_df.to_csv(save_dir + '/crowd_df.csv', index=False)

    return driver

def statiz_record(driver, save_dir):
    # define years and months
    years = ['2017','2018','2019']
    months = ['3','4','5','6','7','8','9','10']
    # statiz url
    statiz_url = 'http://www.statiz.co.kr/schedule.php?opt={}&sy={}'

    # define features
    features = ['date','away','away_score','home_score','home']
    # define records
    records = np.array([]).reshape(0, len(features))

    for year in years:
        for month in months:
            driver.get(statiz_url.format(month, year))
            driver.implicitly_wait(10)

            # crawling record by day
            # 아래 xpath는 webdriver 실행시 실행되는 chrome 창에서 가져와야 아래 xpath가 복사된다.
            tbody = driver.find_element_by_xpath('/html/body/div/div[1]/div/section[2]/div/div[2]/div/div/div/div[2]/table/tbody')
            tds = tbody.find_elements_by_tag_name('td')
            for td in tds:
                # check blank
                check_blank = td.text.split()
                if len(check_blank) != 0:
                    divs = td.find_elements_by_tag_name('div')
                    if len(divs) == 4:
                        day = divs[0].text  # define day
                        date = '/'.join([year, month, day])

                        # check blank
                        check_blank = divs[-1].text.split()
                        
                        if len(check_blank) != 0:
                            a_tags = divs[-1].find_elements_by_tag_name('a')
                            for a in a_tags:
                                spans = a.find_elements_by_tag_name('span')
                                if len(spans) == 4:
                                    away, away_score, home_score, home = [spans[i].text for i in range(4)]
                                    print('No: {0:5d} / Date: {1:} / away: {2:4s}/ away_score: {3:2s}/ home_score: {4:2s}/ home: {5:4s}'.format(records.shape[0], date, away, away_score, home_score, home))
                                else: # 우천취소된 경우
                                    away, home = spans[0].text, spans[-1].text
                                    away_score, home_score = -1, -1 # -1 is missing value
                                records = np.concatenate((records, [[date, away, away_score, home_score, home]]), axis=0)

                            # 오늘자까지 했으면 중단
                            if date == datetime.today().strftime('%Y/%m/%d'):
                                break

    # dataframe
    statiz_record = pd.DataFrame(records, columns=features)
    statiz_record.to_csv(save_dir + '/statiz_record.csv', index=False)

    return driver
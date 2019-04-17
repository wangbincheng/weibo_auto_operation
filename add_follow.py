# 添加指定的用户
def add_follow(uid):
    browser.get('https://m.weibo.com/u/'+str(uid))
    time.sleep(1)
    #browser.find_element_by_id("follow").click()
    follow_button = browser.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]')
    follow_button.click()
    time.sleep(1)
    # 选择分组
    group_button = browser.find_element_by_xpath('//div[@class="m-btn m-btn-white m-btn-text-black"]')
    group_button.click()
    time.sleep(1)
# 每天学点心理学 UID
uid = '1890826225' 
add_follow(uid)

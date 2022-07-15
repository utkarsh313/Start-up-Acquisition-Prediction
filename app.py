# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import joblib   
import numpy as np
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)
model = joblib.load("company_status_predictor.pkl")
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


scaler = MinMaxScaler()
@app.route('/predict',methods=['POST'])
def predict():
    global funding_round_type_angel
    global funding_round_type_crowdfunding
    global funding_round_type_post_ipo
    global funding_round_type_private_equity
    global funding_round_type_series_a
    global funding_round_type_series_b
    global funding_round_type_series_c_plus
    global funding_round_type_venture
    global funding_round_type_other
    global category_code_software
    global category_code_web
    global category_code_ecommerce
    global category_code_advertising
    global category_code_mobile
    global category_code_consulting
    global category_code_games_video
    global category_code_enterprise
    global category_code_biotech
    global category_code_public_relations
    global category_code_others
    if request.method == 'POST':
        #try:
            #name = object(request.form['name'])
            country_code= request.form['country_code']
            if(country_code =='AUS'):
                country_code_AUS=1
                country_code_CAN=0
                country_code_DEU=0
                country_code_ESP=0
                country_code_FRA=0
                country_code_GBR=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_USA=0
                country_code_others=0
            elif(country_code =='CAN'):
                country_code_CAN=1
                country_code_AUS=0
                country_code_DEU=0
                country_code_ESP=0
                country_code_FRA=0
                country_code_GBR=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_USA=0
                country_code_others=0
            elif(country_code =='DEU'):
                country_code_DEU=1 
                country_code_CAN=0
                country_code_AUS=0
                country_code_ESP=0
                country_code_FRA=0
                country_code_GBR=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_USA=0
                country_code_others=0
            elif(country_code =='ESP'):
                country_code_ESP=1
                country_code_DEU=0 
                country_code_CAN=0
                country_code_AUS=0
                country_code_FRA=0
                country_code_GBR=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_USA=0
                country_code_others=0
            elif(country_code =='FRA'):
                country_code_FRA=1 
                country_code_ESP=0
                country_code_DEU=0 
                country_code_CAN=0
                country_code_AUS=0
                country_code_GBR=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_USA=0
                country_code_others=0
            elif(country_code =='GBR'):
                country_code_GBR=1 
                country_code_FRA=0 
                country_code_ESP=0
                country_code_DEU=0 
                country_code_CAN=0
                country_code_AUS=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_USA=0
                country_code_others=0
            elif(country_code =='IND'):
                country_code_IND=1 
                country_code_GBR=0 
                country_code_FRA=0 
                country_code_ESP=0
                country_code_DEU=0 
                country_code_CAN=0
                country_code_AUS=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_USA=0
                country_code_others=0
            elif(country_code =='IRL'):
                country_code_IRL=1
                country_code_GBR=0
                country_code_FRA=0 
                country_code_ESP=0
                country_code_DEU=0 
                country_code_CAN=0
                country_code_AUS=0
                country_code_IND=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_USA=0
                country_code_others=0
            elif(country_code =='ISR'):
                country_code_ISR=1 
                country_code_GBR=0 
                country_code_FRA=0 
                country_code_ESP=0
                country_code_DEU=0 
                country_code_CAN=0
                country_code_AUS=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_NLD=0
                country_code_USA=0
                country_code_others=0
            elif(country_code =='NLD'):
                country_code_NLD=1
                country_code_GBR=0 
                country_code_FRA=0 
                country_code_ESP=0
                country_code_DEU=0 
                country_code_CAN=0
                country_code_AUS=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_USA=0
                country_code_others=0
            elif(country_code =='USA'):
                country_code_USA=1
                country_code_GBR=0 
                country_code_FRA=0 
                country_code_ESP=0
                country_code_DEU=0 
                country_code_CAN=0
                country_code_AUS=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_others=0
            elif(country_code =='Others'):
                country_code_others=1
                country_code_GBR=0 
                country_code_FRA=0 
                country_code_ESP=0
                country_code_DEU=0 
                country_code_CAN=0
                country_code_AUS=0
                country_code_IND=0
                country_code_IRL=0 
                country_code_ISR=0 
                country_code_NLD=0
                country_code_USA=0
            category_code= request.form['category_code']
            if(category_code =='Software'):
                category_code_advertising=0
                category_code_biotech=0
                category_code_consulting=0
                category_code_ecommerce=0
                category_code_enterprise=0
                category_code_games_video=0
                category_code_mobile=0
                category_code_public_relations=0
                category_code_software=1
                category_code_web=0
                category_code_others=0
            elif(category_code =='Web'):
                category_code_biotech=0
                category_code_advertising=0
                category_code_consulting=0
                category_code_ecommerce=0
                category_code_enterprise=0
                category_code_games_video=0
                category_code_mobile=0
                category_code_public_relations=0
                category_code_software=0
                category_code_web=1
                category_code_others=0
            elif(category_code =='Ecommerce'):
                category_code_consulting=0 
                category_code_biotech=0
                category_code_advertising=0
                category_code_ecommerce=1
                category_code_enterprise=0
                category_code_games_video=0
                category_code_mobile=0
                category_code_public_relations=0
                category_code_software=0
                category_code_web=0
                category_code_others=0
            elif(category_code =='Advertising'):
                category_code_ecommerce=0
                category_code_biotech=0
                category_code_advertising=1
                category_code_consulting=0
                category_code_enterprise=0
                category_code_games_video=0
                category_code_mobile=0
                category_code_public_relations=0
                category_code_software=0
                category_code_web=0
                category_code_others=0
            elif(category_code =='Mobile'):
                category_code_enterprise=0 
                category_code_biotech=0
                category_code_advertising=0
                category_code_consulting=0
                category_code_ecommerce=0
                category_code_games_video=0
                category_code_mobile=1
                category_code_public_relations=0
                category_code_software=0
                category_code_web=0
                category_code_others=0
            elif(category_code =='Consulting'):
                category_code_games_video=0 
                category_code_biotech=0
                category_code_advertising=0
                category_code_consulting=1
                category_code_ecommerce=0
                category_code_enterprise=0
                category_code_mobile=0
                category_code_public_relations=0
                category_code_software=0
                category_code_web=0
                category_code_others=0
            elif(category_code =='Video Games'):
                category_code_mobile=0 
                category_code_biotech=0
                category_code_advertising=0
                category_code_consulting=0
                category_code_ecommerce=0
                category_code_enterprise=0
                category_code_games_video=1
                category_code_public_relations=0
                category_code_software=0
                category_code_web=0
                category_code_others=0
            elif(category_code =='Enterprise'):
                category_code_public_relations=0 
                category_code_biotech=0
                category_code_advertising=0
                category_code_consulting=0
                category_code_ecommerce=0
                category_code_enterprise=1
                category_code_games_video=0
                category_code_mobile=0
                category_code_software=0
                category_code_web=0
                category_code_others=0
            elif(category_code =='Biotech'):
                category_code_software=0 
                category_code_biotech=1
                category_code_advertising=0
                category_code_consulting=0
                category_code_ecommerce=0
                category_code_enterprise=0
                category_code_games_video=0
                category_code_mobile=0
                category_code_public_relations=0
                category_code_web=0
                category_code_others=0
            elif(category_code =='Public Relations'):
                category_code_web=0
                category_code_biotech=0
                category_code_advertising=0
                category_code_consulting=0
                category_code_ecommerce=0
                category_code_enterprise=0
                category_code_games_video=0
                category_code_mobile=0
                category_code_public_relations=1
                category_code_software=0
                category_code_others=0
            elif(category_code =='Others'):
                category_code_others=1 
                category_code_biotech=0
                category_code_advertising=0
                category_code_consulting=0
                category_code_ecommerce=0
                category_code_enterprise=0
                category_code_games_video=0
                category_code_mobile=0
                category_code_public_relations=0
                category_code_software=0
                category_code_web=0

            No_of_years_since_foundation= int(request.form['No_of_years_since_foundation'])
            No_of_years_since_first_funding= int(request.form['No_of_years_since_first_funding'])
            No_of_years_since_last_funding= int(request.form['No_of_years_since_last_funding'])
            No_of_years_since_last_milestone= int(request.form['No_of_years_since_last_milestone'])
            No_of_years_since_graduation= int(request.form['No_of_years_since_graduation'])
            funding_rounds= int(request.form['funding_rounds'])
            funding_total_usd= int(request.form['funding_total_usd'])
            funding_total_usd= scaler.fit_transform([[funding_total_usd]])
            
            milestones= int(request.form['milestones'])
            
            twitter_presence=request.form['twitter_presence']
            if(twitter_presence=='Yes'):
                twitter_presence=1
            else:
                twitter_presence=0	
            funding_round_type= request.form['funding_round_type']
            if(funding_round_type =='Angel'):
                funding_round_type_angel=1
                funding_round_type_crowdfunding=0
                funding_round_type_post_ipo=0
                funding_round_type_private_equity=0
                funding_round_type_series_a=0
                funding_round_type_series_b=0
                funding_round_type_series_c_plus=0
                funding_round_type_venture=0
                funding_round_type_other=0
            elif(funding_round_type =='Crowdfunding'):
                funding_round_type_crowdfunding=1
                funding_round_type_angel=0
                funding_round_type_post_ipo=0
                funding_round_type_private_equity=0
                funding_round_type_series_a=0
                funding_round_type_series_b=0
                funding_round_type_series_c_plus=0
                funding_round_type_venture=0
                funding_round_type_other=0
            elif(funding_round_type =='Post-IPO'):
                funding_round_type_post_ipo=1 
                funding_round_type_angel=0
                funding_round_type_crowdfunding=0
                funding_round_type_private_equity=0
                funding_round_type_series_a=0
                funding_round_type_series_b=0
                funding_round_type_series_c_plus=0
                funding_round_type_venture=0
                funding_round_type_other=0
            elif(funding_round_type =='Private-Equity'):
                funding_round_type_private_equity=1 
                funding_round_type_angel=0
                funding_round_type_crowdfunding=0
                funding_round_type_post_ipo=0
                funding_round_type_series_a=0
                funding_round_type_series_b=0
                funding_round_type_series_c_plus=0
                funding_round_type_venture=0
                funding_round_type_other=0
            elif(funding_round_type =='Series-a'):
                funding_round_type_series_a=1 
                funding_round_type_angel=0
                funding_round_type_crowdfunding=0
                funding_round_type_post_ipo=0
                funding_round_type_private_equity=0
                funding_round_type_series_b=0
                funding_round_type_series_c_plus=0
                funding_round_type_venture=0
                funding_round_type_other=0
            elif(funding_round_type =='Series-b'):
                funding_round_type_series_b=1 
                funding_round_type_angel=0
                funding_round_type_crowdfunding=0
                funding_round_type_post_ipo=0
                funding_round_type_private_equity=0
                funding_round_type_series_a=0
                funding_round_type_series_c_plus=0
                funding_round_type_venture=0
                funding_round_type_other=0
            elif(funding_round_type =='Series-c+'):
                funding_round_type_series_c_plus=1
                funding_round_type_angel=0
                funding_round_type_crowdfunding=0
                funding_round_type_post_ipo=0
                funding_round_type_private_equity=0
                funding_round_type_series_a=0
                funding_round_type_series_b=0
                funding_round_type_venture=0
                funding_round_type_other=0
            elif(funding_round_type =='Venture'):
                funding_round_type_venture=1
                funding_round_type_angel=0
                funding_round_type_crowdfunding=0
                funding_round_type_post_ipo=0
                funding_round_type_private_equity=0
                funding_round_type_series_a=0
                funding_round_type_series_b=0
                funding_round_type_series_c_plus=0
                funding_round_type_other=0
            elif(funding_round_type =='Other'):
                funding_round_type_other=1
                funding_round_type_venture=0
                funding_round_type_angel=0
                funding_round_type_crowdfunding=0
                funding_round_type_post_ipo=0
                funding_round_type_private_equity=0
                funding_round_type_series_a=0
                funding_round_type_series_b=0
                funding_round_type_series_c_plus=0

            
            input_values= ([[country_code_AUS,
                             country_code_CAN,
                             country_code_DEU,
                             country_code_ESP,
                             country_code_FRA,
                             country_code_GBR,
                             country_code_IND,
                             country_code_IRL,
                             country_code_ISR,
                             country_code_NLD,
                             country_code_USA,
                             country_code_others,
                             No_of_years_since_foundation,
                             No_of_years_since_first_funding,
                             No_of_years_since_last_funding,
                             No_of_years_since_last_milestone,
                             No_of_years_since_graduation,
                             funding_rounds,
                             funding_total_usd,
                             milestones,
                             twitter_presence,
                             funding_round_type_angel,
                             funding_round_type_crowdfunding,
                             funding_round_type_post_ipo,
                             funding_round_type_private_equity,
                             funding_round_type_series_a,
                             funding_round_type_series_b,
                             funding_round_type_series_c_plus,
                             funding_round_type_venture,
                             funding_round_type_other,
                             category_code_software,
                             category_code_web,
                             category_code_ecommerce,
                             category_code_advertising,
                             category_code_mobile,
                             category_code_consulting,
                             category_code_games_video,
                             category_code_enterprise,
                             category_code_biotech,
                             category_code_public_relations,
                             category_code_others,
                             ]])
            
            input_data_as_numpy_array = np.asarray(input_values)
            input_data_reshaped = input_data_as_numpy_array.reshape(-1,1)
            prediction = model.predict(input_data_reshaped)
            print(prediction)
            
            if (prediction[0] == 0):
                return 'Acquired/Closed'
            else:
                return 'Operating/IPO'
            #print('prediction is', prediction)
            
            return render_template('index.html',prediction_text="The status of the company is {}".format(prediction))


            # showing the prediction results in a UI
            #return render_template('result.html',prediction)
        #except Exception as e:
            #print('The Exception message is: ',e)
            #return 'something is wrong'
        # return render_template('results.html')
    else:   
        return render_template('index.html')
        


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    


    
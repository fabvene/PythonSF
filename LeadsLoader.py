# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 14:46:03 2015

@author: fabvene
"""



from simple_salesforce import Salesforce
sf = Salesforce(username='admin@schiller.edu', password='Schiller2012', security_token='w65YRKxwumpd8muAU0Y8LEUNs')

# Test
# leads = sf.query_all("SELECT Id, Email FROM Lead WHERE LastName = 'Jones'")
# Paris
# leads = sf.query_all("SELECT Id,Salutation,FirstName,LastName,Title,Street,City,State,PostalCode,Country,Phone,Email,Website,Description,LeadSource,Status,CreatedDate,Lead_date__c,Start_Date__c,Comments__c,BKTO__c,Campus_Vue__c,Passport_Nr__c,Comments_2__c,Passport_valid_until__c,SSN__c,Nationality__c,Program__c,Advisor_assigned_to__c,Start_Date_TEXT__c,Date_of_Birth__c,Gender__c,Campus__c,Student_Level__c,English__c,English_Score__c,Phone_2__c,Middle_Name__c,Campaign_Medium__c,Campaign_Source__c,Institution__c,Campaign_Name__c,Previous_Education__c,Campaign_Content__c,Condition__c,Import_Notes__c,Bad_Email__c,Bad_Phone__c,Campaign_Term__c,Landing_Page__c, OwnerId, Region__c FROM Lead WHERE OwnerId='00GD0000003Gm8JMAS' ")
# All
leads = sf.query_all("SELECT Id,Salutation,FirstName,LastName,Title,Street,City,State,PostalCode,Country,Phone,Email,Website,Description,LeadSource,Status,CreatedDate,Lead_date__c,Start_Date__c,Comments__c,BKTO__c,Campus_Vue__c,Passport_Nr__c,Comments_2__c,Passport_valid_until__c,SSN__c,Nationality__c,Program__c,Advisor_assigned_to__c,Start_Date_TEXT__c,Date_of_Birth__c,Gender__c,Campus__c,Student_Level__c,English__c,English_Score__c,Phone_2__c,Middle_Name__c,Campaign_Medium__c,Campaign_Source__c,Institution__c,Campaign_Name__c,Previous_Education__c,Campaign_Content__c,Condition__c,Import_Notes__c,Bad_Email__c,Bad_Phone__c,Campaign_Term__c,Landing_Page__c, OwnerId, Region__c FROM Lead ")

leads_df = pd.DataFrame(leads['records'])


leads_df.describe()
leads_df.columns

leads_df.Advisor_assigned_to__c.value_counts()

leads

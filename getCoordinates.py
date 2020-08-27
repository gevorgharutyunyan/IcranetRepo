import pandas as pd


# https://fermi.gsfc.nasa.gov/ssc/data/access/lat/10yr_catalog/ compared with 4LAC blazars catalog.

# create df for only blazars catalog
blazar_file = pd.read_csv("blazars.txt")
blazars = pd.DataFrame(blazar_file)
blazars.columns = ["Catalog_name", "RA", "DEC", "Sign","Flux","Energy_Flux","Spectrum_type","PL_index","LP_alpha","LP_beta","Type","Assoc_name","Redshift","Synchrotron_peak"]
blazars = blazars.loc[(blazars.Redshift > 2)&(blazars.Redshift < 2.5)] # select blazars between 2 < z < 2.5
blazars=blazars.reset_index() # start indexing from 0
blazars=blazars.drop("index" ,True)
blazars=blazars.sort_values(by =["Catalog_name"])


# create df for 10 year catalog(second release
all_sources_file = pd.read_csv("all_sources.txt")
all_sources = pd.DataFrame(all_sources_file)
all_sources.columns = ["Catalog_name", "RA", "DEC", "Sign","Flux","Energy_Flux","Spectrum_type","PL_index","LP_alpha","LP_beta","Type","Assoc_name"]
all_sources.loc[all_sources['Spectrum_type']=="PowerLaw", "LP_alpha"] = float(0) # for power law need not LP_beta and LP_alpha
all_sources.loc[all_sources['Spectrum_type']=="PowerLaw", "LP_beta"] = float(0)
all_sources=all_sources.loc[all_sources.Catalog_name.isin(blazars.Catalog_name)]

# create a df where column below were given from 10 years catalog
for_check= all_sources[["Catalog_name","RA","DEC","PL_index","LP_alpha","LP_beta"]]
for_check=for_check.reset_index() # start indexing from 0
for_check=for_check.drop("index" ,True)
for_check=for_check.sort_values(by =["Catalog_name"])
for_check["Redshift"] =  blazars["Redshift"]
for_check=for_check.sort_values(by =["Redshift"])
for_check.to_csv("for_check.csv",index=False)

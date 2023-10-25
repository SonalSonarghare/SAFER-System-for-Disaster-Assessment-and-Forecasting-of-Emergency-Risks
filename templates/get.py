import folium

m = folium.Map(location=[20.5937, 78.9629], zoom_start=10,tiles='CartoDB dark_matter' )

folium.Marker(
    [27.5706, 80.0982],
    popup=(
        "<div style='width: 500px; height: 300px;'>"
            <h2 style='color: blue; padding: 5px; background-color: black; display: inline-block;'
            onmouseover='this.style.border="none"' 
            onmouseout='this.style.border="2px solid black";'>
            Uttar Pradesh: Floods Aug-Oct 2022
            </h2>
            "<p style='font-size: 14px; text-align: justify;'>Uttar Pradesh experienced severe floods during August-October 2022 due to unprecedented and intense rains. Major floods have occurred in Ganga River Basin along the Rapti & Ghagra river reaches due to heavy rainfall and runoff. It has affected several districts in Uttar Pradesh, which left scores of population homeless and caused hundreds of fatalities, and washed away homes.<br>According to a report by the relief commissioner's office, the lives of around 5.8 lakh people have been impacted due to the floods.</p>"
            "<p style='font-size: 16px; font-weight:bold;'> Major Affected </p>"
        "</div>"
    ),
    tooltip='Click for UP information',
    icon=folium.Icon(icon='fas fa-house-flood-water', prefix='fa', icon_color='black', color='red')
).add_to(m)


folium.Marker(
    [10.1632, 76.6413],
    popup='Kerala 2020 floods',
    tooltip='Click to more information',
    icon=folium.Icon(icon='fas fa-house-flood-water',prefix='fa',icon_color='black',color='red') 
    
).add_to(m)

m.save('Map_main.html')
<p style="color:white" >Hourly Rainfall in Gorakhpur 1st-30th October 2022.</p>
<div style="width: 100%; height: 40%; margin:10px auto;">                       
    <center><iframe src="/static/Gorakhpur(Daily) (3).html" height="600" width="1000"frameborder="0"></iframe></center>
 </div
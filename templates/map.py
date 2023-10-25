import folium

m = folium.Map(location=[20.5937, 78.9629], zoom_start=10, tiles='CartoDB dark_matter')

popup_content = """
<div style='width: 500px; height: auto; padding: 9px; border: 2px solid #333; border-radius: 10px;'>
    <h2 style='color: #1e73be; background-color: #333; color: white; padding: 18px; border-radius: 5px;font-size:27px;margin-top: -2px;'>
        Uttar Pradesh: Floods Aug-Oct 2022
    </h2>
    <p style='font-size: 15px; text-align: justify;color: black;'>
        Uttar Pradesh experienced severe floods during August-October 2022 due to unprecedented and intense rains. Major floods have occurred in the Ganga River Basin along the Rapti & Ghagra river reaches due to heavy rainfall and runoff. It has affected several districts in Uttar Pradesh, leaving scores of people homeless, causing hundreds of fatalities, and washing away homes.<br>According to a report by the relief commissioner's office, the lives of around 5.8 lakh people have been impacted due to the floods.
    </p>
    <p style='font-size: 20px; font-weight: bold; margin-top: 20px;color: black;'>
        Major Affected Areas
    </p>
</div>

"""

folium.Marker(
    [27.5706, 80.0982],
    popup=folium.Popup(popup_content, max_width=500),
    tooltip='Click for Uttar Pradesh information',
    icon=folium.Icon(icon='fas fa-house-flood-water', prefix='fa', icon_color='black', color='orange')
).add_to(m)



popup_content1 = """
<div style='width: 500px; height: auto; padding: 9px; border: 2px solid #333; border-radius: 10px;'>
    <h2 style='color: #1e73be; background-color: #333; color: white; padding: 18px; border-radius: 5px;font-size:24px;margin-top: -2px;'>
        Himachal Pradesh: Floods Jul-Aug 2023
    </h2>
    <p style='font-size: 15px; text-align: justify;color: black;'>
        The 2023 North India floods were one of the worst disasters in Himachal Pradesh in the past 100 years. The state was hit by excessive rainfall in July and two unprecedented spells in August. The state government estimates that 13,000 houses were destroyed. The state also lost 408 transformers and 149 water supply schemes. 506 roads are still closed.
    </p>
    <p style='font-size: 20px; font-weight: bold; margin-top: 20px;color: black;'>
        Major Affected Areas
    </p>
</div>

"""
folium.Marker(
    [32.1024, 77.5619],
    popup=folium.Popup(popup_content1, max_width=500),
    tooltip='Click for Himachal Pradesh information',
    icon=folium.Icon(icon='fas fa-house-flood-water', prefix='fa', icon_color='black', color='red')
).add_to(m)

popup_content2 = """
<div style='width: 500px; height: auto; padding: 9px; border: 2px solid #333; border-radius: 10px;'>
    <h2 style='color: #1e73be; background-color: #333; color: white; padding: 18px; border-radius: 5px;font-size:24px;margin-top: -2px;'>
        Andhra Pradesh: Floods Aug 2023
    </h2>
    <p style='font-size: 15px; text-align: justify;color: black;'>
        The 2023 Andhra Pradesh floods were one of the worst floods to hit the state in recent years. The floods were caused by heavy monsoon rains and the overflowing of rivers such as the Krishna, Godavari, and Penner. The floods affected over 1 million people and caused widespread damage to property and infrastructure.The floods also had a devastating impact on agriculture. Over 100,000 hectares of crops were destroyed, and thousands of farmers lost their livelihoods.
    </p>
    <p style='font-size: 20px; font-weight: bold; margin-top: 20px;color: black;'>
        Major Affected Areas
    </p>
</div>

"""
folium.Marker(
    [15.9129, 79.7400],
    popup=folium.Popup(popup_content2, max_width=500),
    tooltip='Click for Andhra Pradesh information',
    icon=folium.Icon(icon='fas fa-house-flood-water', prefix='fa', icon_color='black', color='red')
).add_to(m)

m.save('Map_main1.html')

popup_content3 = """
<div style='width: 500px; height: auto; padding: 9px; border: 2px solid #333; border-radius: 10px;'>
    <h2 style='color: #1e73be; background-color: #333; color: white; padding: 18px; border-radius: 5px;font-size:24px;margin-top: -2px;'>
        Assam: Floods June 2023
    </h2>
    <p style='font-size: 15px; text-align: justify;color: black;'>
        The Assam floods of 2023 began on June 14, 2023.The floods were caused by heavy monsoon rains that led to the overflowing of the Brahmaputra river and its tributaries.The floods have affected over 1,00,000 people in 20 districts of the state. The major districts affected are Darrang, Dhubri, Goalpara, Majuli, Morigaon, and Udalguri.<br>The Assam government has launched a massive relief and rescue operation to help the flood victims. Over 400 relief camps have been set up to provide shelter and food to the evacuees.
    </p>
    <p style='font-size: 20px; font-weight: bold; margin-top: 20px;color: black;'>
        Major Affected Areas
    </p>
</div>

"""
folium.Marker(
    [26.2006, 92.9376],
    popup=folium.Popup(popup_content3, max_width=500),
    tooltip='Click for Assam information',
    icon=folium.Icon(icon='fas fa-house-flood-water', prefix='fa', icon_color='black', color='red')
).add_to(m)

m.save('Map_main1.html')

popup_content4 = """
<div style='width: 500px; height: auto; padding: 9px; border: 2px solid #333; border-radius: 10px;'>
    <h2 style='color: #1e73be; background-color: #333; color: white; padding: 18px; border-radius: 5px;font-size:24px;margin-top: -2px;'>
        Bihar: Floods Jul-Aug 2020
    </h2>
    <p style='font-size: 15px; text-align: justify;color: black;'>
        The 2020 Bihar floods were caused by heavy monsoon rains and the overflowing of rivers such as the Ganga, Kosi, and Mahananda.The floods affected over 74 lakh people in 16 districts of the state and caused widespread damage to property and infrastructure.The Bihar government launched a massive relief and rescue operation to help the flood victims. Over 400 relief camps were set up to provide shelter and food to the evacuees.
    </p>
    <p style='font-size: 20px; font-weight: bold; margin-top: 20px;color: black;'>
        Major Affected Areas
    </p>
</div>

"""
folium.Marker(
    [25.9644, 85.2722],
    popup=folium.Popup(popup_content4, max_width=500),
    tooltip='Click for Bihar information',
    icon=folium.Icon(icon='fas fa-house-flood-water', prefix='fa', icon_color='black', color='orange')
).add_to(m)

m.save('Map_main1.html')

popup_content5 = """
<div style='width: 500px; height: auto; padding: 9px; border: 2px solid #333; border-radius: 10px;'>
    <h2 style='color: #1e73be; background-color: #333; color: white; padding: 18px; border-radius: 5px;font-size:24px;margin-top: -2px;'>
        Odisha: Floods Aug 2022
    </h2>
    <p style='font-size: 15px; text-align: justify;color: black;'>
        The 2022 Odisha floods were caused by heavy monsoon rains that led to the overflowing of the Mahanadi river and its tributaries. The floods began in August and affected over 950,000 people in 26 districts of the state.The floods caused widespread damage to property and infrastructure. Over 126,000 hectares of crop land was damaged, 250,000 people were marooned, seven killed, over 14,000 houses were damaged and destroyed by the floods, 440 relief centers were established and ₹126 crore of public property got damaged and destroyed. Due to the crop damage, prices of affected vegetables increased noticeably and supply chains were affected.
    </p>
    <p style='font-size: 20px; font-weight: bold; margin-top: 20px;color: black;'>
        Major Affected Areas
    </p>
</div>

"""
folium.Marker(
    [20.2376, 84.2700],
    popup=folium.Popup(popup_content5, max_width=500),
    tooltip='Click for Odisha information',
    icon=folium.Icon(icon='fas fa-house-flood-water', prefix='fa', icon_color='black', color='orange')
).add_to(m)

m.save('Map_main1.html')


popup_content6 = """
<div style='width: 500px; height: auto; padding: 9px; border: 2px solid #333; border-radius: 10px;'>
    <h2 style='color: #1e73be; background-color: #333; color: white; padding: 18px; border-radius: 5px;font-size:24px;margin-top: -2px;'>
        Kerela: Floods Aug 2018
    </h2>
    <p style='font-size: 15px; text-align: justify;color: black;'>
        The 2018 Kerala floods were the worst floods in the state in nearly a century.The floods were caused by unusually heavy monsoon rains, and resulted in the deaths of over 480 people.The flood also caused widespread damage to property and infrastructure, and displaced over a million people.The floods had a devastating impact on the state's economy, with losses estimated at over $5 billion.The floods also caused significant environmental damage, with the destruction of forests and wildlife habitat.
    </p>
    <p style='font-size: 20px; font-weight: bold; margin-top: 20px;color: black;'>
        Major Affected Areas
    </p>
</div>

"""
folium.Marker(
    [10.1632, 76.6413],
    popup=folium.Popup(popup_content6, max_width=500),
    tooltip='Click for Kerela information',
    icon=folium.Icon(icon='fas fa-house-flood-water', prefix='fa', icon_color='black', color='orange')
).add_to(m)

m.save('Map_main1.html')

popup_content7 = """
<div style='width: 500px; height: auto; padding: 9px; border: 2px solid #333; border-radius: 10px;'>
    <h2 style='color: #1e73be; background-color: #333; color: white; padding: 18px; border-radius: 5px;font-size:24px;margin-top: -2px;'>
        Sikkim: Floods Oct 2023
    </h2>
    <p style='font-size: 15px; text-align: justify;color: black;'>
        The 2023 Sikkim floods were a series of flash floods and landslides that occurred in the Indian state of Sikkim on October 4, 2023.The floods were caused by heavy rainfall, which triggered a glacial lake outburst flood (GLOF) in the Teesta River.The GLOF destroyed the Teesta III Dam and caused widespread flooding downstream.The floods affected over 50,000 people and killed at least 40 people and displaced thousands more. The floods also caused widespread damage to infrastructure, including roads, bridges, and power lines. The estimated cost of the damage is in the billions of rupees.
    </p>
    <p style='font-size: 20px; font-weight: bold; margin-top: 20px;color: black;'>
        Major Affected Areas
    </p>
    <a href="templates/Floods-Maps/Gorakhpur.html" class="btn" style="background-color: #1e73be; color: white; padding: 10px 20px; text-decoration: none; font-weight: bold; border-radius: 5px; margin-top: 10px;">More Details</a>
</div>
</div>

"""
folium.Marker(
    [27.3516, 88.3239],
    popup=folium.Popup(popup_content7, max_width=500),
    tooltip='Click for Sikkim information',
    icon=folium.Icon(icon='fas fa-house-flood-water', prefix='fa', icon_color='black', color='red')
).add_to(m)

m.save('Map_main1.html')
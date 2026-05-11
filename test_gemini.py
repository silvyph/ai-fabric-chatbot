from google import genai

client = genai.Client(api_key="AIzaSyCFmUsicq2O-R_gn35Ycgek3Ql7A-D_oIU")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Rekomendasikan bahan kain adem untuk kemeja"
)

print(response.text)
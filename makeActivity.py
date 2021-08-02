import random
import time
import webbrowser

timesExecute = 15
timePerRefresh = random.randint(600, 1000)

#vega
'''
planets = ['https://vega.ogamex.net/home?planet=e9215b16-b75a-46b5-b7a2-801a4f65122d',
           'https://vega.ogamex.net/home?planet=0850122b-3b35-4171-bc8d-b956d09920a9',
           'https://vega.ogamex.net/home?planet=ec52409d-e8f5-43a3-a6af-b3d615ac6922',
           'https://vega.ogamex.net/home?planet=80ca7d48-dc6d-43f3-9262-695f770d021c',
           'https://vega.ogamex.net/home?planet=0fd8c2d6-658c-4be0-b45b-9968f3e70cce',
           'https://vega.ogamex.net/home?planet=e5ab9f82-398c-48f7-833a-4d6ecc24218a',
           'https://vega.ogamex.net/home?planet=8b794959-4087-4a2a-9f0a-3ae1f456b424',
           'https://vega.ogamex.net/home?planet=9801ddad-9f93-4af9-bd82-c657f2d95fc6',
           'https://vega.ogamex.net/home?planet=74209a1f-0c4f-46cd-ab12-cac616817b7b',
           'https://vega.ogamex.net/home?planet=feec1e65-f5fd-474a-80c0-df78701472ee',
           'https://vega.ogamex.net/home?planet=33103df4-9093-45f4-81f1-52987dfa95ff',
           'https://vega.ogamex.net/home?planet=33333e4f-e744-480d-b3dd-f4c72c101f36',
           'https://vega.ogamex.net/home?planet=00bdc403-1b96-4782-a4dc-546eacb18c73',
           'https://vega.ogamex.net/home?planet=6d9444f1-31f2-4813-b12a-224d869abdb6',
           'https://vega.ogamex.net/home?planet=f4c57bd1-4730-4f32-8ba5-ee2765b164fc',
           'https://vega.ogamex.net/home?planet=c325c385-178d-4810-9ba9-6bd8278a5ff7',
           'https://vega.ogamex.net/home?planet=ba29daa8-19a2-4001-99bb-0dc779474d7c',
           'https://vega.ogamex.net/home?planet=acc5fa6b-3881-48ba-8f37-268c6b58d7f2',
           'https://vega.ogamex.net/home?planet=2f074f75-0aad-4914-82d5-86519085de11',
           'https://vega.ogamex.net/home?planet=687cc926-a9e7-4409-849a-8b771fc7652a',
           'https://vega.ogamex.net/home?planet=43fd62fa-ca04-4e3d-8347-ea32d34e7081']
'''

#nova
'''
planets = [ 'https://nova.ogamex.net/home?planet=91bdcc46-869e-481a-811a-34d444f00af0',
            'https://nova.ogamex.net/home?planet=b7e03be0-a7d7-40fb-82c2-4b3037b91e5c',
            'https://nova.ogamex.net/home?planet=7945b5f4-3e58-461b-b287-846e7a7ec5ba',
            'https://nova.ogamex.net/home?planet=64e5d7a3-5bd3-4f52-91a8-164f5d3f2ced',
            'https://nova.ogamex.net/home?planet=b9deb695-e976-474b-904e-aafdf68dfb4e',
            'https://nova.ogamex.net/home?planet=013a8e31-9807-4a69-9905-624740dd89fd',
            'https://nova.ogamex.net/home?planet=289c1c69-5388-477e-a4ab-f2f7965c32b4',
            'https://nova.ogamex.net/home?planet=c219ec16-e21f-41ae-933a-9f2b8c6a4858',
            'https://nova.ogamex.net/home?planet=3999b1e8-191d-4944-a698-d3dd5a2af627',
            'https://nova.ogamex.net/home?planet=7e9ecb31-86fe-4f89-b421-e219e62bdd56',
            'https://nova.ogamex.net/home?planet=971c7495-9a4a-4bfa-b5b2-3adfa0251418',
            'https://nova.ogamex.net/home?planet=042596df-035e-4600-9dcc-d370a5b8d4dc',
            'https://nova.ogamex.net/home?planet=4501acfc-1ff3-4021-8591-eaf5cef368c5',
            'https://nova.ogamex.net/home?planet=4d80d7b1-1ce1-463a-bdc2-001498605f1c',
            'https://nova.ogamex.net/home?planet=666351a5-1c54-4b1d-b341-5e39ec71671d']
'''
'''
moons = ['https://vega.ogamex.net/home?planet=082546e9-b088-40f4-bfde-8806b121b739',
         'https://vega.ogamex.net/home?planet=95a3b373-1065-4a26-8909-a98bf7ffa0f9',
         'https://vega.ogamex.net/home?planet=13e40d9e-acd8-4249-bf51-ff7b1f87cbd5',
         'https://vega.ogamex.net/home?planet=b3e8f013-d81f-4a34-90c2-b336ce9b2b23',
         'https://vega.ogamex.net/home?planet=d8a761e5-d750-44d6-b0f1-c9a16291cadd',
         'https://vega.ogamex.net/home?planet=c7fdbebe-a78a-45b5-8786-266714e969ac',
         'https://vega.ogamex.net/home?planet=faaa3772-cb0d-45e8-8a66-0588b702402f',
         'https://vega.ogamex.net/home?planet=84e08c0e-0d1e-4d95-a2e7-d5b181c3f997',
         'https://vega.ogamex.net/home?planet=99c17658-c369-4213-8079-e89bd7127dd7',
         'https://vega.ogamex.net/home?planet=319340d5-df2b-40a9-8367-9d1256d81e3f',
         'https://vega.ogamex.net/home?planet=8b9764b1-dd11-4267-92cb-a7d2e6bff04c',
         'https://vega.ogamex.net/home?planet=2af52d19-770e-4213-8a87-a5f045a5982d',
         'https://vega.ogamex.net/home?planet=474cf385-ae36-4e3f-bb65-c526d907d390',
         'https://vega.ogamex.net/home?planet=e72080fd-8837-43fd-a004-0af65192a1f6',
         'https://vega.ogamex.net/home?planet=f0b7f4b1-3efb-4de2-9c02-19b934f02644']

'''
'''
moons = [   'https://nova.ogamex.net/home?planet=c1c0185c-2342-47a7-8cda-e64d831e9f8d',
            'https://nova.ogamex.net/home?planet=d1bec4a4-e021-449a-97c6-30c8bf672ed2']
'''

moons = [   "https://titan.ogamex.net/home?planet=22e51bd8-826b-48d4-ba64-cad1b74671a9",
            "https://titan.ogamex.net/home?planet=e7958abb-a551-452a-a05f-c58ee875e54b",
            "https://titan.ogamex.net/home?planet=9422f494-6799-4998-b453-2b55ad1aa593",
            "https://titan.ogamex.net/home?planet=d9e037db-f45f-49fe-b9e1-950711b0a342",
            "https://titan.ogamex.net/home?planet=f295c051-6d17-4fe6-8e50-f8f570744770",
            "https://titan.ogamex.net/home?planet=6745ada1-e1d4-41cf-a0b9-87f30e14e517",
            "https://titan.ogamex.net/home?planet=0988000e-e306-4437-bc4b-9be8c26c6133",
            "https://titan.ogamex.net/home?planet=c918c814-effc-46ba-8da3-e4526142c7f4",
            "https://titan.ogamex.net/home?planet=26dc291c-baaf-43ac-857d-b3508d4ad921",
            "https://titan.ogamex.net/home?planet=0d64fc88-657a-4d35-8c17-6101ba404707",
            "https://titan.ogamex.net/home?planet=f7571a62-ba6b-4d60-9f52-79c4d95a25c5",
            "https://titan.ogamex.net/home?planet=e04fdaa6-bf6b-4efc-a499-386498f71f0b",
            "https://titan.ogamex.net/home?planet=7e673da7-d6f6-488f-b8cd-d603d4f9bcad",
            "https://titan.ogamex.net/home?planet=205b762d-5e95-474d-8375-67232001dff8",
            "https://titan.ogamex.net/home?planet=8bd0ddc5-51a2-4f8b-b729-59122dac21db",
            "https://titan.ogamex.net/home?planet=1b0a8055-1553-40e3-8621-ac270de28aed",
            "https://titan.ogamex.net/home?planet=9a1d0800-a0fc-478b-8394-24fb07eb16eb",
            "https://titan.ogamex.net/home?planet=6e04f8ce-0ab6-45c2-9f65-feadd67b6855",
            "https://titan.ogamex.net/home?planet=995ad0a4-d6db-4a0c-950d-f93257fa8483",
            "https://titan.ogamex.net/home?planet=decf5b09-ddae-447c-bba9-592bd2851104",
            "https://titan.ogamex.net/home?planet=eb230c60-5f19-4118-b8cb-282b16ac14c0",
            "https://titan.ogamex.net/home?planet=ed60c6da-20f6-48fb-a649-150d50d813f3",
            "https://titan.ogamex.net/home?planet=90dc3740-c9fd-4f7a-a14e-111a80ac9d20",
            "https://titan.ogamex.net/home?planet=4caedd83-0b06-4ede-9ab9-5af52987d7bb",
            "https://titan.ogamex.net/home?planet=28fb04bf-484b-48e4-9dee-e0e8ff821cd1"]

def openMoons():
    lengthMoons = len(moons)
    counter = 0
    while counter < lengthMoons:
        position = random.randint(0, lengthMoons - 1)
        webbrowser.open(moons[position])
        counter = counter + 1

i = 1

while i < 100:
    openMoons()

    time.sleep(timePerRefresh)
    i = i + 1

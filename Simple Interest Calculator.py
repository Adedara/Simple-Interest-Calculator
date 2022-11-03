from unittest import result
import flet
from flet import *

def main(page: Page):
    page.title = "Simple Interest Calculator"
    page.padding = 50

    principal = TextField(label = 'Input Principal', width=600)
    rate = TextField(label="Input Rate", width=600)
    time = TextField(label='Input Time', width=600)
    result = Text(size=20, weight='w600')

    def calcInterest(e):
        p = int(principal.value)
        r = float(rate.value)
        t = int(time.value)

        interest = ((p*r*t)/100)
        result.value = f'Your interest is ${interest}'
        
        #Clear inputs after calculation
        principal.value = ''
        rate.value = ''
        time.value = ''

        page.update()
        
    #Method to add all 'controls' to the page. You add controls after defining them.
    page.add(
        Row(
            [
                Text('Simple Interest Calculator', size = 30, weight= 'bold')
            ]
        ),
        Column(
            [
                principal,
                rate,
                time,
                FilledButton(
                    "Calculate",
                    on_click=calcInterest
                ),

                Row(
                    [result]
                    )
            ]
        )

    )

flet.app(target=main)



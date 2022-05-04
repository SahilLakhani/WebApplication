import pywebio
from pywebio.input import input, FLOAT
from pywebio.output import put_text, put_html, put_markdown, put_table


def moneycalc():
    money_made = input("Input the amount of money you make in a year($): ", type=FLOAT)
    expenses = input("Input a rough estimate of your expenses per month($): ", type=FLOAT)

    amnt_post_tax = money_made * 0.70

    total_expense = expenses * 12

    amnt_post_total = amnt_post_tax - total_expense

    percent_saved = (amnt_post_total / amnt_post_tax) * 100

    top_status = [(90, 'You saved almost all of your money'), (70, 'You saved a lot of money'),
                  (50, 'You saved half of your money'), (30, 'You did not save a lot of money'),
                  (10, 'You barely have any money left!'), (0, 'You have no savings')]

    for top, status in top_status:
        if percent_saved <= 0:
            put_markdown('# **Results**')
            put_text('Your percent saved is: %.2f. Message: %s' % (percent_saved, status))
            break
        elif percent_saved >= top and percent_saved <= 0:
            put_markdown('# **Results**')
            put_text('Your percent saved is: %.2f. Message: %s' % (percent_saved, status))

            break

    if __name__ == '__main__':
        moneycalc()

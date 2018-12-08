{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Months: 86\n",
      "Total: $38,382,578.00\n",
      "Average Change: $6,195.15\n",
      "Greatest Increase in Profits: $1,926,159.00\n",
      "Greatest Decrease in Profits: $-2,196,167.00\n"
     ]
    }
   ],
   "source": [
    "budget = os.path.join(\".\", \"budget_data.csv\")\n",
    "with open(budget, newline='') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    header = next(csvreader)\n",
    "    total = 0\n",
    "    months = 0\n",
    "    lastmonthprof = 0\n",
    "    revchange = 0\n",
    "    greatestchange = 0\n",
    "    leastchange = 0\n",
    "    sum_revchange = 0\n",
    "    for row in csvreader:\n",
    "        months = months + 1\n",
    "        total = total + int(row[1])\n",
    "        currentprof = int(row[1])\n",
    "        if months == 1:\n",
    "            lastmonthprof = currentprof\n",
    "        else:\n",
    "            revchange = currentprof - lastmonthprof\n",
    "            if revchange > greatestchange:\n",
    "                greatestchange = revchange\n",
    "            if revchange < leastchange:\n",
    "                leastchange = revchange\n",
    "        lastmonthprof = currentprof\n",
    "    sum_revchange += revchange                \n",
    "    averagechange = sum_revchange/months -1\n",
    "    \n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"----------------------------\")\n",
    "    print(\"Months: \" + str(months))\n",
    "    print(\"Total: \" + '${:,.2f}'.format(total))\n",
    "    print(\"Average Change: \" + '${:,.2f}'.format(averagechange))\n",
    "    print(\"Greatest Increase in Profits: \" + '${:,.2f}'.format(greatestchange))\n",
    "    print(\"Greatest Decrease in Profits: \" + '${:,.2f}'.format(leastchange))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

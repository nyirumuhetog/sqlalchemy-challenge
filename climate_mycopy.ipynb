{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "from matplotlib import style\n",
    "style.use('fivethirtyeight')\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Reflect Tables into SQLAlchemy ORM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python SQL toolkit and Object Relational Mapper\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func, inspect"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\",echo = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n",
    "# reflect the tables\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['measurement', 'station']"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We can view all of the classes that automap found\n",
    "Base.classes.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save references to each table\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create our session (link) from Python to the DB\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id INTEGER\n",
      "station TEXT\n",
      "date TEXT\n",
      "prcp FLOAT\n",
      "tobs FLOAT\n"
     ]
    }
   ],
   "source": [
    "inspector = inspect(engine)\n",
    "columns = inspector.get_columns('measurement')\n",
    "for c in columns:\n",
    "    print(c['name'], c['type'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 'USC00519397', '2010-01-01', 0.08, 65.0),\n",
       " (2, 'USC00519397', '2010-01-02', 0.0, 63.0),\n",
       " (3, 'USC00519397', '2010-01-03', 0.0, 74.0),\n",
       " (4, 'USC00519397', '2010-01-04', 0.0, 76.0),\n",
       " (5, 'USC00519397', '2010-01-06', None, 73.0)]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "engine.execute('SELECT * FROM measurement LIMIT 5').fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id INTEGER\n",
      "station TEXT\n",
      "name TEXT\n",
      "latitude FLOAT\n",
      "longitude FLOAT\n",
      "elevation FLOAT\n"
     ]
    }
   ],
   "source": [
    "columns = inspector.get_columns('station')\n",
    "for cl in columns:\n",
    "    print(cl['name'], cl['type'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 'USC00519397', 'WAIKIKI 717.2, HI US', 21.2716, -157.8168, 3.0),\n",
       " (2, 'USC00513117', 'KANEOHE 838.1, HI US', 21.4234, -157.8015, 14.6),\n",
       " (3, 'USC00514830', 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 21.5213, -157.8374, 7.0),\n",
       " (4, 'USC00517948', 'PEARL CITY, HI US', 21.3934, -157.9751, 11.9),\n",
       " (5, 'USC00518838', 'UPPER WAHIAWA 874.3, HI US', 21.4992, -158.0111, 306.6),\n",
       " (6, 'USC00519523', 'WAIMANALO EXPERIMENTAL FARM, HI US', 21.33556, -157.71139, 19.5),\n",
       " (7, 'USC00519281', 'WAIHEE 837.5, HI US', 21.45167, -157.84888999999998, 32.9),\n",
       " (8, 'USC00511918', 'HONOLULU OBSERVATORY 702.2, HI US', 21.3152, -157.9992, 0.9),\n",
       " (9, 'USC00516128', 'MANOA LYON ARBO 785.2, HI US', 21.3331, -157.8025, 152.4)]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "engine.execute('SELECT * FROM station').fetchall()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Exploratory Climate Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('2017-08-23')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Design a query to retrieve the last 12 months of precipitation data and plot the results\n",
    "\n",
    "# Calculate the date 1 year ago from the last data point in the database\n",
    "\n",
    "#session.query(func.count(Measurement.date)).all()\n",
    "\n",
    "last_data_point = session.query(Measurement.date).order_by(Measurement.date.desc()).first()\n",
    "\n",
    "last_data_point\n",
    "\n",
    "# session.query(func.extract(Topic.date_created, 'year'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2016-08-23\n"
     ]
    }
   ],
   "source": [
    "\n",
    "year_ago = dt.date(2017,8,23) - dt.timedelta(days= 365)\n",
    "print(year_ago)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform a query to retrieve the data and precipitation scores\n",
    "# sel = [Measurement.date, \n",
    "#        func.avg(Measurement.prcp)]\n",
    "# year_prcp = session.query(*sel).\\\n",
    "\n",
    "year_prcp = session.query(Measurement.date, Measurement.prcp).\\\n",
    "    filter(Measurement.date >= year_ago, Measurement.prcp != None).\\\n",
    "    order_by(Measurement.date).all()\n",
    "#     group_by(Measurement.date).\\\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Precipitation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2016-08-23</th>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2016-08-23</th>\n",
       "      <td>0.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2016-08-23</th>\n",
       "      <td>0.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2016-08-23</th>\n",
       "      <td>0.02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2016-08-23</th>\n",
       "      <td>1.79</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Precipitation\n",
       "Date                     \n",
       "2016-08-23           0.00\n",
       "2016-08-23           0.15\n",
       "2016-08-23           0.05\n",
       "2016-08-23           0.02\n",
       "2016-08-23           1.79"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Save the query results as a Pandas DataFrame and set the index to the date column\n",
    "# Sort the dataframe by date\n",
    "df = pd.DataFrame(year_prcp, columns=['Date', 'Precipitation'])\n",
    "df.set_index('Date', inplace=True)\n",
    "df.head()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfAAAAFgCAYAAABEyiulAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvhp/UCwAAIABJREFUeJzt3XecXGW9P/DPs7vZ7CabBCEEQgvFVS5XlCJ6aRZAQUBRhEvw/hQR7xVQLhCkRCwIcoOgcvGCBenSe5GYEErKppNkk5A6SUjb3mZ2p+xOe35/7M4ys3tm5pwzpz1nPu/XixfZKec8p8zzPU8XUkoQERGRWircTgAREREZxwBORESkIAZwIiIiBTGAExERKYgBnIiISEEM4ERERAoqGsCFEJ8UQjRm/dcrhLjOicQRERGRNmFkHLgQohJAE4DPSyl3AUAoFOJAciIiIptNmjRJZP9ttAr9TADbM8GbiIiI3GE0gE8H8IwdCSEiIiL9dFehCyGqATQD+FcpZVvm9ewq9EAgYHkCiYiIylV9ff3wv0dWoVcZ2M7XAKzODt6FdmSFQCBg+TbdxmNSA49JDX48JsCfx8Vjsp6RKvRLwepzIiIiT9BVAhdCjAPwFQA/sjc5RETkNCklwuEw0um0bfuoqalBKBSybftusPqYKioqUFdXByFE8Q9DZwCXUkYB7FdKwoiIyJvC4TDGjh2L6upq2/YxduxY1NTU2LZ9N1h9TPF4HOFwGBMmTND1ec7ERkRU5tLptK3Bm/Sprq42VAvCAE5ERKQgBnAiIiIFMYATEZHr9t13X5x22mk4+eSTcdlllyEajZa8zTVr1uCmm24q+JmWlhZ873vfAwCsW7cOb731VtHtjvzc7Nmzce+995aWWBMYwImIyHW1tbVoaGjA0qVLUV1djUceeSTnfSml4V7yxx9/PO6+++6Cn5k6dSqeeOIJAMD69esxb968otsd+blzzz0X119/vaG0WcHIRC6+9E5TP9Z3JfDNI2px+ISyPx1ERNjn0SZLtxe8/GBDnz/55JOxYcMG7Nq1CxdffDFOP/10rFixAk899RS2bduGWbNmYWBgAEcccQQeeOAB1NXVYfXq1bjlllsQiUQwduxYvPbaa2hsbMT999+P5557DrNmzcKHH36IlpYWNDU14dprr8Vll12GXbt2Yfr06ViwYAFmzZqFWCyGpUuXYsaMGZg2bRpmzpyJWCyG2tpaPPDAA5g2bdrw55YsWYIbbrgBsVgMjY2NuOeee7B792785Cc/QWdnJyZPnowHHngAhx56KK666ipMmDABjY2NaGtrw+23344LLrigpPNa1iXw13fG8O23unDbql584bV2BAfsGwNJRETFJZNJzJs3D8cccwyAwdnOpk+fjkWLFmH8+PG455578Oqrr2LhwoU4/vjj8cADDyAej+Pyyy/HXXfdhcWLF+PVV19FbW3tqG1v2LABzz//PObNm4e7774bLS0tw+9VV1dj5syZuPDCC9HQ0IALL7wQ9fX1mD17NhYtWoSf/exnuP3223M+98477+DCCy/M2ceNN96I6dOnY8mSJbj44otx8803D7/X1taGOXPm4LnnnsNtt91W8rkq6yLnZe91D/+7NyFx/4Ywfn7CRBdTRERUnmKxGE477TQAgyXw7373u2hpacGhhx6Kk046CQCwcuVKbNmyBWeffTYAIJFI4KSTTkIgEMCBBx6IE044AQAwcaJ2Pn7uueeitrYWtbW1OO2007Bq1Soce+yxedPU29uLq666Cjt27IAQAolEouhxrFy5Ek8++SQAYPr06fjVr341/N55552HiooKHH300ejo6NBxVgor6wA+chmXDd3FLw4REVkv0wY+0vjx44f/LaXEl7/8ZTz88MM5n/nggw90zV428jPFvnPnnXfi9NNPx1NPPYVdu3bh/PPPL7qPQvscO3bs8L/1LiRWSFkHcCIiGs1om7VTTjrpJNx4443YsWMHjjzySESjUTQ3N+MTn/gEWlpasHr1apxwwgno6+vTrEKfPXs2ZsyYgWg0isWLF+O2225DPB4ffr+urg59fX3Df/f29mLq1KkAgKeffjrv57J97nOfw0svvYTp06fj+eefx7/9279ZdfijlHUbOBERqSPTKeyKK67AKaecgrPOOgtbt25FdXU1Hn30Udx000049dRT8a1vfQv9/f2jvn/iiSfi3//933HWWWfhxhtvHA7OGV/4whewZcsWnHbaaXj55Zdx7bXX4vbbb8fZZ5+NVCo16nNnnnkmXn755Zxt/Pa3v8VTTz2FU045Bc899xzuuusue04GDKwHnk/2euBWs3uptpE9Lc89rAZPn2nvlO9uLz9nBx6TGnhM6nD6uEKhECZNmmTrPvr7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\n",
      "text/plain": [
       "<Figure size 504x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Use Pandas Plotting with Matplotlib to plot the data\n",
    "df.plot(figsize=(7,5))\n",
    "plt.tight_layout()\n",
    "plt.savefig('Images/Precipitation.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Precipitation</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>2021.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.177279</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.461190</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.020000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.130000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>6.700000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Precipitation\n",
       "count    2021.000000\n",
       "mean        0.177279\n",
       "std         0.461190\n",
       "min         0.000000\n",
       "25%         0.000000\n",
       "50%         0.020000\n",
       "75%         0.130000\n",
       "max         6.700000"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use Pandas to calcualte the summary statistics for the precipitation data\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Design a query to show how many stations are available in this dataset?\n",
    "\n",
    "#session.query(Measurement.station).group_by(Measurement.station).count()\n",
    "session.query(Measurement.station).distinct().count()\n",
    "               \n",
    "#session.query(func.count(Station.station)).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "#session.query(func.count(Measurement.station)).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('USC00519281', 2772),\n",
       " ('USC00519397', 2724),\n",
       " ('USC00513117', 2709),\n",
       " ('USC00519523', 2669),\n",
       " ('USC00516128', 2612),\n",
       " ('USC00514830', 2202),\n",
       " ('USC00511918', 1979),\n",
       " ('USC00517948', 1372),\n",
       " ('USC00518838', 511)]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# What are the most active stations? (i.e. what stations have the most rows)?\n",
    "# List the stations and the counts in descending order.\n",
    "active_stations = session.query(Measurement.station,func.count(Measurement.station)).\\\n",
    "                               group_by(Measurement.station).\\\n",
    "                               order_by(func.count(Measurement.station).desc()).all()\n",
    "active_stations\n",
    "\n",
    "# session.query(Invoices.BillingCountry, func.sum(Invoices.Total)).\\\n",
    "#     group_by(Invoices.BillingCountry).\\\n",
    "#     order_by(func.sum(Invoices.Total).desc()).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(54.0, 85.0, 71.66378066378067)]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Using the station id from the previous query, calculate the lowest temperature recorded, \n",
    "# highest temperature recorded, and average temperature most active station?\n",
    "result = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\\\n",
    "                filter(Measurement.station == 'USC00519281').order_by(func.min(Measurement.tobs)).all()\n",
    "result\n",
    "#.order_by((Measurement.station).first()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# year_temp = session.query(Measurement.tobs).\\\n",
    "#     filter(Measurement.date >= year_ago, Measurement.station == high_temp_station).\\\n",
    "#     order_by(Measurement.tobs).all()\n",
    "\n",
    "year_temp = session.query(Measurement.tobs).\\\n",
    "      filter(Measurement.date >= year_ago, Measurement.station == 'USC00519281').\\\n",
    "      order_by(Measurement.tobs).all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Tobs</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>59.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>59.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>59.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>60.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>60.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Tobs\n",
       "0  59.0\n",
       "1  59.0\n",
       "2  59.0\n",
       "3  60.0\n",
       "4  60.0"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "df1 = pd.DataFrame(year_temp, columns=['Tobs'])\n",
    "df1.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "bins = 12\n",
    "df1.plot.hist(year_temp,bins)\n",
    "plt.ylim(0,70)\n",
    "plt.savefig('Images/station-histogram.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(62.0, 69.57142857142857, 74.0)]\n"
     ]
    }
   ],
   "source": [
    "# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' \n",
    "# and return the minimum, average, and maximum temperatures for that range of dates\n",
    "def calc_temps(start_date, end_date):\n",
    "    \"\"\"TMIN, TAVG, and TMAX for a list of dates.\n",
    "    \n",
    "    Args:\n",
    "        start_date (string): A date string in the format %Y-%m-%d\n",
    "        end_date (string): A date string in the format %Y-%m-%d\n",
    "        \n",
    "    Returns:\n",
    "        TMIN, TAVE, and TMAX\n",
    "    \"\"\"\n",
    "    \n",
    "    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\\\n",
    "        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()\n",
    "\n",
    "# function usage example\n",
    "print(calc_temps('2012-02-28', '2012-03-05'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(62.0, 68.05714285714286, 74.0)]\n"
     ]
    }
   ],
   "source": [
    "# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax \n",
    "# for your trip using the previous year's data for those same dates.\n",
    "prev_year_start = dt.date(2018,1,1) - dt.timedelta(days= 365)\n",
    "# print(prev_year_start)\n",
    "prev_year_end = prev_year_start + dt.timedelta(days = 5)\n",
    "#print(prev_year_end)\n",
    "calc_temp = calc_temps(prev_year_start,prev_year_end)\n",
    "print(calc_temp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the results from your previous query as a bar chart. \n",
    "# Use \"Trip Avg Temp\" as your Title\n",
    "# Use the average temperature for the y value\n",
    "# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)\n",
    "ta_temp= list(np.ravel(calc_temp))\n",
    "#ta_temp\n",
    "tmin = ta_temp[0]\n",
    "tmax = ta_temp[2]\n",
    "temp_avg = ta_temp[1]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAANAAAAI4CAYAAAAbLGeyAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvhp/UCwAAFFhJREFUeJzt3X+QrQV93/H3R65AgnIBHZRfGTCzaBCjpsiPGi2BTCPGCaSjLVbNraWlTauRqqM2Tmo7aTrGEH+0TVqNEKFahKARAzZKEWOTOvgj2oASctEYuHIRBPklBES//eOci8e9u2cP97u7z55736+ZnbPPc55z9rtn7vs+53nO2d1UFZJ2zWOGHkCaZwYkNRiQ1GBAUoMBSQ0GJDUY0BpKcmuS1w89h9aOAU2RpFb4+PoKd/EM4HdXcZ73JvlekrNX6z5X+Hr/cobH4E3rMctGFV9IXV6SJ08sHg9cNr68ebzue1V1+xK327uqHlrlWfYHvgG8C3hBVR23mve/zNf8EWDzxKr/ChwE/OOJdfdW1XfWepaNyj3QFFV1644P4M7x6tsn1t8OjzxVe0uS9yS5E7hqYv0jT+EmtntfknuT3J7k15NkhnFeBlwL/Cfg6CQ/NXG/T0jyYJJ/MHmDJEcm+X6Sk8fLByf5wyT3j2f5tSQfTHL5Mt//A4seg78FHppctyOeJE9PcnmSe5LcMf786IlZzknyrSQ/n+T6JA8k+fh49hckuS7JfUmuSPLEidu9M8nnk5yd5Kbx7a5IcugMj9maM6DV8zrgb4ATgGlPsV4HfBX4O8AbgNcDvzzD/Z8NvK+q7gcunfwaVXUH8DFgy6LbvBy4CfiT8fL7gacCLwB+FngacNoMX3uqJEcCfwr8JXAS8DzgduCT4z3nDo8HzhnP9TPAMcAfMHoMtgCnAMcCv7HoSzwV+IfALwCnAj8GfLA796qoKj9m+AB+GijgyCWuuxW4Ypn1r1+0fOWibd4O3LjC1z4BeAA4YLz8fOAeYL+Jbc4AHgKeOLHuBuDXx58/Yzz/cyeu32c80+UzPgbvB/54ifXvXLwe2ItRRP9kvHzO4sePUSgF/PjEuv8w+XiM7/sh4JCJdcePb3fc0P8u3AOtns/OuN1nFi3/GfCUJPtOuc2/AC6rqrsAqurTwG3ASye2uYJRVC8FSHICcDRw4fj6Y4DvT85ZVQ8CX5xx7mmeA5wyfgp2X5L7gLsZHS8tTGx3T1V9fWL5VuD+qvrqonUHL7r/r1fV9onlzzGK6phVmL1l09AD7EZ29UB66vFPks3APwL2TfLiiasew+hp3HsBquq7SS4Cfgn4L+PLz1TV1l2c69F4DPAR4FeXuO7bE59/d9F1tcy6ufmP3YDW34mLlk8C/rqq/naZ7V8O3MvoadykJwJXJ3lWVX1pvO5C4FVJfpJRdG+e2P4rjP5hHs9or0eSfYBnA5/fxe9lh88zOqb6elU93LyvpRyZ5Mk1OpEBcBywN3D9GnytR2VuSt+NnJDkzUkWkmxhdALhHVO2Pxv4UFVdt+jjU4yeykyeTPgco1AuAB4HXDxx3bXAlcC7kzwvydMZ7b32ZfS/fse5jJ52XZrkpCRHJXl+kt8ax9z1IHBhkmclOYnR3H82/n4HZUDr7+2Mzn59EfhtRgfJS77YOv7H8pPAJcvc18XAy5LsN7HuQuBZwB/tOGaa8ArgRuDjjE61/xXwaUanp3dZVf0Noz3pd4HLGe0ZLmC0l9zpdbJdcAPwYeCPgKuBW4AzV+F+23whdR0luRU4t6rOHXoWgCSPZRTU+6vqzSttP4Qk7wR+utbhheNd4THQHiTJKYzeWfD/gAMYvf7yZH5wpk6P0ro8hUtyfpLbklw3se6gJFcm2Tq+PHC8Pkn+c5Ibk/zF5Cvuansso9dZ/gL438ChwN+rqhsGnWqOrctTuCTPB+4DLqyqY8fr3gbcWVVvHb8h8cCqemOSFwKvBl7I6MzTu6pq8RkoaUNYt2Og8ds9Lp8I6Abg5KranuQQ4FNV9dQk7x5/ftHi7Sbv7+677/bgTetu8+bNP/S63ZBn4Z60I4rx5Y5Xnw/jB+92Btg2XidtOBvxNPZSr8y7t9GGNGRA3xw/dWN8edt4/TbgiIntDmd03l/acIYM6KP84O33Wxj9sNqO9b80Pht3InD34uMfaaNYl9eBxm9yPBl4YpJtwFuAtwKXJDmL0c+svGS8+ccYnYG7EbgfeOV6zCjtirl9J4Jn4TSEjXQWTpp7BiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNgweU5N8k+XKS65JclGTfJEcluSbJ1iQXJ9l76DmlpQwaUJLDgF8BjquqY4G9gDOB3wTeUVULwLeBs4abUlre4HsgYBPwI0k2AT8KbAdOAS4dX38BcMZAs0lTbRryi1fVN5KcC9wEPAB8AvgCcFdVPTzebBtw2EAj7jYOOOCAH1q+6667Bppk9zJoQEkOBE4HjgLuAv4AOG2JTWva/WzdunX1h9vN+ZjNbmFhYdnrBg0I+Fngr6vqdoAkHwb+LnBAkk3jvdDhwC3T7mTaN6il+ZitjqGPgW4CTkzyo0kCnAp8BbgaePF4my3AZQPNJ001aEBVdQ2jkwV/Dlw7nuc9wBuB1ya5EXgCcN5gQ0pTpGrq4cWGdffdd8/n4APxJMLq2Lx5cyaXh34KJ801A5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkho2DT3AWtnnM3849Agbmo/Pzh486Rcf9W3cA0kNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUMHhASQ5IcmmSv0xyfZKTkhyU5MokW8eXBw49p7SUwQMC3gX8cVU9DXgmcD3wJuCqqloArhovSxvOoAEl2R94PnAeQFU9VFV3AacDF4w3uwA4Y5gJpek2Dfz1nwLcDvx+kmcCXwBeAzypqrYDVNX2JAdPu5OtW7futO7QO+5c/Wl3I3f6+OzkliX+HQEsLCwse5uhA9oE/BTw6qq6Jsm72IWna0t9g/t867r+dLuxg55w0NAjbDj7TQllOUMfA20DtlXVNePlSxkF9c0khwCML28baD5pqkEDqqpbgZuTPHW86lTgK8BHgS3jdVuAywYYT1rR0E/hAF4NfCDJ3sDXgFcyCvuSJGcBNwEvGXA+aVmDB1RVXwKOW+KqU9d7FunRGvoYSJprBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUMPjPA2l9PPC/fn/oEXZL7oGkBgOSGgxIajAgqcGApAYDkhoMSGqYGlCSzUn+VZIrkmxLct/48ookr0pywHoNKm1EywaU5C2Mfs3uCcCHGP120BPHlx8CngNcl+Tfr/2Y0sY07Z0I9wMLVXX/Etd9Bjg/yX7AL6/JZNIcWDagqvqtlW5cVd8Bzl3ViaQ5stIx0MWLll+0tuNI82Wls3CnLVq+cK0GkebRSgFlhWVpj7ZSQLXCsrRHW+nngfZL8lcTy/svWqaqjl79saT5sFJAL1yXKaQ5NTWgqvr4eg0izaNp70Q4O8nUwJJsSnL26o8lzYdpgTwN+GqSjwB/AtwA3As8HjgaOBk4ndGfppf2SNPeifDaJOcC/xR4HfAM4HHAPcC1wMeAk6pq+3oMKm1EKx0D3QL8x/EHSR5TVd9fj8GkefCofh7IeKQf5g/USQ0GJDUYkNQw86/2TfI44OeAQ4FbgE9U1b1rNZg0D2YKKMnzgI8ANwM3AT8GvCfJGVX1f9ZwPmlDm3UP9N+Ac6rqf+xYkeTlwH8Hnr4Wg0nzYNZjoCOA/7lo3UXA4as7jjRfZg3oIuCfLVp3FjtHJe1RZn0KtwCcleQNwDZGe54jgE8n+cSOjarq76/+iNLGNWtAl4w/JE2YKaCqevdaDyLNo0fzOtBzgGczekf2I6rq7as9lDQvZn0d6LeBVwL/F3hg4ip/yYj2aLPugV4JPLOqbl7LYaR5M+tp7G8w+mlUSRNm3QP9c+D3klwA3DZ5RVV9dtWnkubErAH9BKNf83saOx8DHbzaQ0nzYtaA3gacWVWXr+Uw0ryZ9RjoQcDfESctMmtA/w54m3/SUfphsz6FezewF/ArSb43XhegqmrvNZlMmgOzBnTsmk4hzalZ3wt3w47PkxxUVXeu3UjS/JjpGCjJ/knOT/IdRj/WTZIXJfm1NZ1O2uBmPYnwO+PLY4GHxp9/FnjFqk8kzZFZj4F+Dji8qh5KUgBVdVuSJ63daNLGN+se6F7gwMkVSQ4HvrnqE0lzZNaA3gdckuQkIEmeDZwP/N5aDSbNg1mfwv0G8F3gA4x+oO7DjF4bOneN5pLmwtQ9UJKXwuivMlTVW6vqKVX12Ko6arzsD9Rpj7bSUzh/F4I0xUoBZV2mkObUSsdAeyX5GaaEVFWfXN2RpPmxUkD7AOexfEAFPGVVJ5LmyEoBfaeqDERahn9gS2rwJILUMDWgqnr8eg0izSOfwkkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUsOGCCjJXkm+mOTy8fJRSa5JsjXJxUn8S+DakDZEQMBrgOsnln8TeEdVLQDfBs4aZCppBYMHNP5Ldz8PvHe8HOAU4NLxJhcAZwwznTTdrH9gay29E3gDsON30D0BuKuqHh4vbwMOm3YHW7du3WndoXfcuYojak9wyxL/jgAWFhaWvc2gASV5EXBbVX0hyck7Vi+x6dQ/5LXUN7jPt65rz6c9y35TQlnO0Hug5wK/kOSFwL7A/oz2SAck2TTeCx0O3DLgjNKyBj0Gqqp/W1WHV9WRwJnAJ6vqZcDVwIvHm20BLhtoRGmqwU8iLOONwGuT3MjomOi8geeRljT0U7hHVNWngE+NP/8acPyQ80iz2Kh7IGkuGJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1GJDUYEBSgwFJDQYkNRiQ1GBAUoMBSQ0GJDUYkNRgQFKDAUkNBiQ1DBpQkiOSXJ3k+iRfTvKa8fqDklyZZOv48sAh55SWM/Qe6GHgdVX1E8CJwL9OcgzwJuCqqloArhovSxvOoAFV1faq+vPx5/cC1wOHAacDF4w3uwA4Y5gJpemG3gM9IsmRwLOBa4AnVdV2GEUGHDzcZNLyNg09AECSxwEfAs6pqnuSPKrbb926dad1h95x5+oMpz3GLUv8OwJYWFhY9jaDB5TksYzi+UBVfXi8+ptJDqmq7UkOAW6bdh9LfYP7fOu6VZ9Vu7f9poSynKHPwgU4D7i+qt4+cdVHgS3jz7cAl633bNIsht4DPRd4BXBtki+N1/0q8FbgkiRnATcBLxloPmmqQQOqqj8FljvgOXU9Z5F2xYY5CyfNIwOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGgxIajAgqcGApAYDkhoMSGowIKnBgKQGA5IaDEhqMCCpwYCkBgOSGjZsQElekOSGJDcmedPQ80hL2ZABJdkL+B3gNOAY4KVJjhl2Kmlnm4YeYBnHAzdW1dcAknwQOB34yqx38OBJv7hGo0k/sCH3QMBhwM0Ty9vG66QNZaMGlCXW1bpPIa1goz6F2wYcMbF8OHDL5AabN29eKjJpXW3UPdDngIUkRyXZGzgT+OjAM0k72ZB7oKp6OMmrgI8DewHnV9WXBx5L2kmqPLSQdtVGfQonzQUDkhoMSGowIKnBgKQGA5IaDEhq+P8J/P++hhFywQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 216x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#fig, ax = plt.subplots()\n",
    "# x = range(0,1)\n",
    "# print(x)\n",
    "plt.figure(figsize=(3,8))\n",
    "plt.bar(1,temp_avg, color = 'coral',alpha = 0.5)\n",
    "plt.errorbar(1,temp_avg, yerr=(tmax - tmin), color = 'k')\n",
    "plt.ylim(0, 100)\n",
    "plt.xticks([])\n",
    "plt.title('Trip Avg Temp')\n",
    "plt.ylabel(\"Temp (F)\")\n",
    "plt.tight_layout()\n",
    "plt.savefig('Images/temperature.png')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('USC00519523', 'WAIMANALO EXPERIMENTAL FARM, HI US', 21.33556, -157.71139, 19.5, 0.61), ('USC00514830', 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 21.5213, -157.8374, 7.0, 0.6), ('USC00516128', 'MANOA LYON ARBO 785.2, HI US', 21.3331, -157.8025, 152.4, 0.6), ('USC00513117', 'KANEOHE 838.1, HI US', 21.4234, -157.8015, 14.6, 0.29), ('USC00519281', 'WAIHEE 837.5, HI US', 21.45167, -157.84888999999998, 32.9, 0.2), ('USC00519397', 'WAIKIKI 717.2, HI US', 21.2716, -157.8168, 3.0, 0.0)]\n"
     ]
    }
   ],
   "source": [
    "# Calculate the rainfall per weather station for your trip dates using the previous year's matching dates.\n",
    "# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation\n",
    "\n",
    "rainfall_station = session.query(Station.station, Station.name, Station.latitude,\n",
    "                                 Station.longitude, Station.elevation, func.sum(Measurement.prcp)).\\\n",
    "        filter(Measurement.date >= prev_year_start, Measurement.date <= prev_year_end).\\\n",
    "        filter(Measurement.prcp != None).\\\n",
    "        filter(Station.station == Measurement.station).\\\n",
    "        group_by(Measurement.station).\\\n",
    "        order_by(func.sum(Measurement.prcp).desc()).all()\n",
    "print(rainfall_station)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Optional Challenge Assignment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(62.0, 69.15384615384616, 77.0)]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a query that will calculate the daily normals \n",
    "# (i.e. the averages for tmin, tmax, and tavg for all historic data matching a specific month and day)\n",
    "\n",
    "def daily_normals(date):\n",
    "    \"\"\"Daily Normals.\n",
    "    \n",
    "    Args:\n",
    "        date (str): A date string in the format '%m-%d'\n",
    "        \n",
    "    Returns:\n",
    "        A list of tuples containing the daily normals, tmin, tavg, and tmax\n",
    "    \n",
    "    \"\"\"\n",
    "    \n",
    "    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]\n",
    "    return session.query(*sel).filter(func.strftime(\"%m-%d\", Measurement.date) == date).all()\n",
    "    \n",
    "daily_normals(\"01-01\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(62.0, 69.15384615384616, 77.0),\n",
       " (60.0, 69.39622641509433, 77.0),\n",
       " (62.0, 68.9090909090909, 77.0),\n",
       " (58.0, 70.0, 76.0),\n",
       " (56.0, 67.96428571428571, 76.0),\n",
       " (61.0, 68.96491228070175, 76.0),\n",
       " (57.0, 68.54385964912281, 76.0)]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# calculate the daily normals for your trip\n",
    "# push each tuple of calculations into a list called `normals`\n",
    "\n",
    "# Set the start and end date of the trip\n",
    "\n",
    "# Use the start and end date to create a range of dates\n",
    "\n",
    "# Stip off the year and save a list of %m-%d strings\n",
    "\n",
    "# Loop through the list of %m-%d strings and calculate the normals for each date\n",
    "\n",
    "start_date = dt.datetime.strptime('2018-01-01', \"%Y-%m-%d\")\n",
    "end_date = dt.datetime.strptime('2018-01-07', \"%Y-%m-%d\")\n",
    "#st_str_dt = start_date.strftime(\"%m-%d\")\n",
    "normals = []\n",
    "dt_list = []\n",
    "\n",
    "iter_date = start_date\n",
    "while iter_date <= end_date:\n",
    "    dt_list.append(iter_date)\n",
    "    st_str_dt = iter_date.strftime(\"%m-%d\")\n",
    "    #print(st_str_dt)\n",
    "    iter_date += dt.timedelta(1)\n",
    "    normals.append(*daily_normals(st_str_dt))\n",
    "\n",
    "#dt_list\n",
    "normals\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tmin</th>\n",
       "      <th>tavg</th>\n",
       "      <th>tmax</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2018-01-01</th>\n",
       "      <td>62.0</td>\n",
       "      <td>69.153846</td>\n",
       "      <td>77.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-02</th>\n",
       "      <td>60.0</td>\n",
       "      <td>69.396226</td>\n",
       "      <td>77.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-03</th>\n",
       "      <td>62.0</td>\n",
       "      <td>68.909091</td>\n",
       "      <td>77.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-04</th>\n",
       "      <td>58.0</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>76.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-05</th>\n",
       "      <td>56.0</td>\n",
       "      <td>67.964286</td>\n",
       "      <td>76.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-06</th>\n",
       "      <td>61.0</td>\n",
       "      <td>68.964912</td>\n",
       "      <td>76.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-01-07</th>\n",
       "      <td>57.0</td>\n",
       "      <td>68.543860</td>\n",
       "      <td>76.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            tmin       tavg  tmax\n",
       "Date                             \n",
       "2018-01-01  62.0  69.153846  77.0\n",
       "2018-01-02  60.0  69.396226  77.0\n",
       "2018-01-03  62.0  68.909091  77.0\n",
       "2018-01-04  58.0  70.000000  76.0\n",
       "2018-01-05  56.0  67.964286  76.0\n",
       "2018-01-06  61.0  68.964912  76.0\n",
       "2018-01-07  57.0  68.543860  76.0"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Load the previous query results into a Pandas DataFrame and add the `trip_dates` range as the `date` index\n",
    "df2 = pd.DataFrame(normals, columns=['tmin','tavg','tmax'])\n",
    "df2['Date'] = pd.to_datetime(dt_list)\n",
    "df2.set_index('Date', inplace=True)\n",
    "df2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x504 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot the daily normals as an area plot with `stacked=False`\n",
    "df2.plot.area(stacked=False, alpha=0.2,figsize=(10,7))\n",
    "plt.xlabel(\"date\")\n",
    "#plt.xticks(df2[\"Date\"], rotation=45)\n",
    "plt.ylim(0, 80)\n",
    "plt.tight_layout()\n",
    "plt.savefig('Images/daily_normals.png')\n"
   ]
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
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

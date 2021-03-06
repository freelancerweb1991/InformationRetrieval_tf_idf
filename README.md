# InformationRetrieval_tf_idf

below is the result for the query of what is best hotel Maryland area best of area'
total review comments over 159000 exists in our sample data

###### Step 1.
inital query matrix:  (tf-wt) = 1+log(tf)

| term  | tf  | tf-wt  |
| ------------ | ------------ | ------------ |
|area       |2|  1.30103|
|best       |2 | 1.30103|
|hotel      |1 | 1.00000|
|meriland|  1|  1.00000|

####### executaion time: 0:00:05.952490

###### Step 2.
-------------------------------
After searching in all comments, only according to the algorithm used, only 11436 comments out of the total comments, including one of the search terms.
The distribution of each semester has been as follows


|term| docId  | freq  | idf  |
| ------------ | ------------ | ------------ |  ------------ |
|area |   2718   |2718 | 0.624025|
|best  |  2114  | 2114  |0.733169|
|hotel  |11118|  11118 | 0.012247|

-------------------------------

Raw Frequency docs for terms: 11436 

|docId | 1 |10| 100| 1000| 10000| 10001 | 10002 | 10003 | 10004 | 10005 | 10006 | 10007 | ....... | 9995|  9996|  9997|  9998|
| ------------ | -------- | -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |
|term |
|area|  | 3 | 1|  0    |0  |   0 |    0  |   0 |    0 |    2  |   1 |    0  |   0|  ...   | 0 |  0 |   0 |   0 |  ...|
|hotel| | 6|  0 |  5|1|2 | 1| 2|6|2|3 |4|2|  ... |   1|3|2| 9| ...

###### [3 rows x 11436 columns]
-------------------------------
Weighted documents: 11436

|docId | 1 |10| 100| 1000| 10000| 10001 | 10002 | 10003 | 10004 | 10005 | 10006 | 10007 | ....... | 9995|  9996|  9997|  9998|
| ------------ | -------- | -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |
|term |
|area|  | 1.477121|  1.0  |0.00000|   0.0  |0.00000   | 0.0 | 0.00000|  ...  | 0.0 | 0.000000|  |0.00000|  0.00000 | 0.000000 | 0.00000 | 0.000000|
|best | | 0.000000|  0.0  |0.00000|   0.0|  0.00000|    1.0 | 0.00000 | ... |  0.0 | 0.000000 | |0.00000|  0.00000|  0.000000|  0.00000 | 0.000000 |
|hotel || 1.778151 | 0.0|  1.69897  | 1.0 |1.30103|    1.0  |1.30103|  ... |  1.0  |1.477121|  1.60206|  1.30103|  1.845098|  1.30103|  1.477121|

###### [3 rows x 11436 columns]

#### normalized documents: 11436

||docId | 1 |10| 100| 1000| 10000| 10001 | 10002 | 10003 | 10004 | 10005 | 10006 | 10007 | ....... | 9995|  9996|  9997|  9998|
| ------------ | -------- | -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |
|term |
|area ||  0.638991 | 1.0 | 0.0 |  0.0 |   0.0 | 0.000000  |  0.0|    0.0|  0.621276 | ... |  0.0 |  0.0   |0.0 |  0.0 |  0.0|   0.0 |  0.0|   0.0 |  0.0  |
|best||   0.000000|  0.0 | 0.0 |  0.0 |   0.0 | 0.707107|    0.0  |  0.0|  0.477526|  ... |  0.0 |  0.0 |  0.0 |  0.0|   0.0 |  0.0|   0.0|   0.0|   0.0 |
|hotel||  0.769214|  0.0|  1.0 |  1.0|    1.0|  0.707107|    1.0 |   1.0  |0.621276|  ... |  1.0 |  1.0 |  1.0|   1.0 |  1.0 |  1.0 |  1.0|   1.0  | 1.0 |

###### [3 rows x 11436 columns] 

##### Normalized query vector: 
||tf  |  tf-wt   |    idf   |     wt|
| ------------ | ------------ | ------------ |  ------------ |  ------------ |
|term|
|area |      2 | 1.30103 | 0.624025|  0.648118|
|best  |     2 | 1.30103 | 0.733169 | 0.761477|
|hotel |     1 | 1.00000|  0.012247 | 0.009777|
|meriland|   1 | 1.00000|       NaN | 0.000000|
-------------------------------
##### effect of query vector on docs vector to calculate cosinuse similarity:

||docId | 1 |10| 100| 1000| 10000| 10001 | 10002 | 10003 | 10004 | 10005 | 10006 | 10007 | 10008
| ------------ | -------- | -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- |  -------- 
|term |
|area ||  0.414142 | 0.648118 | 0.000000 | 0.000000 | 0.000000  |0.000000 | ... | 0.000000 | 0.000000  |0.000000  |0.000000  |0.000000 | 0.000000
|best ||  0.000000  |0.000000|  0.000000  |0.000000 | 0.000000 | 0.538445|  ...  |0.000000 | 0.000000 | 0.000000  |0.000000 | 0.000000  |0.000000
|hotel||  0.007521|  0.000000 | 0.009777|  0.009777 | 0.009777|  0.006913|  ...  |0.009777|  0.009777  |0.009777  |0.009777  |0.009777 | 0.009777

###### [3 rows x 11436 columns]
-------------------------------
##### all cosinuse similarity score:

   |  | docId   |  score|
| ------------ | -------- | -------- |
|1283 |  7412 | 0.998711|
|1813|  11146 | 0.998711|
|1281  | 7370 | 0.996734|
|497  |  2841|  0.996734|
|568 |   3440|  0.996734|
|...  |   ...  |    ...|
|6010 |  5905  |0.009777
|6008  | 5903 | 0.009777
|6006  | 5900 | 0.009777
|6005|   5898  |0.009777
|5718  | 5468 | 0.009777

##### [11436 rows x 2 columns]
-------------------------------
#### Top 20 cosinuse similarity score:

 ||     docId  |   score|
| ------------ | -------- | -------- |
|1283  | 7412 | 0.998711|
|1813  |11146 | 0.998711|
|1281 |  7370 | 0.996734|
|497  |  2841 | 0.996734|
|568  |  3440 | 0.996734|
|732  |  4418 | 0.996734|
|442  |  2487 | 0.996734|
|1967 | 12466  |0.996734|
|1292|   7481|  0.996734|
|1102 |  6286|  0.996734|
|1421 |  8553 | 0.996734|
|1557 |  9460 | 0.996734|
|1251|   7075|  0.996734|
|954  |  5396 | 0.996734|
|862  |  4845 | 0.996734|
|1032  | 5886|  0.963584|
|90    |  744 |0.880417|
|38   |   286 | 0.871745|
|1992|  12593  |0.857915|
|1996 | 12618|  0.857915|
|449  |  2513  |0.857915|

-------------------------------
##### sample output of this solution is as belowe:

#### **0.9987105700023257      Nov 30 2007**

.......are all way past their best (was brown ever at its .......the microwave in the kitchen area seemed to be an early 

#### ** 0.9987105700023257      Oct 29 2009**

still one of the best values in chicago heart of chicago 

##### **0.9967343315261221      Nov 10 2008**
-------------------------------
.......) was one of the best i have ever had and .......supherb and took us to areas we would never have gone 

####** 0.9967343315261221      Aug 23 2009**
.......close to the main pedestrian areas downtown and also close to .......tidy and fully self contained. best of all the staff were 

#### **0.9967343315261221      Aug 17 2006**
.......knew which gate was the best to approach. anyway, the lobby .......with kids! a large dining area with living room adjacent to 
#### ** 0.9967343315261221      Nov 1 2009**
best area the peninsula is located near the forbidden city, a

#### **0.9967343315261221      Jan 27 2009**
.......buffet is one of the best we've had. the dinner buffet .......was free!!!). use the lounge area for some quiet time -

#### **0.9967343315261221      Aug 27 2008**
.......does not have a shallow/step area and there is not a

#### **0.9967343315261221      Sep 20 2005**
not the best but not the worst either we arrived at .......of the lake and the area museums. if you like to

#### **0.9967343315261221      Nov 15 2009**
.......top! the location is the best part of this property, the

#### **0.9967343315261221      Jul 9 2007**
.......go. the rooms and common areas were all very classy and .......that the conrad is the best of all of them.

#### **0.9967343315261221      Oct 26 2007**
.......morning breakfast buffet. the reception area was rather cool but we

#### ** 0.9967343315261221      Jun 14 2009**
.......it might not be the best of areas (we really are no experts

##### **0.9967343315261221      Oct 29 2008**
.......highly recommend. this is the best value in this area of chicago. nz

##### **0.9967343315261221      Jun 8 2009**
best in beijing you pay for it but worth it fantastic .......service, limo from airport, spa area is great. pool great. just

##### **0.963584012403216      Jul 5 2006**
.......in there, but the sitting area made up for it. the .......toiletries. it is also the best location...right on michigan avenue by

##### **0.8804169224612923      Mar 31 2008**
best mix of everything in wangfujing area in beijing. stay at crowne .......windows facing west or south. hotel reception staff has been very

#####** 0.871744999568423      Sep 3 2007**
.......and the nice communal bar area does food throughout most of .......it to be in the best location compared to othe hotels and hostels. it is walkable

#####0.8579153600838166      Nov 14 2005
best overall value without major sacrifices this is the best value for the dollar of .......the 4 walls. 4. sitting area had couch, chair, coffee table,

#####0.8579153600838166      Jul 12 2004
.......which we really appreciated. the hotel lobby is on the 6th .......7 blocks away, so it's best to take everything out of

#####0.8579153600838166      May 10 2007
.......neighborhood with a non-tourist shopping area near the subway to find

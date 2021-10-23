# Paths_Tree_Project

This project aims at creating a n-tree that represents towns and connections between them.

The program asks the user to enter the inputs then opens the 2 csv files that contain the towns' names and connections details between towns.

## Inputs
* *start town*: string variable
* *destination town*: string variable
* *maximum depth of the tree*: integer variable

## Outputs
For all the examples here, I will enter:
* *start town*: "Paris"
* *destination town*: "Marseille"
* *maximum depth*: 5

### Display a path
```
Paris (0, 0) -> Bourges (2.55, 247) -> Clermont-Ferrand (4.449999999999999, 437) -> Lyon (6.216999999999999, 604) -> Marseille (9.267, 918) 
```

### Display all paths
```
Paris (0, 0) -> Bourges (2.55, 247) -> Clermont-Ferrand (4.449999999999999, 437) -> Lyon (6.216999999999999, 604) -> Marseille (9.267, 918) 
Paris (0, 0) -> Bourges (2.55, 247) -> Clermont-Ferrand (4.449999999999999, 437) -> Lyon (6.216999999999999, 604) -> Montpellier (9.283999999999999, 909) -> Marseille (11.200999999999999, 1078)
Paris (0, 0) -> Bourges (2.55, 247) -> Clermont-Ferrand (4.449999999999999, 437) -> Montpellier (7.799999999999999, 769) -> Lyon (10.866999999999999, 1074) -> Marseille (13.916999999999998, 1388)
Paris (0, 0) -> Bourges (2.55, 247) -> Clermont-Ferrand (4.449999999999999, 437) -> Montpellier (7.799999999999999, 769) -> Marseille (9.716999999999999, 938)
Paris (0, 0) -> Dijon (3.233, 315) -> Lyon (5.216, 510) -> Clermont-Ferrand (6.9830000000000005, 677) -> Montpellier (10.333, 1009) -> Marseille (12.25, 1178)
Paris (0, 0) -> Dijon (3.233, 315) -> Lyon (5.216, 510) -> Marseille (8.266, 824)
Paris (0, 0) -> Dijon (3.233, 315) -> Lyon (5.216, 510) -> Montpellier (8.283000000000001, 815) -> Marseille (10.200000000000001, 984)
```

### Display the shortest path
```
Paris (0, 0) -> Dijon (3.233, 315) -> Lyon (5.216, 510) -> Marseille (8.266, 824)
```

### Display the fastest path
```
Paris (0, 0) -> Dijon (3.233, 315) -> Lyon (5.216, 510) -> Marseille (8.266, 824)
```

### Display the tree
```
Select a menu option: 5
Town: Paris 
Cumulated distance: 0
Cumulated time: 0
Depth: 0
   Town: Amiens
   Cumulated distance: 144
   Cumulated time: 1.933
   Depth: 1
      Town: Caen
      Cumulated distance: 399
      Cumulated time: 4.566
      Depth: 2
         Town: Le-Mans
         Cumulated distance: 565
         Cumulated time: 6.316
         Depth: 3
            Town: Tours
            Cumulated distance: 664
            Cumulated time: 7.516
            Depth: 4
               Town: Bourges
               Cumulated distance: 828
               Cumulated time: 9.199
               Depth: 5
               Town: Nantes
               Cumulated distance: 881
               Cumulated time: 9.749
               Depth: 5
               Town: Niort
               Cumulated distance: 840
               Cumulated time: 9.366
               Depth: 5
            Town: Nantes
            Cumulated distance: 749
            Cumulated time: 8.266
            Depth: 4
               Town: Niort
               Cumulated distance: 892
               Cumulated time: 9.849
               Depth: 5
               Town: Rennes
               Cumulated distance: 862
               Cumulated time: 9.666
               Depth: 5
               Town: Tours
               Cumulated distance: 966
               Cumulated time: 10.499
               Depth: 5
            Town: Rennes
            Cumulated distance: 718
            Cumulated time: 7.983
            Depth: 4
               Town: Nantes
               Cumulated distance: 831
               Cumulated time: 9.383
               Depth: 5
         Town: Rennes
         Cumulated distance: 585
         Cumulated time: 6.399
         Depth: 3
            Town: Le-Mans
            Cumulated distance: 738
            Cumulated time: 8.066
            Depth: 4
               Town: Tours
               Cumulated distance: 837
               Cumulated time: 9.266
               Depth: 5
               Town: Nantes 
               Cumulated distance: 922
               Cumulated time: 10.016
               Depth: 5
            Town: Nantes
            Cumulated distance: 698
            Cumulated time: 7.7989999999999995
            Depth: 4
               Town: Le-Mans
               Cumulated distance: 882
               Cumulated time: 9.748999999999999
               Depth: 5
               Town: Niort
               Cumulated distance: 841
               Cumulated time: 9.382
               Depth: 5
               Town: Tours
               Cumulated distance: 915
               Cumulated time: 10.032
               Depth: 5
      Town: Lille
      Cumulated distance: 288
      Cumulated time: 3.5
      Depth: 2
         Town: Reims
         Cumulated distance: 494
         Cumulated time: 5.5329999999999995
         Depth: 3
            Town: Metz
            Cumulated distance: 685
            Cumulated time: 7.3999999999999995
            Depth: 4
               Town: Strasbourg
               Cumulated distance: 851
               Cumulated time: 9.1
               Depth: 5
   Town: Bourges
   Cumulated distance: 247
   Cumulated time: 2.55
   Depth: 1
      Town: Clermont-Ferrand
      Cumulated distance: 437
      Cumulated time: 4.449999999999999
      Depth: 2
         Town: Bordeaux
         Cumulated distance: 812
         Cumulated time: 8.332999999999998
         Depth: 3
            Town: Bayonne
            Cumulated distance: 996
            Cumulated time: 10.432999999999998
            Depth: 4
               Town: Toulouse
               Cumulated distance: 1296
               Cumulated time: 13.332999999999998
               Depth: 5
            Town: Niort
            Cumulated distance: 1004
            Cumulated time: 10.365999999999998
            Depth: 4
               Town: Nantes
               Cumulated distance: 1147
               Cumulated time: 11.948999999999998
               Depth: 5
               Town: Tours
               Cumulated distance: 1180
               Cumulated time: 12.215999999999998
               Depth: 5
            Town: Toulouse
            Cumulated distance: 1057
            Cumulated time: 10.899999999999999
            Depth: 4
               Town: Bayonne
               Cumulated distance: 1357
               Cumulated time: 13.799999999999999
               Depth: 5
               Town: Montpellier
               Cumulated distance: 1300
               Cumulated time: 13.432999999999998
               Depth: 5
         Town: Lyon
         Cumulated distance: 604
         Cumulated time: 6.216999999999999
         Depth: 3
            Town: Dijon 
            Cumulated distance: 799
            Cumulated time: 8.2
            Depth: 4
               Town: Strasbourg
               Cumulated distance: 1129
               Cumulated time: 11.5
               Depth: 5
            Town: Grenoble
            Cumulated distance: 715
            Cumulated time: 7.449999999999999
            Depth: 4
            Town: Marseille
            Cumulated distance: 918
            Cumulated time: 9.267
            Depth: 4
            Town: Montpellier
            Cumulated distance: 909
            Cumulated time: 9.283999999999999
            Depth: 4
               Town: Marseille
               Cumulated distance: 1078
               Cumulated time: 11.200999999999999
               Depth: 5
               Town: Toulouse
               Cumulated distance: 1152
               Cumulated time: 11.816999999999998
               Depth: 5
         Town: Montpellier
         Cumulated distance: 769
         Cumulated time: 7.799999999999999
         Depth: 3
            Town: Lyon
            Cumulated distance: 1074
            Cumulated time: 10.866999999999999
            Depth: 4
               Town: Dijon
               Cumulated distance: 1269
               Cumulated time: 12.85
               Depth: 5
               Town: Grenoble
               Cumulated distance: 1185
               Cumulated time: 12.1
               Depth: 5
               Town: Marseille
               Cumulated distance: 1388
               Cumulated time: 13.916999999999998
               Depth: 5
            Town: Marseille
            Cumulated distance: 938
            Cumulated time: 9.716999999999999
            Depth: 4
            Town: Toulouse
            Cumulated distance: 1012
            Cumulated time: 10.332999999999998
            Depth: 4
               Town: Bayonne
               Cumulated distance: 1312
               Cumulated time: 13.232999999999999
               Depth: 5
               Town: Bordeaux
               Cumulated distance: 1257
               Cumulated time: 12.899999999999999
               Depth: 5
      Town: Tours
      Cumulated distance: 411
      Cumulated time: 4.233
      Depth: 2
         Town: Le-Mans
         Cumulated distance: 510
         Cumulated time: 5.433
         Depth: 3
            Town: Caen
            Cumulated distance: 676
            Cumulated time: 7.183
            Depth: 4
               Town: Amiens
               Cumulated distance: 931
               Cumulated time: 9.815999999999999
               Depth: 5
               Town: Rennes
               Cumulated distance: 862
               Cumulated time: 9.016
               Depth: 5
            Town: Nantes
            Cumulated distance: 694
            Cumulated time: 7.383
            Depth: 4
               Town: Niort
               Cumulated distance: 837
               Cumulated time: 8.966
               Depth: 5
               Town: Rennes
               Cumulated distance: 807
               Cumulated time: 8.783
               Depth: 5
            Town: Rennes
            Cumulated distance: 663
            Cumulated time: 7.1
            Depth: 4
               Town: Caen
               Cumulated distance: 849
               Cumulated time: 8.933
               Depth: 5
               Town: Nantes
               Cumulated distance: 776
               Cumulated time: 8.5
               Depth: 5
         Town: Nantes
         Cumulated distance: 628
         Cumulated time: 6.465999999999999
         Depth: 3
            Town: Le-Mans
            Cumulated distance: 812
            Cumulated time: 8.415999999999999
            Depth: 4
               Town: Caen
               Cumulated distance: 978
               Cumulated time: 10.165999999999999
               Depth: 5
               Town: Rennes
               Cumulated distance: 965
               Cumulated time: 10.082999999999998
               Depth: 5
            Town: Niort
            Cumulated distance: 771
            Cumulated time: 8.049
            Depth: 4
               Town: Bordeaux
               Cumulated distance: 963
               Cumulated time: 10.081999999999999
               Depth: 5
            Town: Rennes
            Cumulated distance: 741
            Cumulated time: 7.866
            Depth: 4
               Town: Caen
               Cumulated distance: 927
               Cumulated time: 9.699
               Depth: 5
               Town: Le-Mans
               Cumulated distance: 894
               Cumulated time: 9.533
               Depth: 5
         Town: Niort
         Cumulated distance: 587
         Cumulated time: 6.083
         Depth: 3
            Town: Bordeaux
            Cumulated distance: 779
            Cumulated time: 8.116
            Depth: 4
               Town: Bayonne
               Cumulated distance: 963
               Cumulated time: 10.216
               Depth: 5
               Town: Clermont-Ferrand
               Cumulated distance: 1154
               Cumulated time: 11.998999999999999
               Depth: 5
               Town: Toulouse
               Cumulated distance: 1024
               Cumulated time: 10.683
               Depth: 5
            Town: Nantes
            Cumulated distance: 730
            Cumulated time: 7.666
            Depth: 4
               Town: Le-Mans
               Cumulated distance: 914
               Cumulated time: 9.616
               Depth: 5
               Town: Rennes
               Cumulated distance: 843
               Cumulated time: 9.066
               Depth: 5
   Town: Dijon
   Cumulated distance: 315
   Cumulated time: 3.233
   Depth: 1
      Town: Lyon
      Cumulated distance: 510
      Cumulated time: 5.216
      Depth: 2
         Town: Clermont-Ferrand
         Cumulated distance: 677
         Cumulated time: 6.9830000000000005
         Depth: 3
            Town: Bordeaux
            Cumulated distance: 1052
            Cumulated time: 10.866
            Depth: 4
               Town: Bayonne
               Cumulated distance: 1236
               Cumulated time: 12.966
               Depth: 5
               Town: Niort
               Cumulated distance: 1244
               Cumulated time: 12.899
               Depth: 5
               Town: Toulouse
               Cumulated distance: 1297
               Cumulated time: 13.433
               Depth: 5
            Town: Bourges
            Cumulated distance: 867
            Cumulated time: 8.883000000000001
            Depth: 4
               Town: Tours
               Cumulated distance: 1031
               Cumulated time: 10.566
               Depth: 5
            Town: Montpellier
            Cumulated distance: 1009
            Cumulated time: 10.333
            Depth: 4
               Town: Marseille
               Cumulated distance: 1178
               Cumulated time: 12.25
               Depth: 5
               Town: Toulouse
               Cumulated distance: 1252
               Cumulated time: 12.866
               Depth: 5
         Town: Grenoble
         Cumulated distance: 621
         Cumulated time: 6.449
         Depth: 3
         Town: Marseille
         Cumulated distance: 824
         Cumulated time: 8.266
         Depth: 3
         Town: Montpellier
         Cumulated distance: 815
         Cumulated time: 8.283000000000001
         Depth: 3
            Town: Clermont-Ferrand
            Cumulated distance: 1147
            Cumulated time: 11.633000000000001
            Depth: 4
               Town: Bordeaux
               Cumulated distance: 1522
               Cumulated time: 15.516000000000002
               Depth: 5
               Town: Bourges
               Cumulated distance: 1337
               Cumulated time: 13.533000000000001
               Depth: 5
            Town: Marseille
            Cumulated distance: 984
            Cumulated time: 10.200000000000001
            Depth: 4
            Town: Toulouse
            Cumulated distance: 1058
            Cumulated time: 10.816
            Depth: 4
               Town: Bayonne
               Cumulated distance: 1358
               Cumulated time: 13.716000000000001
               Depth: 5
               Town: Bordeaux
               Cumulated distance: 1303
               Cumulated time: 13.383000000000001
               Depth: 5
      Town: Strasbourg
      Cumulated distance: 645
      Cumulated time: 6.5329999999999995
      Depth: 2
         Town: Metz
         Cumulated distance: 811
         Cumulated time: 8.232999999999999
         Depth: 3
            Town: Reims
            Cumulated distance: 1002
            Cumulated time: 10.099999999999998
            Depth: 4
               Town: Lille
               Cumulated distance: 1208
               Cumulated time: 12.132999999999997
               Depth: 5
   Town: Le-Mans
   Cumulated distance: 208
   Cumulated time: 2.217
   Depth: 1
      Town: Tours
      Cumulated distance: 307
      Cumulated time: 3.417
      Depth: 2
         Town: Bourges
         Cumulated distance: 471
         Cumulated time: 5.1
         Depth: 3
            Town: Clermont-Ferrand
            Cumulated distance: 661
            Cumulated time: 7.0
            Depth: 4
               Town: Bordeaux
               Cumulated distance: 1036
               Cumulated time: 10.883
               Depth: 5
               Town: Lyon
               Cumulated distance: 828
               Cumulated time: 8.767
               Depth: 5
               Town: Montpellier
               Cumulated distance: 993
               Cumulated time: 10.35
               Depth: 5
         Town: Nantes
         Cumulated distance: 524
         Cumulated time: 5.65
         Depth: 3
            Town: Niort
            Cumulated distance: 667
            Cumulated time: 7.2330000000000005
            Depth: 4
               Town: Bordeaux
               Cumulated distance: 859
               Cumulated time: 9.266
               Depth: 5
            Town: Rennes
            Cumulated distance: 637
            Cumulated time: 7.050000000000001
            Depth: 4
               Town: Caen
               Cumulated distance: 823
               Cumulated time: 8.883000000000001
               Depth: 5
         Town: Niort
         Cumulated distance: 483
         Cumulated time: 5.2669999999999995
         Depth: 3
            Town: Bordeaux 
            Cumulated distance: 675
            Cumulated time: 7.299999999999999
            Depth: 4
               Town: Bayonne
               Cumulated distance: 859
               Cumulated time: 9.399999999999999
               Depth: 5
               Town: Clermont-Ferrand
               Cumulated distance: 1050
               Cumulated time: 11.183
               Depth: 5
               Town: Toulouse
               Cumulated distance: 920
               Cumulated time: 9.866999999999999
               Depth: 5
            Town: Nantes
            Cumulated distance: 626
            Cumulated time: 6.85
            Depth: 4
               Town: Rennes
               Cumulated distance: 739
               Cumulated time: 8.25
               Depth: 5
      Town: Caen
      Cumulated distance: 374
      Cumulated time: 3.967
      Depth: 2
         Town: Amiens
         Cumulated distance: 629
         Cumulated time: 6.6
         Depth: 3
            Town: Lille
            Cumulated distance: 773
            Cumulated time: 8.167
            Depth: 4
               Town: Reims
               Cumulated distance: 979
               Cumulated time: 10.2
               Depth: 5
         Town: Rennes
         Cumulated distance: 560
         Cumulated time: 5.8
         Depth: 3
            Town: Nantes
            Cumulated distance: 673
            Cumulated time: 7.199999999999999
            Depth: 4
               Town: Niort
               Cumulated distance: 816
               Cumulated time: 8.783
               Depth: 5
               Town: Tours
               Cumulated distance: 890
               Cumulated time: 9.433
               Depth: 5
      Town: Nantes
      Cumulated distance: 392
      Cumulated time: 4.167
      Depth: 2
         Town: Niort
         Cumulated distance: 535
         Cumulated time: 5.75
         Depth: 3
            Town: Bordeaux
            Cumulated distance: 727
            Cumulated time: 7.7829999999999995
            Depth: 4
               Town: Bayonne
               Cumulated distance: 911
               Cumulated time: 9.883
               Depth: 5
               Town: Clermont-Ferrand
               Cumulated distance: 1102
               Cumulated time: 11.666
               Depth: 5
               Town: Toulouse
               Cumulated distance: 972
               Cumulated time: 10.35
               Depth: 5
            Town: Tours
            Cumulated distance: 711
            Cumulated time: 7.6
            Depth: 4
               Town: Bourges
               Cumulated distance: 875
               Cumulated time: 9.283
               Depth: 5
         Town: Rennes 
         Cumulated distance: 505
         Cumulated time: 5.567
         Depth: 3
            Town: Caen
            Cumulated distance: 691
            Cumulated time: 7.4
            Depth: 4
               Town: Amiens
               Cumulated distance: 946
               Cumulated time: 10.033000000000001
               Depth: 5
         Town: Tours
         Cumulated distance: 609
         Cumulated time: 6.4
         Depth: 3
            Town: Bourges
            Cumulated distance: 773
            Cumulated time: 8.083
            Depth: 4
               Town: Clermont-Ferrand
               Cumulated distance: 963
               Cumulated time: 9.983
               Depth: 5
            Town: Niort
            Cumulated distance: 785
            Cumulated time: 8.25
            Depth: 4
               Town: Bordeaux
               Cumulated distance: 977
               Cumulated time: 10.283
               Depth: 5
      Town: Rennes
      Cumulated distance: 361
      Cumulated time: 3.8840000000000003
      Depth: 2
         Town: Caen
         Cumulated distance: 547
         Cumulated time: 5.7170000000000005
         Depth: 3
            Town: Amiens
            Cumulated distance: 802
            Cumulated time: 8.350000000000001
            Depth: 4
               Town: Lille
               Cumulated distance: 946
               Cumulated time: 9.917000000000002
               Depth: 5
         Town: Nantes
         Cumulated distance: 474
         Cumulated time: 5.284000000000001
         Depth: 3
            Town: Niort
            Cumulated distance: 617
            Cumulated time: 6.867000000000001
            Depth: 4
               Town: Bordeaux
               Cumulated distance: 809
               Cumulated time: 8.9
               Depth: 5
               Town: Tours
               Cumulated distance: 793
               Cumulated time: 8.717
               Depth: 5
            Town: Tours
            Cumulated distance: 691
            Cumulated time: 7.517000000000001
            Depth: 4
               Town: Bourges
               Cumulated distance: 855
               Cumulated time: 9.200000000000001
               Depth: 5
               Town: Niort
               Cumulated distance: 867
               Cumulated time: 9.367
               Depth: 5
   Town: Reims
   Cumulated distance: 144
   Cumulated time: 1.6
   Depth: 1
      Town: Lille
      Cumulated distance: 350
      Cumulated time: 3.633
      Depth: 2
         Town: Amiens
         Cumulated distance: 494
         Cumulated time: 5.2
         Depth: 3
            Town: Caen
            Cumulated distance: 749
            Cumulated time: 7.833
            Depth: 4
               Town: Le-Mans
               Cumulated distance: 915
               Cumulated time: 9.583
               Depth: 5
               Town: Rennes
               Cumulated distance: 935
               Cumulated time: 9.666
               Depth: 5
      Town: Metz
      Cumulated distance: 335
      Cumulated time: 3.467
      Depth: 2
         Town: Strasbourg
         Cumulated distance: 501
         Cumulated time: 5.167
         Depth: 3
            Town: Dijon
            Cumulated distance: 831
            Cumulated time: 8.466999999999999
            Depth: 4
               Town: Lyon
               Cumulated distance: 1026
               Cumulated time: 10.45
               Depth: 5
```

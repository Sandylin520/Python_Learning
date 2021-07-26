#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
#Nesting a list in a Dictionary
travel_log = {
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"],
}

#Nesting a Dictionary in a Dictionary
travel_log = {
    "France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits":12}
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visit":5},
}

#One giant dictionay with key value pair
travel_log = {
    #  key  : value
    "France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"cities_visited"["Berlin","Hanmburg","Stuggart"],"total_visits":5},
}

#One giant dictionay with key value pair => turn it into its own key value pair
travel_log = {
    {
      "country":"France",
      "cities_visited":["Paris","Lille","Dijon"],
      "total_visits":12
    },
    {
      "country":"Germany",
      "cities_visited":["Berlin","Hanmburg","Stuggart"],
      "total_visits":5
    },

}


"""
[{
    Key:[List],
    key2:{Dict},
},
{
    Key:Value,
    Key2:Value,
}]


"""
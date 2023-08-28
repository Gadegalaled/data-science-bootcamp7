library(nycflights13)
library(dplyr)

head(flights)

#Data Analysis with dplyr:

jfk_flights <- flights %>%
  filter(origin == "JFK")

selected_cols <- flights %>%
  select(year, month, day, dep_time, arr_time)

avg_delay_by_airline <- flights %>%
  group_by(carrier) %>%
  summarize(avg_delay = mean(dep_delay, na.rm = TRUE))

sorted_flights <- flights %>%
  arrange(dep_delay)


flights_with_travel_time <- flights %>%
  mutate(travel_time = arr_time - dep_time)

flights_per_day_of_week_agg <- flights %>%
  group_by(day_of_week = weekdays(as.Date(paste(year, month, day, sep = "-")))) %>%
  summarize(total_flights = n())

# AlarmClock
Creating an alarm clock / game bomb running on a raspberry PI. The alarm clock can only be switched off by setting some measuring probes to the correct value range. 

## Usage

### start alarmclock

to run the alarm clock

```
python src/alarm_clock --verbose --alarm HH:MM
```

| Option          | description |
| --------------- | ---------------------------- |
| --verbose       | increase logging information |
| --alarm  HH:MM  | start the alarm in HH hours an MM minutes |


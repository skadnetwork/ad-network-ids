# SKAdNetwork id collection

App developers that want to leverage Apples install/conversion attribution API [SKAdNetwork](https://developer.apple.com/documentation/storekit/skadnetwork) need to update their apps for iOS14. Apps that display advertisement have to include each advertising partners Apple issued id in the [Info.plist](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html). (Given that they like to enable measurement for this partner.)

Until there is a centralized place or a tool to curate/update the list this repository can serve as a starting point. If you like to add an id please open a PR.

# Related

* An example implementation of SKAdNetwork: https://github.com/singular-labs/Singular-SKAdNetwork-App.
* A proposal how to implement conversion value managemant: [Elixir](https://github.com/2ndpotion/ElixiriOS) ([demo](https://www.youtube.com/watch?v=cY0jnPw6TOI))  


## List of ids

As Info.plist entries that can be copy and pasted: [ad-network-ids.plist](ad-network-ids.plist)

|Company|Id|Description|
|-------|--|-----------|
|[Aarki](https://www.aarki.com)|4FZDC2EVR5|Mobile user acquisition & retargeting DSP|
|[Applift](https://applift.com)|6xzpu9s2p8|Mobile user acquisition & retargeting DSP|
|[Appreciate](https://appreciate.mobi)|mlmmfzh3r3|Mobile user acquisition & retargeting DSP|
|[Hybrid](https://hybrid.ai)|W9Q455WK68| Mobile user acquisition & retargeting DSP|
|[Jampp](https://jampp.com)|YCLNXRL5PM|Mobile user acquisition & retargeting DSP|
|[Lifestreet](https://lifestreet.com)|T38B2KH725|Programmatic marketing plattform for app developers|
|[Liftoff](https://liftoff.io)|7UG5ZH24HU|Mobile user acquisition & retargeting DSP|
|[Remerge](https://www.remerge.io)|2U9PT9HC89|Mobile retargeting DSP|
|[ScaleMonk](https://www.scalemonk.com)|av6w8kgt66|Mobile user acquisition & retargeting DSP|

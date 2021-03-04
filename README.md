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
|[Aarki](https://www.aarki.com)|4fzdc2evr5|Mobile user acquisition & retargeting DSP|
|[adgoji](https://www.adgoji.com)|23zd986j2c|Omnichannel DSP|
|[Adikteev](https://www.adikteev.com)|ydx93a7ass|Mobile retargeting DSP|
|[Appier](https://www.appier.com)|v72qych5uu|Full-funnel advertising|
|[Applift](https://applift.com)|6xzpu9s2p8|Mobile Performance Network|
|[Appreciate](https://appreciate.mobi)|mlmmfzh3r3|Mobile user acquisition & retargeting DSP|
|[Beeswax](https://beeswax.com)|c6k4g5qg8m|Bidder-as-a-Service|
|[Criteo](https://www.criteo.com/)|hs6bdukanm|Retargeter|
|[Dataseat](https://dataseat.com)|m8dbw4sv7c|In-House programmatic buying platform|
|[Hybrid](https://hybrid.ai)|w9q455wk68| Mobile user acquisition & retargeting DSP|
|[Jampp](https://jampp.com)|yclnxrl5pm|Mobile user acquisition & retargeting DSP|
|[Kayzen](https://kayzen.io)|4468km3ulz|Mobile in-house bidder|
|[Lifestreet](https://lifestreet.com)|t38b2kh725|Programmatic marketing plattform for app developers|
|[Liftoff](https://liftoff.io)|7ug5zh24hu|Mobile user acquisition & retargeting DSP|
|[Moloco](http://www.molocoads.com)|9t245vhmpl|User acquisition & retargeting DSP|
|[MYAPPFREE](http://www.myappfree.com)|cad8qz2s3j|Mobile user acquisition & Self-serve mobile marketing platform|
|[Persona.ly](https://www.persona.ly)|44jx6755aq|Mobile user acquisition & retargeting DSP|
|[PubNative](https://pubnative.net)|tl55sbb4fm|Mobile monetization SSP|
|[Remerge](https://www.remerge.io)|2u9pt9hc89|Mobile retargeting DSP|
|[RevX](https://www.remerge.io)|5a6flpkh64|Self-serve mobile marketing platform|
|[RTB House](http://www.rtbhouse.com)|8s468mfl3y|Retargeting DSP|
|[Sift](https://www.sift.co)|klf5c3l5u5|User acquisition DSP|
|[ScaleMonk](https://www.scalemonk.com)|av6w8kgt66|Mobile user acquisition & retargeting DSP|
|[Smadex](https://www.smadex.com)|ppxm28t8ap|Mobile user acquisition & retargeting DSP|
|[Spyke Media](https://www.spykemedia.com)|44n7hlldy6|Mobile user acquisition|
|[YouAppi](https://www.youappi.com)|3rd42ekr43|Mobile user acquisition & retargeting DSP|


# SKAdNetwork id collection

App developers that want to leverage Apples install/converison attribution API [SKAdNetwork](https://developer.apple.com/documentation/storekit/skadnetwork) need to update their apps for iOS14. An example implementation of SKAdNetork can he found here: https://github.com/singular-labs/Singular-SKAdNetwork-App. Apps that display advertisement have to include each advertising partners Apple issued id in the [Info.plist](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html). (Given that they like to enable measurement for this partner.)

Until there is a centralized place or a tool to currate/update the list this repository can serve as a starting point. If you like to add an id please open a PR.

## List of ids

As Info.plist entries that can be copy and pasted: [ad-network-ids.plist](ad-network-ids.plist)

|Company|Id|Description|
|-------|--|-----------|
|[ExampleCo](https://example.com)|2UABCDE123|Example is a mobile DSP|

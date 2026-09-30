[RU](../../ru/cases/travel-history.md) · [Language selection](../../../README.md)

# Travel history: maps, trips and personal journeys

**2025–2026 · OneTwoTrip / iOS**

I developed travel history, from displaying trips on a map to manually creating and editing itineraries.

[View screens and states](#screens) · [Full gallery](../gallery.md)

## Context

Travel history turns a completed booking into lasting personal content: users can see where they have been, open trip details and add journeys booked outside OneTwoTrip. The product goals included repeat engagement and social use cases; I do not have measured retention gains.

## My contribution

- Built the map screen, pins, clustering, selected-trip carousel and list sheet. Added the profile widget, onboarding, statistics and analytics events.
- Developed trip details with a timeline and different transport types; extended cards with city counts.
- Implemented manual trips: route-point forms, location selection, editing and deletion. Reused a shared location-selection component and integrated geographic search.
- Fixed inconsistencies between the map and list after adding or deleting a trip, other users' history states and widget loading.
- Covered the main journey, errors, trip creation and editing with unit and UI tests; used snapshots for cards and statistics.

## Technologies

Swift, SwiftUI + UIKit, TCA, Combine, Swinject, CoreLocation, Map SDK abstraction / YandexMapKit, REST, XCTest / SnapshotTesting / XCUITest.

## Practical examples

| Scenario | My contribution | Engineering focus |
| --- | --- | --- |
| Trip map and list | Built pins, clusters, a carousel and list sheet; fixed synchronization after changes. | Consistent state across multiple views. |
| Manual itinerary creation | Developed route-point entry, location selection and trip-detail editing. | Forms, validation and reusable search. |
| Trip details | Worked on the timeline and presentation of different transport types. | Turning heterogeneous data into a clear interface. |
| Checking trip changes | Covered creation, editing and errors with unit and UI tests. | Testable business logic and user journeys. |


## Engineering decisions

- Maps are accessed through shared interfaces: the product module handles trips and annotations rather than SDK implementation details.
- Personal and other users' histories have different contexts. Content and available actions must account for ownership.
- Data updates must appear consistently in the widget, list and pins; a successful local deletion response does not guarantee that every screen is synchronized.

## Quality and checks

- Developed unit, snapshot and UI checks for the first version, then extended checks for manual trip creation and editing.
- Tested state logic separately from user journeys. These tests do not imply complete coverage of map rendering.

## Outcome and scope

Travel history evolved from a map of orders into an editable collection of journeys with multiple entry points and shared location-selection components.

## A closer look at the journey

1. **Map / list.** Select a trip
2. **Details.** Loading and timeline
3. **Manual item.** Transport or accommodation form
4. **Update.** Details and statistics after the response

A simplified route through one journey. Error branches and additional actions are discussed below.

### Map, card and list represent the same trip

The map combines pins and clusters, while a selected trip is accessible through a card and the sheet list. My work covered the map, clustering, carousel and navigation to details. The technical challenge was keeping selection coherent as zoom and viewing mode changed across several representations of one trip.

### A timeline with heterogeneous content

One details screen presents flights, rail journeys, stays and manually added items. Each type needs its own UI model while headings, dates and route order remain consistent. I developed this screen composition and data transformation. Separate snapshots demonstrate transport widgets and compact-card constraints.

### Manual trips: editing, deletion and undo

The form adds transport or a stay to a user-created trip. Saving returns updated details. Deleting an item retains information for undo; restoration performs a new request and updates the timeline and statistics. Ownership and trip type determine editing availability. This was part of my work on manual itineraries.

### An empty state and an error are different situations

An empty timeline offers adding an item, while a loading failure offers retry. A save failure needs to preserve the form context. Alongside implementation, I worked on error handling, tests and checks across screen sizes.

<a name="screens"></a>

## Screens and interface states

Original snapshot-test images using prepared data. Each example identifies its source type. Design and overall architecture were team work; my contribution is described above. Select an image to inspect the details.

| Trip card | Trip timeline item |
| :---: | :---: |
| <a name="visual-travel-card"></a><a href="../../../assets/screenshots/travel-card.png"><img src="../../../assets/screenshots/travel-card.png" alt="Trip card" width="250"></a> | <a name="visual-travel-timeline"></a><a href="../../../assets/screenshots/travel-timeline.png"><img src="../../../assets/screenshots/travel-timeline.png" alt="Trip timeline item" width="250"></a> |

| Travel statistics | Rail timeline item |
| :---: | :---: |
| <a name="visual-travel-statistics"></a><a href="../../../assets/screenshots/travel-statistics.png"><img src="../../../assets/screenshots/travel-statistics.png" alt="Travel statistics" width="250"></a> | <a name="visual-travel-rail"></a><a href="../../../assets/screenshots/travel-rail.png"><img src="../../../assets/screenshots/travel-rail.png" alt="Rail timeline item" width="250"></a> |

| Trip card: long dates and several travel types |
| :---: |
| <a name="visual-travel-card-dense"></a><a href="../../../assets/screenshots/travel-card-dense.png"><img src="../../../assets/screenshots/travel-card-dense.png" alt="Trip card: long dates and several travel types" width="250"></a> |

<details>
<summary>Image context and notes</summary>

- **Trip card.** A reusable card combines cover art, dates, destination and travel types. _Original component snapshot using test data._
- **Trip timeline item.** A route item combines the shared timeline with transport-specific presentation. _Original component snapshot using test data._
- **Travel statistics.** Travel statistics are reused across several parts of the feature. _Original component snapshot using test data._
- **Rail timeline item.** A transport widget presents stations, local times and duration within the shared timeline. _Snapshot test using prepared data._
- **Trip card: long dates and several travel types.** A 320 pt variant with a long date range, city count and extra icons. Visible text truncation is part of the tested state. _Snapshot test using prepared data._

</details>

[Full screen and component gallery](../gallery.md)

## Topics for an interview

- How do you keep the map, list and details synchronized after a trip changes?
- Which constraints should be agreed with the backend before implementing manual itineraries?

[All cases](index.md) · [Practical examples](../archive/index.md) · [Technologies](../engineering/technologies.md)

//
//  Complication.swift
//  Pyto Watch Extension
//
//  Created by Emma Labbé on 11-11-20.
//  Copyright © 2020 Adrian Labbé. All rights reserved.
//

import ClockKit

struct Complication: Hashable {
    
    var identifier: String
    
    var family: CLKComplicationFamily
    
    init(_ complication: CLKComplication) {
        self.identifier = complication.identifier
        self.family = complication.family
    }
}

struct ComplicationWithDate: Hashable {
    
    var complication: Complication
    
    var date: Date
}

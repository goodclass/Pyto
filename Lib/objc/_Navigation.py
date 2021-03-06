"""
Classes from the 'Navigation' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


MNLocationMatchInfo = _Class("MNLocationMatchInfo")
MNNanoFormattedStringFormatter = _Class("MNNanoFormattedStringFormatter")
MNNavigationProxyUpdater = _Class("MNNavigationProxyUpdater")
MNTimeballServer = _Class("MNTimeballServer")
MNDeviceTimeProvider = _Class("MNDeviceTimeProvider")
MNNavigationSessionManager = _Class("MNNavigationSessionManager")
MNNavigationStateManager = _Class("MNNavigationStateManager")
MNActiveRouteInfo = _Class("MNActiveRouteInfo")
MNTraceRouteSimulator = _Class("MNTraceRouteSimulator")
MNTraceRouteSimulatorEvent = _Class("MNTraceRouteSimulatorEvent")
MNTraceLoader = _Class("MNTraceLoader")
MNArrivalUpdater = _Class("MNArrivalUpdater")
MNTraceEvent = _Class("MNTraceEvent")
MNTraceEventServerFormattedString = _Class("MNTraceEventServerFormattedString")
MNTimeballNetworkRequester = _Class("MNTimeballNetworkRequester")
MNTimeballMockNetworkRequester = _Class("MNTimeballMockNetworkRequester")
MNNavigationClientProxy = _Class("MNNavigationClientProxy")
MNNavigationSessionLogger = _Class("MNNavigationSessionLogger")
MNGuidanceLaneInfo = _Class("MNGuidanceLaneInfo")
MNTimeManager = _Class("MNTimeManager")
MNTrafficIncidentAlert = _Class("MNTrafficIncidentAlert")
MNButtonActionTitle = _Class("MNButtonActionTitle")
MNXPCActivity = _Class("MNXPCActivity")
MNPhoneCallObserver = _Class("MNPhoneCallObserver")
MNTunnelLocationProjector = _Class("MNTunnelLocationProjector")
MNNavigationSession = _Class("MNNavigationSession")
MNRouteManager = _Class("MNRouteManager")
MNCommuteSession = _Class("MNCommuteSession")
MNVoiceLanguageUtil = _Class("MNVoiceLanguageUtil")
MNDisplayETAInfo = _Class("MNDisplayETAInfo")
MNTracePlayer = _Class("MNTracePlayer")
MNGuidanceEventManager = _Class("MNGuidanceEventManager")
MNNavdStateUpdater = _Class("MNNavdStateUpdater")
MNNavigationDetails = _Class("MNNavigationDetails")
MNHybridLocationProvider = _Class("MNHybridLocationProvider")
MNCommuteDestinationSuggestion = _Class("MNCommuteDestinationSuggestion")
MNLocationHistory = _Class("MNLocationHistory")
_MNTrackedAlternateRoute = _Class("_MNTrackedAlternateRoute")
MNAlternateRoutesUpdater = _Class("MNAlternateRoutesUpdater")
MNXPCTransactionCounter = _Class("MNXPCTransactionCounter")
MNTraceRecordingData = _Class("MNTraceRecordingData")
MNRouteDistanceInfo = _Class("MNRouteDistanceInfo")
MNTimeballSubscriberStore = _Class("MNTimeballSubscriberStore")
MNTimeballSubscription = _Class("MNTimeballSubscription")
MNTraceNavigationEventRecorder = _Class("MNTraceNavigationEventRecorder")
MNTracePlayerTimelineStream = _Class("MNTracePlayerTimelineStream")
_MNTracePlayerTimelineStreamSearchObject = _Class(
    "_MNTracePlayerTimelineStreamSearchObject"
)
MNCoreMotionContextProvider = _Class("MNCoreMotionContextProvider")
MNTimeAndDistanceUpdater = _Class("MNTimeAndDistanceUpdater")
MNNavigationServiceRemoteProxy = _Class("MNNavigationServiceRemoteProxy")
MNKeepAliveManager = _Class("MNKeepAliveManager")
MNDirectionsResponseInfo = _Class("MNDirectionsResponseInfo")
MNLPRRuleHelper = _Class("MNLPRRuleHelper")
MNGuidanceSignDescription = _Class("MNGuidanceSignDescription")
MNETADisplayFormatter = _Class("MNETADisplayFormatter")
MNWeakTimer = _Class("MNWeakTimer")
MNTraceBookmarkRecorder = _Class("MNTraceBookmarkRecorder")
_MNOffRouteInfo = _Class("_MNOffRouteInfo")
MNLocationManager = _Class("MNLocationManager")
MNRingerSwitchObserver = _Class("MNRingerSwitchObserver")
MNVoiceController = _Class("MNVoiceController")
MNVoiceEventQueue = _Class("MNVoiceEventQueue")
MNVoiceEvent = _Class("MNVoiceEvent")
MNDurationRequest = _Class("MNDurationRequest")
MNDurationRequestKey = _Class("MNDurationRequestKey")
MNTimeballServiceRemoteProxy = _Class("MNTimeballServiceRemoteProxy")
MNComparison = _Class("MNComparison")
MNRealtimeUpdate = _Class("MNRealtimeUpdate")
MNRealtimeTransitUpdate = _Class("MNRealtimeTransitUpdate")
MNClassicGuidanceManager = _Class("MNClassicGuidanceManager")
MNDriveGuidanceManager = _Class("MNDriveGuidanceManager")
MNWalkGuidanceManager = _Class("MNWalkGuidanceManager")
MNPlannedDestination = _Class("MNPlannedDestination")
MNTimepoint = _Class("MNTimepoint")
_MNTimepointAndTransportType = _Class("_MNTimepointAndTransportType")
MNXPCTransactionManager = _Class("MNXPCTransactionManager")
MNFilePaths = _Class("MNFilePaths")
MNCommuteDestinationUpdater = _Class("MNCommuteDestinationUpdater")
MNNavigationTraceInfo = _Class("MNNavigationTraceInfo")
MNSimulationLocationProvider = _Class("MNSimulationLocationProvider")
MNRouteCoordinateWithType = _Class("MNRouteCoordinateWithType")
_MNMapPointWithIndex = _Class("_MNMapPointWithIndex")
_MNMapPointsArray = _Class("_MNMapPointsArray")
MNCommuteDestination = _Class("MNCommuteDestination")
MNTracePlayerScheduler = _Class("MNTracePlayerScheduler")
_MNRouteHintSegment = _Class("_MNRouteHintSegment")
MNSuggestionsManager = _Class("MNSuggestionsManager")
MNNavigationAudioSession = _Class("MNNavigationAudioSession")
MNListInstructionContents = _Class("MNListInstructionContents")
MNSpokenInstructionContents = _Class("MNSpokenInstructionContents")
MNSignInstructionContents = _Class("MNSignInstructionContents")
MNSettingsManager = _Class("MNSettingsManager")
MNDirectionsRequestManager = _Class("MNDirectionsRequestManager")
MNRouteRefreshPolicyRulesForeground = _Class("MNRouteRefreshPolicyRulesForeground")
MNTimeballLocationManager = _Class("MNTimeballLocationManager")
MNTimeballLocationRequest = _Class("MNTimeballLocationRequest")
MNCompanionNavigationXPCConnection = _Class("MNCompanionNavigationXPCConnection")
MNCompanionNavigationAdapter = _Class("MNCompanionNavigationAdapter")
MNTrafficIncidentAlertUpdater = _Class("MNTrafficIncidentAlertUpdater")
MNRouteProximitySensor = _Class("MNRouteProximitySensor")
MNTimeballCache = _Class("MNTimeballCache")
MNTimeballCacheEntry = _Class("MNTimeballCacheEntry")
MNJunctionViewImageLoader = _Class("MNJunctionViewImageLoader")
_MNJunctionViewPreloadEvent = _Class("_MNJunctionViewPreloadEvent")
MNTraceEventRecorder = _Class("MNTraceEventRecorder")
MNTraceMiscInfo = _Class("MNTraceMiscInfo")
MNTraceCommuteDirectionsRequestRow = _Class("MNTraceCommuteDirectionsRequestRow")
MNTraceCommuteDestinationRow = _Class("MNTraceCommuteDestinationRow")
MNTraceAnnotatedUserEnvironmentRow = _Class("MNTraceAnnotatedUserEnvironmentRow")
MNTraceAnnotatedUserBehaviorRow = _Class("MNTraceAnnotatedUserBehaviorRow")
MNTraceRouteSelectionsRow = _Class("MNTraceRouteSelectionsRow")
MNTraceVehicleSpeedRow = _Class("MNTraceVehicleSpeedRow")
MNTraceVehicleHeadingRow = _Class("MNTraceVehicleHeadingRow")
MNTraceMotionDataRow = _Class("MNTraceMotionDataRow")
MNTraceHeadingDataRow = _Class("MNTraceHeadingDataRow")
MNTraceETAUpdateRow = _Class("MNTraceETAUpdateRow")
MNTraceDirectionsRow = _Class("MNTraceDirectionsRow")
MNTraceLocationRow = _Class("MNTraceLocationRow")
MNTrace = _Class("MNTrace")
MNNavigationState = _Class("MNNavigationState")
MNNavigationStatePrepareGuidance = _Class("MNNavigationStatePrepareGuidance")
MNNavigationStateNoDestination = _Class("MNNavigationStateNoDestination")
MNNavigationStatePredictingDestination = _Class(
    "MNNavigationStatePredictingDestination"
)
MNNavigationStateGuidance = _Class("MNNavigationStateGuidance")
MNNavigationStateGuidanceStepping = _Class("MNNavigationStateGuidanceStepping")
MNNavigationStateGuidanceTurnByTurn = _Class("MNNavigationStateGuidanceTurnByTurn")
MNNavigationStateLowGuidance = _Class("MNNavigationStateLowGuidance")
MNRouteRefreshPolicyScheduler = _Class("MNRouteRefreshPolicyScheduler")
MNCoreLocationProvider = _Class("MNCoreLocationProvider")
MNLeechedLocationProvider = _Class("MNLeechedLocationProvider")
MNLocationProviderCLParameters = _Class("MNLocationProviderCLParameters")
MNAnnouncementStrategyDelayCompressDrop = _Class(
    "MNAnnouncementStrategyDelayCompressDrop"
)
MNRouteUpdate = _Class("MNRouteUpdate")
MNRouteUpdateFreshness = _Class("MNRouteUpdateFreshness")
MNVehicleMonitor = _Class("MNVehicleMonitor")
MNLPRRuleMatcher = _Class("MNLPRRuleMatcher")
_MNLPRPlate = _Class("_MNLPRPlate")
_MNLPRPlateCharacter = _Class("_MNLPRPlateCharacter")
MNRouteRefreshPolicyRulesTimeToLeave = _Class("MNRouteRefreshPolicyRulesTimeToLeave")
MNNavigationServiceDirectionsRequestTicket = _Class(
    "MNNavigationServiceDirectionsRequestTicket"
)
MNNavigationService = _Class("MNNavigationService")
MNNavigationTraceManager = _Class("MNNavigationTraceManager")
MNTraceRecorder = _Class("MNTraceRecorder")
MNTimeballRoutingProvider = _Class("MNTimeballRoutingProvider")
MNTimeballService = _Class("MNTimeballService")
GeodesicDistancePoint = _Class("GeodesicDistancePoint")
MNTimeballServiceLocalProxy = _Class("MNTimeballServiceLocalProxy")
MNAnnouncementPlanEvent = _Class("MNAnnouncementPlanEvent")
MNAudioOutputSettingsManager = _Class("MNAudioOutputSettingsManager")
MNAudioOutputSetting = _Class("MNAudioOutputSetting")
MNAudioFrameworkSymbols = _Class("MNAudioFrameworkSymbols")
MNRouteRefreshPolicyRulesDefault = _Class("MNRouteRefreshPolicyRulesDefault")
MNNavigationServiceLocalProxy = _Class("MNNavigationServiceLocalProxy")
MNStartNavigationDetails = _Class("MNStartNavigationDetails")
MNArrivalRegionTimer = _Class("MNArrivalRegionTimer")
MNTimeballMockLocationProvider = _Class("MNTimeballMockLocationProvider")
_TimeStampValue = _Class("_TimeStampValue")
_TempToken = _Class("_TempToken")
_TempTokenTimestampValue = _Class("_TempTokenTimestampValue")
_MNDistanceFormatOptions = _Class("_MNDistanceFormatOptions")
MNGuidanceJunctionViewInfo = _Class("MNGuidanceJunctionViewInfo")
MNGuidanceJunctionViewImage = _Class("MNGuidanceJunctionViewImage")
MNRouteRefreshPolicyFactory = _Class("MNRouteRefreshPolicyFactory")
MNSettings = _Class("MNSettings")
MNMutableSettings = _Class("MNMutableSettings")
MNCommuteDestinationScore = _Class("MNCommuteDestinationScore")
MNCommuteDestinationLocationHistoryScore = _Class(
    "MNCommuteDestinationLocationHistoryScore"
)
MNCommuteDestinationOffRouteScore = _Class("MNCommuteDestinationOffRouteScore")
MNCommuteDestinationETAScore = _Class("MNCommuteDestinationETAScore")
MNCommuteDestinationGeodesicDistanceScore = _Class(
    "MNCommuteDestinationGeodesicDistanceScore"
)
MNCommuteDestinationNavigabilityScore = _Class("MNCommuteDestinationNavigabilityScore")
MNCommuteDestinationMapsSuggestionsScore = _Class(
    "MNCommuteDestinationMapsSuggestionsScore"
)
MNCommuteDestinationStartEndTimeScore = _Class("MNCommuteDestinationStartEndTimeScore")
MNNavigationServer = _Class("MNNavigationServer")
MNNotificationManager = _Class("MNNotificationManager")
MNSimulatorAudioSession = _Class("MNSimulatorAudioSession")
MNAnnouncementPlan = _Class("MNAnnouncementPlan")
MNAnnouncementConflict = _Class("MNAnnouncementConflict")
FakeBitsAndPieces = _Class("FakeBitsAndPieces")
MNSessionUpdateManager = _Class("MNSessionUpdateManager")
MNTracePlayerETAUpdater = _Class("MNTracePlayerETAUpdater")
MNEVChargingStateMonitor = _Class("MNEVChargingStateMonitor")
MNTransitInstruction = _Class("MNTransitInstruction")
MNTransitWalkingSegmentInstruction = _Class("MNTransitWalkingSegmentInstruction")
MNTransitStepInstruction = _Class("MNTransitStepInstruction")
MNObserverHashTable = _Class("MNObserverHashTable")
MNGuidanceSignInfo = _Class("MNGuidanceSignInfo")
MNLocationTracker = _Class("MNLocationTracker")
MNSteppingLocationTracker = _Class("MNSteppingLocationTracker")
MNTransitLocationTracker = _Class("MNTransitLocationTracker")
MNCommuteLocationTracker = _Class("MNCommuteLocationTracker")
MNTurnByTurnLocationTracker = _Class("MNTurnByTurnLocationTracker")
MNWalkingTurnByTurnLocationTracker = _Class("MNWalkingTurnByTurnLocationTracker")
MNDrivingTurnByTurnLocationTracker = _Class("MNDrivingTurnByTurnLocationTracker")
MNCyclingTurnByTurnLocationTracker = _Class("MNCyclingTurnByTurnLocationTracker")
MNNavigationServicePeer = _Class("MNNavigationServicePeer")
MNTimeballServicePeer = _Class("MNTimeballServicePeer")
MNTimeballLocalPeer = _Class("MNTimeballLocalPeer")
MNRouteCoordinate = _Class("MNRouteCoordinate")
MNTraceBookmark = _Class("MNTraceBookmark")
MNDirectionsRequestDetails = _Class("MNDirectionsRequestDetails")
MNTracePlaybackDetails = _Class("MNTracePlaybackDetails")
MNGuidanceEventFeedback = _Class("MNGuidanceEventFeedback")
MNRouteAttributes = _Class("MNRouteAttributes")
MNLocation = _Class("MNLocation")

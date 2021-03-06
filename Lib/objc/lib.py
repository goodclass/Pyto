"""
Classes from the 'lib' framework.
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


Object = _Class("Object")
NSObject = _Class("NSObject")
boringssl_concrete_boringssl_session_state = _Class(
    "boringssl_concrete_boringssl_session_state"
)
NWConcrete_nw_establishment_report = _Class("NWConcrete_nw_establishment_report")
NWConcrete_nw_protocol_establishment_report = _Class(
    "NWConcrete_nw_protocol_establishment_report"
)
NWConcrete_nw_resolution_report = _Class("NWConcrete_nw_resolution_report")
NWConcrete_nw_write_request = _Class("NWConcrete_nw_write_request")
NWConcrete_nw_read_request = _Class("NWConcrete_nw_read_request")
NWConcrete_nw_content_context = _Class("NWConcrete_nw_content_context")
AWDAddressBookSyncFullSyncEvent = _Class("AWDAddressBookSyncFullSyncEvent")
AWDBltDelayAckFromSecondaryDevice = _Class("AWDBltDelayAckFromSecondaryDevice")
AWDBltDelayAppReadyToSend = _Class("AWDBltDelayAppReadyToSend")
AWDBltDelayReceiveLocal = _Class("AWDBltDelayReceiveLocal")
AWDBltDelayToPrimaryDevice = _Class("AWDBltDelayToPrimaryDevice")
AWDBltDelayToSecondaryDevice = _Class("AWDBltDelayToSecondaryDevice")
AWDBltDelayToSync = _Class("AWDBltDelayToSync")
AWDBltDelayToSyncUnrestricted = _Class("AWDBltDelayToSyncUnrestricted")
AWDBltDelayUIFromFactory = _Class("AWDBltDelayUIFromFactory")
AWDBltPrimaryDevicePublicationToResponseDelay = _Class(
    "AWDBltPrimaryDevicePublicationToResponseDelay"
)
AWDBltPrimaryDeviceSendAttempt = _Class("AWDBltPrimaryDeviceSendAttempt")
AWDBltPrimaryDeviceSendInTime = _Class("AWDBltPrimaryDeviceSendInTime")
AWDBltPrimaryDeviceSendTimeout = _Class("AWDBltPrimaryDeviceSendTimeout")
AWDBltRequestToResponseDelay = _Class("AWDBltRequestToResponseDelay")
AWDBltSecondaryConnectedToTransport = _Class("AWDBltSecondaryConnectedToTransport")
AWDBltSecondaryProcessStarted = _Class("AWDBltSecondaryProcessStarted")
AWDBltUIBuildAttempt = _Class("AWDBltUIBuildAttempt")
AWDBltUIBuildFail = _Class("AWDBltUIBuildFail")
AWDBltUIBuildSuccess = _Class("AWDBltUIBuildSuccess")
AWDCaptiveSession = _Class("AWDCaptiveSession")
AWDCFNetworkCacheMetrics = _Class("AWDCFNetworkCacheMetrics")
AWDCFNetworkStreamTaskTiming = _Class("AWDCFNetworkStreamTaskTiming")
AWDCFNetworkTaskMetrics = _Class("AWDCFNetworkTaskMetrics")
AWDCFNetworkTransactionMetrics = _Class("AWDCFNetworkTransactionMetrics")
AWDCFNetworkW3CNavigationTiming = _Class("AWDCFNetworkW3CNavigationTiming")
AWDCompanionSyncErrorEvent = _Class("AWDCompanionSyncErrorEvent")
AWDCompanionSyncErrorNotification = _Class("AWDCompanionSyncErrorNotification")
AWDCompanionSyncFullSyncDuration = _Class("AWDCompanionSyncFullSyncDuration")
AWDCompanionSyncReceiveEvent = _Class("AWDCompanionSyncReceiveEvent")
AWDCoreRoutineAssetVersion = _Class("AWDCoreRoutineAssetVersion")
AWDCoreRoutineDeletionGroupStats = _Class("AWDCoreRoutineDeletionGroupStats")
AWDCoreRoutineDeletionRecordStats = _Class("AWDCoreRoutineDeletionRecordStats")
AWDCoreRoutineDeletionStats = _Class("AWDCoreRoutineDeletionStats")
AWDCoreRoutineFMCAssistanceInstance = _Class("AWDCoreRoutineFMCAssistanceInstance")
AWDCoreRoutineFMCCarParkedInstance = _Class("AWDCoreRoutineFMCCarParkedInstance")
AWDCoreRoutineFMCDailyAssessment = _Class("AWDCoreRoutineFMCDailyAssessment")
AWDCoreRoutineFMCDailyAssessments = _Class("AWDCoreRoutineFMCDailyAssessments")
AWDCoreRoutineFMCReturnToCarInstance = _Class("AWDCoreRoutineFMCReturnToCarInstance")
AWDCoreRoutineFMCVehicleConnectionEventInstance = _Class(
    "AWDCoreRoutineFMCVehicleConnectionEventInstance"
)
AWDCoreRoutineFMCViewedInstance = _Class("AWDCoreRoutineFMCViewedInstance")
AWDCoreRoutineHeroAppEngagementInstance = _Class(
    "AWDCoreRoutineHeroAppEngagementInstance"
)
AWDCoreRoutineHeroAppImpressionInstance = _Class(
    "AWDCoreRoutineHeroAppImpressionInstance"
)
AWDCoreRoutineHeroAppSuggestionInstance = _Class(
    "AWDCoreRoutineHeroAppSuggestionInstance"
)
AWDCoreRoutineHintSourceSubmissionInstance = _Class(
    "AWDCoreRoutineHintSourceSubmissionInstance"
)
AWDCoreRoutineHintSourceSubmissionSet = _Class("AWDCoreRoutineHintSourceSubmissionSet")
AWDCoreRoutineHintSourceUsageInstance = _Class("AWDCoreRoutineHintSourceUsageInstance")
AWDCoreRoutineHintSourceUsageSet = _Class("AWDCoreRoutineHintSourceUsageSet")
AWDCoreRoutineHistogramBin = _Class("AWDCoreRoutineHistogramBin")
AWDCoreRoutineLMPAutofillSelectedInstance = _Class(
    "AWDCoreRoutineLMPAutofillSelectedInstance"
)
AWDCoreRoutineLMPDailyAssessment = _Class("AWDCoreRoutineLMPDailyAssessment")
AWDCoreRoutineLMPRequestedInstance = _Class("AWDCoreRoutineLMPRequestedInstance")
AWDCoreRoutineLMPResponseInstance = _Class("AWDCoreRoutineLMPResponseInstance")
AWDCoreRoutineLMPScoreBoard = _Class("AWDCoreRoutineLMPScoreBoard")
AWDCoreRoutineLMPScoreBoardInstance = _Class("AWDCoreRoutineLMPScoreBoardInstance")
AWDCoreRoutineLearnedLocationReconciliationVisit = _Class(
    "AWDCoreRoutineLearnedLocationReconciliationVisit"
)
AWDCoreRoutineLearnedLocationReconciliationVisitDensity = _Class(
    "AWDCoreRoutineLearnedLocationReconciliationVisitDensity"
)
AWDCoreRoutineLearnedLocationTrainingMetrics = _Class(
    "AWDCoreRoutineLearnedLocationTrainingMetrics"
)
AWDCoreRoutineLearnedRouteInstance = _Class("AWDCoreRoutineLearnedRouteInstance")
AWDCoreRoutineLocationAwarenessBasicHistogram = _Class(
    "AWDCoreRoutineLocationAwarenessBasicHistogram"
)
AWDCoreRoutineLocationAwarenessHeartbeatStatistics = _Class(
    "AWDCoreRoutineLocationAwarenessHeartbeatStatistics"
)
AWDCoreRoutineLocationAwarenessIntervalHistogram = _Class(
    "AWDCoreRoutineLocationAwarenessIntervalHistogram"
)
AWDCoreRoutineLocationAwarenessLocationTimeHistograms = _Class(
    "AWDCoreRoutineLocationAwarenessLocationTimeHistograms"
)
AWDCoreRoutineLocationAwarenessStatistics = _Class(
    "AWDCoreRoutineLocationAwarenessStatistics"
)
AWDCoreRoutineLocationTypeItem = _Class("AWDCoreRoutineLocationTypeItem")
AWDCoreRoutineMagicMomentsSuggestionInstance = _Class(
    "AWDCoreRoutineMagicMomentsSuggestionInstance"
)
AWDCoreRoutineMagicalMomentsExpertInstance = _Class(
    "AWDCoreRoutineMagicalMomentsExpertInstance"
)
AWDCoreRoutineMagicalMomentsExperts = _Class("AWDCoreRoutineMagicalMomentsExperts")
AWDCoreRoutineMagicalMomentsFeatureAddon = _Class(
    "AWDCoreRoutineMagicalMomentsFeatureAddon"
)
AWDCoreRoutineMagicalMomentsIndividualMoment = _Class(
    "AWDCoreRoutineMagicalMomentsIndividualMoment"
)
AWDCoreRoutineMagicalMomentsRecommendedAppsHistogramInstance = _Class(
    "AWDCoreRoutineMagicalMomentsRecommendedAppsHistogramInstance"
)
AWDCoreRoutineMagicalMomentsRecommendedAppsHistogramSet = _Class(
    "AWDCoreRoutineMagicalMomentsRecommendedAppsHistogramSet"
)
AWDCoreRoutineMapItem = _Class("AWDCoreRoutineMapItem")
AWDCoreRoutineModelAlgorithmInstance = _Class("AWDCoreRoutineModelAlgorithmInstance")
AWDCoreRoutineModelAlgorithmSet = _Class("AWDCoreRoutineModelAlgorithmSet")
AWDCoreRoutineModelAvailability = _Class("AWDCoreRoutineModelAvailability")
AWDCoreRoutineModelClusterMovementInstance = _Class(
    "AWDCoreRoutineModelClusterMovementInstance"
)
AWDCoreRoutineModelClusterMovementNoiseSet = _Class(
    "AWDCoreRoutineModelClusterMovementNoiseSet"
)
AWDCoreRoutineModelClusterStandardDeviationInstance = _Class(
    "AWDCoreRoutineModelClusterStandardDeviationInstance"
)
AWDCoreRoutineModelClusterStandardDeviationSet = _Class(
    "AWDCoreRoutineModelClusterStandardDeviationSet"
)
AWDCoreRoutineModelConsistencyReconsolidation = _Class(
    "AWDCoreRoutineModelConsistencyReconsolidation"
)
AWDCoreRoutineModelDominantPlaceCount = _Class("AWDCoreRoutineModelDominantPlaceCount")
AWDCoreRoutineModelLearnedNonGeocodeableEvents = _Class(
    "AWDCoreRoutineModelLearnedNonGeocodeableEvents"
)
AWDCoreRoutineModelLength = _Class("AWDCoreRoutineModelLength")
AWDCoreRoutineModelStatus = _Class("AWDCoreRoutineModelStatus")
AWDCoreRoutineModelTransitionInstance = _Class("AWDCoreRoutineModelTransitionInstance")
AWDCoreRoutineModelTransitionSet = _Class("AWDCoreRoutineModelTransitionSet")
AWDCoreRoutineModelVisitCount = _Class("AWDCoreRoutineModelVisitCount")
AWDCoreRoutinePersistenceMirroringAccountDevices = _Class(
    "AWDCoreRoutinePersistenceMirroringAccountDevices"
)
AWDCoreRoutinePersistenceMirroringDelegate = _Class(
    "AWDCoreRoutinePersistenceMirroringDelegate"
)
AWDCoreRoutinePersistenceMirroringDeviceProfile = _Class(
    "AWDCoreRoutinePersistenceMirroringDeviceProfile"
)
AWDCoreRoutinePersistenceMirroringOperations = _Class(
    "AWDCoreRoutinePersistenceMirroringOperations"
)
AWDCoreRoutinePersistenceMirroringResetSync = _Class(
    "AWDCoreRoutinePersistenceMirroringResetSync"
)
AWDCoreRoutinePersistenceMirroringTickleFight = _Class(
    "AWDCoreRoutinePersistenceMirroringTickleFight"
)
AWDCoreRoutinePersistenceStore = _Class("AWDCoreRoutinePersistenceStore")
AWDCoreRoutinePersistenceStoreMigrationDuration = _Class(
    "AWDCoreRoutinePersistenceStoreMigrationDuration"
)
AWDCoreRoutinePlace = _Class("AWDCoreRoutinePlace")
AWDCoreRoutineRankRoutesRequestedInstance = _Class(
    "AWDCoreRoutineRankRoutesRequestedInstance"
)
AWDCoreRoutineRoadClassItem = _Class("AWDCoreRoutineRoadClassItem")
AWDCoreRoutineSettingsClearAll = _Class("AWDCoreRoutineSettingsClearAll")
AWDCoreRoutineSettingsClusterLocationView = _Class(
    "AWDCoreRoutineSettingsClusterLocationView"
)
AWDCoreRoutineSettingsClusterLocationVisitView = _Class(
    "AWDCoreRoutineSettingsClusterLocationVisitView"
)
AWDCoreRoutineSettingsClusterView = _Class("AWDCoreRoutineSettingsClusterView")
AWDCoreRoutineSettingsDeleteType = _Class("AWDCoreRoutineSettingsDeleteType")
AWDCoreRoutineSettingsEnableDisable = _Class("AWDCoreRoutineSettingsEnableDisable")
AWDCoreRoutineSettingsMapInteraction = _Class("AWDCoreRoutineSettingsMapInteraction")
AWDCoreRoutineSettingsSessionDuration = _Class("AWDCoreRoutineSettingsSessionDuration")
AWDCoreRoutineStateModelConfidence = _Class("AWDCoreRoutineStateModelConfidence")
AWDCoreRoutineTrafficConditions = _Class("AWDCoreRoutineTrafficConditions")
AWDCoreRoutineTransitionMotionType = _Class("AWDCoreRoutineTransitionMotionType")
AWDCoreRoutineVisit = _Class("AWDCoreRoutineVisit")
AWDDuetExpertCenterZKWOutcome = _Class("AWDDuetExpertCenterZKWOutcome")
AWDEventKitSyncCompletedNightlySync = _Class("AWDEventKitSyncCompletedNightlySync")
AWDEventKitSyncIsNotifiableEvent = _Class("AWDEventKitSyncIsNotifiableEvent")
AWDEventKitSyncSyncedAttendeeResponseFromWatch = _Class(
    "AWDEventKitSyncSyncedAttendeeResponseFromWatch"
)
AWDEventKitSyncSyncedEventCreatedOnWatch = _Class(
    "AWDEventKitSyncSyncedEventCreatedOnWatch"
)
AWDEventKitSyncSyncedTaskCreatedOnWatch = _Class(
    "AWDEventKitSyncSyncedTaskCreatedOnWatch"
)
AWDFaceTimeCallAcceptReceived = _Class("AWDFaceTimeCallAcceptReceived")
AWDFaceTimeCallAcceptSent = _Class("AWDFaceTimeCallAcceptSent")
AWDFaceTimeCallCancelSent = _Class("AWDFaceTimeCallCancelSent")
AWDFaceTimeCallConnected = _Class("AWDFaceTimeCallConnected")
AWDFaceTimeCallDeclineSent = _Class("AWDFaceTimeCallDeclineSent")
AWDFaceTimeCallEnded = _Class("AWDFaceTimeCallEnded")
AWDFaceTimeCallFailed = _Class("AWDFaceTimeCallFailed")
AWDFaceTimeCallInterruptionBegan = _Class("AWDFaceTimeCallInterruptionBegan")
AWDFaceTimeCallInterruptionEnded = _Class("AWDFaceTimeCallInterruptionEnded")
AWDFaceTimeCallInvitationReceived = _Class("AWDFaceTimeCallInvitationReceived")
AWDFaceTimeCallInvitationSent = _Class("AWDFaceTimeCallInvitationSent")
AWDFaceTimeCallRelayInitiateReceived = _Class("AWDFaceTimeCallRelayInitiateReceived")
AWDFaceTimeCallRelayInitiateSent = _Class("AWDFaceTimeCallRelayInitiateSent")
AWDFaceTimeCallRelayUpdateReceived = _Class("AWDFaceTimeCallRelayUpdateReceived")
AWDFaceTimeCallRelayUpdateSent = _Class("AWDFaceTimeCallRelayUpdateSent")
AWDFaceTimeCallStarted = _Class("AWDFaceTimeCallStarted")
AWDHoneybeeSignature = _Class("AWDHoneybeeSignature")
AWDIDSAppDeliveryReceipt = _Class("AWDIDSAppDeliveryReceipt")
AWDIDSClientProcessReceivedMessage = _Class("AWDIDSClientProcessReceivedMessage")
AWDIDSCloudLinkReEstablished = _Class("AWDIDSCloudLinkReEstablished")
AWDIDSConnectedAfterPipeConnectedTimeInMs = _Class(
    "AWDIDSConnectedAfterPipeConnectedTimeInMs"
)
AWDIDSDeviceConnectionDurationEvent = _Class("AWDIDSDeviceConnectionDurationEvent")
AWDIDSDuplicatedMessage = _Class("AWDIDSDuplicatedMessage")
AWDIDSExternalIPDetectionTime = _Class("AWDIDSExternalIPDetectionTime")
AWDIDSGenericConnectionSetupDurationEvent = _Class(
    "AWDIDSGenericConnectionSetupDurationEvent"
)
AWDIDSLocalDeliveryAppLevelAck = _Class("AWDIDSLocalDeliveryAppLevelAck")
AWDIDSLocalDeliveryMessageDelivered = _Class("AWDIDSLocalDeliveryMessageDelivered")
AWDIDSLocalDeliveryMessageReceived = _Class("AWDIDSLocalDeliveryMessageReceived")
AWDIDSLocalDeliveryMessageSent = _Class("AWDIDSLocalDeliveryMessageSent")
AWDIDSLocalDeliverySocketClosed = _Class("AWDIDSLocalDeliverySocketClosed")
AWDIDSLocalDeliverySocketOpened = _Class("AWDIDSLocalDeliverySocketOpened")
AWDIDSLocalMessageRTT = _Class("AWDIDSLocalMessageRTT")
AWDIDSLocalMessageTimedOut = _Class("AWDIDSLocalMessageTimedOut")
AWDIDSMagnetCorruption = _Class("AWDIDSMagnetCorruption")
AWDIDSMagnetCorruptionDetailed = _Class("AWDIDSMagnetCorruptionDetailed")
AWDIDSMagnetDataCorruptionRecoveryTimeInMs = _Class(
    "AWDIDSMagnetDataCorruptionRecoveryTimeInMs"
)
AWDIDSMessageDeliveryPath = _Class("AWDIDSMessageDeliveryPath")
AWDIDSNoteMessageReceived = _Class("AWDIDSNoteMessageReceived")
AWDIDSOTRSessionNegotiation = _Class("AWDIDSOTRSessionNegotiation")
AWDIDSOutgoingMessageDurationTrace = _Class("AWDIDSOutgoingMessageDurationTrace")
AWDIDSQRAllocation = _Class("AWDIDSQRAllocation")
AWDIDSQuickRelay = _Class("AWDIDSQuickRelay")
AWDIDSRealTimeEncryptionFirstReceivedPacketMKMTimeDelta = _Class(
    "AWDIDSRealTimeEncryptionFirstReceivedPacketMKMTimeDelta"
)
AWDIDSRealTimeEncryptionMembershipChangeEventFirstMKMTimeDelta = _Class(
    "AWDIDSRealTimeEncryptionMembershipChangeEventFirstMKMTimeDelta"
)
AWDIDSRealTimeEncryptionMissingPrekeys = _Class(
    "AWDIDSRealTimeEncryptionMissingPrekeys"
)
AWDIDSRegistrationAccountStatus = _Class("AWDIDSRegistrationAccountStatus")
AWDIDSRegistrationAuthenticate = _Class("AWDIDSRegistrationAuthenticate")
AWDIDSRegistrationAuthenticationParametersReceived = _Class(
    "AWDIDSRegistrationAuthenticationParametersReceived"
)
AWDIDSRegistrationCompleted = _Class("AWDIDSRegistrationCompleted")
AWDIDSRegistrationControlChosen = _Class("AWDIDSRegistrationControlChosen")
AWDIDSRegistrationOperation = _Class("AWDIDSRegistrationOperation")
AWDIDSRegistrationPhoneNumberReceivedSMS = _Class(
    "AWDIDSRegistrationPhoneNumberReceivedSMS"
)
AWDIDSRegistrationPhoneNumberValidationFinished = _Class(
    "AWDIDSRegistrationPhoneNumberValidationFinished"
)
AWDIDSRegistrationProfileHandleOperation = _Class(
    "AWDIDSRegistrationProfileHandleOperation"
)
AWDIDSRegistrationProfileOperation = _Class("AWDIDSRegistrationProfileOperation")
AWDIDSRegistrationRenewCredentialsCompleted = _Class(
    "AWDIDSRegistrationRenewCredentialsCompleted"
)
AWDIDSServerStorageStateMachineCompleted = _Class(
    "AWDIDSServerStorageStateMachineCompleted"
)
AWDIDSSessionAcceptReceived = _Class("AWDIDSSessionAcceptReceived")
AWDIDSSessionAcceptSent = _Class("AWDIDSSessionAcceptSent")
AWDIDSSessionCancelReceived = _Class("AWDIDSSessionCancelReceived")
AWDIDSSessionCancelSent = _Class("AWDIDSSessionCancelSent")
AWDIDSSessionCompleted = _Class("AWDIDSSessionCompleted")
AWDIDSSessionConnected = _Class("AWDIDSSessionConnected")
AWDIDSSessionDeclineReceived = _Class("AWDIDSSessionDeclineReceived")
AWDIDSSessionDeclineSent = _Class("AWDIDSSessionDeclineSent")
AWDIDSSessionEnded = _Class("AWDIDSSessionEnded")
AWDIDSSessionInvitationReceived = _Class("AWDIDSSessionInvitationReceived")
AWDIDSSessionInvitationSent = _Class("AWDIDSSessionInvitationSent")
AWDIDSSessionReinitiateConnected = _Class("AWDIDSSessionReinitiateConnected")
AWDIDSSessionReinitiateRequested = _Class("AWDIDSSessionReinitiateRequested")
AWDIDSSessionReinitiateStarted = _Class("AWDIDSSessionReinitiateStarted")
AWDIDSSessionStarted = _Class("AWDIDSSessionStarted")
AWDIDSSocketPairConnectionTCPInfo = _Class("AWDIDSSocketPairConnectionTCPInfo")
AWDIDSStreamingReport = _Class("AWDIDSStreamingReport")
AWDIDSUniqueIncomingStreamIDs = _Class("AWDIDSUniqueIncomingStreamIDs")
AWDIDSWRMLinkRecommendation = _Class("AWDIDSWRMLinkRecommendation")
AWDIDSWebTunnelRequestCompleted = _Class("AWDIDSWebTunnelRequestCompleted")
AWDIDSWiFiSetupAttempt = _Class("AWDIDSWiFiSetupAttempt")
AWDIDSWiProxConnectionFailed = _Class("AWDIDSWiProxConnectionFailed")
AWDIDSWiProxConnectionSuccess = _Class("AWDIDSWiProxConnectionSuccess")
AWDIDSWiProxDidConnectToPeer = _Class("AWDIDSWiProxDidConnectToPeer")
AWDIDSWiProxDidDisconnectFromPeer = _Class("AWDIDSWiProxDidDisconnectFromPeer")
AWDIDSWiProxDidSendData = _Class("AWDIDSWiProxDidSendData")
AWDIMessageAttachmentDownload = _Class("AWDIMessageAttachmentDownload")
AWDIMessageAttachmentUpload = _Class("AWDIMessageAttachmentUpload")
AWDIMessageCloudKitAttachmentDownloadFailed = _Class(
    "AWDIMessageCloudKitAttachmentDownloadFailed"
)
AWDIMessageCloudKitSyncFailed = _Class("AWDIMessageCloudKitSyncFailed")
AWDIMessageCloudKitValidatePurgeableAttachment = _Class(
    "AWDIMessageCloudKitValidatePurgeableAttachment"
)
AWDIMessageDeduplicated = _Class("AWDIMessageDeduplicated")
AWDIMessageDeliveredMessage = _Class("AWDIMessageDeliveredMessage")
AWDIMessageDowngrade = _Class("AWDIMessageDowngrade")
AWDIMessageHealthCheckPerformed = _Class("AWDIMessageHealthCheckPerformed")
AWDIMessageNicknamePublished = _Class("AWDIMessageNicknamePublished")
AWDIMessageNicknameRetrieved = _Class("AWDIMessageNicknameRetrieved")
AWDIMessageQueryFinished = _Class("AWDIMessageQueryFinished")
AWDIMessageReceivedMessage = _Class("AWDIMessageReceivedMessage")
AWDIMessageSentMessage = _Class("AWDIMessageSentMessage")
AWDSMSReceivedMessage = _Class("AWDSMSReceivedMessage")
AWDSMSSentMessage = _Class("AWDSMSSentMessage")
AWDIMRemoteURLLoadCompleted = _Class("AWDIMRemoteURLLoadCompleted")
AWDIMRemoteURLLoadFailed = _Class("AWDIMRemoteURLLoadFailed")
AWDITesterAppStart = _Class("AWDITesterAppStart")
AWDITesterApplicationUUID = _Class("AWDITesterApplicationUUID")
AWDITesterApplyCustomInputs = _Class("AWDITesterApplyCustomInputs")
AWDITesterCertApplePayTestFinish = _Class("AWDITesterCertApplePayTestFinish")
AWDITesterCertApplePayTestStart = _Class("AWDITesterCertApplePayTestStart")
AWDITesterCertApplePayTestSubmission = _Class("AWDITesterCertApplePayTestSubmission")
AWDITesterCertHomeKitTestFinish = _Class("AWDITesterCertHomeKitTestFinish")
AWDITesterCertHomeKitTestStart = _Class("AWDITesterCertHomeKitTestStart")
AWDITesterCertHomeKitTestSubmission = _Class("AWDITesterCertHomeKitTestSubmission")
AWDITesterCertTestFinish = _Class("AWDITesterCertTestFinish")
AWDITesterCertTestStart = _Class("AWDITesterCertTestStart")
AWDITesterCertTestSubmission = _Class("AWDITesterCertTestSubmission")
AWDITesterTestFinish = _Class("AWDITesterTestFinish")
AWDITesterTestLoad = _Class("AWDITesterTestLoad")
AWDITesterTestShare = _Class("AWDITesterTestShare")
AWDITesterTestStart = _Class("AWDITesterTestStart")
AWDLBClientConnectionReport = _Class("AWDLBClientConnectionReport")
AWDLBConnectionReport = _Class("AWDLBConnectionReport")
AWDLBEndpointsFetchReport = _Class("AWDLBEndpointsFetchReport")
AWDLibnetcoreCellularFallbackReport = _Class("AWDLibnetcoreCellularFallbackReport")
AWDLibnetcoreConnectionDataUsageSnapshot = _Class(
    "AWDLibnetcoreConnectionDataUsageSnapshot"
)
AWDLibnetcoreConnectionStatisticsReport = _Class(
    "AWDLibnetcoreConnectionStatisticsReport"
)
AWDLibnetcoreMPTCPStatsReport = _Class("AWDLibnetcoreMPTCPStatsReport")
AWDLibnetcoreMbufStatsReport = _Class("AWDLibnetcoreMbufStatsReport")
AWDLibnetcoreNetworkdStatsReport = _Class("AWDLibnetcoreNetworkdStatsReport")
AWDLibnetcoreRNFActivityNotification = _Class("AWDLibnetcoreRNFActivityNotification")
AWDLibnetcoreStatsReport = _Class("AWDLibnetcoreStatsReport")
AWDLibnetcoreTCPConnectionReport = _Class("AWDLibnetcoreTCPConnectionReport")
AWDLibnetcoreTCPECNInterfaceStatsReport = _Class(
    "AWDLibnetcoreTCPECNInterfaceStatsReport"
)
AWDLibnetcoreTCPECNStatsReport = _Class("AWDLibnetcoreTCPECNStatsReport")
AWDLibnetcoreTCPKernelStats = _Class("AWDLibnetcoreTCPKernelStats")
AWDLibnetcoreTCPStatsReport = _Class("AWDLibnetcoreTCPStatsReport")
AWDLibnetcoreTCPTFOStatsReport = _Class("AWDLibnetcoreTCPTFOStatsReport")
AWDMPTCPConnectionInterfaceReport = _Class("AWDMPTCPConnectionInterfaceReport")
AWDMPTCPConnectionReport = _Class("AWDMPTCPConnectionReport")
AWDMPTCPSubflowSwitchingReport = _Class("AWDMPTCPSubflowSwitchingReport")
AWDNWAPIUsage = _Class("AWDNWAPIUsage")
AWDNWAccumulator = _Class("AWDNWAccumulator")
AWDNWActivity = _Class("AWDNWActivity")
AWDNWActivityEmptyTrigger = _Class("AWDNWActivityEmptyTrigger")
AWDNWActivityEpilogue = _Class("AWDNWActivityEpilogue")
AWDNWConnectionReport = _Class("AWDNWConnectionReport")
AWDNWDeviceReport = _Class("AWDNWDeviceReport")
AWDNWDurationAccumulation = _Class("AWDNWDurationAccumulation")
AWDNWDurationAccumulationState = _Class("AWDNWDurationAccumulationState")
AWDNWL2Report = _Class("AWDNWL2Report")
AWDDNSDomainStats = _Class("AWDDNSDomainStats")
AWDMDNSResponderDNSMessageSizeStats = _Class("AWDMDNSResponderDNSMessageSizeStats")
AWDMDNSResponderDNSStatistics = _Class("AWDMDNSResponderDNSStatistics")
AWDMDNSResponderResolveStats = _Class("AWDMDNSResponderResolveStats")
AWDMDNSResponderResolveStatsDNSServer = _Class("AWDMDNSResponderResolveStatsDNSServer")
AWDMDNSResponderResolveStatsDomain = _Class("AWDMDNSResponderResolveStatsDomain")
AWDMDNSResponderResolveStatsHostname = _Class("AWDMDNSResponderResolveStatsHostname")
AWDMDNSResponderResolveStatsResult = _Class("AWDMDNSResponderResolveStatsResult")
AWDMDNSResponderServicesStats = _Class("AWDMDNSResponderServicesStats")
AWDMMCSChunkingInfo = _Class("AWDMMCSChunkingInfo")
AWDMMCSError = _Class("AWDMMCSError")
AWDMMCSGetRequestInfo = _Class("AWDMMCSGetRequestInfo")
AWDMMCSHttpInfo = _Class("AWDMMCSHttpInfo")
AWDMMCSPutRequestInfo = _Class("AWDMMCSPutRequestInfo")
AWDMMCSTcpInfo = _Class("AWDMMCSTcpInfo")
AWDNanoPhoneEmergencyCallEnded = _Class("AWDNanoPhoneEmergencyCallEnded")
AWDNanoPhoneIncomingCallConnected = _Class("AWDNanoPhoneIncomingCallConnected")
AWDNanoPhoneIncomingCallPresented = _Class("AWDNanoPhoneIncomingCallPresented")
AWDNetworkServiceProxyConnectionStatistics = _Class(
    "AWDNetworkServiceProxyConnectionStatistics"
)
AWDNetworkServiceProxyControlRequestStatistics = _Class(
    "AWDNetworkServiceProxyControlRequestStatistics"
)
AWDNetworkServiceProxyProbeStatistics = _Class("AWDNetworkServiceProxyProbeStatistics")
AWDNetworkServiceProxyRequestStatistics = _Class(
    "AWDNetworkServiceProxyRequestStatistics"
)
AWDOSAnalyticsSubmissions = _Class("AWDOSAnalyticsSubmissions")
AWDPairedSyncSyncReport = _Class("AWDPairedSyncSyncReport")
AWDAppBBPower = _Class("AWDAppBBPower")
AWDAppRRCConnectionStats = _Class("AWDAppRRCConnectionStats")
AWDBacklightLuxMicroAmpsBucket = _Class("AWDBacklightLuxMicroAmpsBucket")
AWDBasebandPowerToolKPIs = _Class("AWDBasebandPowerToolKPIs")
AWDCpuLoad = _Class("AWDCpuLoad")
AWDLQMDataTransfer = _Class("AWDLQMDataTransfer")
AWDNetworkUsage = _Class("AWDNetworkUsage")
AWDPowerApMetrics = _Class("AWDPowerApMetrics")
AWDPowerAppBBMetrics = _Class("AWDPowerAppBBMetrics")
AWDPowerAudioMetrics = _Class("AWDPowerAudioMetrics")
AWDPowerBBAppRRCMetrics = _Class("AWDPowerBBAppRRCMetrics")
AWDPowerBBCallMetricInfo = _Class("AWDPowerBBCallMetricInfo")
AWDPowerBBCallMetrics = _Class("AWDPowerBBCallMetrics")
AWDPowerBBLQMDataTransferMetrics = _Class("AWDPowerBBLQMDataTransferMetrics")
AWDPowerBBNonDataMetrics = _Class("AWDPowerBBNonDataMetrics")
AWDPowerBBRATConnectedMetrics = _Class("AWDPowerBBRATConnectedMetrics")
AWDPowerBatteryMetrics = _Class("AWDPowerBatteryMetrics")
AWDPowerBluetoothMetrics = _Class("AWDPowerBluetoothMetrics")
AWDPowerCameraMetrics = _Class("AWDPowerCameraMetrics")
AWDPowerDisplayBacklightMetrics = _Class("AWDPowerDisplayBacklightMetrics")
AWDPowerNetworkUsageMetrics = _Class("AWDPowerNetworkUsageMetrics")
AWDPowerPerProcessCPULoadMetrics = _Class("AWDPowerPerProcessCPULoadMetrics")
AWDPowerStateResidencyAndWeight = _Class("AWDPowerStateResidencyAndWeight")
AWDPowerTouchMetrics = _Class("AWDPowerTouchMetrics")
AWDPowerWifiMetrics = _Class("AWDPowerWifiMetrics")
AWDRATConnectedPower = _Class("AWDRATConnectedPower")
AWDPushConnectionConnected = _Class("AWDPushConnectionConnected")
AWDPushConnectionDisconnected = _Class("AWDPushConnectionDisconnected")
AWDPushFilterChanged = _Class("AWDPushFilterChanged")
AWDPushFilterSent = _Class("AWDPushFilterSent")
AWDPushKeepAliveFailed = _Class("AWDPushKeepAliveFailed")
AWDPushKeepAliveSent = _Class("AWDPushKeepAliveSent")
AWDPushProxyManagerReceive = _Class("AWDPushProxyManagerReceive")
AWDPushProxyManagerSend = _Class("AWDPushProxyManagerSend")
AWDPushReceived = _Class("AWDPushReceived")
AWDPushReceivedDropped = _Class("AWDPushReceivedDropped")
AWDPushReceivedSlow = _Class("AWDPushReceivedSlow")
AWDPushSent = _Class("AWDPushSent")
AWDPushTopicPolicyChange = _Class("AWDPushTopicPolicyChange")
AWDSafariActivatedHomeScreenQuickActionEvent = _Class(
    "AWDSafariActivatedHomeScreenQuickActionEvent"
)
AWDSafariAutoFillAuthenticationEvent = _Class("AWDSafariAutoFillAuthenticationEvent")
AWDSafariAutoFillAuthenticationPreferenceEvent = _Class(
    "AWDSafariAutoFillAuthenticationPreferenceEvent"
)
AWDSafariCKBookmarksMigrationFinishedEvent = _Class(
    "AWDSafariCKBookmarksMigrationFinishedEvent"
)
AWDSafariCKBookmarksMigrationStartedEvent = _Class(
    "AWDSafariCKBookmarksMigrationStartedEvent"
)
AWDSafariCKBookmarksSyncEvent = _Class("AWDSafariCKBookmarksSyncEvent")
AWDSafariContactAutoFillDidFillCustomContactSetEvent = _Class(
    "AWDSafariContactAutoFillDidFillCustomContactSetEvent"
)
AWDSafariContactAutoFillDidSelectSetEvent = _Class(
    "AWDSafariContactAutoFillDidSelectSetEvent"
)
AWDSafariContactAutoFillDidShowSetsEvent = _Class(
    "AWDSafariContactAutoFillDidShowSetsEvent"
)
AWDSafariDedupedDAVBookmarksEvent = _Class("AWDSafariDedupedDAVBookmarksEvent")
AWDSafariDidReceiveInvalidMessageFromWebProcessEvent = _Class(
    "AWDSafariDidReceiveInvalidMessageFromWebProcessEvent"
)
AWDSafariDidTerminateWebProcessBeforeNavigation = _Class(
    "AWDSafariDidTerminateWebProcessBeforeNavigation"
)
AWDSafariDuplicatedPasswordsWarningEvent = _Class(
    "AWDSafariDuplicatedPasswordsWarningEvent"
)
AWDSafariEnterPasswordsPreferencesEvent = _Class(
    "AWDSafariEnterPasswordsPreferencesEvent"
)
AWDSafariEnterTwoUpEvent = _Class("AWDSafariEnterTwoUpEvent")
AWDSafariInteractedWithGeneratedPasswordEvent = _Class(
    "AWDSafariInteractedWithGeneratedPasswordEvent"
)
AWDSafariPageLoadCompleteEvent = _Class("AWDSafariPageLoadCompleteEvent")
AWDSafariPageLoadStartedEvent = _Class("AWDSafariPageLoadStartedEvent")
AWDSafariParticipatedInPasswordAutoFill = _Class(
    "AWDSafariParticipatedInPasswordAutoFill"
)
AWDSafariReaderActiveOptInOutEvent = _Class("AWDSafariReaderActiveOptInOutEvent")
AWDSafariReaderChangedOptInOutEvent = _Class("AWDSafariReaderChangedOptInOutEvent")
AWDSafariSafeBrowsingUserActionAfterSeeingWarningEvent = _Class(
    "AWDSafariSafeBrowsingUserActionAfterSeeingWarningEvent"
)
AWDSafariSafeBrowsingWarningShownEvent = _Class(
    "AWDSafariSafeBrowsingWarningShownEvent"
)
AWDSafariSelectedFavoritesGridItemEvent = _Class(
    "AWDSafariSelectedFavoritesGridItemEvent"
)
AWDSafariSetAutoFillQuickTypeSuggestionEvent = _Class(
    "AWDSafariSetAutoFillQuickTypeSuggestionEvent"
)
AWDSafariSharedPasswordEvent = _Class("AWDSafariSharedPasswordEvent")
AWDSafariTappedAutoFillQuickTypeSuggestionEvent = _Class(
    "AWDSafariTappedAutoFillQuickTypeSuggestionEvent"
)
AWDSafariTappedOnToolbarButtonEvent = _Class("AWDSafariTappedOnToolbarButtonEvent")
AWDSafariTwoFingerTappedOnLinkEvent = _Class("AWDSafariTwoFingerTappedOnLinkEvent")
AWDSafariUnableToSilentlyMigrateToCKBookmarksEvent = _Class(
    "AWDSafariUnableToSilentlyMigrateToCKBookmarksEvent"
)
AWDSafariUsingPrivateBrowsingEvent = _Class("AWDSafariUsingPrivateBrowsingEvent")
AWDSafariVersioningEvent = _Class("AWDSafariVersioningEvent")
AWDSafariViewControllerDismissedEvent = _Class("AWDSafariViewControllerDismissedEvent")
AWDSafariViewControllerPresentedFromHostAppEvent = _Class(
    "AWDSafariViewControllerPresentedFromHostAppEvent"
)
AWDSafariViewControllerTappedOnToolbarButtonEvent = _Class(
    "AWDSafariViewControllerTappedOnToolbarButtonEvent"
)
AWDSiriNetworkAnalyzerRun = _Class("AWDSiriNetworkAnalyzerRun")
AWDSiriRequestRecord = _Class("AWDSiriRequestRecord")
AWDSiriServerConnectionFailed = _Class("AWDSiriServerConnectionFailed")
AWDSiriServerConnectionOpen = _Class("AWDSiriServerConnectionOpen")
AWDSiriServerConnectionStart = _Class("AWDSiriServerConnectionStart")
AWDSiriSession = _Class("AWDSiriSession")
AWDSiriSessionLoadTimeout = _Class("AWDSiriSessionLoadTimeout")
AWDSiriSpeechRecognized = _Class("AWDSiriSpeechRecognized")
AWDSiriVoiceRecordingEnd = _Class("AWDSiriVoiceRecordingEnd")
AWDSiriVoiceRecordingStart = _Class("AWDSiriVoiceRecordingStart")
AWDSiriVoiceSendEnd = _Class("AWDSiriVoiceSendEnd")
AWDSiriVoiceSendStart = _Class("AWDSiriVoiceSendStart")
AWDTCPConnectionInfo = _Class("AWDTCPConnectionInfo")
AWDTransportHistoryRecord = _Class("AWDTransportHistoryRecord")
AWDSOSAutomaticCallCountdownEnabled = _Class("AWDSOSAutomaticCallCountdownEnabled")
AWDSOSAutomaticNewtonEnabled = _Class("AWDSOSAutomaticNewtonEnabled")
AWDSOSLongPressTriggersEmergencySOS = _Class("AWDSOSLongPressTriggersEmergencySOS")
AWDSOSNumberOfVoiceLoops = _Class("AWDSOSNumberOfVoiceLoops")
AWDSOSShouldPlayAudioDuringCountdown = _Class("AWDSOSShouldPlayAudioDuringCountdown")
AWDSOSTriggered = _Class("AWDSOSTriggered")
AWDSpringBoardAppBrightness = _Class("AWDSpringBoardAppBrightness")
AWDSpringBoardBiometricUnlock = _Class("AWDSpringBoardBiometricUnlock")
AWDSpringBoardBreadcrumb = _Class("AWDSpringBoardBreadcrumb")
AWDSpringBoardClawGesture = _Class("AWDSpringBoardClawGesture")
AWDSpringBoardDoNotDisturbChange = _Class("AWDSpringBoardDoNotDisturbChange")
AWDSpringBoardFolderStats = _Class("AWDSpringBoardFolderStats")
AWDSpringBoardIconLaunch = _Class("AWDSpringBoardIconLaunch")
AWDSpringBoardPressSequence = _Class("AWDSpringBoardPressSequence")
AWDSpringBoardSOSAlertResponse = _Class("AWDSpringBoardSOSAlertResponse")
AWDSpringBoardSwitcherPresentationInteraction = _Class(
    "AWDSpringBoardSwitcherPresentationInteraction"
)
AWDSpringBoardSwitcherToAppTransition = _Class("AWDSpringBoardSwitcherToAppTransition")
AWDSpringBoardSystemGesture = _Class("AWDSpringBoardSystemGesture")
AWDTuple = _Class("AWDTuple")
AWDVPNSession = _Class("AWDVPNSession")
AWDChipCountersRx = _Class("AWDChipCountersRx")
AWDChipCountersTx = _Class("AWDChipCountersTx")
AWDChipErrorCountersTx = _Class("AWDChipErrorCountersTx")
AWDControlFrames = _Class("AWDControlFrames")
AWDDataFrames = _Class("AWDDataFrames")
AWDHEStats = _Class("AWDHEStats")
AWDLinkQualityMeasurements = _Class("AWDLinkQualityMeasurements")
AWDMacCountersRx = _Class("AWDMacCountersRx")
AWDMacCountersRxErrors = _Class("AWDMacCountersRxErrors")
AWDManagementFrames = _Class("AWDManagementFrames")
AWDNwExclusionCount = _Class("AWDNwExclusionCount")
AWDOMICntrs = _Class("AWDOMICntrs")
AWDRxPhyErrors = _Class("AWDRxPhyErrors")
AWDScanStatsPerSlice = _Class("AWDScanStatsPerSlice")
AWDSidecarBssSteering = _Class("AWDSidecarBssSteering")
AWDSidecarHistogramBin = _Class("AWDSidecarHistogramBin")
AWDSidecarPeerTraffic = _Class("AWDSidecarPeerTraffic")
AWDSlowWiFiNotification = _Class("AWDSlowWiFiNotification")
AWDSlowWiFiReport = _Class("AWDSlowWiFiReport")
AWDWADiagnosisActionAssociationDifferences = _Class(
    "AWDWADiagnosisActionAssociationDifferences"
)
AWDWAQuickDpsStats = _Class("AWDWAQuickDpsStats")
AWDWPA2Counters = _Class("AWDWPA2Counters")
AWDWiFiActionFrameEvent = _Class("AWDWiFiActionFrameEvent")
AWDWiFiAwdlSidecar = _Class("AWDWiFiAwdlSidecar")
AWDWiFiAwdlSidecarCoalesced = _Class("AWDWiFiAwdlSidecarCoalesced")
AWDWiFiBlacklistingEvent = _Class("AWDWiFiBlacklistingEvent")
AWDWiFiCLTM = _Class("AWDWiFiCLTM")
AWDWiFiCLTMSliceSpecific = _Class("AWDWiFiCLTMSliceSpecific")
AWDWiFiConnectionQuality = _Class("AWDWiFiConnectionQuality")
AWDWiFiDPSAWDLSnapshot = _Class("AWDWiFiDPSAWDLSnapshot")
AWDWiFiDPSActiveProbeStats = _Class("AWDWiFiDPSActiveProbeStats")
AWDWiFiDPSBTSnapshot = _Class("AWDWiFiDPSBTSnapshot")
AWDWiFiDPSCountersSample = _Class("AWDWiFiDPSCountersSample")
AWDWiFiDPSEpilogue = _Class("AWDWiFiDPSEpilogue")
AWDWiFiDPSNotification = _Class("AWDWiFiDPSNotification")
AWDWiFiDPSPerACTxCompletionSnapshot = _Class("AWDWiFiDPSPerACTxCompletionSnapshot")
AWDWiFiDPSReport = _Class("AWDWiFiDPSReport")
AWDWiFiDPSSnapshot = _Class("AWDWiFiDPSSnapshot")
AWDWiFiLPMReport = _Class("AWDWiFiLPMReport")
AWDWiFiLTECoexBin = _Class("AWDWiFiLTECoexBin")
AWDWiFiLTECoexCounters = _Class("AWDWiFiLTECoexCounters")
AWDWiFiLTECoexTxBlanking = _Class("AWDWiFiLTECoexTxBlanking")
AWDWiFiLTEWCI2Counters = _Class("AWDWiFiLTEWCI2Counters")
AWDWiFiLTEWCI2CountersSliceSpecific = _Class("AWDWiFiLTEWCI2CountersSliceSpecific")
AWDWiFiLprxStats = _Class("AWDWiFiLprxStats")
AWDWiFiMetric11axLinkChangeData = _Class("AWDWiFiMetric11axLinkChangeData")
AWDWiFiMetric11axStats = _Class("AWDWiFiMetric11axStats")
AWDWiFiMetricActiveProbeStats = _Class("AWDWiFiMetricActiveProbeStats")
AWDWiFiMetricCustomNetworkSetting = _Class("AWDWiFiMetricCustomNetworkSetting")
AWDWiFiMetricExtendedTrapInfo = _Class("AWDWiFiMetricExtendedTrapInfo")
AWDWiFiMetricHotspotTransportType = _Class("AWDWiFiMetricHotspotTransportType")
AWDWiFiMetricIPv4DHCPLatency = _Class("AWDWiFiMetricIPv4DHCPLatency")
AWDWiFiMetricInterfaceStats = _Class("AWDWiFiMetricInterfaceStats")
AWDWiFiMetricJoinTimeout = _Class("AWDWiFiMetricJoinTimeout")
AWDWiFiMetricLinkChangeData = _Class("AWDWiFiMetricLinkChangeData")
AWDWiFiMetricNetworkPrefs = _Class("AWDWiFiMetricNetworkPrefs")
AWDWiFiMetricRssiHistory = _Class("AWDWiFiMetricRssiHistory")
AWDWiFiMetricScanStats = _Class("AWDWiFiMetricScanStats")
AWDWiFiMetricWiFiStats = _Class("AWDWiFiMetricWiFiStats")
AWDWiFiMetricWowState = _Class("AWDWiFiMetricWowState")
AWDWiFiMetricsAssociationHistory = _Class("AWDWiFiMetricsAssociationHistory")
AWDWiFiMetricsAutoJoinNwExclusion = _Class("AWDWiFiMetricsAutoJoinNwExclusion")
AWDWiFiMetricsHealthUIEvent = _Class("AWDWiFiMetricsHealthUIEvent")
AWDWiFiMetricsKnownNetworksEvent = _Class("AWDWiFiMetricsKnownNetworksEvent")
AWDWiFiMetricsManagerAssociationEvent = _Class("AWDWiFiMetricsManagerAssociationEvent")
AWDWiFiMetricsManagerAutoJoinCumulative = _Class(
    "AWDWiFiMetricsManagerAutoJoinCumulative"
)
AWDWiFiMetricsManagerAutoJoinRecord = _Class("AWDWiFiMetricsManagerAutoJoinRecord")
AWDWiFiMetricsManagerAutoJoinSession = _Class("AWDWiFiMetricsManagerAutoJoinSession")
AWDWiFiMetricsManagerAwdlUsage = _Class("AWDWiFiMetricsManagerAwdlUsage")
AWDWiFiMetricsManagerBGScanBlacklistedNetworks = _Class(
    "AWDWiFiMetricsManagerBGScanBlacklistedNetworks"
)
AWDWiFiMetricsManagerBTCoexModeChange = _Class("AWDWiFiMetricsManagerBTCoexModeChange")
AWDWiFiMetricsManagerBTCoexStats = _Class("AWDWiFiMetricsManagerBTCoexStats")
AWDWiFiMetricsManagerBlacklistedNetworkInfo = _Class(
    "AWDWiFiMetricsManagerBlacklistedNetworkInfo"
)
AWDWiFiMetricsManagerBlacklistingInstanceInfo = _Class(
    "AWDWiFiMetricsManagerBlacklistingInstanceInfo"
)
AWDWiFiMetricsManagerChipCounters = _Class("AWDWiFiMetricsManagerChipCounters")
AWDWiFiMetricsManagerChipMemory = _Class("AWDWiFiMetricsManagerChipMemory")
AWDWiFiMetricsManagerDeviceCount = _Class("AWDWiFiMetricsManagerDeviceCount")
AWDWiFiMetricsManagerEvent = _Class("AWDWiFiMetricsManagerEvent")
AWDWiFiMetricsManagerFrameCounterStats = _Class(
    "AWDWiFiMetricsManagerFrameCounterStats"
)
AWDWiFiMetricsManagerInfraInterface = _Class("AWDWiFiMetricsManagerInfraInterface")
AWDWiFiMetricsManagerLastSSIDInfo = _Class("AWDWiFiMetricsManagerLastSSIDInfo")
AWDWiFiMetricsManagerLeakyAPStats = _Class("AWDWiFiMetricsManagerLeakyAPStats")
AWDWiFiMetricsManagerLinkQualityStats = _Class("AWDWiFiMetricsManagerLinkQualityStats")
AWDWiFiMetricsManagerNetworkTransitionCumulative = _Class(
    "AWDWiFiMetricsManagerNetworkTransitionCumulative"
)
AWDWiFiMetricsManagerNetworkTransitionRecord = _Class(
    "AWDWiFiMetricsManagerNetworkTransitionRecord"
)
AWDWiFiMetricsManagerNetworkTransitionSession = _Class(
    "AWDWiFiMetricsManagerNetworkTransitionSession"
)
AWDWiFiMetricsManagerOneStatsAssociationInfo = _Class(
    "AWDWiFiMetricsManagerOneStatsAssociationInfo"
)
AWDWiFiMetricsManagerP2pLegacyUsageReport = _Class(
    "AWDWiFiMetricsManagerP2pLegacyUsageReport"
)
AWDWiFiMetricsManagerPowerStatsUpdateEvent = _Class(
    "AWDWiFiMetricsManagerPowerStatsUpdateEvent"
)
AWDWiFiMetricsManagerPowerStickiness = _Class("AWDWiFiMetricsManagerPowerStickiness")
AWDWiFiMetricsManagerRCU1CoexModeChange = _Class(
    "AWDWiFiMetricsManagerRCU1CoexModeChange"
)
AWDWiFiMetricsManagerRangingReport = _Class("AWDWiFiMetricsManagerRangingReport")
AWDWiFiMetricsManagerRoamStatus = _Class("AWDWiFiMetricsManagerRoamStatus")
AWDWiFiMetricsManagerSoftError = _Class("AWDWiFiMetricsManagerSoftError")
AWDWiFiMetricsManagerSoftErrorUserFeedback = _Class(
    "AWDWiFiMetricsManagerSoftErrorUserFeedback"
)
AWDWiFiMetricsManagerStateMachine = _Class("AWDWiFiMetricsManagerStateMachine")
AWDWiFiMetricsManagerUserBlacklistEvent = _Class(
    "AWDWiFiMetricsManagerUserBlacklistEvent"
)
AWDWiFiMetricsManagerWatchdogEvent = _Class("AWDWiFiMetricsManagerWatchdogEvent")
AWDWiFiMetricsManagerWifidAvailability = _Class(
    "AWDWiFiMetricsManagerWifidAvailability"
)
AWDWiFiMetricsScanObj = _Class("AWDWiFiMetricsScanObj")
AWDWiFiNWActivity = _Class("AWDWiFiNWActivity")
AWDWiFiNWActivityAggregateMetrics = _Class("AWDWiFiNWActivityAggregateMetrics")
AWDWiFiNWActivityAssoc = _Class("AWDWiFiNWActivityAssoc")
AWDWiFiNWActivityBtCoex = _Class("AWDWiFiNWActivityBtCoex")
AWDWiFiNWActivityBtCoexReqestReason = _Class("AWDWiFiNWActivityBtCoexReqestReason")
AWDWiFiNWActivityControllerStats = _Class("AWDWiFiNWActivityControllerStats")
AWDWiFiNWActivityHistogramBin = _Class("AWDWiFiNWActivityHistogramBin")
AWDWiFiNWActivityImpedingFunctions = _Class("AWDWiFiNWActivityImpedingFunctions")
AWDWiFiNWActivityInterfaceStats = _Class("AWDWiFiNWActivityInterfaceStats")
AWDWiFiNWActivityPeerStats = _Class("AWDWiFiNWActivityPeerStats")
AWDWiFiNWActivityPerACTxCompletions = _Class("AWDWiFiNWActivityPerACTxCompletions")
AWDWiFiNWActivityPowerPStats = _Class("AWDWiFiNWActivityPowerPStats")
AWDWiFiNWActivityPowerStats = _Class("AWDWiFiNWActivityPowerStats")
AWDWiFiNWActivityRateAndAggregation = _Class("AWDWiFiNWActivityRateAndAggregation")
AWDWiFiNWActivityScanActivity = _Class("AWDWiFiNWActivityScanActivity")
AWDWiFiNWActivityStateBin = _Class("AWDWiFiNWActivityStateBin")
AWDWiFiNWActivityTraffic = _Class("AWDWiFiNWActivityTraffic")
AWDWiFiNWActivityTxCompletions = _Class("AWDWiFiNWActivityTxCompletions")
AWDWiFiOtaSystemInfo = _Class("AWDWiFiOtaSystemInfo")
AWDWiFiP2PAirplayMetrics = _Class("AWDWiFiP2PAirplayMetrics")
AWDWiFiRangingRttData = _Class("AWDWiFiRangingRttData")
AWDWiFiRetStats = _Class("AWDWiFiRetStats")
AWDWiFiSDB = _Class("AWDWiFiSDB")
AWDWiFiSDBSliceSpecific = _Class("AWDWiFiSDBSliceSpecific")
AWDWiFiSlowWiFiReport = _Class("AWDWiFiSlowWiFiReport")
AWDWiFiSoftAP = _Class("AWDWiFiSoftAP")
AWDWiFiSoftAPClient = _Class("AWDWiFiSoftAPClient")
AWDWiFiTxInhibitEvent = _Class("AWDWiFiTxInhibitEvent")
AWDWiFiUIConfigureEvent = _Class("AWDWiFiUIConfigureEvent")
AWDWiFiUIEvent = _Class("AWDWiFiUIEvent")
AWDWiFiUIJoinEvent = _Class("AWDWiFiUIJoinEvent")
AWDWiFiUIScanCount = _Class("AWDWiFiUIScanCount")
AWDWiFiUIScanSession = _Class("AWDWiFiUIScanSession")
AWDWiFiWcpsStats = _Class("AWDWiFiWcpsStats")
AWDWifiAssociation = _Class("AWDWifiAssociation")
AWDWifiAwdlD2dMigrationStats = _Class("AWDWifiAwdlD2dMigrationStats")
AWDWifiAwdlHistogramBin = _Class("AWDWifiAwdlHistogramBin")
AWDWifiAwdlServiceRecord = _Class("AWDWifiAwdlServiceRecord")
AWDWifiAwdlStateInfo = _Class("AWDWifiAwdlStateInfo")
AWDWifiHardwareVersion = _Class("AWDWifiHardwareVersion")
AWDWifiLinkQualityRecord = _Class("AWDWifiLinkQualityRecord")
AWDWifiMetricWiFiTetheredDeviceOUI = _Class("AWDWifiMetricWiFiTetheredDeviceOUI")
AWDWifiMostUsedNetworks = _Class("AWDWifiMostUsedNetworks")
AWDWifiP2PAirplayHistogramBin = _Class("AWDWifiP2PAirplayHistogramBin")
AWDWifiPowerState = _Class("AWDWifiPowerState")
AWDWifiStats = _Class("AWDWifiStats")
AWDWifiCallingCallEndReport = _Class("AWDWifiCallingCallEndReport")
AWDThroughputEvaluation = _Class("AWDThroughputEvaluation")
AWDWRMAntSelPolicyStats = _Class("AWDWRMAntSelPolicyStats")
AWDWRMFacetimeRecommendation = _Class("AWDWRMFacetimeRecommendation")
AWDWRMLinkPrefChange1 = _Class("AWDWRMLinkPrefChange1")
AWDWRMLinkPrefChange2 = _Class("AWDWRMLinkPrefChange2")
AWDWRMLinkPrefChangeEvent = _Class("AWDWRMLinkPrefChangeEvent")
AWDWRMLinkPrefInit = _Class("AWDWRMLinkPrefInit")
AWDWRMLinkStateChange = _Class("AWDWRMLinkStateChange")
AWDWRMStreamingReport = _Class("AWDWRMStreamingReport")
AWDWRMULCACoexStats = _Class("AWDWRMULCACoexStats")
AWDWRMWiFiCallingEnd = _Class("AWDWRMWiFiCallingEnd")
AWDWRMWiFiCell5GData = _Class("AWDWRMWiFiCell5GData")
Libsysdiagnose = _Class("Libsysdiagnose")
MecabraWordProperties = _Class("MecabraWordProperties")
MecabraCandidate = _Class("MecabraCandidate")
MecabraFacemarkCandidate = _Class("MecabraFacemarkCandidate")
URLConnectionDelegate = _Class("URLConnectionDelegate")
URLSessionDelegate = _Class("URLSessionDelegate")
CAReportingPerformanceObject = _Class("CAReportingPerformanceObject")
CAReportingPerformanceUtility = _Class("CAReportingPerformanceUtility")
CAReporter = _Class("CAReporter")
CATestReporter = _Class("CATestReporter")
CAReportingClient = _Class("CAReportingClient")
PQLConnection = _Class("PQLConnection")
PQLResultSet = _Class("PQLResultSet")
PQLStatement = _Class("PQLStatement")
PQLQueryBuilder = _Class("PQLQueryBuilder")
AXDefaultsObserverPostDarwinNotificationAction = _Class(
    "AXDefaultsObserverPostDarwinNotificationAction"
)
AXDefaultsObserverExecuteBlockNotificationAction = _Class(
    "AXDefaultsObserverExecuteBlockNotificationAction"
)
AXSupportDefaultsObserver = _Class("AXSupportDefaultsObserver")
NWConcrete_nw_socks5_connection = _Class("NWConcrete_nw_socks5_connection")
NWConcrete_nw_browse_result = _Class("NWConcrete_nw_browse_result")
NWConcrete_nw_endpoint_proxy = _Class("NWConcrete_nw_endpoint_proxy")
NWConcrete_nw_ws_request = _Class("NWConcrete_nw_ws_request")
NWConcrete_nw_authentication_protection_space = _Class(
    "NWConcrete_nw_authentication_protection_space"
)
NWConcrete_nw_authentication_challenge = _Class(
    "NWConcrete_nw_authentication_challenge"
)
NWConcrete_nw_authentication_credential = _Class(
    "NWConcrete_nw_authentication_credential"
)
NWConcrete_nw_browse_descriptor = _Class("NWConcrete_nw_browse_descriptor")
NWConcrete_nw_pac_resolver = _Class("NWConcrete_nw_pac_resolver")
nw_listener_inbox = _Class("nw_listener_inbox")
nw_listener_inbox_socket = _Class("nw_listener_inbox_socket")
nw_listener_inbox_protocol = _Class("nw_listener_inbox_protocol")
nw_ip_channel_inbox = _Class("nw_ip_channel_inbox")
NWConcrete_nw_error = _Class("NWConcrete_nw_error")
NWConcrete_nw_endpoint_transform = _Class("NWConcrete_nw_endpoint_transform")
NWConcrete_nw_ws_ping_request = _Class("NWConcrete_nw_ws_ping_request")
NWConcrete_nw_resolver_service = _Class("NWConcrete_nw_resolver_service")
NWConcrete_nw_framer = _Class("NWConcrete_nw_framer")
NWConcrete_nw_connection_group = _Class("NWConcrete_nw_connection_group")
NWConcrete_nw_unique_connection_request = _Class(
    "NWConcrete_nw_unique_connection_request"
)
NWConcrete_nw_unique_connection = _Class("NWConcrete_nw_unique_connection")
NWConcrete_nw_service_connector = _Class("NWConcrete_nw_service_connector")
NWConcrete_nw_protocol_transform = _Class("NWConcrete_nw_protocol_transform")
NWConcrete_nw_group_descriptor = _Class("NWConcrete_nw_group_descriptor")
NWConcrete_nw_browser = _Class("NWConcrete_nw_browser")
NWConcrete_nw_endpoint_fallback = _Class("NWConcrete_nw_endpoint_fallback")
NWConcrete_nw_ethernet_channel = _Class("NWConcrete_nw_ethernet_channel")
NWConcrete_nw_socks5_server = _Class("NWConcrete_nw_socks5_server")
NWConcrete_nw_protocol_instance = _Class("NWConcrete_nw_protocol_instance")
NWConcrete_nw_protocol_data_array = _Class("NWConcrete_nw_protocol_data_array")
NWConcrete_nw_ws_response = _Class("NWConcrete_nw_ws_response")
NWConcrete_nw_interface_status_monitor = _Class(
    "NWConcrete_nw_interface_status_monitor"
)
NWConcrete_nw_nat64_prefixes_resolver = _Class("NWConcrete_nw_nat64_prefixes_resolver")
NWConcrete_tcp_connection = _Class("NWConcrete_tcp_connection")
NWConcrete_nw_fd_wrapper = _Class("NWConcrete_nw_fd_wrapper")
NWConcrete_nw_listener = _Class("NWConcrete_nw_listener")
nw_interpose_flow = _Class("nw_interpose_flow")
NWConcrete_nw_txt_record = _Class("NWConcrete_nw_txt_record")
NWConcrete_nw_path_observer = _Class("NWConcrete_nw_path_observer")
NWConcrete_nw_interpose = _Class("NWConcrete_nw_interpose")
NWConcrete_nw_data_transfer_report = _Class("NWConcrete_nw_data_transfer_report")
NWConcrete_nw_advertise_descriptor = _Class("NWConcrete_nw_advertise_descriptor")
MGIOKitHelper = _Class("MGIOKitHelper")
boringssl_concrete_boringssl_psk = _Class("boringssl_concrete_boringssl_psk")
boringssl_concrete_boringssl_identity = _Class("boringssl_concrete_boringssl_identity")
boringssl_concrete_boringssl_psk_cache = _Class(
    "boringssl_concrete_boringssl_psk_cache"
)
boringssl_concrete_boringssl_session_cache = _Class(
    "boringssl_concrete_boringssl_session_cache"
)
NWConcrete_nw_link_info = _Class("NWConcrete_nw_link_info")
NWConcrete_nw_protocol_metadata = _Class("NWConcrete_nw_protocol_metadata")
boringssl_concrete_boringssl_ctx = _Class("boringssl_concrete_boringssl_ctx")
boringssl_concrete_nw_protocol_boringssl = _Class(
    "boringssl_concrete_nw_protocol_boringssl"
)
NWConcrete_nw_protocol_instance_stub = _Class("NWConcrete_nw_protocol_instance_stub")
NWConcrete_nw_path_flow = _Class("NWConcrete_nw_path_flow")
NWConcrete_nw_path_flow_registration = _Class("NWConcrete_nw_path_flow_registration")
NWConcrete_nw_endpoint_flow = _Class("NWConcrete_nw_endpoint_flow")
NWConcrete_nw_resolver = _Class("NWConcrete_nw_resolver")
NWConcrete_nw_endpoint_resolver = _Class("NWConcrete_nw_endpoint_resolver")
NWConcrete_nw_association = _Class("NWConcrete_nw_association")
NWConcrete_nw_endpoint_handler = _Class("NWConcrete_nw_endpoint_handler")
NWConcrete_nw_connection = _Class("NWConcrete_nw_connection")
NWConcrete_nw_protocol_options = _Class("NWConcrete_nw_protocol_options")
NWConcrete_nw_resolver_config = _Class("NWConcrete_nw_resolver_config")
NWConcrete_nw_protocol_definition = _Class("NWConcrete_nw_protocol_definition")
NWConcrete_nw_interface = _Class("NWConcrete_nw_interface")
NWConcrete_nw_endpoint = _Class("NWConcrete_nw_endpoint")
NWOSCustomEndpoint = _Class("NWOSCustomEndpoint")
NWOSBonjourEndpoint = _Class("NWOSBonjourEndpoint")
NWOSSRVEndpoint = _Class("NWOSSRVEndpoint")
NWOSURLEndpoint = _Class("NWOSURLEndpoint")
NWOSHostEndpoint = _Class("NWOSHostEndpoint")
NWOSAddressEndpoint = _Class("NWOSAddressEndpoint")
NWConcrete_nw_path = _Class("NWConcrete_nw_path")
NWConcrete_nw_path_parameters = _Class("NWConcrete_nw_path_parameters")
NWConcrete_nw_protocol_stack = _Class("NWConcrete_nw_protocol_stack")
NWConcrete_nw_parameters = _Class("NWConcrete_nw_parameters")
NWConcrete_nw_path_evaluator = _Class("NWConcrete_nw_path_evaluator")
NWConcrete_nw_activity = _Class("NWConcrete_nw_activity")
NWConcrete_nw_context = _Class("NWConcrete_nw_context")
AccessibilitySupportOverrides = _Class("AccessibilitySupportOverrides")
PQLNameInjectionBase = _Class("PQLNameInjectionBase")
PQLNameInjection = _Class("PQLNameInjection")
PQLRawInjection = _Class("PQLRawInjection")
PQLFormatInjection = _Class("PQLFormatInjection")
__NSUnrecognizedTaggedPointer = _Class("__NSUnrecognizedTaggedPointer")
Protocol = _Class("Protocol")
__IncompleteProtocol = _Class("__IncompleteProtocol")
OS_at_encoder = _Class("OS_at_encoder")
OS_tcp_listener = _Class("OS_tcp_listener")
OS_network_proxy = _Class("OS_network_proxy")
OS_nw_parallel_array = _Class("OS_nw_parallel_array")
OS_nw_nexus = _Class("OS_nw_nexus")
OS_nw_protocol_socket = _Class("OS_nw_protocol_socket")
OS_nw_frame = _Class("OS_nw_frame")
OS_nw_channel = _Class("OS_nw_channel")
OS_nw_protocol_tcp = _Class("OS_nw_protocol_tcp")
OS_dnssd_object = _Class("OS_dnssd_object")
OS_dnssd_cname_array = _Class("OS_dnssd_cname_array")
OS_dnssd_getaddrinfo_result = _Class("OS_dnssd_getaddrinfo_result")
OS_dnssd_getaddrinfo = _Class("OS_dnssd_getaddrinfo")
OS_nw_dictionary = _Class("OS_nw_dictionary")
OS_nw_array = _Class("OS_nw_array")

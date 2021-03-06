"""
Classes from the 'DeviceManagement' framework.
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


DMFWebsitePolicyMonitor = _Class("DMFWebsitePolicyMonitor")
DMFUser = _Class("DMFUser")
DMFSecurityInformation = _Class("DMFSecurityInformation")
DMFReportingRequirements = _Class("DMFReportingRequirements")
DMFPolicyRegistration = _Class("DMFPolicyRegistration")
DMFPolicyMonitor = _Class("DMFPolicyMonitor")
DMFOSUpdate = _Class("DMFOSUpdate")
DMFOSStateHandler = _Class("DMFOSStateHandler")
DMFProvisioningProfile = _Class("DMFProvisioningProfile")
DMFInstalledProvisioningProfile = _Class("DMFInstalledProvisioningProfile")
DMFProfilePayload = _Class("DMFProfilePayload")
DMFInstalledPayload = _Class("DMFInstalledPayload")
DMFProfile = _Class("DMFProfile")
DMFInstalledProfile = _Class("DMFInstalledProfile")
DMFiCloudPolicyMonitor = _Class("DMFiCloudPolicyMonitor")
DMFEmergencyModeMonitor = _Class("DMFEmergencyModeMonitor")
DMFPrioritizedPolicy = _Class("DMFPrioritizedPolicy")
DMFEffectivePolicy = _Class("DMFEffectivePolicy")
DMFDevice = _Class("DMFDevice")
DMFControlGroupIdentifier = _Class("DMFControlGroupIdentifier")
DMFControlSessionIdentifier = _Class("DMFControlSessionIdentifier")
DMFConnection = _Class("DMFConnection")
DMFConfigurationSourceClient = _Class("DMFConfigurationSourceClient")
DMFConfigurationSource = _Class("DMFConfigurationSource")
DMFConfigurationOrganization = _Class("DMFConfigurationOrganization")
DMFCommunicationPolicyMonitor = _Class("DMFCommunicationPolicyMonitor")
DMFCertificate = _Class("DMFCertificate")
DMFInstalledCertificate = _Class("DMFInstalledCertificate")
DMFCategoryPolicyMonitor = _Class("DMFCategoryPolicyMonitor")
DMFBookmark = _Class("DMFBookmark")
DMFBook = _Class("DMFBook")
DMFApplicationPolicyMonitor = _Class("DMFApplicationPolicyMonitor")
DMFApplicationInstallProgress = _Class("DMFApplicationInstallProgress")
DMFInstalledApplicationInstallProgress = _Class(
    "DMFInstalledApplicationInstallProgress"
)
DMFApplication = _Class("DMFApplication")
DMFInstalledApplication = _Class("DMFInstalledApplication")
DMFAppManagementInformation = _Class("DMFAppManagementInformation")
DMFApp = _Class("DMFApp")
DMFScheduleOSUpdateResultObject = _Class("DMFScheduleOSUpdateResultObject")
DMFRequestAirPlayMirroringResultObject = _Class(
    "DMFRequestAirPlayMirroringResultObject"
)
DMFRefreshStatusResultObject = _Class("DMFRefreshStatusResultObject")
DMFMDMv1InstallAppResultObject = _Class("DMFMDMv1InstallAppResultObject")
DMFInstallManagedBookResultObject = _Class("DMFInstallManagedBookResultObject")
DMFFetchUsersResultObject = _Class("DMFFetchUsersResultObject")
DMFFetchStreamEventsResultObject = _Class("DMFFetchStreamEventsResultObject")
DMFFetchSecurityInformationResultObject = _Class(
    "DMFFetchSecurityInformationResultObject"
)
DMFFetchScreenshotResultObject = _Class("DMFFetchScreenshotResultObject")
DMFFetchSafariBookmarksResultObject = _Class("DMFFetchSafariBookmarksResultObject")
DMFFetchOSUpdateStatusResultObject = _Class("DMFFetchOSUpdateStatusResultObject")
DMFFetchManagedBooksResultObject = _Class("DMFFetchManagedBooksResultObject")
DMFFetchLocationResultObject = _Class("DMFFetchLocationResultObject")
DMFFetchLastLoginDateResultObject = _Class("DMFFetchLastLoginDateResultObject")
DMFFetchProvisioningProfilesResultObject = _Class(
    "DMFFetchProvisioningProfilesResultObject"
)
DMFFetchInstalledProvisioningProfilesResultObject = _Class(
    "DMFFetchInstalledProvisioningProfilesResultObject"
)
DMFFetchProfilesResultObject = _Class("DMFFetchProfilesResultObject")
DMFFetchInstalledProfilesResultObject = _Class("DMFFetchInstalledProfilesResultObject")
DMFFetchRestrictionsResultObject = _Class("DMFFetchRestrictionsResultObject")
DMFFetchGlobalRestrictionsResultObject = _Class(
    "DMFFetchGlobalRestrictionsResultObject"
)
DMFFetchDMDStateResultObject = _Class("DMFFetchDMDStateResultObject")
DMFFetchDevicePropertiesResultObject = _Class("DMFFetchDevicePropertiesResultObject")
DMFDevicePropertiesResultObject = _Class("DMFDevicePropertiesResultObject")
DMFFetchDeclarationsResultObject = _Class("DMFFetchDeclarationsResultObject")
DMFFetchDeclarationCapabilitiesResultObject = _Class(
    "DMFFetchDeclarationCapabilitiesResultObject"
)
DMFFetchControlGroupIdentifiersResultObject = _Class(
    "DMFFetchControlGroupIdentifiersResultObject"
)
DMFFetchConfigurationSourceSyncTokenResultObject = _Class(
    "DMFFetchConfigurationSourceSyncTokenResultObject"
)
DMFFetchConfigurationOrganizationsResultObject = _Class(
    "DMFFetchConfigurationOrganizationsResultObject"
)
DMFFetchClassroomInstructorEndpointResultObject = _Class(
    "DMFFetchClassroomInstructorEndpointResultObject"
)
DMFFetchCertificatesResultObject = _Class("DMFFetchCertificatesResultObject")
DMFFetchInstalledCertificatesResultObject = _Class(
    "DMFFetchInstalledCertificatesResultObject"
)
DMFFetchAvailableOSUpdatesResultObject = _Class(
    "DMFFetchAvailableOSUpdatesResultObject"
)
DMFFetchAppsResultObject = _Class("DMFFetchAppsResultObject")
DMFFetchApplicationsResultObject = _Class("DMFFetchApplicationsResultObject")
DMFFetchInstalledApplicationsResultObject = _Class(
    "DMFFetchInstalledApplicationsResultObject"
)
DMFFetchActivationLockBypassCodeResultObject = _Class(
    "DMFFetchActivationLockBypassCodeResultObject"
)
DMFEchoResultObject = _Class("DMFEchoResultObject")
DMFBeginTransactionResultObject = _Class("DMFBeginTransactionResultObject")
DMFTaskRequest = _Class("DMFTaskRequest")
DMFValidateApplicationsRequest = _Class("DMFValidateApplicationsRequest")
DMFUpdatePickableAirPlayRoutesRequest = _Class("DMFUpdatePickableAirPlayRoutesRequest")
DMFUpdateEnqueuedCommandsRequest = _Class("DMFUpdateEnqueuedCommandsRequest")
DMFUpdateDeclarationsRequest = _Class("DMFUpdateDeclarationsRequest")
DMFTriggerDiagnosticsRequest = _Class("DMFTriggerDiagnosticsRequest")
DMFStopManagingBooksRequest = _Class("DMFStopManagingBooksRequest")
DMFStopAppLockRequest = _Class("DMFStopAppLockRequest")
DMFStopAirPlayMirroringRequest = _Class("DMFStopAirPlayMirroringRequest")
DMFStartAppLockRequest = _Class("DMFStartAppLockRequest")
DMFShutDownDeviceRequest = _Class("DMFShutDownDeviceRequest")
DMFSetVolumeRequest = _Class("DMFSetVolumeRequest")
DMFSetVoiceRoamingEnabledRequest = _Class("DMFSetVoiceRoamingEnabledRequest")
DMFSetPersonalHotspotEnabledRequest = _Class("DMFSetPersonalHotspotEnabledRequest")
DMFSetPasscodeLockGracePeriodRequest = _Class("DMFSetPasscodeLockGracePeriodRequest")
DMFSetMaximumResidentUsersRequest = _Class("DMFSetMaximumResidentUsersRequest")
DMFSetInterfaceOrientationRequest = _Class("DMFSetInterfaceOrientationRequest")
DMFSetDiagnosticSubmissionEnabledRequest = _Class(
    "DMFSetDiagnosticSubmissionEnabledRequest"
)
DMFSetDeviceNameRequest = _Class("DMFSetDeviceNameRequest")
DMFSetDeclarationsRequest = _Class("DMFSetDeclarationsRequest")
DMFSetDataRoamingEnabledRequest = _Class("DMFSetDataRoamingEnabledRequest")
DMFSetBluetoothEnabledRequest = _Class("DMFSetBluetoothEnabledRequest")
DMFSetAppAnalyticsEnabledRequest = _Class("DMFSetAppAnalyticsEnabledRequest")
DMFSetAirPlayRouteRequest = _Class("DMFSetAirPlayRouteRequest")
DMFSendEventRequest = _Class("DMFSendEventRequest")
DMFScheduleOSUpdateRequest = _Class("DMFScheduleOSUpdateRequest")
DMFRestartDeviceRequest = _Class("DMFRestartDeviceRequest")
DMFRequestAirPlayMirroringRequest = _Class("DMFRequestAirPlayMirroringRequest")
DMFRemoveProvisioningProfileRequest = _Class("DMFRemoveProvisioningProfileRequest")
DMFRemoveProfileRequest = _Class("DMFRemoveProfileRequest")
DMFRemoveProtectedProfileRequest = _Class("DMFRemoveProtectedProfileRequest")
DMFRemoveOSUpdateRequest = _Class("DMFRemoveOSUpdateRequest")
DMFRemoveManagedBookRequest = _Class("DMFRemoveManagedBookRequest")
DMFRemoveConfigurationRequest = _Class("DMFRemoveConfigurationRequest")
DMFRegisterConfigurationSourceRequest = _Class("DMFRegisterConfigurationSourceRequest")
DMFRefreshStatusRequest = _Class("DMFRefreshStatusRequest")
DMFRefreshCellularPlansRequest = _Class("DMFRefreshCellularPlansRequest")
DMFProcessStatusRequest = _Class("DMFProcessStatusRequest")
DMFProcessDeclarationsRequest = _Class("DMFProcessDeclarationsRequest")
DMFPlayLostModeSoundRequest = _Class("DMFPlayLostModeSoundRequest")
DMFOpenURLRequest = _Class("DMFOpenURLRequest")
DMFOpenAppRequest = _Class("DMFOpenAppRequest")
DMFManagementUnlockRequest = _Class("DMFManagementUnlockRequest")
DMFManagementLockRequest = _Class("DMFManagementLockRequest")
DMFLogOutUserRequest = _Class("DMFLogOutUserRequest")
DMFLogoutUserRequest = _Class("DMFLogoutUserRequest")
DMFLockDeviceRequest = _Class("DMFLockDeviceRequest")
DMFLeaveControlGroupRequest = _Class("DMFLeaveControlGroupRequest")
DMFJoinControlGroupRequest = _Class("DMFJoinControlGroupRequest")
DMFInviteUserToVPPRequest = _Class("DMFInviteUserToVPPRequest")
DMFInstallProvisioningProfileRequest = _Class("DMFInstallProvisioningProfileRequest")
DMFInstallProfileRequest = _Class("DMFInstallProfileRequest")
DMFInstallManagedBookRequest = _Class("DMFInstallManagedBookRequest")
DMFInstallConfigurationRequest = _Class("DMFInstallConfigurationRequest")
DMFFetchUsersRequest = _Class("DMFFetchUsersRequest")
DMFFetchStreamEventsRequest = _Class("DMFFetchStreamEventsRequest")
DMFFetchSecurityInformationRequest = _Class("DMFFetchSecurityInformationRequest")
DMFFetchScreenshotRequest = _Class("DMFFetchScreenshotRequest")
DMFFetchSafariBookmarksRequest = _Class("DMFFetchSafariBookmarksRequest")
DMFFetchOSUpdateStatusRequest = _Class("DMFFetchOSUpdateStatusRequest")
DMFFetchManagedBooksRequest = _Class("DMFFetchManagedBooksRequest")
DMFFetchLocationRequest = _Class("DMFFetchLocationRequest")
DMFFetchLastLoginDateRequest = _Class("DMFFetchLastLoginDateRequest")
DMFFetchProvisioningProfilesRequest = _Class("DMFFetchProvisioningProfilesRequest")
DMFFetchInstalledProvisioningProfilesRequest = _Class(
    "DMFFetchInstalledProvisioningProfilesRequest"
)
DMFFetchProfilesRequest = _Class("DMFFetchProfilesRequest")
DMFFetchInstalledProfilesRequest = _Class("DMFFetchInstalledProfilesRequest")
DMFFetchRestrictionsRequest = _Class("DMFFetchRestrictionsRequest")
DMFFetchGlobalRestrictionsRequest = _Class("DMFFetchGlobalRestrictionsRequest")
DMFFetchDMDStateRequest = _Class("DMFFetchDMDStateRequest")
DMFFetchDevicePropertiesRequest = _Class("DMFFetchDevicePropertiesRequest")
DMFFetchDeclarationsRequest = _Class("DMFFetchDeclarationsRequest")
DMFFetchDeclarationCapabilitiesRequest = _Class(
    "DMFFetchDeclarationCapabilitiesRequest"
)
DMFFetchControlGroupIdentifiersRequest = _Class(
    "DMFFetchControlGroupIdentifiersRequest"
)
DMFFetchConfigurationSourceSyncTokenRequest = _Class(
    "DMFFetchConfigurationSourceSyncTokenRequest"
)
DMFFetchConfigurationOrganizationsRequest = _Class(
    "DMFFetchConfigurationOrganizationsRequest"
)
DMFFetchClassroomInstructorEndpointRequest = _Class(
    "DMFFetchClassroomInstructorEndpointRequest"
)
DMFFetchCertificatesRequest = _Class("DMFFetchCertificatesRequest")
DMFFetchInstalledCertificatesRequest = _Class("DMFFetchInstalledCertificatesRequest")
DMFFetchAvailableOSUpdatesRequest = _Class("DMFFetchAvailableOSUpdatesRequest")
DMFFetchAppsRequest = _Class("DMFFetchAppsRequest")
DMFFetchApplicationsRequest = _Class("DMFFetchApplicationsRequest")
DMFFetchInstalledApplicationsRequest = _Class("DMFFetchInstalledApplicationsRequest")
DMFFetchActivationLockBypassCodeRequest = _Class(
    "DMFFetchActivationLockBypassCodeRequest"
)
DMFEndTransactionRequest = _Class("DMFEndTransactionRequest")
DMFEnableLostModeRequest = _Class("DMFEnableLostModeRequest")
DMFEchoRequest = _Class("DMFEchoRequest")
DMFDisableLostModeRequest = _Class("DMFDisableLostModeRequest")
DMFDevicePropertyNotificationSubscriptionRequest = _Class(
    "DMFDevicePropertyNotificationSubscriptionRequest"
)
DMFDeleteUserRequest = _Class("DMFDeleteUserRequest")
DMFDeactivateConfigurationOrganizationRequest = _Class(
    "DMFDeactivateConfigurationOrganizationRequest"
)
DMFCreateConfigurationOrganizationRequest = _Class(
    "DMFCreateConfigurationOrganizationRequest"
)
DMFClearRestrictionsPasswordRequest = _Class("DMFClearRestrictionsPasswordRequest")
DMFClearActivationLockBypassCodeRequest = _Class(
    "DMFClearActivationLockBypassCodeRequest"
)
DMFBeginTransactionRequest = _Class("DMFBeginTransactionRequest")
DMFAssignUserRequest = _Class("DMFAssignUserRequest")
DMFAppRequest = _Class("DMFAppRequest")
DMFStopManagingAppRequest = _Class("DMFStopManagingAppRequest")
DMFSetAppVPNUUIDRequest = _Class("DMFSetAppVPNUUIDRequest")
DMFSetAppRemovabilityRequest = _Class("DMFSetAppRemovabilityRequest")
DMFSetAppConfigurationRequest = _Class("DMFSetAppConfigurationRequest")
DMFSetAppAssociatedDomainsRequest = _Class("DMFSetAppAssociatedDomainsRequest")
DMFSetAppAssociatedDomainsEnableDirectDownloadsRequest = _Class(
    "DMFSetAppAssociatedDomainsEnableDirectDownloadsRequest"
)
DMFRemoveAppRequest = _Class("DMFRemoveAppRequest")
DMFUpdateAppRequest = _Class("DMFUpdateAppRequest")
DMFMDMv1UpdateAppRequest = _Class("DMFMDMv1UpdateAppRequest")
DMFMDMv1StartManagingAppRequest = _Class("DMFMDMv1StartManagingAppRequest")
DMFInstallAppRequest = _Class("DMFInstallAppRequest")
DMFMDMv1InstallAppRequest = _Class("DMFMDMv1InstallAppRequest")
DMFActivityTransactionRequest = _Class("DMFActivityTransactionRequest")
DMFBatchRequestOperation = _Class("DMFBatchRequestOperation")

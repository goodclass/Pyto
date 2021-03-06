"""
Classes from the 'SafariSharedUI' framework.
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


WBSMobileAssetController = _Class("WBSMobileAssetController")
WBSTranslationDiagnosticData = _Class("WBSTranslationDiagnosticData")
WBSTranslationContext = _Class("WBSTranslationContext")
WBSTranslationWebpageContentExtractor = _Class("WBSTranslationWebpageContentExtractor")
WBSTranslationURLParser = _Class("WBSTranslationURLParser")
WBSTranslationInformation = _Class("WBSTranslationInformation")
WBSTranslationDataCollectionManager = _Class("WBSTranslationDataCollectionManager")
WBSURLSpoofingMitigator = _Class("WBSURLSpoofingMitigator")
WBSPhishingURLClassifierCache = _Class("WBSPhishingURLClassifierCache")
WBSPhishingURLClassifierConfigurationOverrideAdapter = _Class(
    "WBSPhishingURLClassifierConfigurationOverrideAdapter"
)
WBSMetadataExtractor = _Class("WBSMetadataExtractor")
WBSSiteIconKeyColorExtractor = _Class("WBSSiteIconKeyColorExtractor")
WBSImageUtilities = _Class("WBSImageUtilities")
WBSImageFetchingURLSessionTaskManager = _Class("WBSImageFetchingURLSessionTaskManager")
WBSTranslationErrorController = _Class("WBSTranslationErrorController")
WBSParsecSearchCompletionResultSet = _Class("WBSParsecSearchCompletionResultSet")
WBSPhishingImageClassifierModel = _Class("WBSPhishingImageClassifierModel")
WBSPhishingURLClassifierCrowdsourcedFeedbackAllowListAdapter = _Class(
    "WBSPhishingURLClassifierCrowdsourcedFeedbackAllowListAdapter"
)
WBSParsecSearchMapsResultFeedbackSender = _Class(
    "WBSParsecSearchMapsResultFeedbackSender"
)
WBSParsecSubscriptionManager = _Class("WBSParsecSubscriptionManager")
WBSSearchProvider = _Class("WBSSearchProvider")
WBSTrackingCapableThirdParty = _Class("WBSTrackingCapableThirdParty")
WBSKnownTrackingThirdParty = _Class("WBSKnownTrackingThirdParty")
WBSTrackingCapableFirstParty = _Class("WBSTrackingCapableFirstParty")
WBSTrackedFirstParty = _Class("WBSTrackedFirstParty")
WBSParsecDFeedbackDispatcher = _Class("WBSParsecDFeedbackDispatcher")
WBSParsecHiddenResultInfo = _Class("WBSParsecHiddenResultInfo")
WBSPhishingClassifierController = _Class("WBSPhishingClassifierController")
WBSParsecSearchResult = _Class("WBSParsecSearchResult")
WBSParsecDSession = _Class("WBSParsecDSession")
WBSParsecResultSetPattern = _Class("WBSParsecResultSetPattern")
WBSParsecSearchResultCache = _Class("WBSParsecSearchResultCache")
WBSKnownTrackerFilter = _Class("WBSKnownTrackerFilter")
WBSParsecSearchResponse = _Class("WBSParsecSearchResponse")
WBSParsecSearchUtilities = _Class("WBSParsecSearchUtilities")
_WBSSearchFoundationFeedbackGenerator = _Class("_WBSSearchFoundationFeedbackGenerator")
WBSCompletionListRankingObserver = _Class("WBSCompletionListRankingObserver")
WBSPhishingURLClassifierWithFallback = _Class("WBSPhishingURLClassifierWithFallback")
WBSParsecSubscriptionInfo = _Class("WBSParsecSubscriptionInfo")
_WBSParsecSubscriptionInfoKeyValueStringParser = _Class(
    "_WBSParsecSubscriptionInfoKeyValueStringParser"
)
WBSSiriIntelligenceHistorySearch = _Class("WBSSiriIntelligenceHistorySearch")
WBSSiriIntelligenceDonor = _Class("WBSSiriIntelligenceDonor")
WBSSiriIntelligenceDonorBookmarkData = _Class("WBSSiriIntelligenceDonorBookmarkData")
WBSSiriIntelligenceDonorHistoryData = _Class("WBSSiriIntelligenceDonorHistoryData")
WBSFoundInRecommendationManager = _Class("WBSFoundInRecommendationManager")
WBSForYouTopicManager = _Class("WBSForYouTopicManager")
WBSForYouTopic = _Class("WBSForYouTopic")
WBSForYouRecommendationMediator = _Class("WBSForYouRecommendationMediator")
WBSForYouLinkRecommendation = _Class("WBSForYouLinkRecommendation")
WBSForYouDataSourceWeightManager = _Class("WBSForYouDataSourceWeightManager")
WBSForYouRecommendationMediatorDataSource = _Class(
    "WBSForYouRecommendationMediatorDataSource"
)
WBSForYouRecentParsecResultsManager = _Class("WBSForYouRecentParsecResultsManager")
WBSForYouCloudTabsDataSource = _Class("WBSForYouCloudTabsDataSource")
WBSContextResultGrouper = _Class("WBSContextResultGrouper")
WBSFluidProgressState = _Class("WBSFluidProgressState")
WBSFluidProgressAnimation = _Class("WBSFluidProgressAnimation")
WBSFluidProgressController = _Class("WBSFluidProgressController")
WBSPhishingAssetController = _Class("WBSPhishingAssetController")
WBSAppLink = _Class("WBSAppLink")
WBSPhishingUpdateConfiguration = _Class("WBSPhishingUpdateConfiguration")
WBSWebProcessPlugIn = _Class("WBSWebProcessPlugIn")
WBSTranslationContextSnapshot = _Class("WBSTranslationContextSnapshot")
WBSTemplateIconMonogramConfiguration = _Class("WBSTemplateIconMonogramConfiguration")
WBSTemplateIconMonogramGenerator = _Class("WBSTemplateIconMonogramGenerator")
WBSCachedFont = _Class("WBSCachedFont")
WBSTemplateIconCache = _Class("WBSTemplateIconCache")
WBSTouchIconFetchOperationResult = _Class("WBSTouchIconFetchOperationResult")
WBSPhishingURLClassifierHistoryAdapter = _Class(
    "WBSPhishingURLClassifierHistoryAdapter"
)
WBSLocalAssetController = _Class("WBSLocalAssetController")
WBSLocalePair = _Class("WBSLocalePair")
WBSTouchIconCacheSettingsEntry = _Class("WBSTouchIconCacheSettingsEntry")
WBSTouchIconCache = _Class("WBSTouchIconCache")
WBSWebProcessPlugInPageController = _Class("WBSWebProcessPlugInPageController")
WBSTouchIconWebProcessPlugInPageController = _Class(
    "WBSTouchIconWebProcessPlugInPageController"
)
WBSSVGImageRenderingWebProcessPlugInPageController = _Class(
    "WBSSVGImageRenderingWebProcessPlugInPageController"
)
WBSParsecABGroupManager = _Class("WBSParsecABGroupManager")
WBSPrivacyReportData = _Class("WBSPrivacyReportData")
WBSSVGImageRenderingProvider = _Class("WBSSVGImageRenderingProvider")
_WBSSiteMetadataRequestInfo = _Class("_WBSSiteMetadataRequestInfo")
_WBSSiteMetadataToken = _Class("_WBSSiteMetadataToken")
WBSSiteMetadataManager = _Class("WBSSiteMetadataManager")
WBSSiteMetadataImageCacheSettingsSQLiteStore = _Class(
    "WBSSiteMetadataImageCacheSettingsSQLiteStore"
)
WBSTouchIconCacheSettingsSQLiteStore = _Class("WBSTouchIconCacheSettingsSQLiteStore")
WBSSiteMetadataImageCache = _Class("WBSSiteMetadataImageCache")
WBSOnDiskDataCache = _Class("WBSOnDiskDataCache")
WBSParsecABGroupIdentifierUserDefaultsStore = _Class(
    "WBSParsecABGroupIdentifierUserDefaultsStore"
)
WBSLeadImageSaver = _Class("WBSLeadImageSaver")
WBSLeadImageCache = _Class("WBSLeadImageCache")
WBSFaviconProviderUtilities = _Class("WBSFaviconProviderUtilities")
WBSTranslationAvailability = _Class("WBSTranslationAvailability")
WBSFaviconProviderPrivateCache = _Class("WBSFaviconProviderPrivateCache")
WBSFaviconProviderRecordCache = _Class("WBSFaviconProviderRecordCache")
WBSFaviconProviderPersistenceController = _Class(
    "WBSFaviconProviderPersistenceController"
)
WBSFaviconProviderIconInfo = _Class("WBSFaviconProviderIconInfo")
WBSFaviconProvider = _Class("WBSFaviconProvider")
_WBSFaviconRecord = _Class("_WBSFaviconRecord")
WBSPhishingClassifierResults = _Class("WBSPhishingClassifierResults")
WBSSiteMetadataResponse = _Class("WBSSiteMetadataResponse")
WBSTemplateIconResponse = _Class("WBSTemplateIconResponse")
WBSTouchIconResponse = _Class("WBSTouchIconResponse")
WBSSVGImageRenderingResponse = _Class("WBSSVGImageRenderingResponse")
WBSLeadImageCacheResponse = _Class("WBSLeadImageCacheResponse")
WBSFaviconResponse = _Class("WBSFaviconResponse")
WBSFaviconRequestsController = _Class("WBSFaviconRequestsController")
WBSTranslationConsentAlertHelper = _Class("WBSTranslationConsentAlertHelper")
WBSSiteMetadataRequest = _Class("WBSSiteMetadataRequest")
WBSTemplateIconRequest = _Class("WBSTemplateIconRequest")
WBSTouchIconRequest = _Class("WBSTouchIconRequest")
WBSSVGImageRenderingRequest = _Class("WBSSVGImageRenderingRequest")
WBSLeadImageCacheRequest = _Class("WBSLeadImageCacheRequest")
WBSFaviconRequest = _Class("WBSFaviconRequest")
WBSCacheRetainReleasePolicy = _Class("WBSCacheRetainReleasePolicy")
WBSBookmarkFolderTouchIconProviderInfo = _Class(
    "WBSBookmarkFolderTouchIconProviderInfo"
)
WBSBookmarkFolderTouchIconProviderRequestInfo = _Class(
    "WBSBookmarkFolderTouchIconProviderRequestInfo"
)
WBSBookmarkFolderTouchIconProvider = _Class("WBSBookmarkFolderTouchIconProvider")
WBSPhishingConfiguration = _Class("WBSPhishingConfiguration")
WBSPhishingConfigurationImageClassifierIdentifier = _Class(
    "WBSPhishingConfigurationImageClassifierIdentifier"
)
WBSPhishingConfigurationDomain = _Class("WBSPhishingConfigurationDomain")
WBSPhishingConfigurationOverride = _Class("WBSPhishingConfigurationOverride")
WBSFaviconProviderDatabaseController = _Class("WBSFaviconProviderDatabaseController")
WBSParsecImageRepresentation = _Class("WBSParsecImageRepresentation")
WBSParsecActionButton = _Class("WBSParsecActionButton")
WBSParsecRichText = _Class("WBSParsecRichText")
WBSParsecSportsImage = _Class("WBSParsecSportsImage")
WBSParsecFormattedText = _Class("WBSParsecFormattedText")
WBSParsecPunchout = _Class("WBSParsecPunchout")
WBSParsecSearchSportsAttributionExtraCompletionItem = _Class(
    "WBSParsecSearchSportsAttributionExtraCompletionItem"
)
WBSParsecSportsScoreSummary = _Class("WBSParsecSportsScoreSummary")
WBSParsecLegacySearchResult = _Class("WBSParsecLegacySearchResult")
WBSParsecSearchGenericResult = _Class("WBSParsecSearchGenericResult")
WBSParsecSearchSportsResult = _Class("WBSParsecSearchSportsResult")
WBSParsecSearchMapsResult = _Class("WBSParsecSearchMapsResult")
WBSParsecSearchMoviesResult = _Class("WBSParsecSearchMoviesResult")
WBSParsecSearchSimpleResult = _Class("WBSParsecSearchSimpleResult")
WBSParsecAuxiliaryInfo = _Class("WBSParsecAuxiliaryInfo")
WBSUISafariSandboxBrokerConnection = _Class("WBSUISafariSandboxBrokerConnection")
WBSUISafariSandboxBroker = _Class("WBSUISafariSandboxBroker")
WBSForYouPerSitePreferenceManager = _Class("WBSForYouPerSitePreferenceManager")
WBSPhishingClassifierControllerConfigurationTransformer = _Class(
    "WBSPhishingClassifierControllerConfigurationTransformer"
)
WBSSiteMetadataFetchOperation = _Class("WBSSiteMetadataFetchOperation")
WBSWebViewMetadataFetchOperation = _Class("WBSWebViewMetadataFetchOperation")
WBSTouchIconFetchOperation = _Class("WBSTouchIconFetchOperation")
WBSSVGImageRenderingFetchOperation = _Class("WBSSVGImageRenderingFetchOperation")
